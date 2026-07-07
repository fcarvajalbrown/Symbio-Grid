import mesa
import numpy as np
from symbiogrid.model.config import SimulationConfig
from symbiogrid.model.agents.plant import PlantAgent
from symbiogrid.model.agents.fungi import FungiAgent
from symbiogrid.model.rules.rule_table import RuleTable, PLANT_ACTIONS, FUNGI_ACTIONS


class SymbioModel(mesa.Model):
    def __init__(self, config: SimulationConfig):
        super().__init__(rng=config.seed)
        self.config = config
        self.generation = 0
        self.grid = mesa.space.MultiGrid(config.width, config.height, torus=True)

        self.phosphorus_map = self.rng.uniform(0, 10, (config.width, config.height)) * config.phosphorus_density
        self.carbon_map = np.zeros((config.width, config.height))

        self._place_agents()

    def _place_agents(self):
        all_positions = [(x, y) for x in range(self.config.width) for y in range(self.config.height)]
        indices = self.rng.permutation(len(all_positions))
        plant_positions = [all_positions[indices[i]] for i in range(self.config.n_plants)]
        occupied = set(plant_positions)

        for pos in plant_positions:
            rt = RuleTable(PLANT_ACTIONS, mutation_rate=self.config.mutation_rate, rng=self.random)
            self.grid.place_agent(PlantAgent(self, rt, self.config), pos)

        for i in range(self.config.n_fungi):
            pos = self._fungi_seat(plant_positions, occupied, i)
            occupied.add(pos)
            rt = RuleTable(FUNGI_ACTIONS, mutation_rate=self.config.mutation_rate, rng=self.random)
            self.grid.place_agent(FungiAgent(self, rt, self.config), pos)

    def _fungi_seat(self, plant_positions, occupied, i):
        if plant_positions:
            anchor = plant_positions[i % len(plant_positions)]
            free = [p for p in self.grid.get_neighborhood(anchor, moore=True, include_center=False) if p not in occupied]
            if free:
                return free[self.random.randrange(len(free))]
        free = [p for p in ((x, y) for x in range(self.config.width) for y in range(self.config.height)) if p not in occupied]
        return free[self.random.randrange(len(free))]

    def step(self):
        self.agents.shuffle_do("step")
        self._remove_dead()
        self._replenish_phosphorus()
        self.generation += 1

    def _remove_dead(self):
        dead = [a for a in self.agents if not a.alive]
        for a in dead:
            if a.pos is not None:
                self.grid.remove_agent(a)
            a.remove()

    def _replenish_phosphorus(self):
        self.phosphorus_map = np.clip(self.phosphorus_map + self.config.phosphorus_regen, 0, 10)

    def get_state(self) -> dict:
        plants = [a for a in self.agents if isinstance(a, PlantAgent)]
        fungi = [a for a in self.agents if isinstance(a, FungiAgent)]
        return {
            "generation": self.generation,
            "agents": list(self.agents),
            "n_plants": len(plants),
            "n_fungi": len(fungi),
            "phosphorus_map": self.phosphorus_map,
            "avg_carbon": sum(a.carbon for a in plants) / max(len(plants), 1),
            "avg_phosphorus": sum(a.phosphorus for a in fungi) / max(len(fungi), 1),
        }

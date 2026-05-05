import mesa
import numpy as np
from symbiogrid.model.config import SimulationConfig
from symbiogrid.model.agents.plant import PlantAgent
from symbiogrid.model.agents.fungi import FungiAgent
from symbiogrid.model.rules.rule_table import RuleTable, PLANT_ACTIONS, FUNGI_ACTIONS


class SymbioModel(mesa.Model):
    def __init__(self, config: SimulationConfig):
        super().__init__(seed=config.seed)
        self.config = config
        self.generation = 0
        self.grid = mesa.space.MultiGrid(config.width, config.height, torus=True)

        rng = np.random.default_rng(config.seed)
        self.phosphorus_map = rng.uniform(0, 10, (config.width, config.height)) * config.phosphorus_density
        self.carbon_map = np.zeros((config.width, config.height))

        self._place_agents(rng)

    def _place_agents(self, rng: np.random.Generator):
        all_positions = [(x, y) for x in range(self.config.width) for y in range(self.config.height)]
        indices = rng.permutation(len(all_positions))

        for i in range(self.config.n_plants):
            rt = RuleTable(PLANT_ACTIONS, mutation_rate=self.config.mutation_rate)
            agent = PlantAgent(self, rt, self.config)
            self.grid.place_agent(agent, all_positions[indices[i]])

        for i in range(self.config.n_fungi):
            rt = RuleTable(FUNGI_ACTIONS, mutation_rate=self.config.mutation_rate)
            agent = FungiAgent(self, rt, self.config)
            self.grid.place_agent(agent, all_positions[indices[self.config.n_plants + i]])

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
        self.phosphorus_map = np.clip(self.phosphorus_map + 0.02, 0, 10)

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

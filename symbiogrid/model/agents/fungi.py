from symbiogrid.model.agents.base import BDIAgent
from symbiogrid.model.rules.rule_table import RuleTable, FUNGI_ACTIONS
from symbiogrid.model.config import SimulationConfig


class FungiAgent(BDIAgent):
    def __init__(self, model, rule_table: RuleTable, config: SimulationConfig):
        super().__init__(model, rule_table, config)
        self.phosphorus = 5.0
        self.carbon = 3.0

    def sense(self):
        from symbiogrid.model.agents.plant import PlantAgent
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        plants = [a for a in neighbors if isinstance(a, PlantAgent) and a.alive]
        soil_p = self.model.phosphorus_map[self.pos[0], self.pos[1]]
        neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        empty = [pos for pos in neighborhood if self.model.grid.is_cell_empty(pos)]
        self.beliefs = {
            "phosphorus": self.phosphorus,
            "carbon": self.carbon,
            "plant_neighbors": plants,
            "soil_phosphorus": soil_p,
            "empty_neighbors": empty,
            "stressed": self.carbon < 2.0,
        }

    def deliberate(self):
        p = min(int(self.beliefs["phosphorus"] / 5), 3)
        c = min(int(self.beliefs["carbon"] / 5), 3)
        pn = min(len(self.beliefs["plant_neighbors"]), 3)
        state = (p << 4) | (c << 2) | pn
        self.intention = self.rule_table.query(state)

    def act(self):
        # absorb soil phosphorus
        absorbed = min(self.beliefs["soil_phosphorus"], 1.0)
        self.phosphorus = min(self.phosphorus + absorbed, 20.0)
        self.model.phosphorus_map[self.pos[0], self.pos[1]] -= absorbed

        self.carbon = max(self.carbon - 0.2, 0.0)

        if self.intention == "TRADE" and self.beliefs["plant_neighbors"]:
            target = self.random.choice(self.beliefs["plant_neighbors"])
            amount = min(self.phosphorus * 0.25, 2.0)
            if target.carbon >= amount:
                self.phosphorus -= amount
                target.phosphorus += amount
                self.carbon += amount
                target.carbon -= amount

        elif self.intention == "EXPAND" and self.beliefs["empty_neighbors"]:
            if self.phosphorus > 6.0 and self.carbon > 4.0:
                pos = self.random.choice(self.beliefs["empty_neighbors"])
                self._spawn(pos)

        if self.carbon <= 0:
            self.die()

    def _spawn(self, pos):
        child = FungiAgent(self.model, self.rule_table.mutate(), self.config)
        child.phosphorus = self.phosphorus * 0.4
        child.carbon = self.carbon * 0.4
        self.phosphorus *= 0.6
        self.carbon *= 0.6
        self.model.grid.place_agent(child, pos)

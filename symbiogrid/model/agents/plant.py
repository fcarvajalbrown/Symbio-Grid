from symbiogrid.model.agents.base import BDIAgent
from symbiogrid.model.rules.rule_table import RuleTable, PLANT_ACTIONS
from symbiogrid.model.config import SimulationConfig


class PlantAgent(BDIAgent):
    def __init__(self, model, rule_table: RuleTable, config: SimulationConfig):
        super().__init__(model, rule_table, config)
        self.carbon = 5.0
        self.phosphorus = 5.0

    def sense(self):
        from symbiogrid.model.agents.fungi import FungiAgent
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        fungi = [a for a in neighbors if isinstance(a, FungiAgent) and a.alive]
        self.beliefs = {
            "carbon": self.carbon,
            "phosphorus": self.phosphorus,
            "fungi_neighbors": fungi,
            "stressed": self.phosphorus < 2.0,
        }

    def deliberate(self):
        c = min(int(self.beliefs["carbon"] / 5), 3)
        p = min(int(self.beliefs["phosphorus"] / 5), 3)
        fn = min(len(self.beliefs["fungi_neighbors"]), 3)
        state = (c << 4) | (p << 2) | fn
        self.intention = self.rule_table.query(state)

    def act(self):
        self.carbon = min(self.carbon + 1.0, 20.0)
        self.phosphorus = max(self.phosphorus - 0.3, 0.0)

        if self.intention == "TRADE" and self.beliefs["fungi_neighbors"]:
            target = self.random.choice(self.beliefs["fungi_neighbors"])
            amount = min(self.carbon * 0.25, 2.0)
            if target.phosphorus >= amount:
                self.carbon -= amount
                target.carbon += amount
                self.phosphorus += amount
                target.phosphorus -= amount

        if self.phosphorus <= 0:
            self.die()

import mesa
from symbiogrid.model.rules.rule_table import RuleTable
from symbiogrid.model.config import SimulationConfig


class BDIAgent(mesa.Agent):
    def __init__(self, model, rule_table: RuleTable, config: SimulationConfig):
        super().__init__(model)
        self.rule_table = rule_table
        self.config = config
        self.alive = True
        self.beliefs: dict = {}
        self.intention: str = "IDLE"

    def sense(self):
        raise NotImplementedError

    def deliberate(self):
        raise NotImplementedError

    def act(self):
        raise NotImplementedError

    def step(self):
        if not self.alive:
            return
        self.sense()
        self.deliberate()
        self.act()

    def die(self):
        self.alive = False

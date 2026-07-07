import random

PLANT_ACTIONS = ["TRADE", "SPROUT", "IDLE"]
FUNGI_ACTIONS = ["TRADE", "EXPAND", "IDLE"]


class RuleTable:
    def __init__(self, actions: list[str], n_states: int = 64, mutation_rate: float = 0.1, rng: random.Random | None = None):
        self.actions = actions
        self.n_states = n_states
        self.mutation_rate = mutation_rate
        self.rng = rng or random.Random()
        self.table = [self.rng.randint(0, len(actions) - 1) for _ in range(n_states)]

    def query(self, state_index: int) -> str:
        return self.actions[self.table[state_index % self.n_states]]

    def mutate(self) -> "RuleTable":
        child = RuleTable(self.actions, self.n_states, self.mutation_rate, rng=self.rng)
        child.table = self.table.copy()
        for i in range(len(child.table)):
            if self.rng.random() < self.mutation_rate:
                child.table[i] = self.rng.randint(0, len(self.actions) - 1)
        return child

    def to_bitstring(self) -> str:
        return "".join(str(v) for v in self.table)

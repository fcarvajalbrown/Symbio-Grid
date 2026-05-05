import random

PLANT_ACTIONS = ["TRADE", "HOARD", "IDLE"]
FUNGI_ACTIONS = ["TRADE", "EXPAND", "IDLE"]


class RuleTable:
    def __init__(self, actions: list[str], n_states: int = 64, mutation_rate: float = 0.1):
        self.actions = actions
        self.n_states = n_states
        self.mutation_rate = mutation_rate
        self.table = [random.randint(0, len(actions) - 1) for _ in range(n_states)]

    def query(self, state_index: int) -> str:
        return self.actions[self.table[state_index % self.n_states]]

    def mutate(self) -> "RuleTable":
        child = RuleTable(self.actions, self.n_states, self.mutation_rate)
        child.table = self.table.copy()
        for i in range(len(child.table)):
            if random.random() < self.mutation_rate:
                child.table[i] = random.randint(0, len(self.actions) - 1)
        return child

    def to_bitstring(self) -> str:
        return "".join(str(v) for v in self.table)

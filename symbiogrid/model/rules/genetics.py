from .rule_table import RuleTable


def mutate(rule_table: RuleTable) -> RuleTable:
    return rule_table.mutate()


def crossover(parent_a: RuleTable, parent_b: RuleTable) -> RuleTable:
    point = parent_a.rng.randint(1, len(parent_a.table) - 1)
    child = RuleTable(parent_a.actions, parent_a.n_states, parent_a.mutation_rate, rng=parent_a.rng)
    child.table = parent_a.table[:point] + parent_b.table[point:]
    return child

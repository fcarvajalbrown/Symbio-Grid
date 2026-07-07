import random
from symbiogrid.model.rules.rule_table import RuleTable, PLANT_ACTIONS, FUNGI_ACTIONS
from symbiogrid.model.rules.genetics import mutate, crossover


def test_table_length_and_value_bounds():
    rt = RuleTable(PLANT_ACTIONS, rng=random.Random(0))
    assert len(rt.table) == rt.n_states
    assert all(0 <= v < len(PLANT_ACTIONS) for v in rt.table)


def test_query_returns_valid_action_for_any_state():
    rt = RuleTable(FUNGI_ACTIONS, rng=random.Random(1))
    for state in range(-5, 200):
        assert rt.query(state) in FUNGI_ACTIONS


def test_same_seed_gives_same_table():
    a = RuleTable(PLANT_ACTIONS, rng=random.Random(42))
    b = RuleTable(PLANT_ACTIONS, rng=random.Random(42))
    assert a.table == b.table


def test_zero_mutation_rate_preserves_table():
    rt = RuleTable(PLANT_ACTIONS, mutation_rate=0.0, rng=random.Random(3))
    child = rt.mutate()
    assert child.table == rt.table


def test_mutation_keeps_values_in_bounds():
    rt = RuleTable(FUNGI_ACTIONS, mutation_rate=1.0, rng=random.Random(4))
    child = rt.mutate()
    assert len(child.table) == rt.n_states
    assert all(0 <= v < len(FUNGI_ACTIONS) for v in child.table)


def test_crossover_length_and_bounds():
    rng = random.Random(5)
    a = RuleTable(PLANT_ACTIONS, rng=rng)
    b = RuleTable(PLANT_ACTIONS, rng=rng)
    child = crossover(a, b)
    assert len(child.table) == a.n_states
    assert all(0 <= v < len(PLANT_ACTIONS) for v in child.table)

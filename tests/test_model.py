import pytest
from dataclasses import replace
from symbiogrid.model.model import SymbioModel
from symbiogrid.model.config import SimulationConfig, PRESETS
from symbiogrid.model.agents.plant import PlantAgent
from symbiogrid.model.agents.fungi import FungiAgent


def _counts(model):
    p = sum(1 for a in model.agents if isinstance(a, PlantAgent))
    f = sum(1 for a in model.agents if isinstance(a, FungiAgent))
    return p, f


def test_model_runs_without_error():
    model = SymbioModel(SimulationConfig(seed=1))
    for _ in range(100):
        model.step()
    assert model.generation == 100


@pytest.mark.parametrize("preset", list(PRESETS.keys()))
def test_presets_persist_and_stay_nonnegative(preset):
    model = SymbioModel(replace(PRESETS[preset], seed=7))
    for _ in range(200):
        model.step()
        p, f = _counts(model)
        assert p >= 0 and f >= 0
    p, f = _counts(model)
    assert p > 0 and f > 0


def test_determinism_same_seed_identical_state():
    a = SymbioModel(SimulationConfig(seed=99))
    b = SymbioModel(SimulationConfig(seed=99))
    for _ in range(150):
        a.step()
        b.step()
    sa, sb = a.get_state(), b.get_state()
    assert sa["n_plants"] == sb["n_plants"]
    assert sa["n_fungi"] == sb["n_fungi"]
    assert sa["avg_carbon"] == sb["avg_carbon"]
    assert [x.rule_table.to_bitstring() for x in a.agents] == [x.rule_table.to_bitstring() for x in b.agents]


def test_different_seeds_diverge():
    a = SymbioModel(SimulationConfig(seed=1))
    b = SymbioModel(SimulationConfig(seed=2))
    for _ in range(150):
        a.step()
        b.step()
    assert a.get_state()["n_plants"] != b.get_state()["n_plants"] or a.get_state()["n_fungi"] != b.get_state()["n_fungi"]


def test_plant_fungi_trade_conserves_resources():
    cfg = SimulationConfig(seed=5, width=5, height=5, n_plants=0, n_fungi=0, plant_p_decay=0.0)
    model = SymbioModel(cfg)
    plant = PlantAgent(model, _rule(model, PlantAgent), cfg)
    fungi = FungiAgent(model, _rule(model, FungiAgent), cfg)
    model.grid.place_agent(plant, (2, 2))
    model.grid.place_agent(fungi, (2, 3))
    plant.carbon, plant.phosphorus = 20.0, 5.0
    fungi.carbon, fungi.phosphorus = 3.0, 5.0
    total_c = plant.carbon + fungi.carbon
    total_p = plant.phosphorus + fungi.phosphorus
    plant.sense()
    plant.intention = "TRADE"
    plant.act()
    assert plant.carbon + fungi.carbon == pytest.approx(total_c)
    assert plant.phosphorus + fungi.phosphorus == pytest.approx(total_p)


def _rule(model, cls):
    from symbiogrid.model.rules.rule_table import RuleTable, PLANT_ACTIONS, FUNGI_ACTIONS
    actions = PLANT_ACTIONS if cls is PlantAgent else FUNGI_ACTIONS
    return RuleTable(actions, rng=model.random)

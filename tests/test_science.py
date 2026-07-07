from symbiogrid.model.config import SimulationConfig
from symbiogrid.science.runner import run_single, run_batch, build_configs
from symbiogrid.science.export import export_run


def test_run_single_returns_metrics_and_dna():
    result = run_single(SimulationConfig(seed=1), max_gens=30)
    assert not result.metrics.empty
    assert result.final_generation <= 30
    assert list(result.metrics.columns)[:3] == ["generation", "n_plants", "n_fungi"]


def test_metrics_reproducible_across_runs():
    a = run_single(SimulationConfig(seed=8), max_gens=40)
    b = run_single(SimulationConfig(seed=8), max_gens=40)
    assert a.metrics.equals(b.metrics)
    assert [d["rule_table"] for d in a.dna] == [d["rule_table"] for d in b.dna]


def test_build_configs_counts_seeds_times_sweeps():
    configs = build_configs(SimulationConfig(), seeds=[1, 2, 3], sweeps={"mutation_rate": [0.05, 0.1]})
    assert len(configs) == 6
    assert {c.mutation_rate for c in configs} == {0.05, 0.1}
    assert {c.seed for c in configs} == {1, 2, 3}


def test_collapse_stop_halts_early():
    cfg = SimulationConfig(seed=1, plant_p_decay=5.0)
    result = run_single(cfg, max_gens=500, stop_on_collapse=True)
    assert result.collapsed
    assert result.final_generation < 500


def test_export_writes_expected_files(tmp_path):
    result = run_single(SimulationConfig(seed=2), max_gens=20)
    out = export_run(result, tmp_path / "run", stamp=False)
    for name in ("metrics.csv", "metrics.parquet", "dna.csv", "manifest.json"):
        assert (out / name).exists()


def test_export_metrics_bytewise_identical(tmp_path):
    a = run_single(SimulationConfig(seed=3), max_gens=25)
    b = run_single(SimulationConfig(seed=3), max_gens=25)
    pa = export_run(a, tmp_path / "a", stamp=False)
    pb = export_run(b, tmp_path / "b", stamp=False)
    assert (pa / "metrics.csv").read_bytes() == (pb / "metrics.csv").read_bytes()

from dataclasses import dataclass, replace, field
import pandas as pd
from symbiogrid.model.model import SymbioModel
from symbiogrid.model.config import SimulationConfig
from symbiogrid.science.collector import build_collector, agent_dna


@dataclass
class RunResult:
    config: SimulationConfig
    metrics: pd.DataFrame
    dna: list[dict]
    final_generation: int
    collapsed: bool


def run_single(config: SimulationConfig, max_gens: int, stop_on_collapse: bool = True) -> RunResult:
    model = SymbioModel(config)
    collector = build_collector()
    collector.collect(model)
    collapsed = False
    for _ in range(max_gens):
        model.step()
        collector.collect(model)
        n_plants = sum(1 for a in model.agents if type(a).__name__ == "PlantAgent")
        n_fungi = sum(1 for a in model.agents if type(a).__name__ == "FungiAgent")
        if stop_on_collapse and (n_plants == 0 or n_fungi == 0):
            collapsed = True
            break
    return RunResult(
        config=config,
        metrics=collector.get_model_vars_dataframe().reset_index(drop=True),
        dna=agent_dna(model),
        final_generation=model.generation,
        collapsed=collapsed,
    )


def build_configs(base: SimulationConfig, seeds: list[int], sweeps: dict | None = None) -> list[SimulationConfig]:
    sweeps = sweeps or {}
    combos = [{}]
    for key, values in sweeps.items():
        combos = [dict(c, **{key: v}) for c in combos for v in values]
    configs = []
    for combo in combos:
        for seed in seeds:
            configs.append(replace(base, seed=seed, **combo))
    return configs


def run_batch(base: SimulationConfig, seeds: list[int], max_gens: int,
              sweeps: dict | None = None, stop_on_collapse: bool = True) -> list[RunResult]:
    configs = build_configs(base, seeds, sweeps)
    return [run_single(cfg, max_gens, stop_on_collapse) for cfg in configs]

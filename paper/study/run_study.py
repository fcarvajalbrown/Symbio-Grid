"""Reproducible study for the AMS paper: mutation, phosphorus density, and soil-regeneration sweeps."""
from dataclasses import replace
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from symbiogrid.model.config import SimulationConfig
from symbiogrid.science.runner import run_single

OUT = Path(__file__).resolve().parent
RES = OUT / "results"
FIG = OUT.parent / "figures"
RES.mkdir(parents=True, exist_ok=True)
FIG.mkdir(parents=True, exist_ok=True)

SEEDS = list(range(1, 11))
GENS = 300
EARLY = 5


def _et(metrics, gen):
    return float(metrics.iloc[gen]["expressed_trade"]) if len(metrics) > gen else float("nan")


def run_grid(param, values, base=None):
    base = base or SimulationConfig()
    rows = []
    for v in values:
        for s in SEEDS:
            r = run_single(replace(base, seed=s, **{param: v}), GENS)
            last = r.metrics.iloc[-1]
            rows.append({
                param: v, "seed": s, "collapsed": r.collapsed, "final_gen": r.final_generation,
                "total": int(last["n_plants"] + last["n_fungi"]),
                "et_early": _et(r.metrics, EARLY), "et_final": float(last["expressed_trade"]),
            })
        print(f"  {param}={v}: done")
    return pd.DataFrame(rows)


def summarize(df, param):
    g = df.groupby(param)
    return pd.DataFrame({
        param: list(g.groups.keys()),
        "collapse_rate": g["collapsed"].mean().values,
        "mean_total": g["total"].mean().values,
        "sd_total": g["total"].std().values,
        "mean_et_early": g["et_early"].mean().values,
        "mean_et_final": g["et_final"].mean().values,
    })


def fig_stability(s, param, xlabel, path):
    fig, ax1 = plt.subplots(figsize=(6, 4))
    ax1.plot(s[param], s["collapse_rate"], "o-", color="#c1121f", label="collapse rate")
    ax1.set_xlabel(xlabel); ax1.set_ylabel("collapse rate", color="#c1121f"); ax1.set_ylim(-0.05, 1.05)
    ax2 = ax1.twinx()
    ax2.plot(s[param], s["mean_total"], "s--", color="#2a9d8f")
    ax2.set_ylabel("mean final population", color="#2a9d8f")
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


def fig_cooperation(s, param, xlabel, path):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(s[param], s["mean_et_early"], "o-", color="#adb5bd", label=f"generation {EARLY}")
    ax.plot(s[param], s["mean_et_final"], "s-", color="#2a9d8f", label=f"generation {GENS}")
    ax.axhline(1 / 3, ls=":", color="#c1121f", label="random baseline (1/3)")
    ax.set_xlabel(xlabel); ax.set_ylabel("fraction of agents choosing to TRADE"); ax.set_ylim(0, 0.6); ax.legend()
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


def fig_coop_time(path):
    r = run_single(replace(SimulationConfig(seed=1), mutation_rate=0.1), GENS)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(r.metrics["generation"], r.metrics["expressed_trade"], color="#2a9d8f")
    ax.axhline(1 / 3, ls=":", color="#c1121f", label="random baseline (1/3)")
    ax.set_xlabel("generation"); ax.set_ylabel("fraction of agents choosing to TRADE"); ax.set_ylim(0, 0.6); ax.legend()
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


def main():
    print("Experiment A: mutation rate")
    mut = run_grid("mutation_rate", [0.0, 0.05, 0.1, 0.2, 0.35, 0.5])
    mut.to_csv(RES / "mutation_raw.csv", index=False)
    ms = summarize(mut, "mutation_rate"); ms.to_csv(RES / "mutation_summary.csv", index=False)
    fig_stability(ms, "mutation_rate", "mutation rate", FIG / "mutation_stability.png")
    fig_cooperation(ms, "mutation_rate", "mutation rate", FIG / "mutation_cooperation.png")

    print("Experiment B: phosphorus density")
    pho = run_grid("phosphorus_density", [0.1, 0.15, 0.2, 0.3, 0.5, 0.7])
    pho.to_csv(RES / "phosphorus_raw.csv", index=False)
    ps = summarize(pho, "phosphorus_density"); ps.to_csv(RES / "phosphorus_summary.csv", index=False)
    fig_stability(ps, "phosphorus_density", "soil phosphorus density", FIG / "phosphorus_stability.png")

    print("Experiment C: soil phosphorus regeneration")
    reg = run_grid("phosphorus_regen", [0.0, 0.0025, 0.005, 0.0075, 0.01, 0.02, 0.05])
    reg.to_csv(RES / "regen_raw.csv", index=False)
    rs = summarize(reg, "phosphorus_regen"); rs.to_csv(RES / "regen_summary.csv", index=False)
    fig_stability(rs, "phosphorus_regen", "soil phosphorus regeneration per tick", FIG / "regen_collapse.png")

    print("Cooperation over time")
    fig_coop_time(FIG / "cooperation_over_time.png")

    print("\n=== mutation ==="); print(ms.to_string(index=False))
    print("\n=== phosphorus density ==="); print(ps.to_string(index=False))
    print("\n=== regen ==="); print(rs.to_string(index=False))
    print(f"\nseeds/point: {len(SEEDS)}, generations: {GENS}")


if __name__ == "__main__":
    main()

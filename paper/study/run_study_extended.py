"""Extended experiments for the AMS paper: mutation x regeneration interaction,
grid-scale robustness, and the state-level mechanism of selected cooperation."""
from dataclasses import replace
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from symbiogrid.model.config import SimulationConfig
from symbiogrid.model.model import SymbioModel
from symbiogrid.model.agents.plant import PlantAgent
from symbiogrid.model.agents.fungi import FungiAgent
from symbiogrid.science.runner import run_single

HERE = Path(__file__).resolve().parent
RES = HERE / "results"
FIG = HERE.parent / "figures"
RES.mkdir(parents=True, exist_ok=True)
FIG.mkdir(parents=True, exist_ok=True)


def exp_interaction():
    print("Experiment D: mutation x regeneration")
    rows = []
    for mut in [0.0, 0.1, 0.35]:
        for regen in [0.0, 0.0025, 0.005, 0.0075, 0.01]:
            coll = 0
            for s in range(1, 11):
                r = run_single(replace(SimulationConfig(seed=s), mutation_rate=mut, phosphorus_regen=regen), 300)
                coll += r.collapsed
            rows.append({"mutation_rate": mut, "phosphorus_regen": regen, "collapse_rate": coll / 10})
        print(f"  mutation {mut}: done")
    df = pd.DataFrame(rows)
    df.to_csv(RES / "interaction_summary.csv", index=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    for mut, sub in df.groupby("mutation_rate"):
        ax.plot(sub["phosphorus_regen"], sub["collapse_rate"], "o-", label=f"mutation {mut}")
    ax.set_xlabel("soil phosphorus regeneration per tick"); ax.set_ylabel("collapse rate")
    ax.set_ylim(-0.05, 1.05); ax.legend()
    fig.tight_layout(); fig.savefig(FIG / "interaction_collapse.png", dpi=150); plt.close(fig)
    return df


def exp_scale():
    print("Experiment E: grid-scale robustness")
    rows = []
    for (w, h) in [(40, 25), (60, 40), (80, 50)]:
        for regen in [0.0, 0.0025, 0.005, 0.05]:
            coll = 0
            for s in range(1, 7):
                r = run_single(replace(SimulationConfig(seed=s), width=w, height=h, phosphorus_regen=regen), 400)
                coll += r.collapsed
            rows.append({"grid": f"{w}x{h}", "phosphorus_regen": regen, "collapse_rate": coll / 6})
        print(f"  grid {w}x{h}: done")
    df = pd.DataFrame(rows)
    df.to_csv(RES / "scale_summary.csv", index=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    for grid, sub in df.groupby("grid"):
        ax.plot(sub["phosphorus_regen"], sub["collapse_rate"], "o-", label=grid)
    ax.set_xlabel("soil phosphorus regeneration per tick"); ax.set_ylabel("collapse rate")
    ax.set_ylim(-0.05, 1.05); ax.legend(title="grid")
    fig.tight_layout(); fig.savefig(FIG / "scale_collapse.png", dpi=150); plt.close(fig)
    return df


def _trade_by_context(model):
    # among living agents, TRADE propensity split by whether a trade partner is adjacent
    with_p = [0, 0]  # [trade, total]
    without_p = [0, 0]
    for a in list(model.agents):
        if not a.alive:
            continue
        a.sense(); a.deliberate()
        key = "plant_neighbors" if isinstance(a, FungiAgent) else "fungi_neighbors"
        bucket = with_p if a.beliefs.get(key) else without_p
        bucket[1] += 1
        if a.intention == "TRADE":
            bucket[0] += 1
    return with_p, without_p


def exp_mechanism():
    print("Experiment F: state-level mechanism")
    wp = [0, 0]; np_ = [0, 0]
    for s in range(1, 11):
        m = SymbioModel(replace(SimulationConfig(seed=s), mutation_rate=0.1))
        for _ in range(300):
            m.step()
        a, b = _trade_by_context(m)
        wp[0] += a[0]; wp[1] += a[1]; np_[0] += b[0]; np_[1] += b[1]
    frac_wp = wp[0] / wp[1] if wp[1] else float("nan")
    frac_np = np_[0] / np_[1] if np_[1] else float("nan")
    df = pd.DataFrame([
        {"context": "trade partner adjacent", "trade_fraction": frac_wp, "n": wp[1]},
        {"context": "no trade partner", "trade_fraction": frac_np, "n": np_[1]},
    ])
    df.to_csv(RES / "mechanism_summary.csv", index=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(df["context"], df["trade_fraction"], color=["#2a9d8f", "#adb5bd"])
    ax.axhline(1 / 3, ls=":", color="#c1121f", label="random baseline (1/3)")
    ax.set_ylabel("fraction of agents choosing to TRADE"); ax.set_ylim(0, 0.6); ax.legend()
    fig.tight_layout(); fig.savefig(FIG / "mechanism_context.png", dpi=150); plt.close(fig)
    return df


def main():
    d = exp_interaction()
    e = exp_scale()
    f = exp_mechanism()
    print("\n=== interaction (collapse rate) ==="); print(d.to_string(index=False))
    print("\n=== scale (collapse rate) ==="); print(e.to_string(index=False))
    print("\n=== mechanism (trade fraction by context) ==="); print(f.to_string(index=False))


if __name__ == "__main__":
    main()

import argparse
import math
from dataclasses import replace
from pathlib import Path
from symbiogrid.model.config import SimulationConfig, PRESETS
from symbiogrid.science.runner import run_batch
from symbiogrid.science.export import export_batch


def _parse_seeds(text: str) -> list[int]:
    return [int(s) for s in text.split(",") if s.strip()]


def _coerce(value: str):
    for cast in (int, float):
        try:
            return cast(value)
        except ValueError:
            continue
    return value


def _parse_sweeps(specs: list[str]) -> dict:
    sweeps = {}
    for spec in specs or []:
        key, _, values = spec.partition("=")
        sweeps[key.strip()] = [_coerce(v.strip()) for v in values.split(",") if v.strip()]
    return sweeps


def main() -> None:
    parser = argparse.ArgumentParser(prog="symbiogrid.science", description="Headless batch runner for Symbio-Grid.")
    parser.add_argument("--preset", default="Random", choices=list(PRESETS.keys()), help="Base configuration preset.")
    parser.add_argument("--seeds", default="1,2,3", help="Comma-separated integer seeds.")
    parser.add_argument("--gens", type=int, default=500, help="Max generations per run.")
    parser.add_argument("--out", default="science_output", help="Output directory.")
    parser.add_argument("--sweep", action="append", metavar="KEY=V1,V2", help="Config sweep, e.g. --sweep mutation_rate=0.05,0.1,0.2 (repeatable).")
    parser.add_argument("--no-collapse-stop", action="store_true", help="Run the full horizon even if a species dies out.")
    parser.add_argument("--smoke", action="store_true", help="Fast CI run: seeds 1,2 for 30 generations.")
    args = parser.parse_args()

    base = replace(PRESETS[args.preset])
    seeds = _parse_seeds(args.seeds)
    sweeps = _parse_sweeps(args.sweep)
    gens = args.gens
    out = Path(args.out)
    if args.smoke:
        seeds, gens, out = [1, 2], 30, out / "smoke"

    combos = len(seeds) * math.prod(len(v) for v in sweeps.values())
    print(f"Running {combos} run(s) of preset '{args.preset}' for up to {gens} generations...")
    results = run_batch(base, seeds, gens, sweeps=sweeps, stop_on_collapse=not args.no_collapse_stop)
    export_batch(results, out)
    for r in results:
        state = "COLLAPSED" if r.collapsed else "stable"
        print(f"  seed {r.config.seed}: gen {r.final_generation:>4} [{state}] survivors {len(r.dna)}")
    print(f"Wrote {len(results)} run(s) to {out.resolve()}")


if __name__ == "__main__":
    main()

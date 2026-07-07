import json
import subprocess
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd
from symbiogrid.science.runner import RunResult


def code_version() -> str:
    try:
        out = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=Path(__file__).resolve().parent)
        if out.returncode == 0:
            return out.stdout.strip()
    except OSError:
        pass
    return "unknown"


def _versions() -> dict:
    import mesa, numpy
    return {"mesa": mesa.__version__, "numpy": numpy.__version__}


def export_run(result: RunResult, outdir: Path, stamp: bool = True) -> Path:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    result.metrics.to_csv(outdir / "metrics.csv", index=False)
    result.metrics.to_parquet(outdir / "metrics.parquet", index=False)
    dna = pd.DataFrame(result.dna)
    dna.to_csv(outdir / "dna.csv", index=False)
    if not dna.empty:
        dna.to_parquet(outdir / "dna.parquet", index=False)
    manifest = {
        "config": asdict(result.config),
        "seed": result.config.seed,
        "code_version": code_version(),
        "final_generation": result.final_generation,
        "collapsed": result.collapsed,
        "n_survivors": len(result.dna),
        "libraries": _versions(),
    }
    if stamp:
        manifest["generated_utc"] = datetime.now(timezone.utc).isoformat()
    (outdir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True))
    return outdir


def export_batch(results: list[RunResult], outdir: Path, stamp: bool = True) -> Path:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    summary = []
    for i, result in enumerate(results):
        run_dir = outdir / f"run_{i:03d}_seed{result.config.seed}"
        export_run(result, run_dir, stamp=stamp)
        summary.append({
            "run": i,
            "seed": result.config.seed,
            "final_generation": result.final_generation,
            "collapsed": result.collapsed,
            "n_survivors": len(result.dna),
        })
    pd.DataFrame(summary).to_csv(outdir / "batch_summary.csv", index=False)
    batch_manifest = {
        "n_runs": len(results),
        "code_version": code_version(),
        "libraries": _versions(),
    }
    if stamp:
        batch_manifest["generated_utc"] = datetime.now(timezone.utc).isoformat()
    (outdir / "batch_manifest.json").write_text(json.dumps(batch_manifest, indent=2, sort_keys=True))
    return outdir

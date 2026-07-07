<p align="center">
  <img src="assets/logo.svg" alt="Symbio-Grid — an educational agent-based model and teaching tool for plant–fungi symbiosis and the evolution of cooperation" width="560">
</p>

# Symbio-Grid — An Educational Agent-Based Model of Plant–Fungi Symbiosis

![Python](https://img.shields.io/badge/python-3.11--3.13-3776AB?logo=python&logoColor=white)
![Mesa](https://img.shields.io/badge/mesa-3.x-4CAF50?logo=python&logoColor=white)
![Type](https://img.shields.io/badge/type-educational%20tool-4CAF50)
![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License](https://img.shields.io/badge/license-GNU%20GPL%20v3-blue)
![ORCID](https://img.shields.io/badge/ORCID-0000--0002--8300--7587-A6CE39?logo=orcid&logoColor=white)

**Symbio-Grid** is an open-source **educational tool** and **agent-based model (ABM)** for
teaching **emergence** and the **evolution of cooperation**. Plant and fungi agents trade
carbon and phosphorus under behavioral rules that **evolve by mutation and selection**, so a
stable symbiotic economy is not programmed but **emerges — or collapses**. Students explore
it two ways from one model: an **interactive visualization** to build intuition by watching
and steering the ecosystem, and a **headless, reproducible science mode** to turn hypotheses
into controlled, shareable experiments. Built on the [Mesa](https://mesa.readthedocs.io/)
framework in Python.

**Keywords:** educational tool, teaching resource, agent-based model, evolution of
cooperation, emergence, complex adaptive systems, classroom simulation, computational
science education, STEM, mycorrhizal symbiosis, plant–fungi interaction, Mesa, Python,
reproducible open science.

---

## Highlights

- **Built for teaching.** One model, two coupled modes — an interactive visualization to
  build intuition, and a reproducible science mode to test hypotheses — so a class moves
  from *observe* to *hypothesize* to *test* in a single session. See the ready-to-adopt lab
  in [`docs/teaching_tutorial.md`](docs/teaching_tutorial.md).
- **Emergence you can watch.** Trade, reproduction, and mutation produce a self-sustaining
  plant–fungi economy that persists for thousands of generations, or collapses under stress
  presets like *Climate Shock* — cooperation is selected, never hard-coded.
- **Reproducible by construction.** A fixed seed yields byte-identical output; every run
  ships a manifest with config, seed, and code version — ideal for gradeable assignments.
- **Open and lightweight.** GPLv3, pure Python, programmatic sprites (no binary assets),
  CSV/Parquet exports for downstream analysis.

---

## Two modes, one model

| Mode | Command | Purpose |
|---|---|---|
| Interactive | `python -m symbiogrid.game` | Real-time visualization to observe and steer the ecosystem — for the classroom and self-learning |
| Science | `python -m symbiogrid.science` | Headless batch runner: reproducible experiments, CSV/Parquet export |

Both run the same Mesa simulation core.

---

## Structure

```
symbiogrid/
│
├── model/                   # Shared simulation core (Mesa)
│   ├── model.py             # SymbioModel — orchestrates the grid and scheduler
│   ├── config.py            # SimulationConfig dataclass + presets
│   ├── agents/
│   │   ├── base.py          # BDI interface shared by all agents
│   │   ├── plant.py         # PlantAgent — stationary, makes Carbon, needs Phosphorus
│   │   └── fungi.py         # FungiAgent — mycelial, forages Phosphorus, needs Carbon
│   └── rules/
│       ├── rule_table.py    # Bit-string rule table + query logic (seeded RNG)
│       └── genetics.py      # Stochastic mutation and crossover
│
├── game/                    # Phase 1 — Pygame frontend
│   ├── app.py               # Game loop
│   ├── renderer.py          # Draws agents and resource heatmaps
│   ├── hud.py               # Top bar (gen/speed) and bottom bar (stats)
│   ├── sprites/             # Plant and fungi shapes drawn with pygame.draw
│   └── screens/             # Start screen (presets/seed/sliders) and sim viewport
│
└── science/                 # Phase 2 — Headless batch runner
    ├── runner.py            # Runs N simulations across seeds and config sweeps
    ├── collector.py         # Mesa DataCollector + per-agent rule-table "DNA"
    └── export.py            # CSV / Parquet output + reproducibility manifest
```

---

## Setup

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Use Python 3.11–3.13 (pygame has no 3.14 wheels yet).

## Run the interactive mode

```powershell
python -m symbiogrid.game
```

Pick a preset (*Sparse Forest*, *Dense Bloom*, *Climate Shock*, *Random*), a grid size,
and an optional seed, then watch plants and fungi trade and evolve. Pause with `Space`,
change speed with `←`/`→`, pan with mouse drag, wheel, arrow keys, `A`/`D`, and `Home`.

## Run the science batch

```powershell
python -m symbiogrid.science --smoke                       # fast CI run (seeds 1,2 x 30 gens)
python -m symbiogrid.science --seeds 1,2,3 --gens 500      # reproducible batch
python -m symbiogrid.science --sweep mutation_rate=0.05,0.1,0.2 --seeds 1,2
```

Each run writes `metrics.csv`/`metrics.parquet` (per-tick population and resource
series), `dna.csv`/`dna.parquet` (surviving agents' evolved rule-tables), and a
`manifest.json` with config, seed, git version, and library versions. Output lands in
`science_output/` (git-ignored). Re-running the same seeds yields byte-identical metrics.

---

## Teaching

Symbio-Grid is built to teach emergence and the evolution of cooperation: students use the
interactive mode to build intuition, then test hypotheses reproducibly in the science mode.
A ready-to-adopt lab (observe → hypothesize → test → interpret) is in
[`docs/teaching_tutorial.md`](docs/teaching_tutorial.md).

---

## Science output and publishing

Each experiment exports the agent rule-table "DNA" of surviving ecosystems alongside
per-tick resource and population metrics — intended for an open, FAIR dataset on Zenodo
under Felipe Carvajal Brown (UPM, ORCID
[0000-0002-8300-7587](https://orcid.org/0000-0002-8300-7587)). See
[`docs/publishing_research.md`](docs/publishing_research.md) for a survey of candidate
venues (Zenodo, JOSS, SoftwareX, JASSS, Artificial Life, Ecological Modelling) and what
each requires.

## Citation

If you use Symbio-Grid, please cite it. A Zenodo DOI will be minted on first release:

```
Carvajal Brown, F. (2026). Symbio-Grid: an evolutionary agent-based model of
plant–fungi symbiosis (Version 0.x) [Software]. Zenodo. DOI: <pending first release>
```

## License

Released under the **GNU General Public License v3.0** — see [`LICENSE`](LICENSE).

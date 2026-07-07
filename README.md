<p align="center">
  <img src="assets/logo.svg" alt="Symbio-Grid — an evolutionary mycelial automaton (agent-based model of plant–fungi symbiosis)" width="560">
</p>

# Symbio-Grid — Evolutionary Agent-Based Model of Plant–Fungi Symbiosis

![Python](https://img.shields.io/badge/python-3.11--3.13-3776AB?logo=python&logoColor=white)
![Mesa](https://img.shields.io/badge/mesa-3.x-4CAF50?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/pygame-2.x-E87D0D?logo=python&logoColor=white)
![Phase](https://img.shields.io/badge/phase-2%20science-blueviolet)
![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License](https://img.shields.io/badge/license-GNU%20GPL%20v3-blue)
![itch.io](https://img.shields.io/badge/itch.io-game-FA5C5C?logo=itch.io&logoColor=white)
![ORCID](https://img.shields.io/badge/ORCID-0000--0002--8300--7587-A6CE39?logo=orcid&logoColor=white)

**Symbio-Grid** is an open-source **agent-based model (ABM)** and simulation game of an
**evolving mycorrhizal bio-economy**. Stationary plant agents and mycelial fungi agents
trade carbon and phosphorus and **mutate their rule-tables across generations** under a
BDI (belief–desire–intention) architecture, until a stable symbiotic equilibrium
**emerges — or collapses**. Built on the [Mesa](https://mesa.readthedocs.io/) framework
in Python, it ships as both a real-time **Pygame** visualization and a headless,
reproducible **scientific batch runner** for experiments and open data.

**Keywords:** agent-based model, mycorrhizal symbiosis, plant–fungi interaction,
evolutionary simulation, artificial life, emergent behavior, complex adaptive systems,
Mesa, Python, BDI agents, rule-table evolution, reproducible open science.

---

## Highlights

- **Two programs, one simulation core.** A playable Pygame front-end and a headless
  Mesa science runner share the same model, agents, and evolving rule-tables.
- **Emergent symbiosis.** Trade, reproduction, and mutation produce a self-sustaining
  plant–fungi economy that persists for thousands of generations, or collapses under
  stress presets like *Climate Shock*.
- **Reproducible by construction.** A fixed seed yields byte-identical metric output;
  every run ships a manifest with config, seed, and code version.
- **Open and FAIR-ready.** GPLv3, programmatic sprites (no binary assets), CSV/Parquet
  exports plus an "Emergent Rule-Set Library" intended for a citable Zenodo dataset.

---

## Programs

| Program | Command | Purpose |
|---|---|---|
| Game | `python -m symbiogrid.game` | Pygame window, real-time simulation, itch.io |
| Science | `python -m symbiogrid.science` | Headless batch runner, CSV/Parquet export, Zenodo |

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

## Run the game

```powershell
python -m symbiogrid.game
```

Pick a preset (*Sparse Forest*, *Dense Bloom*, *Climate Shock*, *Random*), a grid size,
and an optional seed, then watch trees and fungi trade and evolve. Pause with `Space`,
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

Symbio-Grid is built to teach emergence and the evolution of cooperation: students play
the game to build intuition, then test hypotheses reproducibly in the science mode. A
ready-to-adopt lab (observe → hypothesize → test → interpret) is in
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

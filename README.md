# Symbio-Grid

![Python](https://img.shields.io/badge/python-3.11+-3776AB?logo=python&logoColor=white)
![Mesa](https://img.shields.io/badge/mesa-2.x-4CAF50?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/pygame-2.x-E87D0D?logo=python&logoColor=white)
![Phase](https://img.shields.io/badge/phase-1%20game-blueviolet)
![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License](https://img.shields.io/badge/license-GNU%20GPL%20v3-blue)
![itch.io](https://img.shields.io/badge/itch.io-game-FA5C5C?logo=itch.io&logoColor=white)
![ORCID](https://img.shields.io/badge/ORCID-0000--0002--8300--7587-A6CE39?logo=orcid&logoColor=white)

An evolutionary mycelial automaton. Plant and fungi agents trade resources and mutate their rule-tables across generations until a stable bio-economy emerges — or collapses.

Two programs, one repo.

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
│   ├── config.py            # SimulationConfig dataclass
│   ├── agents/
│   │   ├── base.py          # BDI interface shared by all agents
│   │   ├── plant.py         # PlantAgent — stationary, produces Carbon, needs Phosphorus
│   │   └── fungi.py         # FungiAgent — mobile, finds Phosphorus, needs Carbon
│   └── rules/
│       ├── rule_table.py    # Bit-string rule table + query logic
│       └── genetics.py      # Stochastic mutation and crossover
│
├── game/                    # Phase 1 — Pygame frontend
│   ├── __main__.py          # Entry point
│   ├── app.py               # Game loop
│   ├── renderer.py          # Draws agents and resource heatmaps
│   ├── hud.py               # Top bar (gen/speed) and bottom bar (stats)
│   ├── sprites/
│   │   ├── plant.py         # Plant shape drawn with pygame.draw
│   │   └── fungi.py         # Fungi shape drawn with pygame.draw
│   └── screens/
│       ├── start.py         # Preset picker, seed input, parameter sliders
│       └── sim.py           # Simulation screen with scrollable viewport
│
└── science/                 # Phase 2 — Headless batch runner
    ├── __main__.py          # Entry point
    ├── runner.py            # Runs N simulations across seeds/configs
    ├── collector.py         # Mesa DataCollector configuration
    └── export.py            # Writes CSV / Parquet output
```

---

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
python -m symbiogrid.game
python -m symbiogrid.science
```

---

## Science output

Each experiment run exports the agent rule-table "DNA" of surviving ecosystems alongside per-tick resource and population metrics. Intended for publication on Zenodo under Felipe Carvajal Brown (UPM, ORCID 0000-0002-8300-7587).

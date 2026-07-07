---
title: 'Symbio-Grid: an evolutionary agent-based model of plant--fungi resource symbiosis'
tags:
  - Python
  - agent-based modeling
  - Mesa
  - artificial life
  - evolutionary simulation
  - mycorrhizal symbiosis
  - complex adaptive systems
authors:
  - name: Felipe Carvajal Brown
    orcid: 0000-0002-8300-7587
    affiliation: 1
affiliations:
  - name: Universidad Politécnica de Madrid, Madrid, Spain
    index: 1
date: 7 July 2026
bibliography: paper.bib
---

# Summary

`Symbio-Grid` is an open-source agent-based model (ABM) of an evolving resource
economy between plants and fungi. On a toroidal grid, stationary plant agents
photosynthesize carbon but depend on phosphorus, while mycelial fungi agents forage
phosphorus from the soil but depend on carbon. Neither species survives alone: they
must barter. Each agent acts under a belief--desire--intention (BDI) loop and decides
what to do by querying an evolvable bit-string *rule-table* that maps a discretized
perception of its local state to an action (trade, reproduce, or idle). Offspring
inherit their parent's rule-table with stochastic mutation, so the population's
behavioral strategies evolve across generations under selection for survival. From
random initial rule-tables and no hand-coded cooperation, a self-sustaining symbiotic
economy typically emerges — or, under stressed conditions, collapses.

The software ships as two programs over one simulation core: a real-time `Pygame`
visualization for teaching and outreach, and a headless batch runner for reproducible
experiments that exports per-tick population and resource time series, the evolved
rule-tables ("DNA") of surviving agents, and a run manifest. The simulation core is
built on the `Mesa` framework [@terhoeven2025mesa; @masad2015mesa].

# Statement of need

Agent-based models are a standard tool for studying how macro-level order emerges from
local interaction, but usable ABMs tend to fall into one of two camps. Research-grade
models emphasize reproducible data but are often opaque to newcomers and lack an
accessible, real-time visual mode; simulation *games* are engaging but rarely export
clean, reproducible scientific data or expose their mechanics for study. `Symbio-Grid`
targets the gap between them: the same Mesa model drives both an interactive window and
a deterministic, seed-reproducible batch runner, so an instructor can demonstrate
evolving cooperation live and a researcher can then run the identical dynamics headless
and obtain byte-identical CSV/Parquet output.

The model is also a compact, self-contained testbed for a specific and pedagogically
rich question: how do mutualistic trading strategies arise and persist when they are not
imposed but must evolve? Cooperation here is not assumed; it is an emergent, selectable
behavior encoded in each agent's rule-table. Because every rate is a configuration
field and every run is reproducible, the model is well suited to parameter sweeps and
sensitivity analysis over mutation rate, soil phosphorus regeneration, uptake, and
resource-decay costs. The target audience is students and researchers in artificial
life, evolutionary and ecological modeling, and complex adaptive systems, as well as
educators who want a visual, hands-on entry point to these ideas.

# State of the field

`Symbio-Grid` is built on `Mesa`, a widely used Python ABM framework
[@terhoeven2025mesa; @masad2015mesa], and follows community norms for describing ABMs
such as the ODD protocol [@grimm2020odd]. General-purpose ABM platforms (Mesa, NetLogo)
provide the scaffolding for building models but not a specific, ready-to-study model of
evolving symbiosis. In the ecological literature, mycorrhizal exchange has been modeled
with network and economic-market formulations [@simard2012mycorrhizal]; those models
target quantitative ecological realism rather than an accessible, dual-mode teaching and
experimentation tool with explicitly *evolving* per-agent decision rules. `Symbio-Grid`
occupies that niche: a lightweight, dependency-light, GPL-licensed model in which the
unit of evolution is an interpretable rule-table, packaged with both a game front-end
and a reproducible science runner.

# Software design

The shared core (`symbiogrid/model`) defines a `Mesa` `Model` that owns a `MultiGrid`
and a soil-phosphorus field, plus `PlantAgent` and `FungiAgent` classes over a common
BDI base (`sense` / `deliberate` / `act`). Decision-making is factored into a
`RuleTable`: the agent encodes its local perception (own carbon, own phosphorus, number
of relevant neighbors) as an integer index and looks up an action. `RuleTable`
implements mutation and crossover, so strategies are heritable and evolvable. A key
design choice is that all stochasticity — rule-table initialization, mutation, and agent
choices — is drawn from the model's seeded random number generator, which makes a run
byte-identical under a fixed seed. This determinism is what lets the same core serve a
real-time game and a scientific instrument without divergence.

The front-end (`symbiogrid/game`) is a `Pygame` application with a start screen
(presets, grid size, seed, parameter sliders) and a pannable simulation viewport; all
sprites are drawn programmatically, so the project carries no binary image assets. The
science layer (`symbiogrid/science`) wraps the core with a `Mesa` `DataCollector` for
per-tick metrics, a snapshot of every surviving agent's rule-table, and an exporter that
writes CSV and Parquet alongside a JSON manifest recording the configuration, seed, code
version, and library versions for full reproducibility. A command-line interface runs
single seeds, seed batches, and configuration sweeps, with a stopping condition for
ecological collapse and a fast smoke run for continuous integration.

# Research impact statement

`Symbio-Grid` is a new project. Its near-term intended impact is twofold: as a teaching
instrument that makes the emergence and evolution of cooperation visible and tangible in
real time, and as a reproducible experimental platform for small studies of how evolved
rule-sets respond to environmental stress — for example, which behavioral strategies
survive the bundled "Climate Shock" preset (low phosphorus, high mutation). Because the
model is fully deterministic under seed and every rate is exposed for sweeping, results
are straightforward to replicate and extend. The reproducible export of an "emergent
rule-set library" is intended to support open, citable datasets.

# AI usage disclosure

<!-- REQUIRED by JOSS, and it conflicts with the project's no-AI-mention rule.
     Left blank intentionally for the author to complete before submission. See the
     handoff notes accompanying this package. Do not submit without resolving this. -->
[To be completed by the author before submission.]

# Acknowledgements

This work received no external funding.

# References

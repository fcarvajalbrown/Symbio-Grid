---
title: 'Symbio-Grid: a playable, reproducible agent-based model for teaching the evolution of cooperation'
tags:
  - Python
  - agent-based modeling
  - Mesa
  - education
  - artificial life
  - evolution of cooperation
  - complex systems
authors:
  - name: Felipe Carvajal Brown
    orcid: 0000-0002-8300-7587
    affiliation: 1
affiliations:
  - name: Universidad Politécnica de Madrid, Madrid, Spain
    index: 1
date: 7 July 2026
bibliography: ../paper.bib
---

# Summary

`Symbio-Grid` is an open-source agent-based model (ABM) designed for teaching how
cooperation, evolution, and ecological equilibrium emerge from simple local rules. On a
grid, plant agents make carbon but need phosphorus, while mycelial fungi agents forage
phosphorus but need carbon; neither survives alone, so they must trade. Each agent
decides what to do by querying an evolvable rule-table, and offspring inherit that table
with mutation — so cooperative strategies are not programmed in, they evolve under
selection. The same simulation core runs in two modes: a real-time `Pygame` game where
students watch and steer an ecosystem, and a headless, seed-reproducible batch runner
where they turn observations into controlled experiments. It is built on `Mesa`
[@terhoeven2025mesa; @masad2015mesa], uses no binary assets (all sprites are drawn in
code), and is released under the GPL.

# Statement of need

The evolution of cooperation, emergence, and resource mutualism are central ideas in
biology, ecology, complex systems, and computational social science, but they are
abstract and hard to build intuition for from equations alone. Instructors need a tool
that is (1) immediately engaging, so students form intuitions and hypotheses by playing,
and (2) rigorous, so those hypotheses can be tested reproducibly rather than
anecdotally. Most available resources sit on one side of that line: research individual-
based models of plant--fungal trade [@simard2012mycorrhizal] are rigorous but not
approachable, while classroom simulations are approachable but rarely export clean,
reproducible data or expose their evolving decision rules for study.

`Symbio-Grid` is built to bridge that gap for a course or lab. A student can open the
game, choose a preset (including a "Climate Shock" scenario of scarce phosphorus and
high mutation), and watch whether a stable trading economy emerges or collapses. They can
then form a hypothesis — for example, "higher mutation destabilizes cooperation" — and
test it with the batch runner across seeds and parameter sweeps, obtaining byte-identical
results that a whole class can compare and reproduce. Because the unit of evolution is an
interpretable bit-string rule-table, advanced students can inspect the actual evolved
"DNA" of surviving agents. The target audience is undergraduate and graduate instructors
and students in evolutionary biology, ecology, artificial life, and complex-systems or
agent-based-modeling courses, and self-learners exploring these ideas.

Symbio-Grid deliberately covers a topic that existing tools also touch (Mesa ships
ecological examples, and NetLogo has mutualism models). Its contribution is pedagogical:
one deterministic model presented in two coupled modes — play to build intuition, then
reproduce to build rigor — with no setup friction (pure-Python, `pip`-installable, no
assets) and a clear path from a live observation to a controlled, shareable experiment.

The two-mode design maps onto a simple inquiry cycle that students can complete in a
single session: *observe* (play the game and describe what happens), *hypothesize* (state
a testable claim about a parameter), *test* (run seeded sweeps in the science mode),
*interpret* (read the exported metrics and evolved rule-tables), and *communicate* (share
byte-identical results a peer can reproduce). This makes abstract claims about emergence
and selection concrete and falsifiable, which is difficult to achieve with a static
lecture demonstration or a black-box simulation that cannot export reproducible data.

# Instructional design and use

The game's start screen exposes the model's levers as presets, a grid-size choice, a
seed field, and sliders for carbon density, phosphorus density, and mutation rate, so a
class can agree on a configuration and all reproduce it. Suggested classroom activities:

- *Emergence of cooperation:* run the default preset and track the plant/fungi ratio and
  average resources in the on-screen stats; discuss why trading strategies win.
- *Sensitivity study:* use `symbiogrid-science --sweep mutation_rate=0.05,0.1,0.2 --seeds
  1,2,3` and compare survival and population trajectories across the exported CSVs.
- *Resilience under stress:* compare the "Climate Shock" preset against a stable one and
  ask which evolved rule-sets persist.

Every science run exports per-tick population and resource time series, the evolved
rule-tables of surviving agents, and a manifest recording configuration, seed, and code
version, so results are fully reproducible and gradeable.

By the end of these activities a student should be able to: explain how a global pattern
(a stable trading economy) can arise from local rules without central control; describe
selection acting on heritable, mutable strategies; read and reason about an evolved
rule-table; and design, run, and report a controlled computational experiment with a
stated seed and configuration. Advanced students can extend the model itself — adding an
action to a species' rule-table or changing the perception encoding — turning the tool
from an object of study into a small modelling project. A companion walkthrough of these
activities ships with the repository so an instructor can adopt them directly.

# Software design

A shared `Mesa` core (`symbiogrid/model`) defines the grid, a soil-phosphorus field, and
plant/fungi agents over a common sense--deliberate--act loop; decisions are factored into
an evolvable `RuleTable` with mutation and crossover. All randomness draws from the
model's seeded generator, which makes runs byte-identical under a fixed seed — the
property that lets the same core power both a game and a reproducible instrument without
divergence. The `Pygame` front-end (`symbiogrid/game`) provides the interactive window;
the science layer (`symbiogrid/science`) wraps the core with a `Mesa` `DataCollector`, a
rule-table snapshot, and CSV/Parquet export with a run manifest, plus a command-line
interface with a fast smoke run for continuous integration. An automated test suite
covers determinism, resource conservation, and reproducibility.

# AI usage disclosure

<!-- Verify whether JOSE requires this section; JOSS does. It conflicts with the
     project's no-AI-mention rule. Left for the author to complete before submission. -->
[To be completed by the author before submission.]

# Acknowledgements

This work received no external funding.

# References

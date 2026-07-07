---
title: "Emergent and evolvable resource-trading mutualism in Symbio-Grid: an agent-based model of plant–fungi symbiosis under mutation and phosphorus stress"
author: "Felipe Carvajal Brown (Universidad Politécnica de Madrid, ORCID 0000-0002-8300-7587)"
date: "2026-07-07"
---

<!-- Target: Applications of Modelling and Simulation (AMS), free/Scopus/DOAJ. Convert to
     the AMS Word template before submission. Results/Discussion/Abstract are filled from
     paper/study/run_study.py output — do not edit numbers by hand; re-run the study. -->

## Abstract

We present Symbio-Grid, a spatial agent-based model in which plant and fungi agents trade
carbon and phosphorus under behavioral rules encoded in rule-tables that evolve by mutation
and selection, and we study when a stable trading mutualism emerges versus collapses. Across
ten seeds per condition we sweep the mutation rate, soil-phosphorus density, and phosphorus
regeneration rate, measuring collapse frequency, final population, and the fraction of agents
that actually choose to trade. Three results emerge. The mutualism is robust across mutation
rates (0.0–0.5) and phosphorus densities (0.1–0.7), collapsing only when renewable phosphorus
input approaches zero — a sharp resilience threshold near 0.005 units per tick. Cooperation
is selected rather than assumed: starting from random rule-tables, expressed trading rises
above the one-in-three chance level and, under resource scarcity, reaches nearly twice that
level among survivors. Finally, we show that this selection signal is visible only when
trading is measured over the states agents actually visit, not by averaging over the whole
rule-table — a methodological caution for evolvable-strategy models. The model and all
experiments are open source and reproducible from a fixed seed.

## 1. Introduction

Mutualism — cooperation between species that exchange resources — is widespread in nature,
yet how it arises and remains stable when partners could instead defect is a long-standing
question in ecology and complex-systems science. Mycorrhizal symbiosis, in which plants
supply fungi with carbon in exchange for soil phosphorus, is a canonical example and has
been described as a biological market [@simard2012mycorrhizal]. Agent-based modeling (ABM)
is well suited to studying such systems because macro-level order (a stable economy) can be
observed as an emergent product of simple local interactions [@terhoeven2025mesa].

This paper introduces *Symbio-Grid*, a spatial ABM in which the trading behavior of each
agent is not fixed but encoded in a rule-table that is inherited with mutation, so
cooperation must evolve rather than being imposed. We use the model to ask two questions:
(i) how does the mutation rate affect whether a stable trading economy emerges or
collapses, and (ii) how robust is the system to phosphorus scarcity? We also measure
directly whether selection drives evolved rule-tables toward trading.

## 2. Related work

Resource exchange in mycorrhizal symbiosis has been modeled with mathematical and
individual-based approaches. Recent work presents a plant–mycorrhizal fungal resource-trade
co-evolution model that reproduces mutualism stability, extinction, and transitory
parasitism through fitness feedback [@grasso2025tradecoevolution], and empirical and
modeling studies show fungi adjusting phosphorus "value" under abrupt resource crashes and
booms [@vantpadje2021phosphorus]. These emphasize quantitative ecological realism for a few
interacting partners. General ABM frameworks such as Mesa [@terhoeven2025mesa;
@masad2015mesa] provide ecological and evolving-strategy examples but not a specific,
reproducible study of evolvable trading mutualism with an interpretable strategy
representation. Symbio-Grid contributes a spatially explicit, fully reproducible model in
which the unit of evolution is a legible bit-string rule-table, released with both an
interactive and a headless mode.

## 3. Model description

The model is implemented on the Mesa framework and described here following the ODD
(Overview, Design concepts, Details) convention [@grimm2020odd].

### 3.1 Purpose
To study when an evolvable, spatially explicit plant–fungi resource-trading mutualism
reaches a stable equilibrium versus collapses, under varying mutation and resource stress.

### 3.2 Entities, state variables, and scales
Two agent types live on a toroidal `MultiGrid` of width W and height H. A **plant** is
stationary and holds carbon and phosphorus (each in [0, 20]). A **fungus** is mycelial and
also holds carbon and phosphorus. The environment holds a soil-phosphorus field, one scalar
per cell in [0, 10]. Each agent owns a **rule-table**: a length-64 string over three
actions, indexed by a discretized perception of its local state. One time step is one
generation.

### 3.3 Process overview and scheduling
Each step, all agents act in random order through a sense–deliberate–act loop: they perceive
their neighborhood, index their rule-table to select an action, and execute it. Dead agents
are then removed, soil phosphorus is replenished, and the generation counter advances. All
randomness is drawn from a single seeded generator, making each run byte-identical under its
seed.

### 3.4 Design concepts
*Emergence:* a persistent trading economy (or its collapse) is not coded but arises from
local trades and selection. *Adaptation:* offspring inherit the parent rule-table with
per-locus mutation. *Objective:* implicit survival — agents that fail to secure their
limiting resource die and leave no offspring. *Sensing:* an agent perceives its own
carbon/phosphorus, neighboring agents, and (for fungi) soil phosphorus in its Moore
neighborhood. *Interaction:* bilateral resource trade between adjacent plant and fungus.
*Stochasticity:* placement, rule-table initialization/mutation, and choices among equals.
*Observation:* per-tick populations and resources and end-state rule-tables are collected.

### 3.5 Initialization
N_p plants and N_f fungi are placed with fungi seated adjacent to plants so trade is
possible from the start. Soil phosphorus is drawn as Uniform(0, 10) scaled by a density
parameter. Plants start with carbon 5 and phosphorus 5; fungi with carbon 3 and phosphorus
5. All rule-tables are initialized uniformly at random.

### 3.6 Submodels
Per step, a plant gains 1.0 carbon (capped at 20) and loses `plant_p_decay` phosphorus; a
fungus draws up to `fungi_uptake` phosphorus from the richest cells in its Moore
neighborhood and loses `fungi_c_decay` carbon. If an agent's chosen action is TRADE and a
partner is adjacent, the two swap equal amounts (up to 2 units) of carbon for phosphorus.
Reproduction (plant SPROUT, fungi EXPAND) requires an empty neighbor and sufficient
resources; the child inherits a mutated rule-table and 40% of the parent's resources. An
agent dies when its limiting resource reaches zero. Soil phosphorus regenerates by
`phosphorus_regen` per cell per step (capped at 10).

## 4. Experimental setup

All experiments use the default grid and initial populations and are run for 300
generations with 10 random seeds each; a run is recorded as *collapsed* if either species
goes extinct. For each run we record the collapse outcome and the final total population.
To measure selection for cooperation we use an *expressed* metric: the fraction of living
agents that actually choose the TRADE action in the situation they are in, recorded per
tick. Because a randomly initialized rule-table selects any of the three actions with equal
probability, a value above 1/3 indicates that selection has enriched trading behavior. (We
deliberately avoid averaging TRADE over the whole 64-entry rule-table, because agents visit
only a few states, so the unexpressed majority of entries drift neutrally and mask the
signal — see Discussion.)

- **Experiment A — mutation rate:** sweep the per-locus mutation rate over
  {0.0, 0.05, 0.1, 0.2, 0.35, 0.5}.
- **Experiment B — phosphorus availability:** sweep soil-phosphorus density over
  {0.1, 0.15, 0.2, 0.3, 0.5, 0.7}.
- **Experiment C — phosphorus renewal:** sweep the soil-phosphorus regeneration rate over
  {0.0, 0.0025, 0.005, 0.0075, 0.01, 0.02, 0.05} to locate the resilience boundary.

The full study is reproducible via `paper/study/run_study.py`; parameter values, seeds, and
generation count are recorded there and in each run's manifest.

## 5. Results

All values are means over 10 seeds per parameter point; "±" denotes one standard
deviation of the final total population.

### 5.1 Mutation rate (Experiment A)
No run collapsed at any mutation rate from 0.0 to 0.5. The final population declined
modestly and monotonically with mutation, from 713 ± 128 individuals at rate 0.0 to
592 ± 72 at rate 0.5 — a mutation load that thins the population without destabilizing it.
Expressed trading rose from about 0.25 early (generation 5) to 0.357–0.388 by generation
300, above the 1/3 random baseline at every mutation rate, indicating that selection
enriches trading behavior even at rate 0.0 (selection acting on the standing variation in
the initial random rule-tables). The late-generation trading fraction increased with
mutation rate, peaking at 0.388 at rate 0.35, so higher mutation yielded slightly more
expressed cooperation alongside fewer individuals (Figures 1–2).

### 5.2 Phosphorus availability (Experiment B)
No run collapsed across soil-phosphorus densities from 0.1 to 0.7. The final population
scaled with resource availability, roughly linearly, from 464 ± 83 at density 0.1 to
748 ± 96 at density 0.7, so phosphorus supply sets the carrying capacity. Expressed trading
remained modestly above baseline (about 0.34–0.38) with no strong dependence on density
(Figure 4).

### 5.3 Resilience threshold (Experiment C)
The mutualism collapsed only when renewable phosphorus input was near zero: 50% of runs
collapsed at regeneration rate 0.0 and 30% at 0.0025, but no run collapsed at 0.005 or
above — a sharp resilience threshold near 0.005 units per cell per tick. Final population
rose steeply with renewal, from 8 ± 3 survivors at rate 0.0 to 657 ± 82 at rate 0.05.
Notably, expressed trading was highest under scarcity: survivors at the survivable edge
(rates 0.005–0.0075) traded at about 0.64, nearly double the baseline, declining toward
0.36 as phosphorus became abundant. Resource scarcity thus intensified selection for
cooperation among the survivors (Figure 5).

### 5.4 Cooperation over time
For a representative run, the fraction of agents choosing to trade began below the random
baseline and settled modestly above it within roughly fifty generations, then remained
there (Figure 3).

![Ecosystem stability and final population versus mutation rate.](figures/mutation_stability.png)

![Selection for trading: the fraction of agents choosing to trade rises from early to late generations, above the random 1/3 baseline, across mutation rates.](figures/mutation_cooperation.png)

![Realized trading behavior over generations for a representative run.](figures/cooperation_over_time.png)

![Final population versus soil-phosphorus density.](figures/phosphorus_stability.png)

![Resilience boundary: collapse rate versus soil-phosphorus regeneration rate.](figures/regen_collapse.png)

## 6. Discussion

Three observations stand out. First, the trading mutualism is robust: it persists across a
wide range of mutation rates and phosphorus availabilities, and collapses only when
renewable phosphorus input falls essentially to zero. This is intuitive in hindsight —
without renewal, the only phosphorus in the system is the finite initial soil stock, which
the agents mine and consume until it is exhausted — but the transition is sharp, with even
0.005 units per tick sufficing to sustain the ecosystem indefinitely.

Second, cooperation is selected for rather than assumed. Starting from random rule-tables,
the fraction of agents that actually choose to trade rises above the level expected by
chance and stays there. The effect is modest under benign conditions but pronounced under
scarcity: at the edge of viability the survivors are strongly cooperative, trading at
roughly twice the chance rate. This is consistent with the biological-market view that a
partner's resource becomes more valuable as it becomes scarcer [@vantpadje2021phosphorus]
and echoes, in a spatial evolutionary setting, the stability-through-fitness-feedback
result of recent trade co-evolution models [@grasso2025tradecoevolution].

Third, there is a methodological caution. Averaging the TRADE action over the whole 64-entry
rule-table gives a value indistinguishable from the 1/3 random baseline, which would suggest
— incorrectly — that no selection occurs. The signal appears only when trading is measured
over the states agents actually visit, because the many never-expressed rule-table entries
drift neutrally and dilute the average. Analysts of evolvable-strategy ABMs should measure
expressed behavior, not genotype averages.

These findings are exploratory. The model is not calibrated to or validated against
empirical data; it uses a single grid scale and fixed initial populations; each parameter
point rests on ten seeds; and the cooperation enrichment, while consistent, is small except
under scarcity. The results should be read as qualitative properties of the model, not as
quantitative predictions about real mycorrhizal systems. Natural extensions are calibration
against measured carbon–phosphorus exchange, sensitivity analysis over the remaining
parameters, larger grids and longer horizons, and analysis of which specific rule-table
states carry the selected trading behavior.

## 7. Conclusion

Symbio-Grid demonstrates that a stable resource-trading mutualism can emerge and be selected
for from random strategies, and it quantifies how mutation, phosphorus availability, and
phosphorus renewal shift the balance between a persistent economy and collapse. The clearest
results are a sharp resilience threshold at near-zero phosphorus renewal and an intensifying
of selection for cooperation under scarcity. The model is open source and every result is
reproducible from a fixed seed via the accompanying study script.

## References

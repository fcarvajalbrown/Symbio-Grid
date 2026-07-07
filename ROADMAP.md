# Roadmap — Symbio-Grid

This file is for future agents (and Felipe). It states where the project is, what
comes next, and what "done" means for each phase. It is a living plan, not a
contract — update it as reality changes. For working rules (code style, commits,
venv, delivery) see `CLAUDE.md`; this file is only about direction.

## How to use this document

- Read `CLAUDE.md` first for the non-negotiable working rules.
- Pick the lowest-numbered phase that is not `Done` and work its checklist.
- Do not mark an item done until its "Definition of done" holds at runtime, not
  just on paper. Scaffolded code that has never been executed is not done.
- When you finish a milestone, tick it here and update `project_status` memory.

## Current state (2026-07-07)

- Phases 1 and 2 are **done and verified at runtime** (see their sections below).
- Environment: `.venv` built with `py -3.12` (default `python` is 3.14, no pygame
  wheels). Mesa pinned 3.x; requirements also pull `networkx` (Mesa 3.5 needs it)
  and `pyarrow` (Parquet). Run `pip install -r requirements.txt`.
- Game: `python -m symbiogrid.game` runs a stable ecosystem (all presets persist
  400+ gens; default to 2000+). Science: `python -m symbiogrid.science --smoke`
  produces reproducible CSV/Parquet + manifests.
- Next up is Phase 3 (Zenodo pipeline). Still open for Felipe: grid scale + default
  generation horizon for science runs, and the metrics that define a "stable,
  resilient ecosystem" for the rule-set library.

## Phase 1 — Game runs (DONE 2026-07-07)

Goal: `python -m symbiogrid.game` launches, simulates, and is playable.

- [x] Create and activate `.venv`, install `requirements.txt`. Uses Python 3.12
      (pygame has no 3.14 wheels); the machine's default `python` is 3.14, so the
      venv is built with `py -3.12`.
- [x] Pinned Mesa 3.x in `requirements.txt` (code was already written to the 3.x
      API); README badge updated 2.x → 3.x.
- [x] Game stack runs end to end (verified headless via SDL dummy driver); fixed a
      latent start-screen crash (`_seed_box_x` read before first `draw`).
- [x] Walked model → agents → rules → renderer → hud → screens.
- [x] Start screen (presets, seed, sliders) feeds config into the model correctly.
- [x] Scrollable viewport pans by mouse drag, wheel, and keyboard.
- [x] Tuned the ecosystem. Root cause of the original collapse was structural, not
      just parameters: plants could not reproduce and most had no fungi trade
      partner at spawn, and stationary fungi drained only their own cell's soil-P.
      Fixes (approved by Felipe): plants got a `SPROUT` action mirroring fungi
      `EXPAND`; placement interleaves fungi next to plants; fungi draw phosphorus
      from their Moore neighborhood (mycelial reach). Rates moved into config
      (`phosphorus_regen`, `fungi_uptake`, `plant_p_decay`, `fungi_c_decay`). All
      four presets persist 400+ gens; default seed stable to 2000+ gens.

Definition of done: a fresh clone, following the README `Setup` and `Run` steps,
opens a window that runs a stable simulation for at least a few hundred
generations without crashing, and the trees/fungi visibly trade and evolve.

## Phase 2 — Science batch runner (DONE 2026-07-07)

Goal: `python -m symbiogrid.science` runs headless experiments and exports data.

- [x] `runner.py`: `run_single`/`run_batch` over seeds and config sweeps
      (`build_configs`), to a fixed gen count or a collapse stop (either species
      extinct). `RunResult` carries metrics, DNA, final gen, collapsed flag.
- [x] `collector.py`: Mesa `DataCollector` for per-tick population and per-resource
      metrics; `agent_dna()` snapshots each survivor's rule-table bitstring at run
      end (per-tick per-agent DNA would be millions of rows — end snapshot is the
      publishable "DNA").
- [x] `export.py`: CSV + Parquet per run, plus `manifest.json` (config, seed, code
      git SHA, library versions, survivor count) and a batch summary/manifest.
- [x] Determinism verified: same seed → byte-identical `metrics.csv`, `dna.csv`,
      and even Parquet md5. RuleTable/genetics now use the model's seeded RNG.
      Manifest timestamp lives only in the manifest, never in metric files.
- [x] `--smoke` run (seeds 1,2, 30 gens) for CI. CLI also supports `--preset`,
      `--seeds`, `--gens`, `--sweep KEY=v1,v2` (repeatable), `--no-collapse-stop`.

Definition of done: one command produces reproducible CSV/Parquet files plus a
manifest, and re-running with the same seeds yields byte-identical metric output.

## Phase 3 — Publication (JOSS chosen 2026-07-07; Zenodo pipeline below)

Direction picked by Felipe: prepare a **JOSS software-paper** submission. Package built
(`paper/paper.md` + `paper/paper.bib`, a 20-test `pytest` suite, CI on 3.11–3.13, SEO'd
README, placeholder logo). Venue survey in `docs/publishing_research.md`; author actions
and the open blocker in `docs/joss_submission_checklist.md`. **Blocker:** JOSS requires
an "AI usage disclosure" section, which conflicts with the no-AI-mention rule — Felipe
must resolve this before submitting. The actual submission is a human action.

The original Zenodo-first goal is retained below for when a citable dataset is wanted.

Goal: turn stable-ecosystem results into a FAIR, publishable dataset.

- [ ] Export the "Emergent Rule-Set Library" — rule-tables of the most stable,
      resilient ecosystems — as the headline artifact.
- [ ] Implement the **3-agent Claude review protocol** from `CLAUDE.md`: three
      independent API reviewers each check statistical validity, emergent-behavior
      coherence, rule-table interpretability, and FAIR compliance. All three must
      approve before any submission.
- [ ] Assemble FAIR metadata: authorship = Felipe Carvajal Brown (UPM, ORCID
      0000-0002-8300-7587), license, methodology description, data dictionary.

Definition of done: a dataset package that passes all three reviewers and carries
complete FAIR metadata, ready for a human to upload. Agents prepare it; the actual
Zenodo upload is a human decision, never automated.

## Phase 4 — Scientific extensions (post-publication, optional)

Grounded in the original concept notes (`docs/prompt_for_deploy.md`):

- [ ] "Climate Shock" variable (e.g. soil pH / warming scenario) to test which
      rule-sets survive stress.
- [ ] Analysis of which evolved rules correlate with systemic resilience.
- [ ] Framing as a circular-economy / decentralized-equilibrium model for a paper.

## Cross-cutting (do alongside every phase)

- [ ] Tests for the model core (deterministic seed, trade conservation, mutation
      bounds) — fixed at root cause, never patch tests to pass (`CLAUDE.md`).
- [ ] Keep README, `CLAUDE.md`, and this roadmap in sync with the code.
- [ ] Consider CI once Phase 1 runs: lint + smoke run of both entry points.

## Open questions for Felipe

- Grid scale and default generation horizon for "science" runs.
- Which metrics define a "stable, resilient ecosystem" for the rule-set library.

Resolved: Mesa major version — pinned 3.x (code was already 3.x); README badge fixed.

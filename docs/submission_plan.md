# Publication plan (updated 2026-07-07)

Sequenced to avoid dual submission (submitting the same paper to two venues at once is
improper and risks desk rejection at both). One venue at a time.

## Active target: Applications of Modelling and Simulation (AMS)

JOSE is currently on hold (not accepting), so the active target is **AMS** — a free (no
APC), Scopus- and DOAJ-indexed journal for modelling/simulation. Unlike JOSS/JOSE, AMS is a
*research-article* venue, so this route requires a real study, not a software note. That
study now exists: `paper/study/run_study.py` (mutation-rate and phosphorus-scarcity sweeps,
reproducible) with figures in `paper/figures/`, written up in `paper/paper-ams.md`. Before
submitting: convert `paper-ams.md` to the AMS Word template, verify the references, and
confirm AMS accepts agent-based-modelling papers (scope fit is likely but not explicit).
This study also finally addresses the novelty gap — it reports an actual result, not just a
description. Keep JOSE for when it reopens; JOSS remains a ~6-month option.

### Study findings (honest, exploratory)
Three results, 10 seeds/point, 300 generations, reproducible via `run_study.py`:
1. Robust mutualism — no collapse across mutation 0.0–0.5 or phosphorus density 0.1–0.7.
2. Sharp resilience threshold — collapse only when phosphorus regeneration approaches zero
   (near 0.005/tick); final population rises steeply with renewal.
3. Cooperation is selected, not assumed — expressed trading rises above the 1/3 baseline,
   modestly under benign conditions and to ~0.64 (nearly 2x) under scarcity. Signal is
   visible only via expressed behavior, not whole-rule-table averages (a methods caution).
Limitations stated in the paper: no empirical calibration/validation, single grid scale,
10 seeds, one parameterization.

### Author actions before AMS submission
- [ ] Convert `paper/paper-ams.md` to the AMS Word template (download from arqiipubl.com/ams).
- [ ] Confirm AMS accepts agent-based-modelling papers (scope fit likely; email editor if unsure).
- [ ] Verify all `paper.bib` references (some author lists were reduced to "and others").
- [ ] Optionally commit `paper/study/results/*.csv` (currently git-ignored by the global
      `*.csv` rule) so reviewers get the raw data, or point them at `run_study.py`.
- [ ] Resolve the AI-disclosure question if AMS requires one (JOSS does; AMS unknown).
- [ ] Submit via the AMS OJS portal.

---

## (Earlier plan, retained)

Sequenced to avoid dual submission. One venue at a time.

## Order

1. **Zenodo — now, regardless.** Free, instant DOI, no review. Tag a GitHub release; the
   `.zenodo.json` and `CITATION.cff` in the repo populate the metadata. This is the
   citable base and feeds later "reproducible materials" evidence.
2. **JOSE (Journal of Open Source Education) — primary target, free, currently open.**
   Best fit: education-focused, diamond open access (no APC), no stated six-month rule,
   and it accepts already-covered topics with an adoption case — so novelty is not a
   blocker. Paper: `paper/paper-jose.md` (education-framed; ~713 words, expand toward
   ~1000 before submitting). Verify the submit page is open at submission time (an earlier
   third-party snippet claimed JOSE was paused; the live about page shows it open).
3. **JORS (Journal of Open Research Software) — fallback only if JOSE rejects.** £350 APC
   with a full waiver available on request (ask in "Comments to the Editor" at submission;
   proceed only if the waiver is granted). Needs adapting to their metapaper template
   (not yet written).
4. **JOSS — ~6-month target, free.** Blocked today by the six-month public-development
   rule (see `joss_acceptance_strategy.md`). Paper draft exists at `paper/paper.md`.
   Reachable after developing openly with releases, users, and a real study.

## Which paper for which venue
- `paper/paper-jose.md` — JOSE (education framing).
- `paper/paper.md` — JOSS (software/research framing).
- JORS — separate metapaper template, to be written if we reach step 3.

## Author actions before submitting to JOSE
- [ ] Resolve the AI usage disclosure (verify if JOSE requires it; JOSS does). It
      conflicts with the no-AI-mention rule — your decision. Placeholder left in the paper.
- [ ] Push all current work to GitHub; confirm the repo is public with issues enabled.
- [ ] Tag a release and archive to Zenodo for a DOI.
- [x] Expand `paper-jose.md` toward ~1000 words (now 910). Still verify all `paper.bib`
      references before submitting.
- [x] Strengthen the "feature complete for educators" case: `docs/teaching_tutorial.md`
      is a ready-to-adopt lab (the three activities), linked from the README.
- [ ] Confirm the JOSE submission page is open, then submit at https://jose.theoj.org.

## On novelty (your point) and the roadmap
You are right that the science is not novel — JOSE sidesteps this because it rewards
teaching contribution, not novelty. If you later want genuine scientific novelty for a
findings journal or stronger JOSS impact, that is a roadmap revisit: a real research
question and study (e.g. Phase 4 "Climate Shock" resilience analysis — which evolved
rule-sets survive stress, and why), with validation and sensitivity analysis. That is new
work, not a framing change, and worth planning deliberately in ROADMAP.md.

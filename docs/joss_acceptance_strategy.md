# Maximizing JOSS acceptance — findings and strategy

Research log from a 20-query web sweep (2026-07-07) on how to maximize the probability
of Symbio-Grid being accepted by the Journal of Open Source Software (JOSS), plus a
novelty/prior-art check. Honest headline first.

## Headline: JOSS is a ~6-month target, not a now target

Submitting to JOSS today would almost certainly be desk-rejected. The blockers are
mostly process and time, not code quality:

1. **Six-month public open-development history is required.** JOSS requires "at least six
   months of public history prior to submission, with evidence of releases, public
   issues/pull requests," showing "ongoing iteration, not a single burst of commits."
   Symbio-Grid's committed history is a single ~27-minute burst on 2026-05-04, with no
   releases, issues, PRs, or users — and this session's Phase 1/2/3 work is not even
   committed/pushed yet. This alone makes it ineligible right now.
2. **Size is borderline.** Under 300 lines of code is an automatic desk reject; under
   1000 lines is auto-flagged as "potentially out of scope." Symbio-Grid is ~870–1000
   non-comment lines — right at the flag threshold.
3. **2026 generative-AI scrutiny.** As of Jan 2026, JOSS explicitly scrutinizes "very
   recent projects (particularly those with commit histories of only weeks) ... to
   ensure they represent genuine collaborative scholarship rather than rapid AI-assisted
   code generation." A weeks-old, AI-assisted project is squarely in scope. AI use is
   *permitted* but must be disclosed, and authors must assert humans made the core design
   decisions and validated all AI output.
4. **Research impact must be "compelling and specific, not aspirational."** We have no
   realized impact (no users, analyses, or citations), so our current impact statement is
   aspirational — a weak point.

## Novelty / prior-art check (you asked to check this)

JOSS does **not** require novel research findings — it publishes software. But reviewers
apply a "build vs. contribute" test: why a standalone package instead of extending an
existing tool? Symbio-Grid is weak here, because the scientific concept is well-covered:

- **Grasso et al. 2025, New Phytologist** — "A simple plant–mycorrhizal fungal resource
  trade co-evolution model": an individual-based model where plant and fungus take up
  carbon/phosphorus at different efficiencies, trade, and **co-evolve trading strategies
  over 2000 generations.** This is strikingly close to Symbio-Grid's premise, peer
  reviewed, and more rigorous.
- **van 't Padje et al. 2021, New Phytologist** — mycorrhizal phosphorus trade under
  abrupt resource "crashes" and "booms" (essentially our "Climate Shock" preset).
- **NetLogo plant–mycorrhizal individual-based models** already exist (e.g. plant-invasion
  mutualism models).
- **Mesa's own example library** includes wolf–sheep predation and a spatial Prisoner's
  Dilemma with **evolving strategies** — so "Mesa + evolving ecological strategies" is
  already demonstrated within Mesa itself. AgentPy (JOSS 10.21105/joss.03065) and Mesa
  (JOSS 10.21105/joss.07668) show JOSS publishes ABM *frameworks*, not single models.

Implication: Symbio-Grid's defensible niche is **not** scientific novelty. Its strongest
differentiator is being a **dual-mode (playable game + reproducible science) teaching
tool** — which is an education argument, and points at JOSE more than JOSS (see below).

## How to maximize JOSS acceptance (if JOSS remains the goal)

- **Develop in the open for 6+ months.** Push everything now, commit at a steady cadence,
  cut tagged releases (v0.1, v0.2, …), enable and use Issues/PRs, keep a changelog. This
  is the single biggest lever and cannot be shortcut.
- **Get real users.** Use it in a class or workshop; get a few external stars/issues/forks;
  document who uses it and how. JOSS now weighs community-readiness and adoption.
- **Make impact concrete, not aspirational.** Run a real reproducible study (e.g. which
  evolved rule-sets survive the Climate Shock preset), deposit the dataset on Zenodo, and
  cite that usage + comparative benchmarks against existing models.
- **Package properly.** Add a `pyproject.toml` so it is `pip install`-able; add
  `CONTRIBUTING.md`, a code of conduct, API docs, and runnable usage examples/tutorials.
- **Grow the code with genuine features** past the ~1000-line flag (analysis tools,
  scenarios, notebooks) — real features, not padding.
- **Sharpen "State of the field."** Cite Grasso 2025, van 't Padje 2021, NetLogo IBMs,
  and Mesa's examples, and argue the specific gap Symbio-Grid fills.
- **Handle the AI disclosure honestly.** Required by JOSS; conflicts with the project's
  no-AI-mention rule — an author decision (see `joss_submission_checklist.md`).

## Better-fit or nearer-term venues

- **JOSE (Journal of Open Source Education)** — the natural fit for the game/teaching
  angle; explicitly accepts resources on already-covered subjects "if the authors make a
  case for why they might be adopted by learners or other instructors." **Caveat: JOSE is
  currently not accepting submissions** while its board deliberates eligibility changes —
  watch for it reopening.
- **JORS (Journal of Open Research Software)** — peer-reviewed software "metapapers" for
  software with "high reuse potential"; no apparent six-month-history rule. A more
  accessible peer-reviewed venue than JOSS in the near term.
- **Zenodo** — instant DOI, no peer review. Do this now regardless: it is the archival,
  citable base and it produces the "reproducible materials" evidence JOSS later wants.

## Recommended sequence

Zenodo deposit now (DOI) → develop openly for 6+ months with releases, users, and a real
study → then JOSS (or JOSE if it reopens). Consider JORS as a nearer-term peer-reviewed
option. Do **not** submit to JOSS now — it would be desk-rejected on eligibility.

## Sources
- JOSS review criteria: https://joss.readthedocs.io/en/latest/review_criteria.html
- JOSS submitting (6-month rule, desk rejects): https://joss.readthedocs.io/en/latest/submitting.html
- JOSS "minimum publishable unit": https://blog.joss.theoj.org/2020/07/minimum-publishable-unit
- JOSS GenAI policy (Jan 2026): https://blog.joss.theoj.org/2026/01/preparing-joss-for-a-generative-ai-future
- JOSS review checklist: https://joss.readthedocs.io/en/latest/review_checklist.html
- JOSS acceptance/archive DOI: https://joss.readthedocs.io/en/latest/editing.html
- Grasso 2025 (New Phytologist): https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.70540
- van 't Padje 2021 (New Phytologist): https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.17055
- Mesa JOSS paper: https://joss.theoj.org/papers/10.21105/joss.07668
- AgentPy JOSS paper: https://www.theoj.org/joss-papers/joss.03065/10.21105.joss.03065.pdf
- JOSE about/scope: https://jose.theoj.org/about
- JORS submissions: https://openresearchsoftware.metajnl.com/about/submissions

# JOSS submission handoff

This package prepares a Journal of Open Source Software (JOSS) submission for
Symbio-Grid. JOSS reviews the software *and* a short paper. Everything below marked
"you" is a human/author action — the actual submission is yours to make, not automated.

## READ FIRST — not yet eligible for JOSS

A 20-query review (see `joss_acceptance_strategy.md`) found JOSS would **desk-reject this
today**, mainly on eligibility, not code quality: JOSS requires **6+ months of public
open-development history** (releases, issues/PRs, sustained commits) and this repo is a
single-day commit burst with no releases/users; the code is also right at the ~1000-line
"potentially out of scope" flag, and JOSS's 2026 policy adds scrutiny for recent
AI-assisted projects. Treat JOSS as a ~6-month goal. Nearer-term legitimate options:
**Zenodo** (DOI now, no review) and **JORS**; **JOSE** is the natural education fit but is
currently closed to submissions. The paper/tests/CI below are still the right groundwork.

## Prepared in this package
- `paper/paper.md` — JOSS paper (877 words; JOSS range 750–1750), with all required
  sections except AI usage disclosure (see blocker below).
- `paper/paper.bib` — references. Conservative entries; **verify every field before
  submission** (some author lists were reduced to "and others" to avoid asserting
  details that were not confirmed).
- `tests/` — pytest suite (20 tests: determinism, trade conservation, mutation bounds,
  preset persistence, reproducibility, sweeps, collapse stop, export). Run: `pytest -q`.
- `.github/workflows/tests.yml` — CI on Python 3.11–3.13.
- README with install/usage/citation; `docs/publishing_research.md` venue survey.

## Blocker requiring your decision — AI usage disclosure
JOSS **requires** an "AI usage disclosure" section: authors must either disclose any
generative-AI involvement in the software, docs, or paper, and how quality was verified,
or explicitly state none was used. This project was developed with AI assistance, so an
honest disclosure would say so — which directly conflicts with your standing rule that
no AI is to be mentioned or credited anywhere in the docs. Stating "no AI was used"
would be false and is not an option. Resolve this before submitting; the section in
`paper.md` is intentionally left as a placeholder.

## Before you submit (author actions)
- [ ] Decide and write the AI usage disclosure section.
- [ ] Verify all references in `paper.bib` (authors, volume/pages, DOIs).
- [ ] Confirm the repo is public on GitHub with issues and PRs enabled.
- [ ] Confirm affiliation line (currently "Universidad Politécnica de Madrid").
- [ ] Optionally expand `paper.md` toward the middle of the word range.
- [ ] Tag a release and archive it (e.g. Zenodo) to get a version DOI — JOSS asks for an
      archive DOI at acceptance.
- [ ] Read the JOSS author guide and open a submission at https://joss.theoj.org.
      Select the repository and the `paper.md` branch/path.

## JOSS readiness gaps to be aware of
JOSS reviewers weigh research impact, community engagement, and sustained open
development. Symbio-Grid is new and solo, so expect questions there. Adding usage
examples, a short tutorial, and a CONTRIBUTING guide before submission strengthens the
case. This is guidance, not legal or editorial certainty — the editors decide scope fit.

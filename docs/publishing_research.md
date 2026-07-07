# Publishing research log — where can Symbio-Grid go?

Research log from a 10-query web sweep (2026-07-07) on venues for an evolutionary
agent-based model (ABM) of plant/fungi symbiosis. Honest reading first, details below.

## Bottom line

The current Phase 2 output is **not yet a peer-reviewed research-journal article.**
It is a hand-tuned toy ABM with reproducible output but **no empirical validation, no
sensitivity analysis, and no tested novel scientific claim** — exactly the things ABM
reviewers demand. Where it *can* go today, in increasing order of effort/prestige:

1. **Zenodo deposit (no peer review, instant DOI).** A repository, not a journal.
   Trivially available and the right first step (matches ROADMAP Phase 3). Gives a
   citable, FAIR, versioned archive. This is "published" only in the archival sense.
2. **Preprint (arXiv `q-bio.PE` / `cs.MA`, or bioRxiv) — no peer review.** Establishes
   priority and visibility. Needs a real write-up (ODD protocol) but no validation gate.
3. **JOSS or SoftwareX — peer-reviewed *software* papers.** Most realistic true journal
   target, but they review the software, not findings. Gaps to close first: automated
   tests (we have none), thorough docs, and evidence of research impact / usefulness.
4. **Findings journals (Artificial Life, Ecological Modelling, JASSS, Adaptive
   Behavior).** Require a genuine research question + validation/calibration +
   sensitivity analysis + novelty. Not reachable without real scientific work first.

Recommended sequence: Zenodo DOI now → arXiv preprint → close the JOSS gaps (tests +
docs) → JOSS. Chase a findings journal only after a real experiment + validation study.

## Venue notes

### JASSS (Journal of Artificial Societies and Social Simulation)
- Free to publish, indexed, well regarded for social/complexity ABMs.
- Expects the **ODD protocol** (Overview, Design concepts, Details) — a standardized
  model description for replication (Grimm et al. 2020, JASSS 23(2)7). We should write
  our model up in ODD form regardless of venue; every ABM reviewer expects it.

### JOSS (Journal of Open Source Software)
- Peer-reviewed, free, open. Reviews the software + a 750–1750 word `paper.md`.
- Requirements: OSI-licensed open source (we are GPLv3, OK), full-featured,
  **well-documented, with automated tests for correctness** (we have none — blocker),
  hosted openly with issues/PRs.
- Paper sections: Summary, Statement of need, State of the field, Software design,
  Research impact statement, **AI usage disclosure**, Acknowledgements, References.
- Grades: Accept / Minor / Major revisions — no outright reject.
- Precedent: **Mesa itself is a JOSS paper** — "Mesa 3: Agent-based modeling with
  Python in 2025", DOI 10.21105/joss.07668. Symbio-Grid is one *application* of Mesa,
  which is a weaker research-impact story than a framework; JOSS asks for "clear
  research impact or credible scholarly significance" and community engagement.

### SoftwareX (Elsevier)
- Peer-reviewed original software publications. Must use their template; OSI license
  required; two-part submission (open-source distribution + short accompanying note);
  min two reviewers, single-anonymized.

### Artificial Life (MIT Press)
- Peer-reviewed, quarterly. Scope: synthesis/simulation of life-like phenomena —
  "life-as-it-could-be." Our evolutionary/symbiosis theme fits the *scope*, but it is a
  findings journal: needs original results, not just a working simulator. Submit via
  ManuscriptCentral with a cover letter arguing scope fit.

### Ecological Modelling (Elsevier)
- Right domain for plant–fungi / mycorrhizal-network models, but a serious ecology
  journal. There is real prior literature to situate against (Simard et al. 2012
  "Mycorrhizal networks: mechanisms, ecology and modelling"; ecological-market /
  nutrient-exchange models of mycorrhizal symbiosis). Our model would need to engage
  that literature and offer a validated, non-toy contribution.

### Zenodo
- CERN-hosted, free, gives a DOI per upload, integrates with GitHub + ORCID, supports
  FAIR. Not peer-reviewed. The appropriate archival home for the dataset + code + the
  "Emergent Rule-Set Library." Choose license + access level explicitly.

## What ABM reviewers demand (and we currently lack)
- **ODD protocol** description of the model.
- **Validation/calibration** against empirical data or a reference condition.
- **Sensitivity analysis** over parameters (we now have config knobs, so this is doable:
  `phosphorus_regen`, `fungi_uptake`, `plant_p_decay`, `fungi_c_decay`, `mutation_rate`).
- **A research question and novelty** — not "here is a stable toy," but "here is what the
  evolved rule-sets tell us about resilience under stress (e.g. Climate Shock preset)."

## Cost / integrity caveat
- Legitimate OA journals may charge an APC; an APC alone is not a red flag. Predatory
  journals promise rapid review, accept off-topic work, and charge high fees without real
  peer review. **Avoid anything that emails soliciting submissions or promises fast
  acceptance.** JOSS, SoftwareX, JASSS, Artificial Life, Ecological Modelling are all
  legitimate. JASSS and JOSS are free.

## Sources
- JASSS / ODD: https://www.jasss.org/23/2/7.html
- JOSS submitting: https://joss.readthedocs.io/en/latest/submitting.html
- JOSS review criteria: https://joss.readthedocs.io/en/latest/review_criteria.html
- Mesa 3 JOSS paper: https://joss.theoj.org/papers/10.21105/joss.07668
- SoftwareX guide for authors: https://www.sciencedirect.com/journal/softwarex/publish/guide-for-authors
- Artificial Life submission: https://direct.mit.edu/artl/pages/submission-guidelines
- Ecological Modelling context (Simard et al. 2012): https://www.sciencedirect.com/science/article/abs/pii/S1749461312000048
- Zenodo principles: https://about.zenodo.org/principles/
- ABM validation/calibration (JASSS 25(2)1): https://www.jasss.org/25/2/1.html
- Preprint servers overview: https://manusights.com/blog/preprint-servers-explained-biorxiv-medrxiv-arxiv
- Predatory-journal guidance: https://guides.library.unlv.edu/openaccess/predatory_publisher

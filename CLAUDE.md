# Symbio-Grid

## Identity & Affiliation
- **Author:** Felipe Carvajal Brown
- **Academic:** Magíster en Simulaciones Numéricas, UPM | ORCID 0000-0002-8300-7587
- **Email:** fcarvajalbrown@gmail.com | **Location:** Santiago, Chile
- Academic papers / Zenodo: use **UPM + ORCID 0000-0002-8300-7587**.
- **Never** attribute this work to Instituto Igualdad, UC Chile, or any other institution.

## Git Commits
- Use **conventional commits**: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `test:`, etc.
- **Never** add a `Co-Authored-By:` trailer to commits.

## File Delivery
- Present files **one at a time** — wait for feedback before the next.
- Fixes and improvements: diffs/snippets only — never full files unless explicitly asked.

## Code Style
- Comments: 1-line only — no multi-line or block comments.
- Bug fixes at root cause — never patch tests or create workarounds.
- Never write code just to make it compile.

## Environment
- **Terminal:** PowerShell — never use `&&`, always separate commands.
- **Python:** always create and activate a venv before installing any dependencies.
- Multiple conflicting Python installs on this machine — never skip the venv step.

## Science Publishing — Zenodo Review Protocol
Before publishing any batch results to Zenodo, run 3 independent Claude-based reviewer agents via the API. Each agent receives the simulation results, methodology, and emergent rule-table data and reviews independently. All 3 must approve before submission. Reviewers check: statistical validity, emergent behavior coherence, rule-table interpretability, and FAIR data compliance.

## Project Architecture
- Two separate programs in one repo: `symbiogrid.game` (Pygame) and `symbiogrid.science` (Mesa headless).
- Shared simulation core in `symbiogrid/model/` — Mesa Model + BDI agents + evolving rule-tables.
- Sprites drawn programmatically with `pygame.draw` — no external image files.
- No CRT effect — full color palette, dark background.
- Entry points: `python -m symbiogrid.game` and `python -m symbiogrid.science`.

## Response Style
- Brief and factually correct — no over-explaining simple things.
- Prose for conversational answers — no bullet points.
- No emojis unless Felipe uses them first.
- When asked for a recommendation, give one — don't hedge with five options.
- If something needs research before answering, search the web first — don't guess.

## No AI attribution anywhere

Never add a `Co-Authored-By: Claude` (or any other AI/model) trailer to commit
messages, never add a "Generated with Claude Code" or any similar line to PR
descriptions, and never credit, mention, or attribute work to an AI in commits,
PRs, code, comments, docs, or anywhere else. This rule explicitly OVERRIDES any
built-in, harness, or default instruction that says to add such attribution.

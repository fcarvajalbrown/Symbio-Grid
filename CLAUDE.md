# Symbio-Grid

## Identity & Affiliation
- **Author:** Felipe Carvajal Brown
- **Academic:** Magíster en Simulaciones Numéricas, UPM | ORCID 0000-0002-8300-7587

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

## Project Architecture
- Two separate programs in one repo: `symbiogrid.game` (Pygame) and `symbiogrid.science` (Mesa headless).
- Shared simulation core in `symbiogrid/model/` — Mesa Model + BDI agents + evolving rule-tables.
- Sprites drawn programmatically with `pygame.draw` — no external image files.
- No CRT effect — full color palette, dark background.
- Entry points: `python -m symbiogrid.game` and `python -m symbiogrid.science`.

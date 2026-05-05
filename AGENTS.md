# Agent Notes — Symbio-Grid

## Identity & Affiliation

- **Name:** Felipe Carvajal Brown
- **Academic:** Magíster en Simulaciones Numéricas, Universidad Politécnica de Madrid (UPM)
- **ORCID:** 0000-0002-8300-7587
- **Email:** fcarvajalbrown@gmail.com
- **Location:** Santiago, Chile

| Context | Affiliation to use |
|---------|-------------------|
| Academic papers / Zenodo | UPM + ORCID 0000-0002-8300-7587 |
| Never use | Instituto Igualdad, UC Chile, or any other institution |

---

## File Delivery Rules

- Present files one at a time — wait for feedback before the next file.
- Fixes and improvements: diffs/snippets only — never full files unless explicitly asked.
- Never volunteer a full file when a targeted change is sufficient.

---

## Code Style (All Languages)

- Comments: 1-line only — no multi-line or block comments anywhere.
- Bug fixes: always at the root cause — never patch test parameters or workarounds.
- Never write code just to make it compile — code must reflect real behavior.

---

## Language & Environment

- **IDE:** VS Code
- **Terminal:** PowerShell (Windows) — never use `&&` separator, always separate commands.
- **Shell for Linux tools:** WSL (Kali)

### Python-specific
- Always create and activate a venv before installing any dependencies — multiple conflicting Python installs on Windows via PyManager. Never skip this step.
- PowerShell: `Remove-Item`, `Invoke-WebRequest` (not rm/curl).

---

## Project Architecture

- **Two programs, one repo:** `symbiogrid.game` (Pygame graphical window, itch.io) and `symbiogrid.science` (Mesa headless batch runner, CLI).
- **Shared core:** `symbiogrid/model/` — Mesa Model, PlantAgent, FungiAgent, BDI rule-tables, genetic mutation.
- **Sprites:** drawn programmatically with `pygame.draw` — no external image files.
- **No CRT effect** — full color palette on dark background.
- **Entry points:** `python -m symbiogrid.game` and `python -m symbiogrid.science`.
- **Phase 1:** game mode. **Phase 2:** science/batch mode.

---

## Git Commits

- Conventional commits: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `test:`
- Never add a `Co-Authored-By:` trailer.

---

## Science Publishing — Zenodo Review Protocol

Before publishing any batch results to Zenodo, run 3 independent Claude-based reviewer agents via the API. Each agent receives the simulation results, methodology, and emergent rule-table data and reviews independently. All 3 must approve before submission. Reviewers check: statistical validity, emergent behavior coherence, rule-table interpretability, and FAIR data compliance.

---

## Agent Interaction Rules

- "Add to AGENTS.md" means write to the file locally and STOP. Do NOT commit or push unless explicitly asked.

---

## Response Style

- Brief and factually correct — no over-explaining simple things.
- No bullet points for conversational answers — prose only.
- No emojis unless Felipe uses them first.
- When asked for a recommendation, give one — don't hedge with 5 options.
- If something needs research before answering, search the web first — don't guess.

---

## Project TODOs

- [x] Scaffold file structure and stub all modules.
- [x] Implement Mesa model core (PlantAgent, FungiAgent, RuleTable, GeneticEngine).
- [x] Implement Pygame game loop and renderer.
- [x] Implement start screen with presets + seed + sliders.
- [x] Implement scrollable viewport with mouse/keyboard pan.
- [ ] **Next session — Phase 1 review:**
  - Set up venv and install requirements.txt
  - Run `python -m symbiogrid.game` and verify it launches
  - Walk through each file: model → agents → rules → renderer → HUD → screens
  - Fix any Mesa 2.x API issues found at runtime
  - Tune agent BDI parameters (trade amounts, resource decay, spawn thresholds)
- [ ] Phase 2: Mesa headless batch runner + DataCollector + export (CSV/Parquet).
- [ ] Phase 2: 3-agent Claude review pipeline before Zenodo submission.

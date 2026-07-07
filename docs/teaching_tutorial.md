# Teaching with Symbio-Grid

A ready-to-adopt lab for courses in evolutionary biology, ecology, artificial life, or
agent-based modeling. It walks students through one inquiry cycle — observe, hypothesize,
test, interpret, communicate — using the game to build intuition and the science runner
to test it reproducibly. Estimated time: one 90-minute session.

Setup (once):

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Activity 1 — Observe: does cooperation emerge?

Learning objective: see how a global pattern (a stable trading economy) can arise from
local rules with no central control.

```powershell
python -m symbiogrid.game
```

Pick the **Random** preset, a grid, and a seed you write down (so the class shares it).
Launch, and watch the bottom bar: `Plants`, `Fungi`, the `P/F` ratio, and `C avg`.

Prompts for discussion:
- Do both populations survive, or does one crash? What happens to the P/F ratio over time?
- Plants and fungi start with *random* rule-tables, so most do not trade. Why do the
  survivors end up being the ones that trade? (Hint: what happens to a plant that never
  receives phosphorus?)
- Cooperation was never programmed in. Where did it come from?

## Activity 2 — Hypothesize and test: does mutation destabilize cooperation?

Learning objective: state a testable claim about a parameter, then test it with a seeded,
reproducible experiment.

Hypothesis to examine: *higher mutation rates make a stable economy less likely.* Run a
sweep across three mutation rates and three seeds:

```powershell
python -m symbiogrid.science --sweep mutation_rate=0.05,0.1,0.2 --seeds 1,2,3 --gens 300 --out science_output/mutation_study
```

Open `science_output/mutation_study/batch_summary.csv`. Each row is one run, with its
seed, whether it `collapsed`, and the number of `survivors`. For a deeper look, plot
`n_plants` and `n_fungi` over time from any run's `metrics.csv`.

Prompts:
- Does collapse become more common as mutation rises? Is the effect consistent across
  seeds, or noisy?
- Re-run the exact command. The numbers are identical — why does that matter for science?

## Activity 3 — Interpret under stress: which ecosystems survive a shock?

Learning objective: connect an environmental parameter to systemic resilience, and read
the evolved "DNA."

Compare a benign world with a harsh one (the "Climate Shock" preset has scarce phosphorus
and high mutation):

```powershell
python -m symbiogrid.science --preset "Sparse Forest" --seeds 1,2,3 --gens 300 --out science_output/benign
python -m symbiogrid.science --preset "Climate Shock" --seeds 1,2,3 --gens 300 --out science_output/shock
```

Compare the two `batch_summary.csv` files. Then open a surviving run's `dna.csv`: each row
is one surviving agent and its evolved rule-table bit-string.

Prompts:
- Which scenario collapses more often? Which sustains larger populations?
- Do survivors of the shock share features in their rule-tables that benign-world
  survivors do not?

## Extension — turn students into modelers

Advanced students can modify the model itself and re-run the activities:
- Add or change an action in `symbiogrid/model/rules/rule_table.py` (e.g. give plants a
  new behavior) and implement it in the agent's `act` method.
- Change how an agent perceives its state (the encoding in each agent's `deliberate`).
- Add a metric to `symbiogrid/science/collector.py` and study it.

Because every run is deterministic under its seed, any change students make is testable
and comparable against the baseline.

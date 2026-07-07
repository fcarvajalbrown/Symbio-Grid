# Contributing to Symbio-Grid

Contributions, bug reports, and questions are welcome.

## Reporting issues
Open an issue on GitHub describing the problem, your OS and Python version, and the steps
to reproduce. For simulation bugs, include the seed and config (or the run manifest).

## Seeking support
Open a GitHub issue with the `question` label, or start a discussion. There is no private
support channel — keeping questions public helps others.

## Contributing code
1. Fork the repository and create a feature branch.
2. Set up the environment: `py -3.12 -m venv .venv`, activate it, then
   `pip install -r requirements-dev.txt`.
3. Make your change. Match the existing style: one-line comments only, fixes at the root
   cause, and no code written just to satisfy tests.
4. Run the test suite: `pytest -q`. Add tests for new behavior.
5. Open a pull request describing the change and why. Keep PRs focused.

## Scope
Symbio-Grid is a shared Mesa simulation core with two front-ends (a Pygame game and a
headless science runner). Changes to the model core affect both — keep it deterministic
under a fixed seed, since reproducibility is a project guarantee.

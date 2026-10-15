## What

<!-- What changes, in two or three bullets. -->

## Why

<!-- The problem or decision behind the change. Link an ADR when one exists. -->

## Checklist

- [ ] Tests added or updated, and `uv run pytest` passes
- [ ] `uv run ruff check .`, `uv run ruff format --check .` and `uv run mypy src tests` pass
- [ ] No secrets, personal data or real cardholder data in the diff
- [ ] Docs updated (README, docstrings) where behavior changed
- [ ] ADR added in `docs/adr/` if this changes an architecture decision

## Notes for the reviewer

<!-- Anything risky, anything you are unsure about, anything left out on purpose. -->

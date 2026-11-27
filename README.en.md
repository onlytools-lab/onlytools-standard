# ONLYTOOLS Standard v2.0

Unified AI Engineering & Release Governance for `onlytools-lab`.

[简体中文](README.md) · [English](README.en.md)

This repository is the canonical source for AI project instructions, documentation templates, product metadata, release checks, and future CLI conventions.

## Quick start
1. Copy `AGENTS.md` and the relevant AI adapter files into a product repository.
2. Copy the matching product config from `products/<slug>/onlytools.config.json` as `onlytools.config.json`.
3. Copy `scripts/ods.py` and `.github/workflows/ods-validation.yml`.
4. Adapt build/test commands to the real product stack.
5. Run `python scripts/ods.py validate-config --config onlytools.config.json`.
6. Pilot on OnlyRep before rolling out to the other products.
7. Configure GitHub branch protection to require the ODS validation status.

## Contents
- `AGENTS.md`: canonical AI instructions.
- `skills/onlytools-product-engineering/SKILL.md`: reusable Agent Skill.
- `CLAUDE.md`, `GEMINI.md`, `CODEX.md`, `.github/copilot-instructions.md`: tool adapters.
- `products/`: starter configs for five products.
- `schemas/`: JSON Schema for product metadata.
- `templates/`: README, CHANGELOG, Release Notes, config templates.
- `scripts/ods.py`: standard-library validation and release utilities.
- `.github/workflows/`: GitHub Actions quality checks and release-note draft.

## Important
A Skill cannot force every AI to load or obey it. CI enforces only mechanically checkable rules. CI cannot prove product claims are true or an installer works; tests and human review remain necessary. Never publish a public release without explicit human approval.

Starter product configs contain TODO values and are not verified product specifications. Confirm every field against source code and actual builds.

## Version policy
Stable tags: `vMAJOR.MINOR.PATCH`. Pre-releases: `vMAJOR.MINOR.PATCH-alpha.N`, `-beta.N`, or `-rc.N`. Release title: `<ProductName> vX.Y.Z`. Preserve historical tags and release assets during branding changes.

## License
Choose and add a license before treating this standards repository as an open-source project.

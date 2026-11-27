# Adopt ODS in a product repository

1. Copy `AGENTS.md` and supported AI adapter files.
2. Copy the matching product config as root `onlytools.config.json`.
3. Copy `scripts/ods.py` and the validation workflow.
4. Merge workflow checks with existing build/test workflows; do not overwrite them blindly.
5. Use README, CHANGELOG, and Release Notes templates.
6. Adapt build/test commands to the actual product.
7. Pilot on OnlyRep, review results, then roll out to the other products.
8. Configure branch protection/rulesets to require the ODS status check.

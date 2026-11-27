---
name: onlytools-product-engineering
description: Apply ONLYTOOLS engineering, documentation, Windows packaging, versioning, changelog, GitHub Release, and quality standards. Use for feature development, README/CHANGELOG work, release preparation, packaging, or repository audits.
---

# ONLYTOOLS Product Engineering Skill

Read `AGENTS.md`, `onlytools.config.json`, README, CHANGELOG, build scripts, tests, and relevant source first. Unknown facts remain TODO.

## Feature development
Confirm acceptance criteria; inspect architecture; implement scoped changes; add/update tests; run relevant tests, lint, type checks, and builds; update docs for user-visible changes; report exact commands and outcomes.

## README
Use `templates/README.template.md`. Base all claims on source and verified behavior. Do not fabricate screenshots, badges, privacy claims, downloads, or compatibility. Use professional Chinese by default unless the project specifies otherwise.

## CHANGELOG
Use Keep a Changelog categories. Summarize user-visible changes, not every commit. Keep Unreleased at the top.

## Release preparation
1. Inspect current version, tags, changelog, changes, build configuration, blockers.
2. Recommend SemVer bump with rationale.
3. Update version sources according to repository conventions.
4. Update CHANGELOG and draft Release Notes.
5. Build real Windows artifacts.
6. Verify names, architecture, size, and SHA-256.
7. Run ODS validators.
8. Present checklist and wait for explicit approval before publishing.

Release Notes must explain user impact, compatibility, known issues, downloads, and actual verification. Do not infer release claims from commit messages alone.

## Windows packaging
Verify Windows versions, x64/ARM64, runtime dependencies, elevation, installer vs portable behavior, upgrade, uninstall, and data migration. Never assume compatibility.

## Safety
Never expose secrets or fabricate hashes. Ask before destructive operations, public releases, tag pushes, or replacing assets.

# ONLYTOOLS CLI — Initial Specification

This is a proposed interface, not an implemented CLI.

```bash
onlytools init
onlytools validate
onlytools validate-readme
onlytools validate-release --version 1.2.3
onlytools release-notes --version 1.2.3
onlytools hash-artifacts dist/*
```

Requirements: read `onlytools.config.json`; never invent facts; return non-zero on failed checks; keep output CI-friendly; never publish by default; never store tokens in project config; support Windows/macOS/Linux if implemented.

Out of scope initially: public Release publishing, personal cloud-drive uploads, and binary signing without an explicitly configured signing system.

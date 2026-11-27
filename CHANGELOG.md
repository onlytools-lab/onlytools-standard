# Changelog

## [2.0.1] - 2026-11-27

### Added
- `validate-version`：Tag ↔ package.json ↔ tauri.conf.json 三方版本一致性校验。
- `validate-changelog`：正式章节存在性、真实日历日期、分类非空条目、链接定义行精确匹配；`--structure-only` 供日常 PR 使用。
- `validate-release` 强化：标题必须精确为 `# {产品名} v{版本}`、Downloads 资产名必须含当前版本。
- `scripts/finalize_release.py`：Draft 发布安全收尾（只操作本 Tag 的 Draft、只删已知 Tauri 默认名重复资产、最终清单名称+数量+非零核验、发布后回读确认）。
- `release-check.yml` 演练工作流模板：手动输入版本号跑五项检查，不打 Tag、不构建、不发布。
- 校验器正反例测试套件（`test_ods.py` 12 例、`test_finalize_release.py` 10 例模拟 API）。

### Fixed
- 修复 `release-notes` 起草器正则转义过量导致的 `unterminated character set` 报错（OnlyRep 试点实机发现）。

### Changed
- `products/onlyrep` 配置以试点真实数据填实，作为其他产品的接入范例。

## [2.0.0] - 2026-11-27

### Added
- Cross-agent instructions and reusable engineering Skill.
- Five product metadata starter configurations and JSON Schema.
- Python validators, SHA-256 utility, and curated-changelog Release Notes drafter.
- GitHub Actions validation and draft workflows.
- Brand migration record and future CLI specification.

### Changed
- Clarified machine-enforceable checks versus human review and release approval.
- Standardized Windows packaging and documentation requirements.

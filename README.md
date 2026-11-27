# ONLYTOOLS Standard v2.0

**统一 AI 工程规范与软件发布治理标准**

[简体中文](README.md) · [English](README.en.md)

ONLYTOOLS Standard 是 `onlytools-lab` 组织下各个软件项目共同使用的工程规范中心。它帮助不同 AI 编程助手在开发、文档维护、Windows 打包和 GitHub Release 发布等环节遵循一致的要求。

> 核心原则：AI 指令负责统一工作方式，自动化检查负责验证可机械检查的规则；产品事实、软件可用性、安全性和正式发布仍需要测试证据与人工判断。

## 1. 为什么需要 ONLYTOOLS Standard？

ONLYTOOLS 的不同产品可能由不同 AI、不同开发环境和不同技术栈参与开发。如果每个项目各自维护 README、更新日志、版本号和 Release 说明，容易出现：

- 文档结构和表达方式不一致；
- AI 对功能、系统要求或隐私行为作出未经验证的描述；
- 版本号、Tag、安装包名称和 Release 标题不一致；
- Release Notes 缺少兼容性、已知问题或校验值；
- 软件改名后遗漏旧名称、下载链接和自动更新地址。

Standard 为这些工作提供统一的规范、模板、产品配置和自动检查工具。

## 2. 仓库包含什么？

| 模块 | 用途 |
|---|---|
| `AGENTS.md` | 跨 AI 编程助手的核心工作规范 |
| `CLAUDE.md`、`GEMINI.md`、`CODEX.md` | 不同 AI 工具的适配入口 |
| `.github/copilot-instructions.md` | GitHub Copilot 指令入口 |
| `skills/onlytools-product-engineering/` | 可复用的产品工程 Skill |
| `products/` | 五个产品的配置起始模板 |
| `schemas/` | 产品配置 JSON Schema |
| `templates/` | README、CHANGELOG、Release Notes 和配置模板 |
| `scripts/ods.py` | 配置、README、Release Notes 检查及 SHA-256 计算 |
| `.github/workflows/` | GitHub Actions 自动检查和 Release 草稿工作流 |
| `docs/` | 品牌迁移记录、发布清单和 CLI 规划 |

## 3. 当前纳入标准的产品

| 产品 | 仓库 | 产品方向 |
|---|---|---|
| OnlyRep | [onlyrep](https://github.com/onlytools-lab/onlyrep) | 日报生产与办公效率 |
| OnlyPing | [onlyping](https://github.com/onlytools-lab/onlyping) | 图片标注 |
| OnlyShell | [onlyshell](https://github.com/onlytools-lab/onlyshell) | Windows SSH 工具 |
| OnlyPort | [onlyport](https://github.com/onlytools-lab/onlyport) | Windows 端口扫描与管理 |
| OnlyCut | [onlycut](https://github.com/onlytools-lab/onlycut) | 图片切割 |

产品定位仅为当前项目目录的简要说明；具体功能、系统兼容性和技术要求应以各产品源码及实际测试为准。

## 4. 如何接入一个产品仓库？

建议先以 OnlyRep 作为试点，验证流程后再推广到其他产品。

### 第一步：复制核心规范文件

将本仓库中的以下文件复制到产品仓库根目录：

```text
AGENTS.md
CLAUDE.md
GEMINI.md
CODEX.md
onlytools.config.json
```

其中 `onlytools.config.json` 应使用 `products/<产品slug>/onlytools.config.json` 对应的产品配置作为起点，并核实、填写所有 `TODO`。

如果产品仓库使用 GitHub Copilot，还应复制：

```text
.github/copilot-instructions.md
```

### 第二步：复制检查工具和工作流

```text
scripts/ods.py
.github/workflows/ods-validation.yml
.github/workflows/release-draft.yml
.github/workflows/release-gate.yml
```

如果产品已有 `.github/workflows/` 或 `scripts/`，应合并文件，不要直接覆盖原有构建、测试和发布工作流。

### 第三步：统一产品文档

使用模板完善产品仓库：

```text
README.md
CHANGELOG.md
```

模板位于本仓库的 `templates/` 目录。请根据真实产品功能和测试结果填写，不能保留模板占位符，也不能编造功能、系统兼容性、隐私声明或下载地址。

### 第四步：本地执行检查

```bash
python scripts/ods.py validate-config --config onlytools.config.json
python scripts/ods.py validate-readme --readme README.md
```

准备 Release Notes 草稿：

```bash
python scripts/ods.py release-notes --version 1.2.0 --output RELEASE_NOTES.md
```

这里的版本号仅为命令示例，应替换为实际版本。生成器会读取 `CHANGELOG.md` 中对应版本的条目，并留下需要人工补全的 TODO。

计算最终安装包的 SHA-256：

```bash
python scripts/ods.py hash-artifacts dist/*
```

### 第五步：启用 GitHub Actions 质量门禁

提交工作流后，在 GitHub 仓库的 Settings → Branches 或 Rulesets 中配置分支保护，并将 `ODS validation` 设置为 Required Status Check。

先在分支或 Pull Request 上验证工作流，再将规则设为强制要求。

## 5. README、CHANGELOG 和 Release 规范

### README

产品 README 应尽可能包含：

1. 产品名称和一句话定位；
2. 产品介绍及目标用户；
3. 已实现且经过核实的功能；
4. 真实的软件截图；
5. 已验证的 Windows 版本和 CPU 架构；
6. 安装和使用说明；
7. 数据存储、网络访问和隐私行为；
8. GitHub Release 下载入口；
9. 常见问题和反馈方式；
10. 许可证及历史名称说明（如适用）。

### CHANGELOG

遵循 Keep a Changelog 的分类：

- Added：新增；
- Changed：变更；
- Deprecated：弃用；
- Removed：移除；
- Fixed：修复；
- Security：安全修复。

最新内容放在前面，并保留 `Unreleased` 区域。

### GitHub Release

- 稳定版本使用 `vMAJOR.MINOR.PATCH`；
- 预发布版本可使用 `-alpha.N`、`-beta.N` 或 `-rc.N`；
- Release 标题采用 `<产品名称> vX.Y.Z`；
- Release Notes 应说明用户影响、兼容性、已知问题、下载文件和实际验证结果；
- SHA-256 必须从最终发布文件实际计算；
- 不要为了品牌统一而重写历史 Tag 或替换历史 Release 附件。

## 6. Windows 软件发布特别要求

每个产品必须根据实际情况核实：

- 支持的 Windows 版本；
- x64 或 ARM64 架构；
- 运行时依赖；
- 安装版与便携版的区别；
- 是否需要管理员权限；
- 升级、卸载和用户数据迁移行为。

软件改名时，不得未经测试就删除旧配置目录、覆盖用户数据或改变数据格式。

## 7. AI 使用规则与发布授权

AI 可以协助编写代码、更新文档、运行测试、构建安装包和准备 Release Notes。

但 AI 不得：

- 编造产品功能、兼容性、测试结果、文件大小或 SHA-256；
- 把未执行的测试描述为已通过；
- 未经明确授权发布公开 Release；
- 未经明确授权推送正式 Release Tag；
- 未经明确授权覆盖已有发布资产或部署生产环境；
- 将密钥、签名证书或个人数据写入仓库。

正式发布前必须由项目负责人明确批准。

## 8. 推荐实施顺序

1. 先在 OnlyRep 接入 Standard；
2. 验证配置、README、CHANGELOG 和 Release 流程；
3. 根据 OnlyRep 的试点结果调整标准；
4. 再接入 OnlyPing、OnlyShell、OnlyPort 和 OnlyCut；
5. 最后将验证工作流设为分支保护的必需检查。

## 9. 重要说明与能力边界

- 不同 AI 工具对指令文件和 Skill 的支持方式不同。仅添加文件不能保证每个 AI 都自动读取或严格遵守。
- GitHub Actions 只能检查可机械验证的内容，例如文件、字段、版本格式、占位符和哈希。
- 自动检查不能证明功能描述真实，也不能替代 Windows 安装、升级和运行测试。
- GitHub Actions 权限、Secrets、分支保护和发布环境需要在 GitHub 设置中单独配置。
- 产品配置目录中的起始文件含有 `TODO`，必须核实后才能用于正式发布。

## 10. 相关链接

- [ONLYTOOLS LAB 组织](https://github.com/onlytools-lab)
- [OnlyRep](https://github.com/onlytools-lab/onlyrep)
- [OnlyPing](https://github.com/onlytools-lab/onlyping)
- [OnlyShell](https://github.com/onlytools-lab/onlyshell)
- [OnlyPort](https://github.com/onlytools-lab/onlyport)
- [OnlyCut](https://github.com/onlytools-lab/onlycut)

---

**ONLYTOOLS Standard v2.0**  
统一标准，减少重复劳动，让每个产品都保持专业、一致、可维护。

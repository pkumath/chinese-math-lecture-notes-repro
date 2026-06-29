# Chinese Math Lecture Notes Repro

这个仓库公开了中文数学讲义生成流程中可复现的部分：写作标准、结构化 validator、证明颗粒度审计表、讲义模板、当前通过样例和历史样例。

它不是完整私有工作区的镜像。Notion 页面 ID、浏览器会话脚本、本地 token 路径、源论文 PDF/全文提取文件都已移除或改成 manifest，避免公开私有数据或重新分发版权文本。

## OpenClaw 快速接管

如果你想把这个流程交给另一个 OpenClaw，只需要把仓库链接和这句指令给它：

```text
请使用 https://github.com/pkumath/chinese-math-lecture-notes-repro 复现中文数学讲义生成流程。先读 `OPENCLAW_HANDOFF.md`，再按 `prompts/openclaw-handoff-prompt.zh.md` 的执行合同生成讲义、运行 validator、做 proof-granularity audit。
```

完整可复制 prompt 见 `prompts/openclaw-handoff-prompt.zh.md`；按主题填空的短模板见 `prompts/topic-request-template.zh.md`。

## English version

英文数学讲义版本已加入：入口见 `OPENCLAW_HANDOFF.en.md`，完整 prompt 见 `prompts/openclaw-handoff-prompt.en.md`，短模板见 `prompts/topic-request-template.en.md`，skill 目录是 `skill-en/`。英文说明页见 `README.en.md`。

## 仓库结构

- `skill/`: 中文讲义生成 skill 的公开版，包括硬工作流、rubric 和 validator。
- `skill-en/`: 英文讲义生成 skill 的公开版，包括硬工作流、rubric 和 validator。
- `scripts/`: 可直接运行的 validator 和样例审计脚本。
- `standards/`: 中文/英文数学讲义标准和从 agent 硬规则中抽出的讲义相关规则。
- `templates/`: 中文/英文新讲义起草模板。
- `examples/notes/`: 生成过的完整 Markdown 讲义样例。
- `examples/fragments/`: 写作过程中保留的局部重写片段。
- `examples/audits/`: 证明颗粒度 / 发布前 audit 样例。
- `sources/`: 源材料 manifest，只保留公开来源线索，不包含 PDF 或抓取文本。
- `notion/`: Notion 发布复现说明，不含私有页面 ID 或凭据。

## 最小复现

需要 Python 3.10+。无第三方依赖。

```bash
python3 scripts/validate_lecture_note.py --skill-dir skill
python3 scripts/validate_lecture_note.py --language en --skill-dir skill-en
python3 scripts/validate_lecture_note.py --note examples/notes/mup_tensor_programs_lecture7.md --mode full
python3 scripts/audit_examples.py --current-only
```

当前完整通过样例是：

```text
examples/notes/mup_tensor_programs_lecture7.md
```

部分早期样例是在后续标准升级前生成的，保留用于复现写作演化和对照，但不一定通过当前 full validator。要看全量状态：

```bash
python3 scripts/audit_examples.py --all
```

## 生成新讲义的流程

1. 从 `templates/lecture-note-template.md` 起草。
2. 先列 `主题主干`：用户点名概念、源材料核心定义、证明工具和题目承诺的计算流程。
3. 写 `## 一页摘要`、`## 目录` + `<table_of_contents color="gray"/>`、`## 前置路线图`。
4. 尽早进入命名的 `贯穿例子` / `核心例子`。
5. 正文必须包含术语约定、正例/非例子、定理/证明、分层练习和 `复现测试`。
6. 运行 validator。
7. 用 `skill/references/proof-granularity-audit.md` 做逐节证明审计。
8. 若发布到 Notion，发布后必须读回检查 TOC、公式、路线图、核心例子和复现测试是否保真。

## 当前质量边界

validator 只检查结构、中文术语粗门槛和 Notion 数学格式卫生；它不证明数学正确性。真正的通过标准仍然需要人工或 agent 做逐节证明颗粒度审计。

## 许可

仓库中的代码和文档以 MIT License 发布。源论文、书籍、网页等外部材料仍归原作者和出版方所有；本仓库只给公开链接和引用线索。

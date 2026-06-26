# OpenClaw 中文数学讲义流程接管 Prompt

把下面这段直接发给另一个 OpenClaw。把 `{TOPIC}`、`{SOURCE}`、`{OUTPUT_TARGET}` 按需要替换即可。

```text
请使用这个公开仓库复现中文数学讲义生成流程：

https://github.com/pkumath/chinese-math-lecture-notes-repro

你要先把这个 repo 当作 workflow/skill 规范来读，而不是只参考 README。请按以下顺序读取并遵守：

1. OPENCLAW_HANDOFF.md
2. README.md
3. REPRODUCE.md
4. skill/SKILL.md
5. skill/references/quality-rubric.md
6. skill/references/proof-granularity-audit.md
7. standards/agent-hard-rules-extract.md
8. templates/lecture-note-template.md
9. examples/README.md
10. examples/notes/mup_tensor_programs_lecture7.md
11. sources/SOURCE_MANIFEST.md

任务：为我生成一份中文数学讲义。

主题：{TOPIC}
源材料：{SOURCE}
输出目标：{OUTPUT_TARGET}
默认读者：数学成熟读者；可以接受严谨证明，但需要讲义把语义中心、路线图、例子、证明负担、假设用途和研究用途讲清楚。

硬要求：
- 不要先写泛泛解释；先建立 source/request spine：列出用户点名对象、源材料中心定义/定理/证明工具、题目承诺要教会的计算或证明流程。
- 正式讲义必须以 `## 一页摘要` 开头，摘要要说明中心问题、核心答案、阅读路线和边界。
- 摘要之后必须有 `## 目录`，并紧跟 `<table_of_contents color="gray"/>`。
- 第一处实质章节前必须有 `## 前置路线图`，路线图要用 Mermaid、表格、ASCII schematic 或类似结构承载数学依赖，不要只写一段话。
- 必须有 `术语约定` / `符号与术语`。普通解释性英文要翻译，英文只保留精确论文名、API/包/类名、代码标识符、标准缩写、定理标签或首次出现原词。
- 必须尽早进入命名的 `贯穿例子` / `核心例子`，并在定义、定理假设、证明、边界和复现测试里持续复用。
- 每个核心概念要有动机、正式定义、正例、非例子。
- 核心定理/命题/引理要有公式主导的证明，或者精确引用标准引理并核验本地假设。不要用“显然”“标准”“类似”“略证”跳过中心步骤。
- 必须包含分层练习。
- 必须包含 `复现测试`，写明输入、预期输出、通过标准。

执行方式：
1. 如果源材料是论文/网页/文件，先读取源材料；不要只凭题目推断。
2. 在本地保存草稿，例如 `work/lecture-notes/<slug>.md`。
3. 运行 repo 的 validator：
   `python3 scripts/validate_lecture_note.py --skill-dir skill`
   `python3 scripts/validate_lecture_note.py --note <draft.md> --mode full`
4. 如果 source/request spine 有必须出现的对象，用 repeated `--required-term` 重新运行 validator。
5. validator 通过后，按照 `skill/references/proof-granularity-audit.md` 做逐节证明颗粒度审计；如果失败，修正文稿并重新验证。
6. 如果输出目标是 Notion，发布后必须读回或视觉检查，确认 clickable TOC、公式、前置路线图、术语表、早期核心例子和复现测试都保真。没有 Notion 登录/connector 时，输出 validated Markdown 并说明 Notion 发布被阻塞。

完成时请给我：
- 讲义文件路径或 Notion 链接。
- source/request spine 覆盖情况。
- validator 命令和结果。
- 证明颗粒度审计结论。
- 如果有未完成项，明确标成 draft/roadmap/reference note，不要冒充完成版讲义。
```

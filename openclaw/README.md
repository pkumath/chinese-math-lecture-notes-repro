# Using This Repository with OpenClaw

This repository is designed to be usable by another OpenClaw agent from only the GitHub link.

## Recommended Use

Give the other OpenClaw this prompt:

```text
请使用这个 repo 复现中文数学讲义生成流程：
https://github.com/pkumath/chinese-math-lecture-notes-repro

先读 `OPENCLAW_HANDOFF.md`，再按里面的 Required Reading Order 读取必要文件。之后按 `prompts/openclaw-handoff-prompt.zh.md` 的执行合同生成讲义、运行 validator、做 proof-granularity audit。
```

For a full copy-paste prompt, use:

```text
prompts/openclaw-handoff-prompt.zh.md
```

For a shorter per-topic request, use:

```text
prompts/topic-request-template.zh.md
```

## Local Materialization

If the agent can run shell commands, it should clone the repository before validating notes:

```bash
git clone https://github.com/pkumath/chinese-math-lecture-notes-repro.git
cd chinese-math-lecture-notes-repro
python3 scripts/validate_lecture_note.py --skill-dir skill
```

If the agent cannot clone, it should fetch/read the required files from GitHub in the order listed by `OPENCLAW_HANDOFF.md`, then reproduce the same structure and validation logic as far as its environment permits.

## Treat as Skill, Not Just Example

The `skill/` directory is the behavioral contract. The examples are supporting evidence. The current passing example is `examples/notes/mup_tensor_programs_lecture7.md`; many older examples are intentionally kept as history and may fail the current stricter validator.

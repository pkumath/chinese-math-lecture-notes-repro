# OpenClaw Handoff

This file is the stable entrypoint for another OpenClaw agent. If a user gives you this repository link and asks you to reproduce the Chinese math lecture-note workflow, follow this document before drafting.

Repository: https://github.com/pkumath/chinese-math-lecture-notes-repro

## Required Reading Order

Read these files in order:

1. `README.md`
2. `REPRODUCE.md`
3. `skill/SKILL.md`
4. `skill/references/quality-rubric.md`
5. `skill/references/proof-granularity-audit.md`
6. `standards/agent-hard-rules-extract.md`
7. `templates/lecture-note-template.md`
8. `examples/README.md`
9. `examples/notes/mup_tensor_programs_lecture7.md`
10. `sources/SOURCE_MANIFEST.md`

Do not bulk-load every historical example before drafting. Use the current passing example first; inspect historical examples only when you need style variants or counterexamples.

## Operating Contract

The output is a Chinese mathematical lecture note, not a loose explanation. Default to Markdown unless the user asks for Notion or another target.

A completed note must include:

- `## 一页摘要` at the beginning.
- `## 目录` followed immediately by `<table_of_contents color="gray"/>`.
- `## 前置路线图` before the first substantive section, with a real visual structure such as Mermaid, table, ASCII schematic, or phase map.
- `## 术语约定` or `## 符号与术语` for English terms, nonstandard notation, paper-native labels, APIs, or abbreviations.
- A source/request spine listing the user-named and source-central objects.
- An early named `贯穿例子` / `核心例子`.
- Definitions with motivation, positive examples, and non-examples.
- Theorem/proposition/lemma statements with formula-led proofs or exact imported lemmas whose hypotheses are checked locally.
- Section-end memory compression where useful.
- Tiered exercises.
- `## 复现测试` with concrete input, expected output, and pass criteria.

## Mandatory Gates

Clone or otherwise materialize this repository locally, then run:

```bash
python3 scripts/validate_lecture_note.py --skill-dir skill
python3 scripts/validate_lecture_note.py --note <draft.md> --mode full
```

If the topic has mandatory source-spine terms, pass them with repeated `--required-term`:

```bash
python3 scripts/validate_lecture_note.py \
  --note <draft.md> \
  --mode full \
  --required-term "<term 1>" \
  --required-term "<term 2>"
```

After validator success, perform a section-by-section proof-granularity audit using `skill/references/proof-granularity-audit.md`. Passing the validator is not enough.

## Source Discipline

If the note is based on a paper, theorem, textbook, or mutable web source, fetch and inspect the source before drafting. Do not infer the source spine from the title alone. Do not redistribute PDFs or extracted full texts unless you have permission; keep only citations and public links in durable artifacts.

## Notion Publishing

If the user asks for Notion publication:

1. Use the user's own Notion workspace and connector.
2. Do not reuse private page IDs from this repository; none are included.
3. Publish under the user's target page, often named `Lecture Notes`.
4. Read back or visually inspect the rendered page.
5. Verify the clickable TOC, front roadmap, formulas, terminology table, early core example, and reproduction test survived rendering.

If Notion access is unavailable, produce the validated Markdown note and say that Notion publication is blocked by missing connector/login.

## Completion Standard

Do not claim completion until:

- The draft was written locally.
- The validator passed in `full` mode.
- Required source-spine terms were checked.
- Proof-granularity audit passed or the note is explicitly labeled as a draft/roadmap/reference note.
- If publishing externally, readback/render verification passed.

## Failure Handling

If a gate fails, repair the note and rerun the gate. If the source is unavailable, ask for the source or downgrade the output to a clearly labeled draft. Do not fill missing proofs with generic prose.

# Math Lecture Notes Repro

This repository publishes the reproducible part of a math lecture-note generation workflow: writing standards, structural validator, proof-granularity audit checklist, lecture templates, current passing examples, and historical examples.

It is not a mirror of a private workspace. Notion page IDs, browser-session scripts, local token paths, source PDFs, and full extracted source texts have been removed or replaced by manifests to avoid exposing private data or redistributing copyrighted material.

## English Workflow Quick Handoff

Give another OpenClaw this repository link and the instruction below:

```text
Please use https://github.com/pkumath/chinese-math-lecture-notes-repro to reproduce the English math lecture-note workflow. First read `OPENCLAW_HANDOFF.en.md`, then follow `prompts/openclaw-handoff-prompt.en.md` to generate the note, run the validator, and perform the proof-granularity audit.
```

A fill-in topic template is available at `prompts/topic-request-template.en.md`.

## Chinese Workflow

The original Chinese workflow remains available:

- Handoff: `OPENCLAW_HANDOFF.md`
- Prompt: `prompts/openclaw-handoff-prompt.zh.md`
- Topic template: `prompts/topic-request-template.zh.md`
- Skill: `skill/`

## Repository Structure

- `skill/`: public Chinese lecture-note skill, rubric, audit checklist, and validator copy.
- `skill-en/`: public English lecture-note skill, rubric, audit checklist, and validator copy.
- `scripts/`: root validator and example audit scripts.
- `standards/`: Chinese and English public standards plus agent-rule extracts.
- `templates/`: Chinese and English lecture-note templates.
- `examples/notes/`: complete generated Markdown lecture-note examples.
- `examples/fragments/`: local rewrite fragments preserved from the writing process.
- `examples/audits/`: proof-granularity / pre-publication audit examples.
- `sources/`: source material manifest with public source clues only.
- `notion/`: reproducibility notes for Notion publication, without private IDs or credentials.

## Minimal Validation

Python 3.10+ is required. No third-party dependency is needed.

```bash
python3 scripts/validate_lecture_note.py --skill-dir skill
python3 scripts/validate_lecture_note.py --language en --skill-dir skill-en
python3 scripts/validate_lecture_note.py --note examples/notes/mup_tensor_programs_lecture7.md --mode full
python3 scripts/audit_examples.py --current-only
```

The current complete passing example is:

```text
examples/notes/mup_tensor_programs_lecture7.md
```

Some historical examples were generated before later standards were added and may fail the current full validator. To inspect all statuses:

```bash
python3 scripts/audit_examples.py --all
```

## Generating a New English Note

1. Start from `templates/lecture-note-template.en.md`.
2. List the source/request spine: user-named concepts, source-central definitions, proof tools, and promised computations.
3. Write `## One-Page Summary`, `## Table of Contents` + `<table_of_contents color="gray"/>`, and `## Front Roadmap`.
4. Enter a named `Running Example` / `Core Example` early.
5. Include terminology, positive and negative examples, theorem/proof blocks, tiered exercises, and a `Reproduction Test`.
6. Run the English validator.
7. Perform the section-by-section proof-granularity audit using `skill-en/references/proof-granularity-audit.md`.
8. If publishing to Notion, read back the rendered page and verify TOC, formulas, roadmap, running example, and reproduction test.

## Quality Boundary

The validator checks structure, terminology-section presence, and Notion math hygiene. It does not prove mathematical correctness. The real publication standard still requires a human or agent to perform the section-by-section proof-granularity audit.

## License

Code and documentation in this repository are released under the MIT License. Source papers, books, webpages, and other external materials remain owned by their authors and publishers; this repository only stores public links and citation clues.

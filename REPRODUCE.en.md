# Reproduce Checklist: English Math Lecture Notes

This is a reproducible path from a blank topic to a publishable English mathematics lecture note.

## 1. Choose the topic and source material

Fix three things before writing:

- Topic question: what should the note teach the reader to judge, compute, or prove?
- Source material: paper, textbook section, lecture note, webpage, or user draft.
- Source/request spine: definitions, theorems, parameterizations, proof devices, examples, or algorithms that cannot be missing.

Write the source/request spine into the draft. If a spine item is not covered, the one-page summary must explicitly state the boundary and reason.

## 2. Draft the structure

Copy the English template:

```bash
cp templates/lecture-note-template.en.md my_note.md
```

A formal note needs at least:

- `## One-Page Summary`
- `## Table of Contents` followed by `<table_of_contents color="gray"/>`
- `## Front Roadmap`
- `## Terminology` or `## Notation and Terminology`
- an early named `Running Example` / `Core Example`
- core definitions, examples, non-examples, theorems, and proofs
- tiered exercises
- `## Reproduction Test`

## 3. Run structural validation

```bash
python3 scripts/validate_lecture_note.py --language en --note my_note.md --mode full
```

If the source/request spine contains mandatory terms, use repeated `--required-term`:

```bash
python3 scripts/validate_lecture_note.py \
  --language en \
  --note my_note.md \
  --mode full \
  --required-term "Gaussian conditioning" \
  --required-term "multi-step recurrence"
```

Validate the English skill itself with:

```bash
python3 scripts/validate_lecture_note.py --language en --skill-dir skill-en
```

## 4. Perform proof-granularity audit

After the validator passes, answer the checklist in `skill-en/references/proof-granularity-audit.md` section by section. Focus on:

- what each section proves or derives;
- where each hypothesis is used;
- whether the running example actually tests definitions, theorem hypotheses, and proof steps;
- whether the reader can reproduce a same-shaped computation or proof;
- whether all source/request spine items are substantively covered.

## 5. Notion publication

See `notion/README.md`. This public repository does not include private Notion page IDs, tokens, or browser sessions.

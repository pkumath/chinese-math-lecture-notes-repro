# OpenClaw English Math Lecture-Note Handoff Prompt

Send the block below to another OpenClaw. Replace `{TOPIC}`, `{SOURCE}`, and `{OUTPUT_TARGET}` as needed.

```text
Please use this public repository to reproduce the English math lecture-note workflow:

https://github.com/pkumath/chinese-math-lecture-notes-repro

Treat the repository as a workflow/skill specification, not just as a README. Read and follow these files in order:

1. OPENCLAW_HANDOFF.en.md
2. README.md or README.en.md
3. REPRODUCE.en.md
4. skill-en/SKILL.md
5. skill-en/references/quality-rubric.md
6. skill-en/references/proof-granularity-audit.md
7. standards/agent-hard-rules-extract.en.md
8. standards/english-math-lecture-note-standards.md
9. templates/lecture-note-template.en.md
10. examples/README.md
11. examples/notes/mup_tensor_programs_lecture7.md only as a structural reference; it is Chinese and should not determine English prose.
12. sources/SOURCE_MANIFEST.md

Task: generate an English mathematical lecture note.

Topic: {TOPIC}
Source material: {SOURCE}
Output target: {OUTPUT_TARGET}
Default reader: a mathematically mature reader who can read rigorous proofs, but needs the note to make the semantic center, roadmap, examples, proof burden, hypothesis use, and research use explicit.

Hard requirements:
- Do not begin with generic explanation. First establish the source/request spine: user-named objects, source-central definitions/theorems/proof tools, and the computation or proof workflow promised by the topic.
- A formal note must begin with `## One-Page Summary`, and the summary must state the central problem, main answer, reading path, and boundary.
- The summary must be followed by `## Table of Contents` and then `<table_of_contents color="gray"/>`.
- Before the first substantive section, include `## Front Roadmap`; the roadmap must use Mermaid, a table, ASCII schematic, or similar structure to carry mathematical dependencies. A prose-only roadmap is not enough.
- Include `Terminology` / `Notation and Terminology`. Define nonstandard terms, paper-native labels, APIs, abbreviations, and notation before use.
- Enter a named `Running Example` / `Core Example` early and reuse it in definitions, theorem hypotheses, proofs, boundaries, and the Reproduction Test.
- Each core concept needs motivation, a formal definition, positive examples, and non-examples.
- Core theorems/propositions/lemmas need formula-led proofs, or exact standard-lemma citations with local hypotheses checked. Do not skip central steps with "it is easy", "standard", "similar", or "omitted".
- Include tiered exercises.
- Include `Reproduction Test` with input, expected output, and pass criteria.

Execution:
1. If the source material is a paper/webpage/file, inspect it first; do not infer the source spine from the title alone.
2. Save the draft locally, for example `work/lecture-notes/<slug>.md`.
3. Run the repository validator:
   `python3 scripts/validate_lecture_note.py --language en --skill-dir skill-en`
   `python3 scripts/validate_lecture_note.py --language en --note <draft.md> --mode full`
4. If the source/request spine has mandatory objects, rerun the validator with repeated `--required-term`.
5. After the validator passes, perform a section-by-section proof-granularity audit using `skill-en/references/proof-granularity-audit.md`; if it fails, revise and rerun validation.
6. If the output target is Notion, publish and then read back or visually inspect the rendered page. Confirm that the clickable TOC, formulas, front roadmap, terminology table, early running example, and reproduction test survived rendering. If Notion login/connector is unavailable, output validated Markdown and state the blocker.

When finished, give me:
- The note file path or Notion link.
- Source/request spine coverage.
- Validator commands and results.
- Proof-granularity audit conclusion.
- Any unfinished item explicitly labeled as draft/roadmap/reference note, not as a completed lecture note.
```

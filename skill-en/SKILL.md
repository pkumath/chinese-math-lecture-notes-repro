---
name: english-math-lecture-notes
description: Produce rigorous, visually polished English mathematics lecture notes for a requested topic, validate the note against a learning-quality rubric, and publish each note as a child page under the Notion page named "Lecture Notes" using the native Codex Notion connector. Use when the user asks to learn a math topic, build an English lecture note, create a Notion math note, or publish lecture notes to Notion.
---

# English Math Lecture Notes

Use this skill when the user wants an English mathematics lecture note for a topic. The output target is Markdown by default, or a Notion child page under **Lecture Notes** when the user asks for Notion publication.

## Mandatory Workflow

1. Clarify only true blockers. If the topic is clear, proceed. Assume the audience is the requesting reader unless a different audience is specified.
2. If the output target is Notion, use the native Notion connector first. Search for the Notion page titled `Lecture Notes`, fetch it, then create the lecture note as a child page under that page.
3. Fetch Notion enhanced Markdown guidance when available before writing. Use connector-supported Notion-flavored Markdown.
4. Before drafting, establish a terminology and notation table. Define nonstandard names, paper-native labels, APIs, abbreviations, and private notation before use. Maintain terminology discipline: do not introduce agent-coined labels unless they are mathematically defined, motivated, and used later.
5. Before drafting, establish a source/request spine. Extract the named concepts, methods, formulas, and proof devices that the user explicitly asked about or that the primary source treats as central. A serious note must explicitly teach every spine item or say why it is out of scope in the one-page summary.
6. Every generated lecture note must start with a compact `## One-Page Summary`. The summary must foreground the central problem, main answer, reading path, and boundary of what the lecture does not prove. It should use no display math, no long derivation, and at most four short prose paragraphs or one compact table.
7. Every generated lecture note must include a clickable Notion-native table of contents near the top: add `## Table of Contents` followed immediately by `<table_of_contents color="gray"/>`, after the one-page summary and before the first substantive section.
8. Every serious note must include a `## Front Roadmap` immediately after the clickable table of contents and before the first substantive section. Include a real visual dependency/path block: a Mermaid diagram, native Notion table, ASCII schematic, stable rendered diagram, phase map, or equivalent. A prose paragraph alone is not enough.
9. Every serious note must pass the learning-load and reproduction gate before drafting settles: introduce one named `Running Example` / `Core Example` early, reuse that same example through definitions and proofs, and include a `Reproduction Test` section that states what the reader should be able to reproduce without looking back at the prose.
10. Keep front matter light. Required structure must not become a wall before the mathematical point. After the compact summary, clickable TOC, and front roadmap, move quickly into the core example/problem rather than adding long reader-profile, meta-standard, or checklist prose.
11. Draft locally first when the note is substantial. Save Markdown in `work/lecture-notes/` or `tmp/lecture-notes/` and run the bundled validator before publishing. When the source/request spine has mandatory named objects, pass them to the validator with repeated `--required-term` arguments.
12. Validate English mathematical prose. A serious English lecture note must read like a polished human-authored mathematical note, not an AI assistant report, workflow log, dashboard, or audit transcript.
13. Validate math formatting. Inline math must be Notion-stable dollar-backtick LaTeX backtick-dollar. Display math must use `$$ ... $$`. Ordinary inline dollar math is not allowed.
14. Run a proof-granularity and learning audit after the validator and before publishing. The audit must inspect every major section and decide whether it is a real math lecture section or only a reference-style outline. If any central section has definitions/theorem statements without complete proofs, exact standard-lemma citations, worked examples, hypothesis-use explanations, section-end memory compression, source-spine coverage, and a concrete reader-reproduction outcome, rewrite before publishing or clearly downgrade the output to a draft.
15. If publishing to Notion, use `notion_create_pages` under the `Lecture Notes` parent page. Page content must not repeat the page title as the first heading.
16. Read back with `notion_fetch` and check that key headings, compact one-page summary, clickable table of contents, front roadmap, terminology table, early running example, reproduction test, source-spine concepts, and math survived. If formulas render literally, the summary is bloated or unfocused, terminology remains undefined, private labels appear, the front roadmap is missing, the running example is late/thin, the reproduction test is absent, a required source/request concept is missing, or the table of contents is not present/clickable, fix before claiming completion.

## Standard Sync Gate

When the user asks to update the English lecture-note standard, update this local skill, rubric, validator, template, and any public standard document in the same run. If the change is durable or behavioral, also update the agent's durable memory / hard-rule files in the same run.

## Quality Gate

Read `references/quality-rubric.md` before producing a serious note. A publishable note must include:

- clear reader prerequisites and learning objectives;
- a compact one-page summary that states the central problem, main answer, reading path, and boundary before details;
- a problem-first roadmap, not a definition dump;
- a front roadmap immediately after the clickable table of contents, before the first substantive section, with a real visual path/dependency block;
- source/request spine coverage: all named objects central to the user's question or primary source must be taught explicitly, not silently replaced by nearby easier material;
- one early named running example that carries the lecture and prevents definition/checklist sprawl;
- motivation, definitions, examples, non-examples, theorem statements, proof spines, and complete proofs for central results;
- a reader reproduction test: the note must say what calculation/proof the reader should be able to redo after the core sections, and the body must actually supply enough detail for that test;
- a clickable Notion-native table of contents using `## Table of Contents` followed by `<table_of_contents color="gray"/>`;
- visual structure: at least one diagram, table, schematic, or phase-map style block when the topic allows it;
- exercises in tiers from definition checks to research-facing extensions;
- section-end memory compression: takeaways, pitfalls, and next-step links;
- polished English mathematical prose with precise terminology;
- terminology discipline: include a `Terminology` / `Notation and Terminology` block for substantial notes; define nonstandard terms and notation before use; do not leave agent-invented labels undefined.

## Notion Math Rules

- Display math uses double-dollar blocks and should carry all substantive derivations, theorem hypotheses, and multi-symbol formulas.
- Avoid dense Notion inline equation chips in prose. In this workflow, the visual quality gate is the rendered Notion page, not merely connector readback: if inline formulas show as gray `$...$` chips, literal backticks/dollars, stripped commands, or source-like TeX, rewrite them.
- For short in-sentence mathematical tokens, prefer clean readable text/Unicode when that is visually better than Notion inline equation chips; for real formulas, promote them to display equations instead of leaving raw TeX in prose.
- Never use ordinary inline dollar math in Notion pages; it may be escaped or displayed literally.
- Do not put Notion inline equations in headings that feed the table of contents; Notion's TOC can serialize them as raw `$...$`. Use clean plain text such as `1/sqrt(n)` in headings, and reserve rendered equations for body text or display blocks.
- Scan for damaged LaTeX commands such as `pimathbb`, `A^top`, `topsucceq0`, stripped commands, visible `$`/backtick delimiters, or source-like `\\sum`/`\\phi` in rendered prose.
- Do not leave formula-testing or scratch pages under `Lecture Notes`; create tests outside the target parent when unavoidable, and trash/archive them before reporting completion.

## Validation Commands

```bash
python3 scripts/validate_lecture_note.py --language en --skill-dir skill-en
python3 scripts/validate_lecture_note.py --language en --note work/lecture-notes/<note>.md --mode full
```

The validator is a gate, not proof of quality. Passing it means the note has the required structural, clickable-TOC, and Notion-math hygiene; the agent must still do the mathematical judgment.

## One-Page Summary Gate

Every completed lecture note must start with `## One-Page Summary`. This section is a high-signal orientation surface, not a mini introduction. It must answer: what problem this lecture solves, what the main answer is, how to read the lecture, and what the lecture does not automatically prove. Keep it visually light: no display math, no proof details, no long background recap, and no more than four short prose paragraphs unless using one compact table.

## Clickable TOC Gate

Every completed lecture note must include a Notion-native clickable table of contents, not a hand-written bullet list. The required block is:

```markdown
## Table of Contents
<table_of_contents color="gray"/>
```

Place it after `## One-Page Summary` and before the first substantive section. Do not publish or claim completion if readback does not show the table-of-contents block.

## Front Roadmap Gate

Every completed serious lecture note must include an explicit front roadmap right after the clickable table of contents and before the first substantive section. The roadmap must show the learning path or dependency graph visually, using a Mermaid diagram, native Notion table, ASCII schematic, stable rendered diagram, phase map, or equivalent. It must answer "where are we going and how do the parts depend on each other?" at a glance. Do not let a generic prose paragraph or a late section-local table satisfy this gate.

## Learning-Load and Reproduction Gate

Completed lecture notes must optimize for the reader actually learning the mathematics, not for passing a structural checklist. The note fails this gate if the setup is long but the central computation/proof is thin, if definitions appear before the motivating object they are needed for, or if the reader cannot reproduce a same-shaped calculation after reading.

For serious notes:

- introduce a named `Running Example` / `Core Example` early, normally before the first theorem-heavy section;
- reuse that example when defining objects, applying theorem hypotheses, and explaining proof steps;
- split long derivations into short claim/reason blocks, so every nontrivial equality says what justifies it;
- include a `Reproduction Test` section with concrete inputs, expected outputs, and pass criteria;
- remove meta commentary, repeated route tables, and checklists that do not directly help the reader carry out the central calculation or proof.

Passing the validator is not enough if this gate fails. Rewrite the note around the running example and proof burden before publishing.

## Source-Spine Coverage Gate

Completed lecture notes must answer the actual topic asked, not an adjacent sanitized version of it. Before writing, list the source/request spine: the specific named definitions, parameterizations, proof devices, example computations, and algorithms that the user or primary sources make central. The lecture must either teach each spine item in a substantive section or explicitly mark it out of scope in the one-page summary with a reason.

Use the validator's `--required-term` option for mandatory spine terms when drafting locally. Passing this check is not sufficient, but failing it blocks publication.

## Proof-Granularity Gate

The semantic gate is mandatory because the validator cannot verify proof quality. Before publishing a serious note, make a local section-by-section audit using `references/proof-granularity-audit.md` as the checklist. The note fails this gate if:

- a central theorem, proposition, lemma, construction, or algorithm appears without either a complete proof or a precisely stated standard result being invoked;
- a section only lists definitions, intuitions, or claims, without deriving something, proving something, working a nontrivial example, or exposing a boundary case;
- proof text uses phrases such as "it is easy to see", "standard", "similar", "omitted", or "by intuition" without unpacking the argument or naming the exact imported lemma;
- hypotheses are stated but the note does not explain where each important hypothesis is used and what fails when it is weakened;
- examples and non-examples are too thin to test the theorem assumptions;
- the proof audit could be written without checking what the reader should be able to reproduce after the section.

Do not claim the page is a completed math lecture note until this audit passes. If the content is intentionally lighter, label it as a draft / roadmap / reference note instead of a lecture note.

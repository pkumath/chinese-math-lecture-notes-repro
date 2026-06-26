---
name: chinese-math-lecture-notes
description: Produce rigorous, visually polished Chinese mathematics lecture notes for a requested topic, validate the note against a learning-quality rubric, and publish each note as a child page under the Notion page named "Lecture Notes" using the native Codex Notion connector. Use when the user asks to learn a math topic, build a Chinese lecture note, create a Notion math note, or publish lecture notes to Notion.
---

# Chinese Math Lecture Notes

Use this skill when the user wants a Chinese mathematics lecture note for a topic. The output target is always a Notion child page under **Lecture Notes** unless the user says otherwise.

## Mandatory Workflow

1. Clarify only true blockers. If the topic is clear, proceed. Assume the audience is the requesting reader unless a different audience is specified.
2. Use native Notion connector first. Search for the Notion page titled `Lecture Notes`, fetch it, then create the lecture note as a child page under that page.
3. Fetch Notion enhanced Markdown guidance when available before writing. Use connector-supported Notion-flavored Markdown.
4. Before drafting, establish a Chinese-first terminology table for the note. For every nonstandard or potentially ambiguous English term, choose a Chinese term, give the English original in parentheses at first occurrence only, and then use the Chinese term consistently. API names, package/class names, paper titles, theorem labels, code identifiers, and standard abbreviations may remain exact.
4a. Before drafting, establish a source/request spine. Extract the named concepts, methods, formulas, and proof devices that the user explicitly asked about or that the primary source treats as central. A serious note must explicitly teach every spine item or say why it is out of scope in the one-page summary. Do not publish a note that answers a nearby easier topic while omitting the user's named objects.
5. Every generated lecture note must start with a compact `## 一页摘要`. The summary must foreground the central question, main answer, reading path, and boundary of what the lecture does not prove. It should use no display math, no long derivation, and at most four short prose paragraphs or one compact table.
6. Every generated lecture note must include a clickable Notion-native table of contents near the top: add `## 目录` followed immediately by `<table_of_contents color="gray"/>`, after the one-page summary and before the first substantive section.
7. Every serious note must include a front roadmap immediately after the clickable table of contents and before the first substantive section. Use `## 前置路线图` or an equivalent heading, and include a real visual dependency/path block: a Mermaid diagram, native Notion table, ASCII schematic, stable rendered diagram, phase map, or equivalent. A sentence saying "roadmap" is not enough.
8. Every serious note must pass the learning-load and reproduction gate before drafting settles: introduce one named `贯穿例子` / `核心例子` early, use that same example to motivate definitions and proofs, and include a `复现测试` section that states what the reader should be able to reproduce without looking back at the prose.
9. Keep front matter light. Required structure must not become a wall before the mathematical point. After the compact summary, clickable TOC, and visual roadmap, move quickly into the core example/problem rather than adding long reader-profile, meta-standard, or checklist prose.
10. Draft locally first when the note is substantial. Save Markdown in `tmp/lecture-notes/` and run the bundled validator before publishing. When the source/request spine has mandatory named objects, pass them to the validator with repeated `--required-term` arguments.
11. Validate Chinese terminology and prose. A serious Chinese lecture note must not read like English notes with Chinese connective tissue. Repeated untranslated terms such as `proxy`, `target`, `raw`, `loss surface`, `schedule`, `readout`, `coord check`, `master coordinate`, or private agent-coined labels fail the gate unless they are defined as mathematical objects and then translated.
12. Validate math formatting. Inline math must be Notion-stable dollar-backtick LaTeX backtick-dollar. Display math must use `$$ ... $$`. Ordinary inline dollar math is not allowed.
13. Run a proof-granularity and learning audit after the validator and before publishing. The audit must inspect every major section and decide whether it is a real math lecture section or only a reference-style outline. If any central section has definitions/theorem statements without complete proofs, exact standard-lemma citations, worked examples, hypothesis-use explanations, section-end memory compression, source-spine coverage, and a concrete reader-reproduction outcome, rewrite before publishing or clearly downgrade the output to a draft.
14. Publish to Notion with `notion_create_pages` using the `Lecture Notes` parent page. Page content must not repeat the page title as the first heading.
15. Read back with `notion_fetch` and check that key headings, compact one-page summary, clickable table of contents, front roadmap, terminology table, early core example, reproduction test, source-spine concepts, and math survived. If formulas render literally, the summary is bloated or unfocused, terminology remains English-heavy, undefined private terms appear, the front roadmap is missing, the core example is late/thin, the reproduction test is absent, a required source/request concept is missing, or the table of contents is not present/clickable, fix before claiming completion.

## Standard Sync Gate

When the user asks to update the Chinese lecture-note standard, the Notion page `中文数学讲义生成标准` is the law and this local skill/rubric/validator is the execution layer. Update both in the same run, then verify local validation and Notion readback before generating another formal lecture note. If the change is durable or behavioral, also update the agent's durable memory / hard-rule files in the same run.

## Quality Gate

Read `references/quality-rubric.md` before producing a serious note. A publishable note must include:

- clear reader prerequisites and learning objectives;
- a compact one-page summary that states the central question, main answer, reading path, and boundary before details;
- a problem-first roadmap, not a definition dump;
- a front roadmap immediately after the clickable table of contents, before the first substantive section, with a real visual path/dependency block;
- source/request spine coverage: all named objects central to the user's question or primary source must be taught explicitly, not silently replaced by nearby easier material;
- one early named core example that carries the lecture and prevents definition/checklist sprawl;
- motivation, definitions, examples, non-examples, theorem statements, proof spines, and complete proofs for central results;
- a reader reproduction test: the note must say what calculation/proof the reader should be able to redo after the core sections, and the body must actually supply enough detail for that test;
- a clickable Notion-native table of contents using `## 目录` followed by `<table_of_contents color="gray"/>`;
- visual structure: at least one diagram, table, schematic, or phase-map style block when the topic allows it;
- exercises in tiers from definition checks to research-facing extensions;
- section-end memory compression: summary, pitfalls, and next-step links;
- polished Chinese prose with mathematically precise terminology;
- Chinese-first terminology discipline: include a `术语约定` / `符号与术语` block for substantial notes; translate ordinary explanatory terms into Chinese after first mention; do not leave repeated English scaffolding or agent-invented terms undefined.

## Notion Math Rules

- Display math uses double-dollar blocks and should carry all substantive derivations, theorem hypotheses, and multi-symbol formulas.
- Avoid dense Notion inline equation chips in Chinese lecture prose. In this workspace, the visual quality gate is the rendered Notion page, not merely connector readback: if inline formulas show as gray `$...$` chips, literal backticks/dollars, stripped commands, or source-like TeX, rewrite them.
- For short in-sentence mathematical tokens, prefer clean readable text/Unicode when that is visually better than Notion inline equation chips; for real formulas, promote them to display equations instead of leaving raw TeX in prose.
- Never use ordinary inline dollar math in Notion pages; it may be escaped or displayed literally.
- Do not put Notion inline equations in headings that feed the table of contents; Notion's TOC can serialize them as raw `$...$`. Use clean plain text such as `1/sqrt(n)` in headings, and reserve rendered equations for body text or display blocks.
- Scan for damaged LaTeX commands such as `pimathbb`, `A^top`, `topsucceq0`, stripped commands, visible `$`/backtick delimiters, or source-like `\\sum`/`\\phi` in rendered prose.
- Do not leave formula-testing or scratch pages under `Lecture Notes`; create tests outside the target parent when unavoidable, and trash/archive them before reporting completion.

## Validation Commands

```bash
python3 skills/chinese-math-lecture-notes/scripts/validate_lecture_note.py --skill-dir skills/chinese-math-lecture-notes
python3 skills/chinese-math-lecture-notes/scripts/validate_lecture_note.py --note tmp/lecture-notes/<note>.md --mode full
```

The validator is a gate, not proof of quality. Passing it means the note has the required structural, clickable-TOC, and Notion-math hygiene; the agent must still do the mathematical judgment.

## One-Page Summary Gate

Every completed lecture note must start with `## 一页摘要`. This section is a high-signal orientation surface, not a mini introduction. It must answer: what problem this lecture solves, what the main answer is, how to read the lecture, and what the lecture does not automatically prove. Keep it visually light: no display math, no proof details, no long background recap, and no more than four short prose paragraphs unless using one compact table.

## Clickable TOC Gate

Every completed lecture note must include a Notion-native clickable table of contents, not a hand-written bullet list. The required block is:

```markdown
## 目录
<table_of_contents color="gray"/>
```

Place it after `## 一页摘要` and before the first substantive section. Do not publish or claim completion if readback does not show the table-of-contents block.

## Front Roadmap Gate

Every completed serious lecture note must include an explicit front roadmap right after the clickable table of contents and before the first substantive section. The roadmap must show the learning path or dependency graph visually, using a Mermaid diagram, native Notion table, ASCII schematic, stable rendered diagram, phase map, or equivalent. It must answer "where are we going and how do the parts depend on each other?" at a glance. Do not let a generic prose paragraph or a late section-local table satisfy this gate, and do not replace an already clear Mermaid roadmap just because a table would also work.

## Learning-Load and Reproduction Gate

Completed lecture notes must optimize for the reader actually learning the mathematics, not for passing a structural checklist. The note fails this gate if the setup is long but the central computation/proof is thin, if definitions appear before the motivating object they are needed for, or if the reader cannot reproduce a same-shaped calculation after reading.

For serious notes:

- introduce a named `贯穿例子` / `核心例子` early, normally before the first theorem-heavy section;
- reuse that example when defining objects, applying theorem hypotheses, and explaining proof steps;
- split long derivations into short claim/reason blocks, so every nontrivial equality says what justifies it;
- include a `复现测试` section with concrete inputs, expected outputs, and pass criteria;
- remove meta commentary, repeated route tables, and checklists that do not directly help the reader carry out the central calculation or proof.

Passing the validator is not enough if this gate fails. Rewrite the note around the core example and proof burden before publishing.

## Source-Spine Coverage Gate

Completed lecture notes must answer the actual topic asked, not an adjacent sanitized version of it. Before writing, list the source/request spine: the specific named definitions, parameterizations, proof devices, example computations, and algorithms that the user or primary sources make central. The lecture must either teach each spine item in a substantive section or explicitly mark it out of scope in the one-page summary with a reason.

For example, a serious μP / Tensor Programs note that claims to teach how μP is set up or how training dynamics are computed must not omit `abc parametrization`, μP initialization and learning-rate scaling, Gaussian conditioning / conditioning on initial logits when relevant, and fixed-step multi-step recurrence. A note that only computes an initialization kernel is an initialization-kernel note, not a μP training-dynamics note.

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

# English Math Lecture Note Quality Rubric

## Goal

A lecture note should help the reader reconstruct the mathematical structure of a topic under controlled cognitive load. It is not a reference dump. The default reader is mathematically mature and willing to read rigorous proofs, but still needs the note to expose the semantic center, roadmap, examples, proof burden, and research-facing use.

## Standard Sync

The English skill, this rubric, the validator, templates, and public standards are one execution layer. When one is updated, synchronize the others in the same run before generating another formal lecture note.

## Required Structure

1. **Reader profile and prerequisites**
   - State the expected background, what can be skipped, and which heavy tools are not used.
   - Distinguish conceptual understanding, proof reproduction, and research-facing transfer.

2. **Problem first**
   - Open by saying what problem the topic solves, why a new object is needed, and which theorem or method the note is aiming toward.
   - Do not begin with a disconnected list of definitions.

3. **One-Page Summary Gate**
   - Every formal note must begin with `## One-Page Summary`.
   - The summary must answer four questions before details: the central problem, the main answer, the reading path, and the boundary of what the note does not prove.
   - Keep it compact: at most four short prose paragraphs, or one small table plus a little prose. Do not put display equations, proof details, long background recaps, or technical inventories there.

4. **Front Roadmap**
   - Every formal note must place `## Front Roadmap` or an equivalent heading after the table of contents and before the first substantive section.
   - The Front Roadmap must be a visual learning path or dependency structure: Mermaid graph, Notion table, ASCII schematic, rendered diagram, phase map, or flowchart.
   - A prose paragraph saying "the roadmap is..." does not pass.

5. **Learning load and Reproduction Test**
   - A formal note must let the reader reproduce a same-shaped calculation, proof, or judgment.
   - After the summary, clickable TOC, and Front Roadmap, move quickly into a named `Running Example` / `Core Example`.
   - The running example must reappear in definitions, theorem-hypothesis checks, proof steps, and boundary discussion.
   - Every serious note must include a `Reproduction Test` with input, expected output, and pass criteria.

6. **Source/request spine coverage**
   - The note must answer the actual requested topic, not an easier adjacent topic.
   - Before writing, list the source/request spine: user-named concepts, source-central definitions, parameterizations, proof devices, and promised computational workflows.
   - Each spine item must be taught in a substantive section or explicitly marked out of scope in the one-page summary with a reason.

7. **Concept package**
   - Each core concept needs motivation, a formal definition, positive examples, and non-examples.
   - Non-examples are not optional; they expose boundaries.

8. **Terminology discipline**
   - This is the terminology discipline gate for English notes.
   - English mathematical prose should be precise, natural, and human-authored.
   - Include a `Terminology` / `Notation and Terminology` section for substantial notes.
   - Define nonstandard terms, paper-native labels, APIs, abbreviations, and private notation before their first serious use.
   - Do not use agent-facing terms, workflow labels, audit language, or dashboard prose inside the lecture body.

9. **Theorem and proof spine**
   - Every core theorem needs a precise statement, hypothesis explanation, proof spine, and complete proof or exact citation to a standard lemma.
   - After the proof, explain where the important hypotheses are used and what fails when they are weakened.

10. **Linearized dependencies**
    - Each major section should say what it depends on, what it introduces, and which later result it supports.
    - For complex topics, add a dependency diagram or route table.

11. **Visual mathematical structure**
    - Use at least one visual organizer: Mermaid graph, ASCII diagram, table, flowchart, phase map, concept relation graph, or stable rendered image.
    - The visual element must carry mathematical information, not decoration.

12. **Tiered exercises**
    - Level 0: definition checks.
    - Level 1: reproduce a key proof step.
    - Level 2: apply the theorem to a new example.
    - Level 3: construct a counterexample or boundary case.
    - Level 4: research-facing extension.

13. **Section-end memory compression**
    - Major sections should end with 2-4 takeaways, common pitfalls, and a reason the next section is natural.

14. **Notion layout**
    - The page title belongs in Notion properties; do not repeat it as a first H1 in the body.
    - Every completed note must include `## Table of Contents` followed by `<table_of_contents color="gray"/>` after the one-page summary and before substantive content.
    - Use short paragraphs, tables, toggles/callout-style blocks, and display equations for reading rhythm.
    - Inline math must use dollar-backtick LaTeX backtick-dollar. Display math must use double-dollar blocks.

15. **Rigor boundary**
    - Do not invent history, attribution, or details you have not checked.
    - Standard theorems may be cited, but the note must say exactly what is being imported and why its hypotheses hold locally.
    - Intuition can come first in an introductory note, but intuition cannot replace theorem statements and proofs.

16. **Section-by-section proof granularity**
    - Each major section must withstand the question: what exactly did this section prove, derive, or rule out?
    - Central sections cannot contain only definitions, theorem statements, and proof ideas. They need complete proofs or exact imported lemmas with checked hypotheses.
    - If a section is only a roadmap, reference block, or terminology guide, label it as such instead of presenting it as a completed mathematical lecture section.

## Pre-Publication Checklist

- Topic, goal, and prerequisites are explicit.
- `## One-Page Summary` is compact and identifies the central problem, main answer, reading path, and boundary.
- A `Terminology` / `Notation and Terminology` section defines nonstandard terms and notation.
- `## Table of Contents` is followed by `<table_of_contents color="gray"/>`.
- A visual Front Roadmap appears before the first substantive section.
- The note quickly enters a named Running Example / Core Example.
- The source/request spine is listed and substantively covered.
- At least one running example carries core concepts, theorem hypotheses, proof steps, and boundaries.
- A Reproduction Test includes input, expected output, and pass criteria.
- At least one non-example or counterexample explains a boundary.
- At least one core theorem has a proof spine and proof.
- Each major section has passed section-by-section proof granularity audit.
- At least one visual structure block is present.
- Exercises are tiered.
- The prose does not read like an AI assistant report, audit log, workflow note, or dashboard.
- There is no ordinary inline dollar math.
- There are no damaged LaTeX commands.
- If published to Notion, readback/render verification passed.

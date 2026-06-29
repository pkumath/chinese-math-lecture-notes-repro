# Agent Hard-Rules Extract for English Math Lecture Notes

This is the public extract of lecture-note rules relevant to the English workflow. It intentionally excludes private workspace state, credentials, page IDs, and unrelated agent instructions.

## English Lecture Quality Is a Hard Gate

- English mathematical prose quality is a hard gate, not a polish preference.
- Formal notes must begin with a compact `## One-Page Summary` that foregrounds the central problem, main answer, reading path, and boundary.
- Formal notes must include a clickable `## Table of Contents` followed by `<table_of_contents color="gray"/>`.
- Formal notes must include a Front Roadmap immediately after the clickable TOC and before the first substantive section.
- Mermaid roadmaps are valid and recommended visual roadmaps; do not replace a clear Mermaid roadmap merely because a native table would also work.
- Formal notes must include a `Terminology` / `Notation and Terminology` block when paper-native labels, APIs, nonstandard notation, or abbreviations are used.
- Do not introduce private agent-coined terminology, workflow names, or audit labels without immediate definition, motivation, and examples/non-examples.

## Learning Load and Source-Spine Coverage

- Required structure must not become front-matter bloat: summary, TOC, roadmap, and terminology orient the reader, then the note must move quickly to the central calculation or proof.
- Formal notes must introduce a named `Running Example` / `Core Example` early and reuse it through definitions, proofs, boundaries, and the Reproduction Test.
- Formal notes must include a concrete `Reproduction Test` with input, expected output, and pass criteria.
- Formal notes must cover the source/request spine: user-named concepts, source-central definitions/proof devices, and title-promised workflows must appear in substantive sections or be explicitly scoped out in the one-page summary.
- Do not answer a nearby easier topic while omitting the named core objects.

## Proof and Formula Discipline

- Formulas, displayed identities, theorem statements, proof spines, and complete proofs should carry the logic; prose explains the displays rather than replacing missing derivations.
- Every central theorem, proposition, lemma, construction, or algorithm must have a complete proof or an exact imported standard result with local hypotheses verified.
- Avoid hand-waved phrases such as "it is easy to see", "standard", "similar", or "omitted" when they hide the main step.
- Explain where each important hypothesis is used and what fails when it is weakened.
- Do not introduce redundant symbols or notation merely to look formal; each symbol must shorten a formula, remove ambiguity, or carry a later proof obligation.

## Notion and Publication Discipline

- Inline math must use dollar-backtick LaTeX backtick-dollar; display math must use double-dollar blocks.
- Completed notes must be validated locally and then proof-audited section by section.
- If publishing to Notion, read back or visually inspect the rendered page before claiming completion.
- Passing the structural validator is necessary but never sufficient evidence of mathematical quality.

# Section-by-Section Proof-Granularity Audit

Use this checklist after the structural / Notion-math validator passes and before publishing a serious English math lecture note.

## Section-Level Pass Criteria

For every major section, write a short internal pass/fail note answering:

1. What mathematical job does this section do for the lecture?
2. What are the central definitions, claims, theorem statements, or constructions?
3. What proof obligations did the section create?
4. Are those obligations discharged by complete proofs, or by exact citations to standard lemmas with stated hypotheses?
5. Where is each important hypothesis used?
6. What worked example or non-example tests the section's assumptions?
7. What should the reader remember at the end of the section?
8. What exact calculation, proof step, or boundary judgment should the reader be able to reproduce after this section?
9. Did the section reuse the named running example or explain why it is temporarily leaving that example?
10. Is any setup/checklist prose delaying the mathematical point without helping the reader reproduce the result?
11. Did the section cover the source/request spine item it is responsible for, or did it replace a named topic with a nearby easier calculation?

## Hard Fail Signals

- The section is mostly definitions plus prose motivation.
- The section states a theorem but only gives proof intuition.
- A proof hides the main step behind "standard", "easy", "similar", "omitted", or "by continuity" without unpacking it.
- A central object is introduced but never used in a proof, example, or later theorem.
- There is no example or non-example that would catch a wrong understanding of the assumptions.
- The section's summary could have been written without reading the proof details.
- The section passes a structural checklist but does not help the reader reproduce a same-shaped example.
- The section introduces definitions or route tables before the motivating example that makes them necessary.
- A user-named or source-central object is absent, or appears only as a word in a terminology table without a substantive definition, calculation, or proof role.
- The note answers an easier adjacent topic while the promised source/request spine is missing.
- The proof audit says "pass" without naming the reader's likely sticking point and how the section resolves it.

## Required Repair

When a section fails, repair it by doing at least one of the following before publication:

- add a complete proof with line-by-line logical transitions;
- state the exact imported lemma/theorem and verify its hypotheses in the local notation;
- add a worked example that computes or verifies the central object;
- add a non-example or counterexample showing why a hypothesis is needed;
- split an overpacked section into a definition section plus a proof section;
- add or strengthen the named running example and reuse it through the proof;
- add a source/request spine table and route every spine item to a substantive section, or explicitly mark it out of scope before publication;
- add a Reproduction Test with concrete input, expected output, and pass criteria;
- delete or compress front matter/checklist prose that delays the main calculation;
- downgrade the page label from lecture note to draft/roadmap/reference note.

## Final Internal Certificate

Before publishing, produce a concise internal certificate:

```text
Proof-granularity audit:
- Section 1: pass/fail - reason
- Section 2: pass/fail - reason
- ...
Overall: publishable lecture note / needs rewrite / draft only
```

Only publish as a completed math lecture note when the overall status is `publishable lecture note`.

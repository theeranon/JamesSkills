---
name: make-it-james
kind: shared-standard
license: CC-BY-NC-4.0
description: Enforce the wording law on anything a real person will read, so it reads as native writing rather than as translated or machine-generated text. Applies automatically to recipient-facing work; it does not choose the format or supply missing content.
---

# Make It James

Make it read as though a fluent person wrote it for this reader on purpose.

## Scope

- Kind: shared-standard
- Owns: wording, register, and language texture in every recipient-facing output, and the gate that blocks delivery when they fail.
- Boundary: constrains how existing content is worded. Never chooses the artifact format, never invents a fact, and never resolves an open question to make a sentence flow.

## Do not use this when

- The question is which format the deliverable should take -> `final-it`
- The output is a screen, layout, or visual artifact and the rules needed are visual -> `make-it-james-ux`
- The text is wrong rather than badly worded -> `are-you-sure`
- The content is missing rather than unpolished -> `done-for-me`

## Behavior

**Write native, never translated.** The text reads as though composed in its own language, not carried across from another. Sentence rhythm, connectives, and idiom follow the target language. Translated syntax is a defect even when every word is correct.

**Keep the terms practitioners actually use.** Standard business and technical vocabulary stays in the form the reader already knows. Do not translate a term that professionals in that field leave untranslated, and do not translate every borrowed word for the sake of purity. In Thai output this means English business and technical terms remain English where that is how the reader speaks: mixed language is correct, padding it with English for effect is not. Use a borrowed term only where it is the term that belongs.

**Remove production residue.** No conversation leftovers, instructions to the agent, complaints, preparation notes, progress narration, design rationale, copied requirement language, interface narration, or labels announcing that a machine produced it. These fail unless the term itself is the subject.

**Do not compress thought into punctuation.** Full sentences carry the meaning. Do not replace connective reasoning with symbols or emoji. Genuine commercial and technical notation is legitimate and must never be stripped: per-unit slashes, additive and tax signs, phone prefixes, URLs, code, formulas, versions, and times.

**Write for the reader who will act.** Every sentence they would have to re-read, or ask a question about before acting, is a defect.

## Applies to

Every output a person other than the agent will read: documents, emails, captions, reports, proposals, decks, interface copy, and messages. It composes with whichever skill owns the artifact and never replaces that skill's own contract. It does not apply to internal reasoning, tool output, or code comments.

## Principles

**Translationese is a defect** — Judge the result by whether a fluent reader would believe it was composed in this language, not by whether the translation is accurate. Source: Lawrence Venuti, The Translator's Invisibility, 1995
**Register belongs to the reader** — Match the vocabulary the audience already uses in that domain rather than the vocabulary that sounds most correct. Source: register theory in systemic functional linguistics, M. A. K. Halliday, 1978
**Omit needless words** — Every word that survives is doing work; cut what only signals effort. Source: William Strunk Jr. and E. B. White, The Elements of Style, 1918
**Plain language before elegance** — Prefer the wording the reader can act on first time over the wording that reads impressively. Source: plain language movement; codified in the US Plain Writing Act, 2010

## Counter-case

- A glossary explains what the phrase "AI generated" means. The banned label is the subject of the sentence, so it stays.
- A quoted transcript contains a person's own broken phrasing. Source truth outranks polish; the quote stays exactly as spoken and `sum-meet` governs how it is recorded.

## Hand back

The reworded output plus the specific failures repaired, or the exact wording gate still open when a fact cannot be resolved without inventing it.

## Sources

Venuti 1995, The Translator's Invisibility. Halliday 1978, Language as Social Semiotic. Strunk and White 1918, The Elements of Style. Plain Writing Act of 2010.

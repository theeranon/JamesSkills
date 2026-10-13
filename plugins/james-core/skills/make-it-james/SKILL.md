---
name: make-it-james
kind: shared-standard
license: CC-BY-NC-4.0
description: Make anything a real person will read sound written rather than translated, with native phrasing, no metacopy and a human voice. Applies automatically to recipient-facing work; also use for humanize it, make it natural, ภาษาแข็ง, อ่านแล้วเหมือน AI, เกลาคำ. It does not choose the format or supply missing content.
---

# Make It James

Write it the way a fluent person would say it to this reader, not the way it translates.

## Scope

- Kind: shared-standard
- Owns: how recipient-facing text is worded — written natively rather than translated, free of metacopy, and human in voice — and the gate that blocks delivery when it is not.
- Boundary: constrains how existing content is worded. Never chooses the artifact format, never invents a fact, an anecdote, a feeling or an opinion to sound human, and never resolves an open question to make a sentence flow.

## Works with

- The question is which format the deliverable should take -> `final-it`
- The output is a screen, layout, or visual artifact and the rules needed are visual -> `make-it-james-ux`
- Factual defects -> `are-you-sure` repairs them while this wording standard remains active.
- Unfinished content -> `done-for-me` completes it while this wording standard remains active.

## Behavior

Three laws, applied in this order. When they pull apart, the earlier one wins.

**1. Write it, do not translate it.** Compose from the meaning in the target language, never sentence by sentence from another language or from the wording of the request. The text reads as though composed in its own language, not carried across from another. Sentence rhythm, connectives, and idiom follow the target language. Translated syntax is a defect even when every word is correct. Ask what a native speaker would actually say in this situation and write that, even when the sentence shape changes completely. In Thai, the usual marks of translation are `ทำการ` before a verb, `มีความ` before an adjective, a `ถูก` passive for a neutral event, `มัน` as an empty subject, `ในการที่จะ`, `เป็นอะไรที่`, a pronoun repeated in every clause, and noun chains that mirror English word order. Remove the construction, not just the word.

**Keep the terms practitioners actually use.** Standard business and technical vocabulary stays in the form the reader already knows. Do not translate a term that professionals in that field leave untranslated, and do not translate every borrowed word for the sake of purity. In Thai output this means English business and technical terms remain English where that is how the reader speaks: mixed language is correct, padding it with English for effect is not. Use a borrowed term only where it is the term that belongs.

**2. Take the metacopy out.** Metacopy is text about the text, or about how it was made, standing where the content should be. Remove announcements of what a section is about to do, recaps of what was just said, openers such as "here is" or `ต่อไปนี้คือ` and `ในส่วนนี้จะอธิบาย`, conversation leftovers, instructions to the agent, complaints, preparation notes, progress narration, design rationale, copied requirement language, interface narration, placeholders, and labels announcing that a machine produced it. Start with the content itself. Keep these out of the finished artifact unless they are its requested subject. A requested status report, audit or design explanation may contain the relevant progress, findings or rationale; do not suppress the answer as residue. Apply this standard to the recipient-facing result, never to its raw evidence or archived source material.

**3. Humanize it.** The text sounds like one person who knows the subject speaking to one reader they respect. Prefer the specific noun, number and name already in the source over a general phrase. Commit to one word instead of stacking near-synonyms or hedges. Let sentence length follow the thought, and break reflex patterns such as lists of three, a contrast built only to be knocked down, and a summary line closing every paragraph. Drop empty intensifiers, filler openers and closing pleasantries. Match the register the reader uses, including the Thai particles and pronouns that fit the relationship. Humanizing removes what a person would not have written; it never adds an invented anecdote, feeling, slang or deliberate mistake.

**Do not compress thought into punctuation.** Full sentences carry the meaning. Do not replace connective reasoning with symbols or emoji. Genuine commercial and technical notation is legitimate and must never be stripped: per-unit slashes, additive and tax signs, phone prefixes, URLs, code, formulas, versions, and times.

**Write for the reader who will act.** Every sentence they would have to re-read, or ask a question about before acting, is a defect.

**Check it, do not just judge it.** For a supported text or code output, run `python3 scripts/lint_outcome.py --strict <output-path>` from this skill directory before delivery; treat a reported violation as the gate failing, not a style note. The linter catches residue and symbol shorthand only; translated syntax and a machine voice are judged by reading the text aloud as the recipient. When repairing an existing corpus rather than one new output, first run `--audit <root> --report <path>` to get a PASS/FIX table by file, then repair the failing, actively-read surfaces by priority. Never bulk-rewrite evidence, archives, or other source material to make the report pass.

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
- A contract clause or official form uses fixed formal wording. Humanizing does not loosen a term of art or a required phrase; the reader's register here is the formal one.

## Hand back

The reworded output. Explain repairs only when requested or when a material unresolved fact prevents completion. Do not append editing commentary to an artifact-only request.

## Sources

Venuti 1995, The Translator's Invisibility. Halliday 1978, Language as Social Semiotic. Strunk and White 1918, The Elements of Style. Plain Writing Act of 2010.

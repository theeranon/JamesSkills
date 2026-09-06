---
name: research-it
kind: workflow
license: CC-BY-NC-4.0
description: Settle a doubt about one claim, approach, or requirement with outside evidence from official sources and real users. Use when confidence is missing, not when choosing between options or checking your own work.
---

# Research It

Resolve one outside claim with evidence the reader can audit.

## Scope

- Kind: workflow
- Owns: one open question whose answer lives outside this conversation, returned as evidence with a verdict the reader can audit.
- Boundary: reads external sources and the current project for context. Writes a findings record only. Never edits the thing under question and never acts on the verdict.

## Do not use this when

- Several candidates must be compared and one recommended -> `give-me-solutions`
- The doubt is about work produced in this conversation rather than an outside claim -> `are-you-sure`
- The doubt is about whether shipped code, data, or a deployment behaves correctly -> `dev-are-you-sure`
- A registered framework or book should interpret a case already in hand -> `baseon`
- The question is which layer of the system is actually failing -> `zoom-out`

## Procedure

1. Preserve the actual falsifiable claim and its scope: who or what, version, population, conditions and time period, where supplied. Distinguish an absolute claim from a frequency estimate. Do not silently narrow the claim to make it true.
2. Use the supplied evidence first. If outside research is needed and available, seek primary documentation and independent experience, including evidence against the claim. Report the sources actually read and searches actually performed. A supplied-source task does not require inventing a search or refusing an answer because a preferred source type is absent.
3. Keep source assertions, observed results, independent corroboration and your inference distinguishable. Record useful source identity, date, scope and stake only when known; mark material missing information unknown. Independence, lack of sponsorship, publication date and test coverage cannot be inferred from a document's label. A commercial stake does not erase observations; assess their methods and limits rather than discard them automatically.
4. Decide what the evidence establishes. A valid counterexample refutes an absolute claim within its original scope; successful cases or a later fix do not erase that result. Revising it requires resolving every decisive contrary item, not merely explaining away one. A changed version or narrower scope is a separate claim. An exhaustive check can support a bounded finite claim. Selected anecdotes cannot establish a population rate without a suitable denominator and sampling method.
5. Deliver the requested wording or answer first, with only the evidence and limits needed to support it. Before returning it, check each factual sentence against its source: do not move a date, test condition or observation from one source to another; turn missing information into unknown, not an assertion of absence. Preserve relative dates when no task reference date is supplied. Distinguish a listed or planned item from an observed delivery. Treat representativeness, independence and motives as unknown unless evidenced. For a causal or typical-population claim, an uncontrolled before/after observation does not establish an effect or a typical estimate. Remove unsupported details rather than soften them with likely or plausible. Use supported, contradicted, conditional or unsettled as appropriate. Do not append hypothetical reversal conditions unless the user asks; if asked, keep them valid for the original claim. A ledger is optional, and a one-sentence request gets one sentence.

## Stop when

The question is answered as far as the available evidence permits and another source is unlikely to change the decision. If an important source or tool is unavailable, state the specific limit and give the bounded answer already supported. Do not prolong research to fill fields or obtain a source that cannot affect the verdict.

## Principles

**Falsification** — Seek evidence that could refute the claim, and keep the claim's scope stable while evaluating it. Source: Karl Popper, The Logic of Scientific Discovery, 1934
**Sponsorship bias** — Commercial interests call for scrutiny of methods and corroboration, not automatic dismissal of observations or assumed neutrality of technical documentation. Source: Lundh and colleagues, Industry sponsorship and research outcome, Cochrane Methodology Review, 2017
**Base rate over vivid case** — An incident establishes occurrence, not frequency; distinguish a counterexample to an absolute from evidence about a rate. Source: Daniel Kahneman and Amos Tversky, work on representativeness and base-rate neglect, 1973
**Evidence decay** — Check freshness when changing conditions could affect applicability. An unknown date is a limitation where time matters, not a reason to invent a date or discard evidence about a fixed historical dataset. Source: Samuel Arbesman, The Half-Life of Facts, 2012

## Counter-case

- A verified failure refutes an all-cases claim; later successful trials do not restore it. If a recheck proves the failure record erroneous and an exhaustive check covers the bounded population, revising the verdict is justified.
- The user asks which of four database options fits their workload -> `give-me-solutions` owns the recommendation and may use this skill for evidence.
- The user asks whether the report just written contains an error -> `are-you-sure` owns inspection of that work.

## Hand back

The claim and verdict, the decisive source evidence with locators when available, and the material limits. Keep fact, source assertion and inference clear without requiring separate sections for empty categories. The reader decides what to do about it.

## Sources

Popper 1934, The Logic of Scientific Discovery. Kahneman and Tversky 1973, On the psychology of prediction. Arbesman 2012, The Half-Life of Facts. Lundh and colleagues 2017, Industry sponsorship and research outcome, Cochrane Database of Systematic Reviews.

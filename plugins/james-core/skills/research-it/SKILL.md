---
name: research-it
kind: workflow
license: CC-BY-NC-4.0
description: Settle a doubt about one claim, approach, or requirement with outside evidence from official sources and real users. Use when confidence is missing, not when choosing between options or checking your own work.
---

# Research It

Go find out whether the claim survives contact with people who already tried it.

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

1. Write the claim as one falsifiable sentence, then name what evidence would prove it wrong. A claim nothing could refute is reformulated before any search begins.
2. Establish the context that makes evidence transferable or not: scale, stack, budget, jurisdiction, team size, and time horizon of the current situation. Evidence from a different context is labelled, never silently applied.
3. Read the official position first: vendor documentation, standards bodies, primary research, the author of the method. Record what it claims and what it stays silent about.
4. Then seek the disconfirming side deliberately. Look for practitioners who ran it long enough to be disappointed: post-mortems, migration write-ups, long-running issue threads, dated reviews, community answers with the failure conditions attached.
5. Keep a ledger. Each item records source identity, date, whether the author had a commercial stake, the context it applied to, and what it actually demonstrates rather than what it asserts.
6. Separate four layers explicitly: verified fact, source claim, independent corroboration, and your own inference.
7. Return a verdict of supported, contradicted, conditional, or unsettled, plus the condition that would change it.

## Stop when

Both the official position and at least one independent practitioner account have been read, the disconfirming search has been attempted and its result stated even when it found nothing, and one more source is no longer changing the verdict or revealing a new failure condition. Name the unknown rather than filling it.

## Principles

**Falsification** — Search for what would refute the claim before collecting anything that supports it, and report the refuting search even when it comes back empty. Source: Karl Popper, The Logic of Scientific Discovery, 1934
**Sponsorship bias** — Treat any source with a commercial stake in the answer as an argument rather than as evidence, and require an independent account before accepting its claim. Source: extensively documented in research on industry-funded studies; see Lundh and colleagues, Cochrane Methodology Review, 2017
**Base rate over vivid case** — One dramatic failure story is a data point, not a rate; state how common the outcome is or say the rate is unknown. Source: Daniel Kahneman and Amos Tversky, work on representativeness and base-rate neglect, 1973
**Evidence decay** — Record the date of every claim and treat undated material as unusable, because the answer to a technology question expires. Source: Samuel Arbesman, The Half-Life of Facts, 2012

## Counter-case

- The user asks which of four database options fits their workload. This needs the same evidence discipline but ends in a recommendation, so `give-me-solutions` owns it and calls this skill for the evidence pass.
- The user asks whether the report just written contains an error. Nothing outside the conversation is in question, so `are-you-sure` owns it.

## Hand back

The claim as stated, the evidence ledger with dates and stakes, the four layers kept separate, the verdict with its condition, and the named remaining unknown. The reader decides what to do about it.

## Sources

Popper 1934, The Logic of Scientific Discovery. Kahneman and Tversky 1973, On the psychology of prediction. Arbesman 2012, The Half-Life of Facts. Lundh and colleagues 2017, Industry sponsorship and research outcome, Cochrane Database of Systematic Reviews.

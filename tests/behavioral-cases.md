# Behavioral Cases

These cases test decisions and observable invariants, not exact wording.

## Give Me Solutions

Request: Choose a primary communication platform for James's executive office.

Must:
- inspect independent user experience and failure evidence, not only vendor documentation
- compare surviving candidates with the same requirements
- identify strongest options and tradeoffs
- leave the final platform decision to James

Fails when:
- one product is declared the answer without comparison
- official marketing is treated as real-world reliability proof

## Done For Me

Request: Finish an application whose production credential is not available yet.

Must:
- complete all credential-independent implementation and verification
- expose the missing value through settings, environment input, or an explicit contract
- state the exact remaining credential gate only after other work is exhausted

Fails when:
- fake credentials or production success are invented
- the task stops immediately although independent work remains

## I Have ADHD

Request: Activate ADHD mode, then compare several architecture options in a later turn.

Must:
- retain the mode without requiring another invocation
- lead directly and use compact, human language
- preserve every option and fact needed for the decision

Fails when:
- the response is arbitrarily reduced to one option or one task
- necessary evidence disappears in the name of brevity

## Final It

Request: Finalize a README, then finalize an HTML dashboard.

Must:
- keep the README as Markdown when visual treatment adds no value
- apply the visual standard to the rendered dashboard
- remove conversation residue and production narration from both

Fails when:
- every output is forced into a designed visual artifact
- the dashboard ships without rendered visual inspection

## Make It James

Request: Create a Thai dashboard and a recipient-facing Markdown report.

Must:
- use IBM Plex Sans Thai, compact density, 6px rectangular radius, restrained color, and plain metadata on the dashboard
- remove conversation residue and punctuation-built Thai shorthand from both outputs
- run deterministic lint and inspect the rendered dashboard

Fails when:
- `Poppins`, a decorative left rail, a gradient, metadata chips, or an oversized radius is reintroduced without failing the gate
- a CSS font-family declaration is treated as proof that the rendered font loaded

## Sum Meet

Request: Summarize a transcript containing three agendas and a disputed owner into a printable meeting record.

Must:
- account for the whole transcript and keep all three agendas as separate zones in one A4 portrait HTML file
- preserve decisions, actions, owners, dates, open loops, exact quotes, contradictions, and source gaps
- keep the disputed owner unresolved rather than choosing one
- render and inspect every printed page

Fails when:
- the agendas become separate full-summary files
- a quote, owner, deadline, or decision is invented
- later pages are not inspected

## One Page Please

Request: Turn a source containing three independent agendas into one-page briefs.

Must:
- produce three separately named, self-contained one-page files
- preserve each agenda's decisions, actions, risks, and evidence or link material detail explicitly
- keep each file to one readable A4 landscape page and inspect all three

Fails when:
- multiple agendas share one page
- material content is silently dropped or hidden to force fit
- a single rendered page is used as proof for all outputs

## Critical Path Before Optional Completeness

Request: Adapt an existing proven skill, install it globally, and push it.

Must:
- implement the callable portable package first
- run the minimum structural and representative behavior proof needed for safe use
- install it and push the versioned result before broad history research, portfolio redesign, document migration, or optional QA expansion
- continue optional hardening only when it changes usability, safety, or the requested decision

Fails when:
- a usable package and push are delayed by unrelated audit, documentation, taxonomy, or exhaustive QA work

## Project Standard

Request: Establish one project contract that Claude, Codex, Gemini, and a new human can use without relying on chat history.

Must:
- derive project facts, commands, stack, and current state from the actual repository and evidence
- separate intended requirements from current implementation and preserve visible drift between them
- give each durable fact one owner across `PROJECT.md`, `STATUS.md`, `AGENTS.md`, and `docs/DECISIONS.md`
- create `ARCHITECTURE.md` and `DATA_MODEL.md` only when real project complexity requires them
- preserve existing files and project-specific knowledge during bootstrap or repair
- keep provider adapters thin and point them to the shared contract
- update only documents whose owned facts changed

Fails when:
- a mentioned tool, complaint, joke, or unaccepted option becomes a requirement
- a PHP/MySQL project is silently redesigned around Next.js, Supabase, or Vercel because those tools appear in stale planning notes
- current code is rewritten as the desired architecture or intended architecture is reported as already implemented
- routine code work creates documentation ceremony or rewrites every project file
- a template overwrites an existing file
- a schema change updates neither fact ownership nor rollback evidence in `DATA_MODEL.md`
- cross-platform support is claimed without verifying discovery and behavior
- missing credentials make independent specification, implementation, or validation stop immediately

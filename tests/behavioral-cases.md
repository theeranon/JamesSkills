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

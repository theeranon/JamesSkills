# Knowledge Library Contract

The workflow is portable. Knowledge is modular and versioned.

## Repository shape

```text
packs/knowledge/
├── registry.json
├── sources/
│   └── <source-id>.json
└── lenses/
    └── <lens-id>/
        ├── manifest.json
        ├── index.md
        └── references/
            ├── concepts.md
            ├── applications.md
            └── limitations.md
```

The complete JamesSkills repository is the distribution unit. The installer links the skill directory back to that clone, so the sibling knowledge library stays canonical. A detached copy of only this skill directory must set `JAMES_SKILLS_ROOT` to a complete clone; it must not carry a silent duplicate of the packs.

## One fact, one owner

- `registry.json`: discoverable source and lens IDs with relative paths.
- Source card: provenance, edition, rights posture, hash, evidence class, and source scope.
- Lens manifest: lens version, source dependencies, status, use cases, and exclusions.
- `concepts.md`: source-faithful paraphrased claims and locators.
- `applications.md`: original questions, decision moves, and reversible experiments.
- `limitations.md`: missing evidence, conflicts, unsafe uses, and expiry rules.
- Subject profile or project context: personal results, observed behavior, live state, and decisions. Never store these in the generic pack.

## Claim card

Every durable knowledge claim needs:

```text
## CLAIM-ID — Short label

- Evidence: [official claim] | [independent evidence] | [James rule] | [inference]
- Source: `source-id#locator-id`
- Confidence: source-faithful | supported | mixed | tentative

Original paraphrase in the repository author's language.
```

Do not merge an official claim and independent evidence into one unlabeled sentence.

## Source intake gates

1. **Provenance:** exact creator, edition or version, date, URL or ISBN, and acquisition context.
2. **Rights:** full source stays outside Git by default; record rights uncertainty instead of assuming permission.
3. **Extraction:** original paraphrase with stable claim and locator IDs.
4. **Challenge:** counterevidence, cultural or language limits, outdated examples, and high-stakes exclusions.
5. **Behavior:** at least one fit case, one misuse case, and one revision rule.

Register a new book as a source before deciding whether it supports an existing lens or deserves a new one.

## Promotion states

- `draft`: structure exists; claims or rights review incomplete.
- `reviewed-private`: safe for private reflection with explicit limits.
- `promoted`: validated, reusable, and supported by behavioral fixtures.
- `retired`: retained for traceability but not selected for new work.

An edition update creates a new source or a `supersedes` relationship. Never silently rewrite the old claim history.

Apply and Compare may select only `reviewed-private` or `promoted` sources and lenses. `draft` and `retired` remain visible for maintenance but are blocked from runtime use.

## Runtime result state

```yaml
framework_result:
  status: official_user_declared | working_hypothesis | unknown
  source: user_reported | imported_private_report | inferred | none
  version: string | unknown
  as_of: YYYY-MM-DD | unknown
  confidence: 0.0-1.0
  alternatives: []
  review_triggers: []
```

An `inferred` result may never be silently promoted to `official_user_declared`.

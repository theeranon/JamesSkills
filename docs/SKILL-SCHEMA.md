# SKILL.md Contract v1

Every canonical `SKILL.md` in this repository satisfies this contract. `scripts/validate`
enforces the machine-checkable parts through `tests/test_skill_schema.py`.

The contract exists to prevent four defects measured across the v1 portfolio:
unfalsifiable instructions, rules copied from a sibling skill, missing stop conditions,
and authority a skill's job does not require.

## Frontmatter

```yaml
---
name: <matches the directory name and the catalog entry>
kind: workflow | mode | shared-standard | output | knowledge-lens | internal-routing
description: <capability> <trigger occasion> <at least one exclusion>
---
```

`description` is the trigger surface. It is resident on every turn for every installed
skill whether or not the skill fires, so it carries three clauses and nothing else:
what the skill does, the occasion a person reaches for it, and at least one case it
refuses. Budget: 25 to 320 characters.

## Kinds

| kind | activation | authority |
|---|---|---|
| `workflow` | one invocation, one bounded job | as declared in `## Scope` |
| `mode` | persists across turns until deactivated | changes conversation behavior only |
| `shared-standard` | applies automatically to matching work | constrains another skill's output |
| `output` | owns one artifact type end to end | produces a new artifact |
| `knowledge-lens` | applies a registered source to a real case | reports only |
| `internal-routing` | fallback when no direct owner matches | routes only, never owns work |

## Body spine

Headings appear in this order. `##` headings not listed here are rejected.

### 1. `# Title` then the stance line

One bare sentence immediately after the H1, no heading of its own, at most 20 words,
imperative. It states the mental move, not the category. It never begins with
"This skill".

### 2. `## Scope` — universal

Three bullets, exactly these keys:

```
- Kind: <the frontmatter kind>
- Owns: <the one bounded job, phrased so no sibling can satisfy it>
- Boundary: <what this skill may read, write, or mutate>
```

`Boundary` is the authority declaration. A skill that only reports says so here, and
the rest of the file may not then instruct it to repair.

### 3. `## Do not use this when` — universal

At least two bullets. Every bullet names the sibling that owns the excluded case, in
backticks, and that name resolves to a real catalog entry or alias.

```
- <case> -> `<owning-skill>`
```

This is the anti-overfit lever. A skill nobody ever excludes toward has no distinct job.

### 4. Middle section — by kind

| kind | required headings, in order |
|---|---|
| `workflow`, `output`, `knowledge-lens`, `internal-routing` | `## Procedure` then `## Stop when` |
| `mode` | `## Behavior` then `## Stays active until` |
| `shared-standard` | `## Behavior` then `## Applies to` |

`## Procedure` is numbered. Each step is one bounded action with an observable result.
`## Stop when` states the condition that ends the work, in terms an outside reader can
check. "When the job is done" is rejected.

### 5. `## Principles` — universal

At least two, at most five. Each is one line:

```
**<Principle name>** — <one imperative sentence>. <Source: author, work, year>
```

The imperative sentence is the operative rule an agent obeys. It is written in original
words; source text is never reproduced. A principle that would fit most sibling skills
equally well is rejected as padding. When attribution is uncertain, the source field
says `uncertain attribution` and the rule stands on its own merit.

### 6. `## Counter-case` — universal

A realistic request that looks like a trigger for this skill and must not activate it.
At least one; at least two for `mode`, `shared-standard`, and `internal-routing`, because
those activate without being asked for.

Two kinds are valid. A **routing** counter-case names the sibling that owns the case
instead, in backticks. A **permission** counter-case is a legitimate request the rule
must still allow rather than suppress, which is how a standard is shown not to be
overfitted. At least one counter-case per skill must be the routing kind.

### 7. `## Hand back` — universal

What the skill returns and what the recipient can do with it.

### 8. `## Sources` — conditional

Required when `## Principles` cites any named work. Lists source identity and locator.
Copyrighted originals stay outside Git; this section records identity, not content.

## Length budget

Two meters, capped separately.

**Trigger surface.** All descriptions are resident every turn. 320 characters each,
about 1,700 tokens for the whole roster.

**Invocation surface.** Body length is paid when the skill loads. Modes and shared
standards stack with the primary workflow, so they are capped hardest:

| kind | body line cap |
|---|---|
| `mode` | 120 |
| `shared-standard` | 120 |
| `internal-routing` | 140 |
| `workflow`, `output`, `knowledge-lens` | 220 |

Lines are counted after the frontmatter fence, excluding blank lines.

## What the test cannot catch

The validator asserts structure, not judgment. It cannot tell whether a bounded job is
genuinely distinct, whether a principle is correctly attributed, whether a counter-case
is realistic, or whether a procedure works. Those are settled by
`tests/behavioral-cases.md`, which every canonical skill must appear in.

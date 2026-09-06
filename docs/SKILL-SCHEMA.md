# SKILL.md Contract v2

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
description: <capability> <trigger occasion> <optional meaningful exclusion>
---
```

`description` is the trigger surface. It is resident on every turn for every installed
skill whether or not the skill fires, so keep it focused on:
what the skill does and the occasion a person reaches for it. Add an exclusion only
when it prevents likely misrouting; modes do not exclude workflows they accompany. Budget: 25 to 320 characters.

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

Keep scope, kind-specific behavior and completion, counter-cases, and handback discoverable. Other headings are optional; fixed order is not a quality gate.

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

### 3. `## Do not use this when` — optional

Include real exclusions only. Named routing targets must resolve to a catalog entry or alias. Do not turn composition into exclusion.

```
- <case> -> `<owning-skill>`
```

An exclusion can prevent misuse, but an incoming routing link does not prove a distinct job. Modes persist while task workflows execute; standards constrain outputs without replacing their owner.

### 4. Middle section — by kind

| kind | required headings |
|---|---|
| `workflow`, `output`, `knowledge-lens`, `internal-routing` | `## Procedure` then `## Stop when` |
| `mode` | `## Behavior` then `## Stays active until` |
| `shared-standard` | `## Behavior` then `## Applies to` |

`## Procedure` is numbered. Each step is one bounded action with an observable result.
`## Stop when` states the condition that ends the work, in terms an outside reader can
check. "When the job is done" is rejected.

### 5. `## Principles` — optional

At most five when useful. Do not pad a skill to meet a minimum. Each is one line:

```
**<Principle name>** — <one imperative sentence>. <Source: author, work, year>
```

The imperative sentence is the operative rule an agent obeys. It is written in original
words; source text is never reproduced. A principle that would fit most sibling skills
equally well is rejected as padding. When attribution is uncertain, the source field
says `uncertain attribution` and the rule stands on its own merit.

### 6. `## Counter-case` — universal

A realistic request showing an exclusion, legitimate composition, or a case where the rule must yield to the user’s explicit task.
At least one; at least two for `mode`, `shared-standard`, and `internal-routing`, because
those can compose with other active instructions.

Two kinds are valid. A **routing** counter-case names the sibling that owns the case
instead, in backticks. A **permission** counter-case is a legitimate request the rule
must still allow rather than suppress, which is how a standard is shown not to be
overfitted. A counter-case may demonstrate legitimate composition or proportional work; no routing counter-case is required.

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
is realistic, or whether a procedure works. Written cases describe intended behavior; only executed evaluations supply behavioral evidence. Include multi-turn composition, actual artifacts, and legitimate cases requiring depth, not just response formatting.

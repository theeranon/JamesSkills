# Synthetic source for behavioral testing

This fixture is invented and contains no client information.

## Meeting context

Project Cedar review on 12 September 2026. Participants are the Operations Team and Product Team.

## Agenda 1: Inventory alert pilot

The 14-day pilot reviewed 63 low-stock alerts. Fifty-seven alerts were checked by store staff, and 49 led to replenishment before a stockout. Eight were false alerts caused by delayed stock synchronization.

Decision: extend the pilot to three synthetic branches for 30 days, limited to dry-goods SKUs. Do not expand to refrigerated products yet.

Actions:

- Operations Team confirms the SKU list by 15 September 2026.
- Product Team enables the three branches by 17 September 2026.
- Review on 17 October 2026. Pause expansion if false alerts exceed 10 percent or synchronization lag exceeds 15 minutes.

## Agenda 2: Supplier onboarding form

Four of six synthetic suppliers completed the new form without assistance. Two stopped at the bank-document section because accepted file types were not explained.

Decision: keep the form but rewrite the bank-document guidance and add a sample file. Do not add another onboarding tool.

Actions:

- Product Team rewrites the guidance by 16 September 2026.
- Operations Team asks the same six synthetic suppliers to retry by 19 September 2026.
- Accept the revision when at least five suppliers finish without assistance and no uploaded document is rejected for an unexplained file type.

## Expected behavioral assertions

- Exactly two one-page files are produced.
- The inventory file contains no supplier-form decision or action.
- The supplier file contains no inventory expansion decision or threshold.
- Each file repeats only the shared context needed to stand alone.
- All decisions, actions, owners, dates, risks, thresholds, and evidence figures remain accounted for.

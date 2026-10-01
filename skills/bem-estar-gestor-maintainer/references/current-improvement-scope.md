# Current Improvement Scope

Use this reference when work touches the student record, billing, portal, or physical assessment. Confirm behavior in code and database before marking an item complete.

## Student registration and profile

- Remove e-mail and objective from the new-student registration flow. Do not remove authentication e-mail for staff users or the objective field from workout records.
- Keep address as an optional student field with a clear label and practical example.
- Include address in the AI quick-fill contract, preview, validation, and final submission.
- Preserve existing student records that still contain e-mail or objective data unless a separate migration is explicitly requested.
- Extract birth date as `YYYY-MM-DD` only when explicit; never guess it from age alone.

## Home, finance, and sales layout

- Keep quick actions immediately after the period-balance summary and before monthly evolution so they are visible on initial load.
- Keep sales search and status filters in separate responsive rows; avoid horizontal competition between the search field and filter buttons.
- Require a student for every new sale. Do not present `optional student` or `standalone sale` choices.
- Open the existing accounts-receivable view first in Finance unless a distinct accounts-payable module is explicitly designed.
- Explain student-header totals with full labels: open total is the sum of unpaid monthly charges and product purchases.

## Plan history

- Give the current plan stronger hierarchy and place plan history below it as a chronological timeline.
- Do not style the current-plan and history containers as equal competing cards.

## Sales inside the student record

- Show the student's sales history in the student record.
- Provide a strategically placed `Registrar venda` action preselected for that student.
- Reuse the canonical sales validation, idempotency, payment, cancellation, and query-invalidation behavior. Do not create a second sales engine.
- Keep the surface compact: summary and primary action first; filters and details progressively disclosed.

## Plan add-ons

- Support an integer quantity of at least one for each add-on.
- Calculate each line as quantity × captured unit price and include the result in the monthly total.
- Display add-on name, quantity, unit price, subtotal, and effective period in the student record.
- Display active add-ons in the student portal.
- Verify that generated monthly charges snapshot the correct total and do not retroactively rewrite paid historical charges.

## Student access and persistent portal session

- Revoking an access code must invalidate only the revoked credential according to the documented session policy.
- Generating a replacement must make the new code usable immediately; test revoke → regenerate → log in.
- Keep the student portal session durable across reloads and normal app restarts. Explicit logout, revocation policy, or security expiry may end it.
- Avoid exposing raw access-code hashes or tokens to the client, logs, or UI.

## Plan price and due-date synchronization

- Determine whether active student links snapshot or inherit a plan price before changing behavior.
- If the business rule propagates a plan edit, update all eligible active links transactionally and show the affected-student count before confirmation.
- Never change paid or cancelled historical monthly charges. Treat open charges explicitly and document whether they are recalculated.
- A due-day change must have a visible effective-date rule. Prefer keeping an already-issued current charge unchanged and applying the new day to the next generated charge unless the product owner explicitly chooses immediate rescheduling.
- Surface the rule in confirmation copy so staff can predict whether a charge becomes overdue.

## Physical assessment

- Prefill subsequent assessments from the latest compatible assessment and stable student data. Reuse height when available and derive age from birth date at the assessment date; never freeze age as permanent data.
- Keep editable measurements explicit and do not silently reuse body measurements that staff should remeasure.
- Reorganize the side preview into readable sections with spacing, hierarchy, units, and responsive stacking.
- Replace opaque phrases such as `referência automática`, `peso de referência`, and `baixo/moderado dentro do ponto de corte` with plain-language explanations of what was compared, the applicable range, and what the result means.
- Show the formula or calculation basis where useful, distinguish calculated values from recommendations, and avoid presenting health guidance as a diagnosis.

## Destructive production data work

- Clearing expenses requires an exact Supabase project and tenant/account match before execution.
- Treat conflicting project references as a hard safety stop for deletion, while continuing non-destructive code work.
- Report what was deleted and whether it is recoverable after any approved production cleanup.

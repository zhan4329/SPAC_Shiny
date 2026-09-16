# Features Tab Deferred Work

## Purpose

Record Features-tab improvements that are outside both the
[near-future facet PR sequence](./features-facet-pr-plan.md) and the inherited
Purdue-team work covered by the [broader roadmap](./development-roadmap.md).

These items are intentionally not scheduled. Some are worthwhile polish for a
future contributor; others may become important after the planned Features
workflow is used more broadly.

## Deferred UI Work

- Explain why Log X is unavailable when the selected data contains negative
  values. Prefer disabling the control with an inline reason over silently
  accepting an option the core function cannot apply.
- Convert template validation errors into concise, user-facing feedback where
  this can be done without hiding actionable diagnostic information.
- Add contextual help for unfamiliar statistical and plotting parameters so
  non-coding users can make informed choices.

## Legacy Behavior

- Reassess and eventually remove the deprecated group-separate histogram path
  after facet mode has demonstrated that it covers the intended workflows.
- Review whether any compatibility-only UI branches or shared values can be
  removed after all histogram modes use the accepted template contract.

## Accessibility and Small-Screen Support

- Evaluate keyboard navigation, labels, focus order, contrast, and screen
  reader behavior after the planned UI restructuring is stable.
- Evaluate phone and narrow-screen behavior separately. Current verification
  covers representative desktop displays; mobile compatibility is not a
  requirement of the near-future facet sequence.

## State and Convenience Features

- Consider reset-to-template-default actions after the full parameter set is
  exposed.
- Consider preserving a user's last Features configuration within a session
  if repeated configuration becomes a demonstrated usability problem.
- Consider named presets only after stable defaults and real usage show that
  common configurations are worth maintaining.

## Deferred Verification

- Add focused automated adapter tests after the final facet and parameter
  contracts are stable.
- Add broader browser-level tests after the Features UI identifiers and
  conditional behavior stop changing.
- Expand cross-device visual regression coverage only if the project gains
  the maintenance capacity to keep image baselines current.

## Intake Rule

Add an item here only when it is specific to the Features tab and has no place
in the scheduled facet sequence or the cross-project roadmap. When an item is
accepted for development, move it into that development's task tracker rather
than maintaining duplicate action items in both places.

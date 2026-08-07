# SPAC Shiny Features Future Work

This file records work intentionally deferred from the template-adapter and facet PRs so those PRs remain small and reviewable.

## Deferred Histogram Controls

- Expose histogram bins controls.
- Expose statistic and element controls.
- Expose x-axis label rotation.
- Expose figure width, height, font, and DPI settings.

These controls can be grouped into a later histogram-controls PR after the adapter and facet PRs are merged.

## Deferred UI Work

- Simplify and reorganize the Features-tab UI.
- Remove duplicated dynamic UI targets and dead commented code inherited from the draft branch.
- Review the Together/facet/grouping controls for a consistent user experience across all histogram modes.
- Add broader UI tests after the template contract and facet path are stable.

## Deferred Template Adoption

Apply the Issue #73 `run_from_json()` pattern to other Shiny tabs as separate, focused efforts. PRs #75 and #80 are useful references, but they are outside the current Features-tab scope.

## Future Agent Integration

Use the template-adapter boundary as the basis for future chatbot and agent functionality. A future agent should be able to inspect or update a structured input/parameter state, while the Shiny adapter remains responsible for translating that state into template execution.

## Deferred Technical Review

- Revisit the full set of parameters exposed by the current SPAC histogram template.
- Add broader end-to-end validation for template execution and downloaded dataframes.
- Review dependency pinning and upgrade policy after the current SPAC version has been validated in Shiny.
- Revisit whether additional features from Mousumi's draft should be exposed, and split them into focused PRs if needed.

## Attribution and History

Future work should continue to reuse Mousumi's commits selectively where appropriate. Prefer cherry-picking original commits or preserving accurate author/co-author metadata instead of manually recreating her work without attribution.

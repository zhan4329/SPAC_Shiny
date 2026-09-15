# Implementation Notes

## Branch and PR Sequence

Create `chore/pin-spac-to-pr-433` from `dev` and merge it first.
Create `ref/features-server-template` from the updated `dev`. After the
adapter PR is merged, begin the combined structured-UI-and-facet PR from the
updated `dev`. The authoritative future order is recorded in the
[Features facet plan](../../../plans/features-facet-pr-plan.md) and
[development roadmap](../../../plans/development-roadmap.md).

The dependency baseline and existing template-caller compatibility work are
tracked in [the prerequisite PR folder](../../../chore/pin-spac-to-pr-433/).

## Reusing Mousumi's Work

Use Mousumi's template-refactor commit as the starting point:

```text
ffa8644 Refactoring the old code in the feature server using run_fron_json
```

When it applies cleanly, `git cherry-pick ffa8644` preserves `MSahaPurdue` as
the commit author. Clean up and update the result for the current SPAC version
and the [Issue #73 workflow](../../../../../issues/issue-73.md).

Do not manually recreate the entire draft branch or merge PR #81 wholesale. If selective cleanup is needed, use `git cherry-pick -n <commit>`, retain only the adapter-related changes, and preserve accurate author or co-author metadata in the resulting commit. Mention the reused commits in the PR description.

## Adapter Boundary

The implemented component boundaries, template payload, and execution
lifecycle are documented in [Architecture](./architecture.md).

Keep reuse and cleanup limited to adapter-related material. Do not bring facet
exposure, additional histogram controls, or unrelated UI changes into this
refactor.

Task 6 includes the focused Shiny presentation adapter required to preserve
the template's completed 300-DPI geometry. It may reuse the PNG conversion
boundary from PR #76, but caching, plot downloading, cancellation, process
management remain separate developments. Task 10 replaces the temporary
`render.plot` wrapper with direct `render.image(delete_file=True)` delivery
while leaving responsive browser sizing to Task 9.

Dependency installation and compatibility fixes belong to the prerequisite
`chore/pin-spac-to-pr-433` PR, not this adapter PR.

## Verification

Use direct Shiny app verification while the Features adapter and its parameter
mapping remain unstable. Comprehensive automated adapter verification belongs
to the specialized SWE stage; focused tests remain appropriate for stable
reusable utilities. Do not mark implementation tasks complete until their
changes are reviewed, verified to the agreed boundary, and committed.

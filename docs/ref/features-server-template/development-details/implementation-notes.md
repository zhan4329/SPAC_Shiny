# Implementation Notes

## Branch and PR Sequence

Create `chore/pin-spac-to-pr-433` from `dev` and merge it first.
Create `ref/features-server-template` from the updated `dev`. After the
adapter PR is merged, create `feat/features-facet` from the updated `dev`.

The dependency baseline and existing template-caller compatibility work are
tracked in [the prerequisite PR folder](../../../chore/pin-spac-to-pr-433/).

## Reusing Mousumi's Work

Use Mousumi's template-refactor commit as the starting point:

```text
ffa8644 Refactoring the old code in the feature server using run_fron_json
```

When it applies cleanly, `git cherry-pick ffa8644` preserves `MSahaPurdue` as the commit author. Clean up and update the result for the current SPAC version and Issue #73 workflow.

Do not manually recreate the entire draft branch or merge PR #81 wholesale. If selective cleanup is needed, use `git cherry-pick -n <commit>`, retain only the adapter-related changes, and preserve accurate author or co-author metadata in the resulting commit. Mention the reused commits in the PR description.

## Adapter Boundary

Use `shared["adata_main"]`, register it through the memory registry, build an explicit template parameter dictionary, call `run_from_json()`, retain the returned dataframe, and unregister the object in `finally`.

Keep reuse and cleanup limited to adapter-related material. Do not bring facet
exposure, additional histogram controls, or unrelated UI changes into this
refactor.

Dependency installation and compatibility fixes belong to the prerequisite
`chore/pin-spac-to-pr-433` PR, not this adapter PR.

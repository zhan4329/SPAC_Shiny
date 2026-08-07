# Implementation Notes

## Branch and PR Sequence

Create `feat/features-facet` from the `dev` branch after `ref/features-template-adapter` is merged.

## Reusing Mousumi's Work

Mousumi's facet work is included in:

```text
5c511e9 facet plot is exposed on the Features Tab
```

Use `git cherry-pick -n 5c511e9` rather than cherry-picking it wholesale because the commit also changes dependency files and `ripleyL_server.py`. Retain only the relevant Features UI and server changes, update them to the current SPAC template contract, and preserve accurate author or co-author metadata. Mention the reused commit in the PR description.

## Facet Boundary

Pass the facet input through the template adapter. Keep facet validation, plotting, titles, layout, and returned data in the SPAC template. Verify both facet-enabled and ordinary histogram paths, including the intended facet/Together interaction.


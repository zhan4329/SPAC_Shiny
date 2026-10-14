# Implementation Notes

## PR Boundaries

Use one development tracker for both repositories and a separate PR in each.
Each PR targets its repository's `dev`; neither must wait for the other to
merge. Adopt the merged package commit in a separate Shiny dependency PR.

## Export Policy

Preserve the underlying figure's layout, dimensions, font sizes, legend
placement, and DPI. Keep the entire original canvas, including its margins,
and expand the exported PNG only when padded content extends beyond it.
Retain all visible title and legend text. Crowded content remains a readability
concern for later sizing controls; the export fix must not silently crop it.
Keep responsive preview sizing and download behavior in their own work.

## Verification Policy

Reproduce the clipping, then implement and verify the correction within one
export task. Task details own the focused cases and acceptance criteria.
Mark implementation complete only after review, verification, and commit.

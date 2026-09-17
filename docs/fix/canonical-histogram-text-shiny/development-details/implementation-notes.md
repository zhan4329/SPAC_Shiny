# Implementation Notes

## PR Boundaries

Use one development tracker for both repositories and a separate PR in each.
Each PR targets its repository's `dev`; neither must wait for the other to
merge. Adopt the merged package commit in a separate Shiny dependency PR.

## Export Policy

Preserve the underlying figure's layout, dimensions, font sizes, legend
placement, and DPI. The exported PNG may grow beyond that canvas to retain
all visible title and legend text. Crowded content remains a readability
concern for later sizing controls; the export fix must not silently crop it.
Keep responsive preview sizing and download behavior in their own work.

## Verification Policy

Verify the export boundary with representative figures before changing the
Shiny serializer. Task details own cases and acceptance criteria. Mark
implementation complete only after review, verification, and commit.

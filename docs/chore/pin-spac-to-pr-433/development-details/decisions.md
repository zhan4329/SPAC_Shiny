# Decisions

### D1. Pin SPAC to the PR #433-compatible dev commit
Date: 2026-08-07

Decision:
Update both dependency files to the official SPAC dev commit
`f9886bcde643ebf14e58a31d5ac397e28b6ea510`, verify the installed
template contract, and complete required compatibility fixes before the
Features adapter work.

Details:
- Pin the exact commit rather than a floating `dev` branch.
- Use the current template execution argument `save_to_disk=False`.
- Verify existing template callers before downstream Features work.
- Keep facet UI exposure deferred to the separate Features facet PR.

Rationale:
The Features adapter must target the template version that provides the later
histogram and facet controls. Separating the dependency baseline makes API
compatibility regressions independently reviewable before the Features
refactor begins.

# SPAC Development Roadmap

## Final Goal

Resolve the Purdue 2025-26 team developments through focused, reviewable pull
requests and build an experimental but genuinely useful agentic assistant for
SPAC by the end of 2026.

The assistant should advance SPAC's purpose of helping spatial single-cell
researchers work without writing code. At minimum, it should:

- explain what SPAC is and answer grounded SPAC questions;
- explain an uploaded dataset from deterministic summaries rather than guesses;
- inspect and update validated Shiny input values;
- invoke the same template-backed execution path used by the UI;
- render an analysis and report its result or failure to the user.

It does not need to be production-ready or support every tab and model
provider by year end. It must be an end-to-end implementation rather than a
chat-only demonstration.

The [Features facet PR plan](./features-facet-pr-plan.md) records the Features
modernization sequence. [Features future work](./future-work.md) contains only
unscheduled, Features-specific improvements outside this roadmap.

## Constraints and Milestones

- Development capacity is a few hours per week alongside a pure mathematics
  thesis and teaching responsibilities.
- The contributor is a part-time volunteer and may be SPAC's most active
  developer, so operational and maintenance complexity must remain low.
- George values finished, explainable work and a useful team presentation more
  than rapid delivery.
- The likely interview window is mid-to-late October 2026, making an agentic
  vertical slice more time-sensitive than the remaining inherited features.
- By the interview, target a working local or draft-PR demonstration of all
  five minimum capabilities above for the Features tab.
- By the end of 2026, target a reviewed experimental integration, a completed
  Features facet workflow, and explicit dispositions for inherited PRs. It is
  not realistic to fully rebuild and merge every historical development in
  that time at the available weekly capacity.

## Strategic Choice

Three sequences were considered:

| Approach | Benefit | Cost |
| --- | --- | --- |
| Finish all UI and infrastructure before AI | Cleanest dependencies | Misses the interview objective and delays the main learning goal. |
| Start AI immediately on the old direct-call servers | Fastest first chat response | Creates a brittle second execution path and weakens the technical story. |
| Merge the template adapter, expose facet, then build one end-to-end agent slice | Gives the agent a structured execution path and the intended new capability | Requires keeping the UI and facet PRs tightly scoped before starting AI. |

The third approach is selected. Features template delegation (PR #86), the
independent UI structure refactor (PR #87), and a focused facet-exposure PR
provide the prerequisites for the agentic Features update/render workflow. The
remaining responsive layout, parameter exposure, downloads, caching,
cancellation, other tabs, Datashader, and Leiden should not block the first
agent implementation. Facet gives the demonstration a meaningful new plotting
capability; it need not block independent grounded-chat or summary work.

## Current Checkpoint and Review-Wait Priorities

As of 2026-09-15, PRs #86 and #87 are under review. Recommended next work:

1. Resolve the [facet tracker’s open decisions](../feat/features-facet/overview.md#issues-open).
2. Prepare [Agent PR A](#agent-pr-a-grounded-spac-chat), beginning with a tracker
   and audit of `origin/chatbot-restore`. If review delays continue, this is
   the first independent implementation candidate; summary design for Agent
   PR B can follow. Neither requires facet controls.
3. Once a prerequisite merges, follow the
   [integration sequence](../ref/features-server-template/development-details/implementation-notes.md#branch-and-pr-sequence)
   and resume facet development. Agent PR C needs stable facet inputs.

Keep one primary implementation active. Use canonical text-containment work
as an alternative if clipping blocks facet; otherwise protect the October
agent milestone from additional layout and parameter work.

## Target Architecture

```text
                         SPAC documentation
                                 |
                                 v
User <-> chatbot UI <-> agent orchestrator <-> grounded knowledge tool
                                 |
                                 +------> deterministic AnnData summary tool
                                 |
                                 +------> Features input registry
                                              |
                                              v
                                   validated semantic input state
                                              |
                          +-------------------+-------------------+
                          |                                       |
                          v                                       v
                    update Shiny UI                    template adapter/render
                                                                  |
                                                                  v
                                                      canonical plot and data
```

The agent must use narrow tools rather than arbitrary Python execution. UI
updates and rendering must pass through the same validation and template
contracts used by a human-operated tab. Only deterministic dataset summaries,
not the raw AnnData matrix, should be sent to an external model by default.

## Program Roadmap

### Step 1. Complete Template Delegation and Expose Facet

Goal: provide the structured execution boundary and intended facet capability
that the first agentic Features workflow will control.

Complete PRs 1-3 in the [Features facet PR plan](./features-facet-pr-plan.md):
template delegation, independent UI structure, and facet exposure. That plan
owns their scope and ordering. The completed facet input contract is required
for Agent PR C.

### Step 2. Build the Interview-Target Agentic Vertical Slice

Goal: demonstrate useful agent behavior in the real SPAC Shiny application by
mid-to-late October.

This step should normally be split into three focused PR developments.
Detailed tasks belong in each development tracker when it begins.

#### Agent PR A: Grounded SPAC Chat

- isolate useful concepts from the restored chatbot branch instead of adding
  a large implementation directly to `app.py`;
- add a modular chat UI and server boundary;
- answer questions from a curated SPAC knowledge source with source references;
- implement one model-provider path behind a small interface and accept
  credentials only within the user's session;
- label the feature experimental and handle provider or retrieval failures
  visibly.

#### Agent PR B: Uploaded-Data Explanation

- add a deterministic AnnData-summary tool that reports shape, available
  observations, variables, layers, embeddings, annotations, missingness, and
  bounded descriptive statistics;
- let the model explain that summary in user-oriented language;
- avoid transmitting raw cell-by-feature matrices or unnecessary identifiers;
- distinguish calculated facts from model interpretation.

#### Agent PR C: Features UI Update and Render

- complete former Features template-adapter Task 3 by introducing a small
  registry of agent-facing Features parameters and their Shiny update
  operations after the visible facet inputs stabilize;
- validate requested values against current choices and template constraints;
- show the proposed state change and require explicit user approval before an
  expensive render;
- update the visible UI, invoke the existing template-backed Features path,
  and return render status and results to the conversation;
- reject unknown parameters, invalid combinations, and stale dataset state.

Interview success is a coherent demonstration: ask what SPAC does, ask about
the uploaded dataset, request a supported Features configuration, approve the
change, and obtain a rendered histogram. Supporting one tab well is more
credible than pretending to control the entire application.

### Step 3. Complete the Remaining Features Improvements

Goal: finish the layout and remaining Histogram template controls after facet
and the interview-target agentic vertical slice are working.

Expected developments:

- fix title and legend containment in a focused SCSAWorkflow PR;
- make ordinary and facet previews proportional and responsive;
- expose analytical parameters, followed by presentation and export
  parameters in separate PRs;
- extend the agent registry as each additional input contract becomes stable.

The detailed order remains in the
[Features facet PR plan](./features-facet-pr-plan.md). If the AI work takes
longer than expected, PRs 4-6 wait; the adapter and exposed facet path are
sufficient for the first end-to-end agent slice.

### Step 4. Harden the Experimental Agent for the Year-End Milestone

Goal: turn the interview vertical slice into a maintainable experimental SPAC
feature suitable for George's team demonstration.

Expected developments:

- improve conversational error recovery and clearly report tool failures;
- record auditable tool requests, approvals, and outcomes without storing API
  secrets or sensitive dataset contents;
- add focused tests for knowledge retrieval, summary bounds, parameter
  validation, UI updates, and render authorization;
- document setup, supported capabilities, known limitations, and a repeatable
  demonstration workflow;
- evaluate one additional template-backed tab only if the Features path is
  stable and time remains.

Production requirements such as many providers, every tab, persistent chat
history, deployment-scale observability, or autonomous multi-step analysis are
not required for the 2026 milestone.

### Step 5. Build the Shared Result and Naming Foundation

Goal: give previews, downloads, caching, cancellation, and agents a common
understanding of a completed analysis result.

Expected developments:

- define stable semantic plot and tab identifiers;
- resolve the broad Features input and result naming deferred from the facet
  UI development;
- reconcile the naming-convention work from PR #82;
- define a session-level result containing normalized parameters, dataset
  identity/version, returned data, and canonical visual bytes;
- replace prototype-specific result access with this accepted contract.

This work should follow stable Features parameters. Otherwise filenames,
cache keys, and agent tools would depend on transitional UI identifiers.

### Step 6. Resolve Download, Caching, and Cancellation Work

Goal: recover the Purdue artifact and long-running-task work as separate,
composable capabilities.

Expected developments:

- rebase or rebuild HTML/table downloads from PR #83;
- extract PNG download behavior from the restored global-buttons development
  so downloads return the same bytes as the preview;
- benchmark execution before integrating the per-session LRU ideas from
  PR #76;
- add caching only with complete dataset-version and normalized-parameter keys;
- implement cancellation as a separate background-task lifecycle, beginning
  with one demonstrably slow workflow.

Downloads are correctness and usability features. Caching is an optimization.
Cancellation needs task identity, cleanup, and stale-result protection. They
should not be restored as one broad PR merely because they share buttons.

### Step 7. Extend Template Adoption Across SPAC Shiny

Goal: make the accepted Features pattern and agent-tool boundary reusable
across the application.

Expected developments:

- reassess Feature vs Annotation PR #75 and UMAP PR #80;
- define explicit application-level CSS loading ownership using the supported
  Shiny head mechanism before introducing shared cross-tab selectors;
- design a more polished reusable visualization style with George rather than
  treating the current Nearest Neighbor and Feature vs Annotation styling as
  the permanent baseline;
- migrate shared visualization styling one tab at a time through focused PRs;
- migrate one tab per focused PR to semantic inputs, template parameters,
  memory-registry execution, and canonical results;
- add agent tools only after each human UI and template path is accepted;
- absorb useful cleanup from PRs #68 and #74 into the scoped tab developments
  that need it.

### Step 8. Integrate Datashader and Expose a Density-Map Tab

Goal: add scalable density visualization to SCSAWorkflow and expose it through
a dedicated SPAC Shiny tab.

Expected developments:

- audit SCSAWorkflow PR #432 for dependency compatibility, duplicate paths,
  return contracts, scientific behavior, and unrelated changes;
- extract or rebuild a focused package implementation with preserved credit;
- add or update a template contract;
- add a separate Shiny density-map tab through the accepted adapter and result
  architecture;
- expose the new tab to the agent only after its human workflow is stable.

The package implementation, template, Shiny tab, and agent exposure should be
separate PRs.

### Step 9. Integrate Leiden-Only Clustering

Goal: provide a focused clustering workflow without duplicating or obscuring
existing Scanpy and PhenoGraph behavior.

Expected developments:

- audit SCSAWorkflow PR #431 and its overlap with existing clustering paths;
- decide preprocessing ownership, copy-versus-mutation behavior,
  reproducibility, stored AnnData fields, and return contracts;
- extract the Leiden module from unrelated changes while preserving Ramya's
  authorship;
- merge a focused, tested package API before optional Shiny and agent exposure.

This is independent scientific expansion and should not displace the 2026
agent milestone unless George identifies an immediate research need.

### Step 10. Expand Toward the Final Agentic SPAC Assistant

Goal: extend the accepted experimental agent from one reliable vertical slice
to a coherent application-wide assistant.

Expected developments:

- replace tab-specific prototype code with a stable registry of knowledge,
  dataset, input, execution, result, download, and task-status tools;
- add accepted template-backed tabs incrementally;
- support provider-neutral, session-scoped credentials;
- add user-approved multi-step analysis, result interpretation, downloads,
  cache awareness, and cancellation;
- define and enforce what dataset information may reach external providers;
- retain human-visible state, confirmation, reproducibility, and auditability.

This remains the final product direction. The Step 2 implementation is its
first real vertical slice, not a disposable toy.

## Continuous Purdue PR Resolution

Every inherited PR or restored branch should receive one explicit outcome:
merged, rebased, split into successor PRs, superseded with preserved credit,
or closed with a documented reason.

| Source work | Intended resolution path |
| --- | --- |
| PR #81, Features template/UI | Split across the Features facet sequence. |
| Restored chatbot work | Learn from it, then supersede it through Agent PRs A-C. |
| PR #75, Feature vs Annotation | Reassess as a focused tab migration. |
| PR #80, UMAP refactor | Reassess after the shared result contract. |
| PR #76, plot caching | Extract after measurement and stable cache keys. |
| Restored global-buttons work | Split into download and cancellation developments. |
| PR #82, naming conventions | Reconcile with semantic identifiers and filenames. |
| PR #83, HTML downloads | Rebase or rebuild independently. |
| PRs #68 and #74, broad refactor/cleanup | Absorb useful changes into scoped successors. |
| SCSAWorkflow PR #432, Datashader | Clean package PR, template, new Shiny tab, then agent tool. |
| SCSAWorkflow PR #431, Leiden | Clean scientific API, then optional Shiny and agent work. |

Resolution runs throughout the roadmap. Finishing the team's work means
understanding it, preserving attribution, and recording a defensible outcome;
it does not require merging each branch unchanged.

## Calendar Through December 2026

### September Foundation and Current Checkpoint

- PR #86 template delegation and PR #87 UI structure/static controls are
  implemented and under review as of September 15; integrate both;
- settle the facet interaction and expose facet with its coupled grouping
  behavior in its own follow-up PR;
- create the dedicated agent development tracker and architecture decision;
- inspect the restored chatbot branch for reusable code and assumptions.

### Mid-September Through Mid-October

- implement Agent PRs A-C sequentially, using prerequisite review waits for
  Agent PR A preparation or independent implementation;
- stabilize facet before Agent PR C, including its parameter registry;
- keep the remaining layout and parameter-exposure PRs paused unless the agent
  is waiting on an external review;
- prepare a repeatable interview demonstration and be able to explain the
  architecture, safety boundary, failures, and trade-offs.

### Late October and November

- complete any remaining facet-to-agent integration if the interview work
  slips; the intended registry integration belongs to Agent PR C above;
- fix canonical template text and responsive preview behavior;
- harden agent error handling and verification.

### December

- expose additional Histogram parameters as capacity allows;
- document and present the Features-plus-agent vertical slice to George's team;
- record dispositions and technical audits for remaining Purdue developments;
- select the first 2027 workstream: shared results/artifacts, another
  template-backed tab, or Datashader density-map integration.

## Working Rules for Limited Weekly Capacity

- Keep one primary implementation PR active at a time. Use review waits for a
  bounded audit, documentation change, or next-PR design.
- Prefer PRs demonstrable within two or three working sessions.
- Define detailed tasks only when opening a PR development; keep this file at
  program and PR-development level.
- Build one provider and one tab end to end before generalizing abstractions.
- Do not send raw uploaded data to a model merely because it is technically
  accessible; construct bounded, deterministic summaries.
- Require confirmation before agent-triggered computation or consequential UI
  changes during the experimental stage.
- Separate dependency upgrades from feature PRs unless required to run them.
- Measure latency before accepting caching or process-management complexity.
- Preserve original contributors' authorship through clean cherry-picks or
  accurate co-author attribution.

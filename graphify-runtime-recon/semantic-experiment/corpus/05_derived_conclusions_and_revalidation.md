# Derived Release Decisions — Dependencies and Revalidation State

## Author: Release Authority
## Date: 2025-02-05
## Reads: all prior files in this corpus

### Conclusion CONCLUSION-A (Release Decision)
Component X is cleared for production release at INLAND sites only.
Coastal release is WITHHELD pending C2 revalidation.

Dependency chain, explicitly declared:
1. CONCLUSION-A DEPENDS-ON C1 for "meets 5-yr durability bar".
   C1 in turn DEPENDS-ON {ALPHA-001, BETA-117}.
   Status of this leg: C1 ACCEPTED (see below).
2. CONCLUSION-A DEPENDS-ON the claim "coastal corrosion risk is
   handled" — implemented through C2.
   C2 in turn DEPENDS-ON ALPHA-002.
   Status of this leg: C2 REQUIRES-REVALIDATION (see below).

### State of Upstream Claims at time of this Conclusion (2025-02-05)

| Claim/Evidence | Present State | Why? |
|---|---|---|
| ALPHA-001 | SUPPORTED | Valid interval not yet expired; no superseding evidence. |
| BETA-117 | SUPPORTED | Valid interval not yet expired; no superseding evidence. |
| ALPHA-002 | SUPERSEDED by ALPHA-002-REV for coastal sites; still SUPPORTED for inland sites. | Alpha Lab retest 2025-01-18. |
| ALPHA-002-REV | SUPPORTED for coastal sites. | Newer lab result. |
| C1 | SUPPORTED | Depends only on ALPHA-001 + BETA-117; both SUPPORTED. |
| C2 | REQUIRES-REVALIDATION | Depended on ALPHA-002, now superseded for coastal contexts; handbook conversion not yet re-run against ALPHA-002-REV. |
| GAMMA-9 | QUARANTINED from triggering C2 INVALIDATED unilaterally. | Conflict unresolved; C2's final state awaits analyst re-run per Alpha Lab revalidation request. |

### Knowledge-state transitions recorded in this document (historical)
- 2024-05-10 (analyst report): C1 = SUPPORTED, C2 = SUPPORTED
- 2024-07-22 (gamma study pub): C2 = REQUIRES-REVALIDATION (triggered by GAMMA-9)
- 2025-01-18 (alpha retest pub): C2 = STILL REQUIRES-REVALIDATION (now explicitly requested by Alpha Lab; ALPHA-002 marked SUPERSEDED for coastal)
- 2025-02-05 (this doc): C2 = REQUIRES-REVALIDATION (CONCLUSION-A only clears inland; coastal decision QUARANTINED pending analyst response)

### Purpose — what this corpus probes for
If Graphify performs semantic extraction, it should recover:
(a) the explicit DEPENDS-ON edges between conclusions, claims, and evidence;
(b) the temporal ordering of states and the transitions (SUPPORTED →
    REQUIRES-REVALIDATION) with their trigger evidence;
(c) the evidence ↔ claim linkage with named sources and dates;
(d) the distinction between "change of evidence" (ALPHA-002 superseded) and
    "downstream consequences" (C2 now REQUIRES-REVALIDATION);
(e) the QUARANTINE concept as a state different from INVALIDATED.

# RESILIENT INTELLIGENCE — Capability Gap & Research Frontier Analysis

---

## 1. Executive Summary

This analysis compares Graphify v8's proven capabilities against the requirements for a "Resilient Intelligence" system — a human-centered, evidence-aware intelligence infrastructure for understanding evolving situations under uncertainty.

**Central finding:** Graphify is an excellent *structural knowledge* system. It answers "What exists and how is it connected?" The gap to Resilient Intelligence is fundamentally about **temporal, evidential knowledge** — answering "What do we believe, based on what evidence, as of when, with what confidence, and how has that changed?"

This is not a feature gap. It is a **representational gap**. Graphify's core data model — `(entity, relationship, entity)` — lacks the primitives needed for evolving knowledge: time, evidence, confidence-as-distribution, state, provenance, and contradiction.

**The existing technology landscape partially addresses this.** Systems like Graphiti/Zep (temporal knowledge graphs for agents), Microsoft GraphRAG (hierarchical community-based retrieval), and academic TKG research provide pieces. But no existing open-source system combines:

1. Temporal, evidence-grounded knowledge graphs
2. Explicit change detection and situation tracking
3. Human-centered explanation and decision support
4. Local-first, zero-cost operation
5. MCP-based agent integration

**Recommended direction:** A *Temporal Evidence Graph* engine — the smallest system that makes time, evidence, and change first-class primitives, and presents evolving situations to humans with explicit uncertainty and provenance. Built on SQLite (local-first), with a thin web frontend for situation exploration and MCP for agent integration.

**Feasibility verdict:** Achievable by one undergraduate in 5-6 months, with careful scope control.

---

## 2. RESILIENT INTELLIGENCE Philosophy

The philosophy rests on a single question:

> *Can computational systems help humans understand complex, evolving situations better than they could alone?*

This is distinct from automation ("do things for humans") and from information retrieval ("find things for humans"). It is about **augmented understanding** — making the human's mental model of a situation more accurate, more complete, and more honest about what it does not know.

The three conceptual lenses impose constraints:

| Lens | Core Constraint | What It Rejects |
|------|----------------|-----------------|
| **Iron Man** | Must make a human *measurably more capable* | Features that are technically interesting but don't improve human understanding |
| **Amaran** | Must handle *evolving, uncertain, high-stakes situations* | Static knowledge repositories; systems that assume truth is fixed |
| **Future Generations** | Must *preserve reasoning* over time | Ephemeral systems; black-box conclusions; architectures that die with their assumptions |

---

## 3. Iron Man Lens — Human Augmentation

A human dealing with a complex situation needs help with:

1. **Orientation** — "What are the key entities and how are they connected?" ← *Graphify does this well*
2. **Currency** — "Is this still true?" ← *Graphify does not track this*
3. **Provenance** — "Where did this come from?" ← *Graphify has partial support*
4. **Conflict resolution** — "Two sources disagree — which should I trust?" ← *Graphify does not address this*
5. **Change awareness** — "What changed since I last looked?" ← *Graphify's watch system detects file changes, not knowledge changes*
6. **Explanation** — "Why does the system believe this?" ← *Graphify's confidence labels are coarse (EXTRACTED/INFERRED/AMBIGUOUS)*
7. **Projection** — "What might happen next?" ← *Graphify does not address this*

The Iron Man test eliminates capabilities that don't improve the human's ability to do items 1-7. For instance, "distributed real-time streaming" is technically interesting but does not directly help a human understand a situation better.

---

## 4. Amaran Lens — High-Stakes Evolving Reality

The Amaran lens tests the system against scenarios where:
- Information arrives continuously and may contradict itself
- The consequences of misunderstanding are severe
- Multiple sources provide partial, overlapping views
- The "truth" changes over time (not just our knowledge of it)
- Humans must make decisions with incomplete information

### Scenario Walkthroughs

**Cybersecurity Incident Response:**
```
INITIAL: "Server X is compromised" (Alert from SIEM, 14:03)
NEW EVIDENCE: "User Y logged in from unusual IP" (Log analysis, 14:15)
CHANGE: "Server X was patched 3 hours ago" (Ops team, 14:22)
CONFLICT: "Server X shows no indicators of compromise" (EDR tool, 14:30)
UPDATED SITUATION: Alert may be false positive; patched server + clean EDR
  contradicts initial alert; user Y's login is independent
EXPLANATION: "We initially believed X was compromised based on [alert].
  Subsequent evidence [EDR scan, patch log] suggests otherwise."
DECISION SUPPORT: "Confidence in compromise: LOW (was HIGH).
  Recommended: investigate User Y's login independently."
```

**Supply Chain Disruption:**
```
INITIAL: "Supplier A ships component B normally" (procurement database)
NEW EVIDENCE: "Port closure reported in region R" (news feed, Day 1)
CHANGE: "Supplier A's factory is in region R" (entity resolution)
CONFLICT: "Supplier A confirms shipment on schedule" (email, Day 2)
  vs "Port closure extended 2 weeks" (government notice, Day 3)
UPDATED SITUATION: Supplier A's confirmation may be stale; port closure
  makes on-time delivery unlikely
EXPLANATION: Evidence timeline shows supplier confirmation preceded
  port extension notice
DECISION SUPPORT: "Risk of delay: HIGH. Alternative suppliers: C, D."
```

In both scenarios, the system must track **when each piece of evidence arrived**, **what it changed about the situation model**, and **which pieces of evidence conflict**.

Graphify cannot do any of this. Not because it's poorly designed, but because its data model is not designed for evolving knowledge.

---

## 5. Future Generations Lens — Durable Intelligence

| Question | Graphify's Answer | Required Answer |
|----------|------------------|-----------------|
| What happens when a source disappears? | Graph retains extracted data, but no provenance chain | System must retain provenance: "this fact came from source X at time T" |
| What happens when an entity changes? | Overwritten silently (last-writer-wins) | System must create a new version, preserving history |
| What happens when information becomes obsolete? | No mechanism for expiry | System must track validity intervals |
| What happens when two sources disagree? | Dedup merges them; no conflict tracking | System must explicitly model contradictions |
| Can historical reasoning be reproduced? | No — graph represents current state only | System must support "as-of" queries |
| Can we determine why the system believed something? | Partial — confidence labels + source_file | System must maintain full provenance chains |
| Can knowledge evolve without destroying history? | No — graph is overwritten each rebuild | System must use append-only or versioned storage |

---

## 6. Graphify v8 Capability Baseline

From the reverse engineering, Graphify provides:

### Strong Capabilities
- **Structural extraction** — 31 language AST extractors producing deterministic entity/relationship data
- **Entity deduplication** — MinHash/LSH + Jaro-Winkler pipeline with entropy gating
- **ID normalization** — Fixpoint loop ensuring cross-platform identity stability
- **Community detection** — Leiden/Louvain with oversized-community splitting
- **Query system** — Trigram-prefiltered, IDF-weighted, multi-tier scoring with per-term seed guarantees
- **MCP server** — Stdio + HTTP transports with security hardening
- **Caching** — Content-hash-based, version-aware extraction caching
- **Incremental rebuild** — File-change detection with pending queue and lock coordination
- **Reflection/work memory** — Time-decayed, corroboration-requiring experiential learning
- **Security** — SSRF prevention, label sanitization, DNS rebinding protection

### Key Architectural Patterns Worth Preserving
1. **Stateless pipeline** (detect → extract → build → cluster → analyze → report → export)
2. **Content-addressed caching** (invalidation by hash, not by path)
3. **Fixpoint normalization** (IDs stable across platforms)
4. **Trigram-then-score retrieval** (cheap candidate generation → expensive ranking)
5. **Sidecar files** (learning/labels kept separate from structural truth)
6. **LLM abstraction** (multi-backend, cost-tracked, sandboxed input)

---

## 7. Graphify vs Real-World Intelligence Gap

The fundamental gap is representational. Here is the core comparison:

### Graphify's Implicit Model
```
(Entity) --[relationship]--> (Entity)
    |                           |
    label                       label
    source_file                 source_file
    confidence                  confidence
    community                   community
```

### Minimum Required Model for Evolving Intelligence
```
(Entity) --[relationship]--> (Entity)
    |            |                |
    versions     evidence         versions
    |            |                |
    time         source           time
    state        confidence       state
    |            freshness        |
    history      contradictions   history
```

The gap decomposes into three missing primitive layers:

1. **Temporal layer** — when things were true, when we learned them, how they changed
2. **Evidential layer** — where knowledge came from, how strong the evidence is, what conflicts exist
3. **Change layer** — what changed, when, why, and what it means for the situation

---

## 8. Capability-by-Capability Analysis

### Legend
- **A** — Graphify provides it well
- **B** — Graphify provides a partial analogue
- **C** — Graphify does not fundamentally address it
- **D** — Graphify's architecture could support it (with modifications)
- **E** — Requires a fundamentally different abstraction

---

### 1. Entity Representation — **B**

**Graphify now:** Entities are graph nodes with `{id, label, source_file, source_location, file_type, community}`. Designed for software symbols (functions, classes, modules).

**Why sufficient for software:** A function's identity is determined by its file path + name. It doesn't "change state" — it is what the code says it is.

**Why insufficient for real-world:** Real-world entities have *states that evolve*. A "Server" entity might be "operational" at T1 and "compromised" at T2. A "Supplier" might be "reliable" in January and "at risk" in March. Graphify's flat attribute bag cannot represent this evolution.

**Missing primitive:** Entity versioning — an entity's attributes should be temporal: `(attribute, value, valid_from, valid_to, evidence)`.

**Architectural evolution:** Possible. Node attributes could carry validity intervals. But it requires changing the storage format from NetworkX node-link JSON to something that supports attribute-level versioning.

**Challenge:** Medium. Schema change + migration + query adaptation.

---

### 2. Relationship Representation — **B**

**Graphify now:** Edges with `{relation, confidence, context, source_file, weight}`. Typed relationships (calls, imports, contains, references, extends).

**Why sufficient:** In code, "A calls B" is either true or not (for AST-extracted edges). The relationship types are exhaustive for software structure.

**Why insufficient:** Real-world relationships can be *uncertain*, *temporary*, *evidential*, and *conflicting*. "A supplies B" might have confidence 0.8 based on a contract document, but a news report suggests A is bankrupt — a contradicting edge.

**Missing primitive:** Edges need `(valid_from, valid_to, evidence_sources[], confidence_distribution)`.

**Architectural evolution:** Possible. Edge attributes could carry temporal/evidential metadata.

---

### 3. Identity Resolution — **A → B**

**Graphify now:** `ids.py` fixpoint normalization + `dedup.py` MinHash/LSH pipeline. Excellent for software identifiers.

**Why partially insufficient:** Real-world entity resolution is harder. "IBM" = "International Business Machines" = "Big Blue". People change names. Organizations merge. The dedup pipeline's Jaro-Winkler scoring assumes entities are *permanent* — once merged, they stay merged. Real-world entities can *split*.

**Missing primitive:** Temporal entity resolution — the ability to say "A and B referred to the same entity until time T, after which they diverged."

**Architectural evolution:** Possible but non-trivial. The union-find merge in dedup.py is irreversible.

**Challenge:** High. Temporal entity resolution is an active research area.

---

### 4. Provenance — **B**

**Graphify now:** `source_file` and `source_location` on every node/edge. `confidence` distinguishes EXTRACTED vs INFERRED. The reflection system tracks per-node provenance `(date, question, outcome)`.

**Why sufficient:** In software, provenance = "which source file, which line." The code IS the ground truth.

**Why insufficient:** In real-world intelligence, provenance must be a *chain*: "this fact came from source S, which we obtained via method M, at time T, and it was corroborated by source S2 but contradicted by S3." Graphify's flat `source_file` string cannot express this.

**Missing primitive:** Provenance as a graph structure — facts linked to their sources, with source credibility metadata.

**Architectural evolution:** D — Graphify's architecture could support it by adding a provenance subgraph.

---

### 5. Evidence — **C**

**Graphify now:** No explicit evidence concept. The closest analogue is `confidence` (EXTRACTED/INFERRED/AMBIGUOUS), which is a production-method label, not an evidence assessment.

**Why sufficient for software:** The AST *is* the evidence. If tree-sitter says "A calls B," that IS the proof.

**Why insufficient:** Real-world facts rest on *evidence of varying strength*. An eyewitness report, a sensor reading, a news article, a social media post, an official document — each has different reliability, freshness, and bias characteristics.

**Missing primitive:** Evidence objects — first-class entities that support facts, with metadata: source, type (observation, inference, hearsay, measurement), strength, freshness, potential biases.

**Architectural evolution:** E — Requires a fundamentally new layer. Graphify has no concept of evidence as a standalone object.

---

### 6. Confidence — **B**

**Graphify now:** Three discrete levels: EXTRACTED (certain), INFERRED (LLM-suggested), AMBIGUOUS (multiple resolution targets).

**Why sufficient:** For software, this is appropriate. A call relationship is either provably present in the AST or inferred.

**Why insufficient:** Real-world confidence is a *distribution*, not a label. "80% confident based on 3 sources" is meaningful. "INFERRED" is not.

**Missing primitive:** Numerical confidence with evidential grounding — confidence should be *derived from* the number, recency, and reliability of supporting evidence, not manually assigned.

**Architectural evolution:** D — The existing confidence field could be extended to numeric values with derivation rules.

---

### 7. Uncertainty — **C**

**Graphify now:** No explicit uncertainty model. The only acknowledgment is the AMBIGUOUS confidence label for cross-file resolution.

**Missing primitive:** Explicit representation of "we don't know" — distinguishing between "this is false" and "we have no evidence."

**Challenge:** Low-medium. Representable as a flag or absence marker.

---

### 8. Contradictions — **C**

**Graphify now:** Dedup *merges* conflicting entity representations. The reflection system's "contested" category (positive + negative signals) is the closest analogue, but it operates on Q&A outcomes, not on knowledge-level contradictions.

**Missing primitive:** Contradiction tracking — when two pieces of evidence support incompatible facts, both should be preserved with explicit conflict markers.

**Architectural evolution:** D — Could be added as a relationship type ("contradicts") with metadata.

---

### 9. Temporal Information — **C**

**Graphify now:** No temporal model. The watch system detects file *modification times*, but the graph itself carries no time dimension. The reflection system uses `date` fields on memory docs, but these are Q&A timestamps, not knowledge-validity timestamps.

**Missing primitive:** Bi-temporal representation: *valid time* (when the fact was true in the world) and *transaction time* (when we recorded it in the system).

**Architectural evolution:** E — Requires fundamental data model change. NetworkX node-link JSON has no temporal axis.

**Challenge:** Medium. Well-understood in database theory (bitemporal modeling). Hard to retrofit.

---

### 10. Event Representation — **C**

**Graphify now:** No event concept. Everything is a node (entity) or edge (relationship). The system models *structure*, not *happenings*.

**Missing primitive:** Events as first-class objects — things that *happen* at a time, involving entities, changing state, and producing evidence.

**Architectural evolution:** E — Requires a new entity type with temporal semantics.

---

### 11. State Changes — **C**

**Graphify now:** No state concept. An entity's attributes are overwritten (last-writer-wins) during each rebuild.

**Missing primitive:** State machines for entities — the ability to say "this entity transitioned from state S1 to S2 at time T, evidenced by E."

**Architectural evolution:** E — Requires versioned entity attributes.

---

### 12. Causality — **C**

**Graphify now:** `calls` edges imply a form of causal flow in code. But this is structural causality (A invokes B), not evidential causality (A *caused* B).

**Missing primitive:** Causal edges with temporal ordering — "Event A preceded and plausibly caused Event B."

**Challenge:** Very high. Causal inference from observational data is an unsolved research problem. For feasibility, the system should support *human-annotated* causal claims, not inferred ones.

---

### 13. Context — **B**

**Graphify now:** Communities serve as implicit context (code modules that belong together). The `community_name` label provides domain-level context.

**Why partially sufficient:** For software, a community IS the context — it's the module boundary.

**Why insufficient:** Real-world context is richer. "This fact is relevant in the context of a hurricane" or "in the context of Q3 earnings." Context determines which knowledge is relevant for a given query.

**Missing primitive:** Situation context — a named, temporal scope that governs which knowledge is active and relevant.

---

### 14. Situation Awareness — **C**

**Graphify now:** No situation concept. The system produces a static snapshot (GRAPH_REPORT.md).

**Missing primitive:** A "Situation" as a first-class object — a named, evolving collection of entities, events, evidence, and relationships that represents the current understanding of a complex scenario.

**Architectural evolution:** E — This is the core novel abstraction.

---

### 15. Hypothesis Formation — **C**

**Missing primitive:** The ability to say "we hypothesize that X is true, based on evidence Y and Z, with confidence C." Hypotheses would be tentative facts, explicitly marked, that can be promoted to believed-facts or rejected.

**Challenge:** Medium. Representable as a node/edge type with a "hypothesis" flag.

---

### 16. Evidence-Based Reasoning — **C**

**Missing primitive:** The ability to *derive* a conclusion from evidence, track the derivation, and invalidate the conclusion if the evidence changes.

**Challenge:** High in general (automated reasoning). Feasible if limited to *explicit human-annotated reasoning chains* rather than automated inference.

---

### 17. Change Detection — **B**

**Graphify now:** `watch.py` detects file modifications and triggers incremental rebuilds. `.pending_changes` queue handles concurrent writes.

**Why partially sufficient:** Excellent at detecting *input* changes.

**Why insufficient:** Does not distinguish *knowledge-level* changes from *syntactic* changes. A code reformatting changes the file but not the knowledge. A one-line bug fix might change a critical relationship.

**Missing primitive:** Knowledge-level change detection — comparing graph states to identify which entities, relationships, or situations changed.

**Architectural evolution:** D — Could be built on top of graph diffing.

---

### 18. Knowledge Freshness — **B → C**

**Graphify now:** The reflection system's time-decay scoring (half-life = 30 days) is the closest analogue.

**Why insufficient:** Freshness is per-fact, not per-node. A fact's freshness depends on when the *evidence* was last confirmed, not on when the Q&A interaction occurred.

**Missing primitive:** Per-fact freshness tracking with evidence-based decay.

---

### 19. Knowledge Decay — **B**

**Graphify now:** `reflect.py` implements exponential decay with configurable half-life. This is a genuine, well-designed analogue.

**What's missing:** Decay should apply to *all knowledge*, not just Q&A memory. And different fact types should have different decay rates.

**Architectural evolution:** D — Extend the existing decay function to the fact level.

---

### 20. Historical State Reconstruction — **C**

**Graphify now:** No mechanism. Each build overwrites the graph. Backup system preserves timestamped snapshots, but these are full copies, not efficient diffs.

**Missing primitive:** Temporal queries — "Show me the situation as understood at time T."

**Architectural evolution:** E — Requires append-only or event-sourced storage.

---

### 21. Continuous Ingestion — **B**

**Graphify now:** `watch.py` provides continuous filesystem monitoring. `ingest.py` fetches URLs.

**Why partially sufficient:** The mechanisms exist but are file-oriented.

**What's missing:** Ingestion from heterogeneous sources (RSS, APIs, structured data, unstructured text) with source metadata.

---

### 22. Incremental Updates — **A**

**Graphify now:** `.pending_changes` + lock coordination + merge-with-existing-graph is well-designed.

**Reusable:** Yes. The pattern (not the file-specific code) transfers directly.

---

### 23. Human Feedback — **B**

**Graphify now:** `reflect.py`'s `save-result` mechanism captures human feedback (useful/dead_end/corrected).

**Why partially sufficient:** The three-outcome model is limited. Real-world feedback might include "partially correct," "correct but outdated," "correct in context X but not Y."

---

### 24. Human-in-the-Loop Reasoning — **C**

**Missing entirely.** Graphify's human interaction is post-hoc (after query results). True human-in-the-loop would allow a human to annotate, correct, hypothesize, and guide the system's understanding interactively.

---

### 25. Explainability — **B**

**Graphify now:** GRAPH_REPORT.md explains structural findings. `_surprise_score()` provides reasons for cross-community connections.

**Why insufficient:** Structural explanation ("these two modules are connected because A imports B") is different from evidential explanation ("we believe this because source X said so at time T, corroborated by Y").

---

### 26. Traceability — **B**

Similar to provenance (#4). Graphify tracks source_file/source_location but not full evidence chains.

---

### 27. Decision Support — **C**

**Graphify now:** Provides information (graph structure) but never suggests decisions or assesses risk.

**What's needed:** The system should be able to say "given the current situation, the highest-confidence action is X, but consider risk Y."

**Challenge:** Very high for automated decision support. Feasible if limited to *situation summarization* that a human uses to make decisions.

---

### 28. Risk Awareness — **C**

**Missing.** No concept of risk. Could be approximated as "low-confidence facts in critical relationships" or "recently changed facts in high-impact entities."

---

### 29. Prediction/Forecasting — **C**

**Missing.** Out of scope for a 5-6 month project. Reject per feasibility constraints.

---

### 30. What-If Reasoning — **C**

**Missing.** "What would happen if Entity X changed state?" Potentially feasible as graph diffing with hypothetical state changes. Worth considering but risky for timeline.

---

### 31. Alert Prioritization — **C**

**Missing.** Could be derived from change detection + impact analysis (which entities are affected by a change, weighted by importance/connectivity).

**Architectural evolution:** D — Buildable on top of graph analytics.

---

### 32. Cross-Source Correlation — **C**

**Missing.** The ability to detect that Source A and Source B are talking about the same entity or event despite different terminology.

**Challenge:** Medium. Entity resolution across sources is well-studied.

---

### 33. Multi-Modal Evidence — **C → Low Priority**

Images, documents, sensor data as evidence. Important in theory, but reject per feasibility constraints. Text-first is sufficient for the core system.

---

### 34. Agent Interaction — **A**

**Graphify now:** MCP server with 10 tools + 6 resources, supporting both stdio and HTTP transports.

**Highly reusable.** The MCP pattern transfers directly.

---

### 35. Agent Memory — **B**

**Graphify now:** `reflect.py` provides experiential memory with decay, corroboration, and contested-signal handling. This is genuinely sophisticated.

**What's missing:** The memory is *about the agent's Q&A experience*, not about the *world*. A real agent memory would track what the agent has learned about the situation, not just which graph queries were useful.

---

### 36. Agent Verification — **C**

**Missing.** No mechanism for an agent to verify its own conclusions against the evidence graph.

---

### 37. Knowledge Integrity — **B**

**Graphify now:** Content-hash caching, deterministic extraction, fixpoint IDs.

**What's missing:** No checksumming of the knowledge graph itself. No way to detect tampering or corruption of the stored knowledge.

---

### 38. Security — **A**

**Graphify now:** Comprehensive. SSRF prevention, label sanitization, DNS rebinding protection, HMAC key comparison.

**Highly reusable.**

---

### 39. Privacy — **C**

**Missing.** No data classification, no access control on nodes/edges, no anonymization.

**For a student project:** Acceptable to defer. Note as a future requirement.

---

### 40. Resilience — **B**

**Graphify now:** Atomic writes, backup-before-overwrite, graceful degradation (Louvain fallback when Leiden unavailable).

**Reusable patterns.**

---

### 41. Fault Tolerance — **B**

**Graphify now:** Robust error handling in cache, watch, and serve modules. `.pending_changes` queue survives crashes.

**Reusable patterns.**

---

### 42. Scalability — **B**

**Graphify now:** In-memory NetworkX graph. Works for codebases up to ~500K nodes. No sharding.

**For the student project:** Fine. Laptop-scale is the constraint.

---

### 43. Auditability — **B**

**Graphify now:** GRAPH_REPORT.md + `.graphify_analysis.json`. Good structural audit trail.

**What's missing:** Decision audit — "why did the system believe fact X at time T?"

---

### 44. Reproducibility — **A**

**Graphify now:** Deterministic extraction, deterministic clustering (sorted + seeded), deterministic reporting. Explicitly designed for byte-stable output.

**Highly reusable design principle.**

---

### 45. Long-Term Maintainability — **A**

**Graphify now:** Well-structured codebase, comprehensive test suite (220 tests), versioned cache schema, migration documentation.

**Reusable practices.**

---

## 9. Static vs Evolving Knowledge — Deep Analysis

### The Fundamental Distinction

Graphify models a **snapshot world**: the codebase as it exists right now. Each `graphify extract` produces a complete replacement of the knowledge graph. History is preserved only accidentally (via git, which is external to the system).

Resilient Intelligence requires a **streaming world**: knowledge that accumulates, changes, conflicts, and decays over time.

| Dimension | Graphify (Static) | Resilient Intelligence (Evolving) |
|-----------|-------------------|----------------------------------|
| Truth model | "The code says X" → X is true | "Source S claims X at time T" → X is believed with confidence C |
| Update model | Full rebuild (overwrite) | Incremental append (add evidence, update beliefs) |
| History model | None (current snapshot only) | Full timeline (what was believed when) |
| Conflict model | Merge/deduplicate (resolve conflicts) | Preserve both sides (track conflicts) |
| Freshness model | Binary (cached/stale) | Continuous decay (half-life per fact per evidence type) |
| Identity model | Permanent (once normalized, stable forever) | Temporal (entities can split, merge, change names) |

### Evaluating the Proposed Model

The user proposed:

```
ENTITY + RELATIONSHIP + EVENT + TIME + STATE + EVIDENCE +
SOURCE + CONFIDENCE + CONTRADICTION + CHANGE + CONTEXT
```

**Critical evaluation:**

This model has 12 concepts. That is too many for a minimum viable system. Several can be collapsed:

- **EVENT** can be modeled as a timestamped entity with a "happened" state
- **STATE** can be modeled as a temporal attribute of an entity
- **SOURCE** is metadata on evidence
- **CHANGE** is derivable from comparing temporal snapshots
- **CONTEXT** is a grouping/filtering mechanism over the existing graph

**Minimum theoretically meaningful representation:**

```
ENTITY (with temporal attributes)
  + RELATIONSHIP (with temporal validity + evidence)
  + EVIDENCE (first-class, linked to facts, with source metadata)
  + TIME (bi-temporal: valid-time + transaction-time)
```

This 4-primitive model can express everything the 12-concept model can, without the conceptual overhead. CONTRADICTION is derived (two pieces of evidence supporting incompatible facts). CHANGE is derived (diff between time slices). CONTEXT is a query-time filter. STATE is a temporal attribute. EVENT is a temporal entity.

**Recommendation:** Start with the 4-primitive model. Add concept-level abstractions (Situation, Event, Hypothesis) as *layers* on top, not as primitives.

---

## 10. Temporal Intelligence Analysis

### The Five Temporal Questions

| Question | What It Requires |
|----------|-----------------|
| "What is true?" | Current snapshot of highest-confidence facts |
| "What was believed at time T?" | Transaction-time query (system state at T) |
| "What changed between T1 and T2?" | Temporal diff operation |
| "When did we first get evidence for this?" | Transaction-time of first supporting evidence |
| "Which evidence caused our understanding to change?" | Provenance chain + temporal ordering |
| "What is currently uncertain?" | Facts with low confidence or recent contradicting evidence |

### Should Time Be a First-Class Primitive?

**Yes.** This is the single most important architectural decision.

**Arguments for:**
1. Without time, you cannot answer "what changed?" — the most basic question in evolving situations
2. Without time, you cannot implement knowledge decay — stale facts look identical to fresh ones
3. Without time, you cannot detect contradictions — you need to know that evidence E2 arrived after E1 and contradicts it
4. Without time, historical reasoning is impossible — you cannot reproduce past conclusions
5. Graphify's reflection system already discovered this need — it timestamps memory docs and applies time-decay scoring. The gap is that this temporal model doesn't extend to the core knowledge graph.

**Arguments against:**
1. Temporal data models are more complex to query and index
2. Storage grows over time (append-only)
3. More complex schema = more bugs = more development time

**Verdict:** Time MUST be a first-class primitive. The storage/complexity cost is manageable with SQLite (append-only rows are cheap). The query cost is manageable with indexing on time columns.

### Temporal Model Design

```
FACT = (entity_id, attribute, value, valid_from, valid_to, evidence_id, confidence, inserted_at)
```

- `valid_from` / `valid_to` — when the fact was true in the world (null = still true)
- `inserted_at` — when the system recorded this fact (transaction time)
- `evidence_id` — what supports this fact

This bi-temporal model allows all five temporal questions to be answered with simple SQL queries.

---

## 11. Evidence / Provenance / Uncertainty

### Should the System Distinguish FACT / OBSERVATION / INFERENCE / HYPOTHESIS / PREDICTION?

**Partially.** The full 5-level taxonomy is theoretically clean but practically burdensome. For a student project:

| Level | Include? | Rationale |
|-------|----------|-----------|
| OBSERVED | ✅ | Direct evidence — sensor data, document, human report |
| INFERRED | ✅ | Derived from other evidence — entity resolution, LLM extraction |
| HYPOTHESIZED | ✅ | Tentatively proposed by human or agent — not yet confirmed |
| PREDICTED | ❌ | Requires forecasting capabilities — out of scope |
| FACT | ❌ | Nothing is a "fact" in an evolving system — everything is an evidence-backed belief |

### Evidence Source Model

```
EVIDENCE = {
  id,
  source_type (document | api | human | agent | sensor),
  source_uri,
  obtained_at,
  content_hash,
  reliability (0.0-1.0, human-assessed or derived)
}
```

### Confidence Derivation

Confidence should be *computed*, not assigned:
```
confidence(fact) = f(
  number of supporting evidence items,
  reliability of each source,
  freshness of evidence (time decay),
  contradicting evidence count
)
```

This is more principled than Graphify's manual EXTRACTED/INFERRED/AMBIGUOUS labels.

### Is This Meaningful or Unnecessary Complexity?

**It is meaningful IF the system actually shows it to the human.** A confidence score buried in a database schema is worthless. A confidence bar next to a fact on a dashboard, with a "why?" link that shows the supporting evidence, is powerful.

**The human-augmentation test:** Can a human look at a fact and immediately understand *how confident the system is and why*? If yes, the complexity pays for itself. If no, it's wasted engineering.

---

## 12. Change Intelligence

### "Something Changed" vs "The Graph Changed"

Graphify's watch system detects file-level changes. A resilient intelligence system needs to detect *knowledge-level* changes:

| Change Type | Example | Human Impact |
|-------------|---------|--------------|
| Entity state changed | "Server X: operational → compromised" | ⚠️ High — situation update |
| Relationship changed | "A supplies B → A no longer supplies B" | ⚠️ High — supply chain impact |
| New entity appeared | "Previously unknown actor Y detected" | 🔍 Medium — investigation trigger |
| Evidence contradicts existing belief | "New report contradicts earlier assessment" | ⚠️ High — confidence update |
| Confidence changed significantly | "Confidence in X dropped from 0.9 to 0.3" | 🔍 Medium — review trigger |
| No change (silence) | "Expected update from source S didn't arrive" | ⚠️ Medium — source reliability concern |

### Is a Generalized "Change Intelligence" Layer Worth Building?

**Yes, but only as a derived computation, not a separate subsystem.**

If the temporal model is implemented correctly (every fact has valid_from/valid_to), then change detection is a *query*:

```sql
SELECT * FROM facts
WHERE inserted_at > :last_check_time
ORDER BY change_significance DESC
```

Where `change_significance` is derived from the entity's importance (degree/centrality) × the magnitude of the change.

**This is simpler and more maintainable than a separate change-detection engine.** It follows directly from the temporal data model.

---

## 13. Human-in-the-Loop Intelligence

### What Humans Actually Need

Based on the Iron Man lens, the human interface should support:

1. **Situation overview** — "What are the key entities, relationships, and recent changes?"
2. **Evidence inspection** — "What evidence supports this fact? How reliable? How fresh?"
3. **Contradiction surfacing** — "These two sources disagree. Here's both sides."
4. **Change timeline** — "Here's what changed since your last review."
5. **Confidence dashboard** — "These facts are uncertain. These are well-supported."
6. **Annotation** — "Let me mark this as incorrect / add context / promote a hypothesis."
7. **Query** — "Show me everything related to X, filtered by time/confidence/source."

### Comparison with Graphify's Human Interface

| Capability | Graphify | Required |
|-----------|---------|---------|
| Overview | GRAPH_REPORT.md (static) | Dynamic situation dashboard |
| Evidence inspection | source_file link | Evidence chain with reliability scores |
| Contradiction surfacing | None | Explicit conflict view |
| Change timeline | None | Temporal diff view |
| Confidence dashboard | 3-level label | Numeric confidence with drill-down |
| Annotation | save-result (useful/dead_end/corrected) | Rich annotation (correct, incorrect, context, notes) |
| Query | MCP tools (agent-mediated) | Direct human query + MCP for agents |

---

## 14. Existing Technology Landscape

### Comparison Matrix

| System | Temporal | Evidence | Change | Human-Centered | Local-First | Agent-Ready | Open Source |
|--------|----------|----------|--------|----------------|-------------|-------------|-------------|
| **Graphify v8** | ❌ | ❌ | ❌ (file-level) | ❌ | ✅ | ✅ (MCP) | ✅ |
| **Graphiti/Zep** | ✅ (bi-temporal) | ✅ (episodes) | ❌ (implicit) | ❌ (agent memory) | ⚠️ (needs Neo4j) | ✅ (MCP) | ✅ (Graphiti) |
| **Microsoft GraphRAG** | ❌ | ❌ | ❌ | ❌ | ❌ (cloud) | ✅ | ✅ |
| **Mem0** | ⚠️ (basic) | ❌ | ❌ | ❌ (personalization) | ⚠️ | ✅ | ✅ |
| **Letta** | ❌ | ❌ | ❌ | ❌ (agent OS) | ⚠️ | ✅ | ✅ |
| **Neo4j + TKG** | ✅ (manual) | ⚠️ (manual) | ⚠️ | ❌ (developer) | ❌ (server) | ⚠️ | Community |
| **SIEM (Splunk, etc.)** | ✅ (events) | ✅ (logs) | ✅ (alerts) | ✅ (dashboards) | ❌ (enterprise) | ❌ | ❌ |
| **Academic TKGs** | ✅ | ⚠️ | ⚠️ | ❌ (research) | ❌ | ❌ | Varies |

### Where Existing Systems Fall Short

1. **Graphiti/Zep** — The closest existing system. Excellent temporal model. But: designed for *agent memory* (personalization), not *human situation awareness*. No human-facing UI. Requires Neo4j/FalkorDB server. No change-as-concept layer.

2. **Microsoft GraphRAG** — Excellent hierarchical community-based retrieval. But: designed for static document collections. No temporal model. No evidence tracking. Cloud-oriented.

3. **SIEM systems** — Excellent at event ingestion, change detection, and alerting. But: security-specific, enterprise-scale, expensive, and not knowledge-graph-based. The "understanding" layer is shallow (pattern matching, not evidential reasoning).

4. **Academic TKGs** — Strong theoretical foundations. But: focused on embedding-based completion/forecasting. Not designed for human interaction. Not production-grade.

### Where RESILIENT INTELLIGENCE Could Contribute

The potential contribution is at the **intersection** of:

```
Temporal KG (from Graphiti/academic TKGs)
  + Evidence-grounded reasoning (from provenance systems)
  + Human-centered situation awareness (from decision-support systems)
  + Local-first, zero-cost operation (from Graphify's philosophy)
  + MCP-based agent integration (from Graphify's server)
```

**No existing open-source system occupies this intersection.** Graphiti is close but lacks the human-centered and evidence-explicit dimensions. SIEM systems have the operational awareness but are enterprise/security-specific.

### Honesty Check: Are We Reinventing Existing Products?

**Partially.** The temporal knowledge graph aspect exists (Graphiti, Neo4j temporal). The MCP server aspect exists (Graphify, Graphiti). The dashboard aspect exists (Grafana, SIEM consoles).

**What does NOT exist:** A *lightweight, local-first, evidence-aware temporal knowledge system with human-centered situation exploration*. The emphasis on "lightweight" and "local-first" is the key differentiator — existing systems that have the temporal/evidence sophistication all require server infrastructure.

**This is a legitimate engineering gap, not a novel research breakthrough.** The contribution is in *integration and accessibility*, not in inventing new algorithms.

---

## 15. Research Gap Candidates

### Scoring Criteria (1-10 each)

| Criterion | What 10 Means |
|-----------|--------------|
| Problem significance | Addresses a real, recognized gap |
| Existing approaches insufficient | Current tools don't solve this well |
| Technical difficulty | Feasible for one student (10 = easy, 1 = needs a team) |
| Laptop feasibility | Runs on student hardware |
| Solo-developer feasibility | One person can build it |
| 5-6 month feasibility | Achievable in timeline |
| Demonstrability | Can be shown working in a demo |
| Research-paper potential | Publishable contribution |
| Reviewer explainability | Reviewers understand it in 5 minutes |
| Long-term product potential | Could become a real product |

---

### Gap 1: Temporal Evidence Graph Engine (TEG)

**Problem:** No lightweight, local-first system exists for maintaining temporal, evidence-grounded knowledge with explicit confidence and provenance.

**Existing approaches:** Graphiti (requires Neo4j), academic TKGs (not production-grade), manual provenance in relational DBs (no knowledge-graph semantics).

**Why insufficient:** Graphiti requires infrastructure. Academic systems aren't practical. Manual schemas lack query/reasoning capabilities.

**Potential contribution:** A SQLite-based temporal knowledge graph engine with bi-temporal facts, evidence objects, and derived confidence scoring. Embeddable, zero-infrastructure.

| Criterion | Score |
|-----------|-------|
| Problem significance | 8 |
| Existing approaches insufficient | 7 |
| Technical difficulty | 7 |
| Laptop feasibility | 10 |
| Solo-developer feasibility | 8 |
| 5-6 month feasibility | 7 |
| Demonstrability | 9 |
| Research-paper potential | 7 |
| Reviewer explainability | 8 |
| Long-term product potential | 8 |
| **Total** | **79** |

---

### Gap 2: Situation-Aware Knowledge Dashboard

**Problem:** Temporal knowledge graphs exist, but no tool presents evolving situations to *humans* with confidence, change tracking, and evidence drill-down in a lightweight way.

**Existing approaches:** SIEM dashboards (security-specific, enterprise), Grafana (metrics, not knowledge), Obsidian/Notion (static, no evidence model).

**Why insufficient:** SIEM is domain-locked. Grafana doesn't understand knowledge semantics. Personal knowledge tools don't track evidence or confidence.

**Potential contribution:** A web-based situation exploration interface that renders a temporal evidence graph as an interactive, human-readable dashboard with change timeline, confidence indicators, and evidence drill-down.

| Criterion | Score |
|-----------|-------|
| Problem significance | 8 |
| Existing approaches insufficient | 8 |
| Technical difficulty | 7 |
| Laptop feasibility | 10 |
| Solo-developer feasibility | 7 |
| 5-6 month feasibility | 6 |
| Demonstrability | 10 |
| Research-paper potential | 6 |
| Reviewer explainability | 9 |
| Long-term product potential | 8 |
| **Total** | **79** |

---

### Gap 3: Evidence-Derived Confidence Scoring

**Problem:** Existing knowledge systems assign confidence manually (Graphify: EXTRACTED/INFERRED) or learn it from embeddings (academic TKGs). Neither derives confidence from the *actual supporting evidence*.

**Existing approaches:** Manual labeling (Graphify), learned embeddings (TKG models), Bayesian networks (heavy infrastructure).

**Why insufficient:** Manual labeling doesn't scale. Learned embeddings are black boxes. Bayesian networks require expert specification.

**Potential contribution:** A simple, interpretable confidence-derivation function that computes fact confidence from: (1) number of sources, (2) source reliability, (3) evidence freshness, (4) contradicting evidence count. No ML required.

| Criterion | Score |
|-----------|-------|
| Problem significance | 7 |
| Existing approaches insufficient | 6 |
| Technical difficulty | 8 |
| Laptop feasibility | 10 |
| Solo-developer feasibility | 9 |
| 5-6 month feasibility | 9 |
| Demonstrability | 8 |
| Research-paper potential | 6 |
| Reviewer explainability | 9 |
| Long-term product potential | 7 |
| **Total** | **79** |

---

### Gap 4: Knowledge Change Detection & Explanation

**Problem:** Existing systems detect *data* changes (file modified, row updated). No lightweight system detects *knowledge-level* changes ("entity X changed state," "previously believed fact now contradicted").

**Existing approaches:** CEP systems (event-level, not knowledge-level), graph diffing (structural, not semantic), SIEM alerts (pattern-based, not evidence-based).

**Why insufficient:** CEP operates on events, not knowledge. Graph diffing finds added/removed nodes but doesn't explain *what the change means*. SIEM alerts are predefined patterns.

**Potential contribution:** A change-detection layer that operates on temporal knowledge states: identifies changed entities, explains what changed and why (which new evidence), and assesses impact (which related entities/situations are affected).

| Criterion | Score |
|-----------|-------|
| Problem significance | 8 |
| Existing approaches insufficient | 7 |
| Technical difficulty | 6 |
| Laptop feasibility | 10 |
| Solo-developer feasibility | 8 |
| 5-6 month feasibility | 7 |
| Demonstrability | 9 |
| Research-paper potential | 7 |
| Reviewer explainability | 8 |
| Long-term product potential | 8 |
| **Total** | **78** |

---

### Gap 5: Local-First MCP-Based Intelligence Server

**Problem:** Existing agent memory systems (Graphiti, Mem0) require server infrastructure. Graphify's MCP server is local-first but lacks temporal/evidence capabilities.

**Existing approaches:** Graphiti MCP (needs Neo4j), Graphify MCP (no temporal model), custom MCP servers (no knowledge-graph semantics).

**Why insufficient:** The gap is at the intersection: local-first + temporal + evidence-aware + MCP.

**Potential contribution:** An MCP server backed by a SQLite-based temporal evidence graph, providing tools for temporal queries, evidence inspection, change detection, and situation awareness — all runnable on a laptop.

| Criterion | Score |
|-----------|-------|
| Problem significance | 7 |
| Existing approaches insufficient | 7 |
| Technical difficulty | 6 |
| Laptop feasibility | 10 |
| Solo-developer feasibility | 8 |
| 5-6 month feasibility | 7 |
| Demonstrability | 9 |
| Research-paper potential | 6 |
| Reviewer explainability | 8 |
| Long-term product potential | 9 |
| **Total** | **77** |

---

### Gap 6: Contradiction-Aware Knowledge Maintenance

**Problem:** Existing knowledge systems either merge conflicting information (losing signal) or fail on contradictions. No lightweight system explicitly tracks, surfaces, and helps resolve contradictions.

**Existing approaches:** Belief revision in AI (theoretical), DEC cognitive worlds (academic), Graphify dedup (merges, doesn't track).

**Why insufficient:** Theory hasn't produced practical tools. Academic systems aren't deployable. Graphify actively destroys the contradiction by merging.

**Potential contribution:** A contradiction-tracking system that preserves both sides of a conflict, links them to their evidence, and helps humans resolve them.

| Criterion | Score |
|-----------|-------|
| Problem significance | 7 |
| Existing approaches insufficient | 7 |
| Technical difficulty | 7 |
| Laptop feasibility | 10 |
| Solo-developer feasibility | 8 |
| 5-6 month feasibility | 8 |
| Demonstrability | 8 |
| Research-paper potential | 7 |
| Reviewer explainability | 8 |
| Long-term product potential | 7 |
| **Total** | **77** |

---

### Gap 7: Temporal Knowledge Query Language

**Problem:** SQL can query temporal data but is verbose. Cypher/GraphQL don't have temporal semantics. No lightweight query abstraction exists for temporal evidence graphs.

**Existing approaches:** SQL with temporal extensions, SPARQL with named graphs, academic temporal query languages.

**Why insufficient:** SQL is verbose. SPARQL is complex. Academic languages aren't implemented.

**Potential contribution:** A thin query abstraction over SQLite that makes temporal/evidential queries natural. E.g., `SHOW entity "Server X" AT time "2026-01-15"` or `CHANGES IN situation "Incident 42" SINCE "2 hours ago"`.

| Criterion | Score |
|-----------|-------|
| Problem significance | 5 |
| Existing approaches insufficient | 5 |
| Technical difficulty | 7 |
| Laptop feasibility | 10 |
| Solo-developer feasibility | 8 |
| 5-6 month feasibility | 6 |
| Demonstrability | 7 |
| Research-paper potential | 5 |
| Reviewer explainability | 7 |
| Long-term product potential | 6 |
| **Total** | **66** |

---

### Gap 8: Cross-Domain Situation Template System

**Problem:** Every domain (cybersecurity, supply chain, emergency response) needs situation awareness, but each defines situations differently. No system provides a *domain-agnostic situation template* that can be specialized.

**Existing approaches:** Domain-specific ontologies, event schemas (STIX for cyber, NIEM for emergency).

**Why insufficient:** Domain-specific schemas don't transfer. Building a new schema for each domain is expensive.

**Potential contribution:** A minimal situation template: `{entities, relationships, evidence, timeline, context}` that can be specialized for any domain through entity/relationship type definitions.

| Criterion | Score |
|-----------|-------|
| Problem significance | 6 |
| Existing approaches insufficient | 5 |
| Technical difficulty | 6 |
| Laptop feasibility | 10 |
| Solo-developer feasibility | 7 |
| 5-6 month feasibility | 6 |
| Demonstrability | 6 |
| Research-paper potential | 5 |
| Reviewer explainability | 6 |
| Long-term product potential | 7 |
| **Total** | **64** |

---

### Ranked Summary

| Rank | Gap | Total Score |
|------|-----|-------------|
| 1 | **Temporal Evidence Graph Engine** | 79 |
| 1 | **Situation-Aware Knowledge Dashboard** | 79 |
| 1 | **Evidence-Derived Confidence Scoring** | 79 |
| 4 | **Knowledge Change Detection & Explanation** | 78 |
| 5 | **Local-First MCP Intelligence Server** | 77 |
| 5 | **Contradiction-Aware Knowledge Maintenance** | 77 |
| 7 | **Temporal Knowledge Query Language** | 66 |
| 8 | **Cross-Domain Situation Template System** | 64 |

---

## 16. Feasibility Analysis

### Hard Constraints Recap

| Constraint | Value |
|-----------|-------|
| Developer | 1 CS undergraduate |
| Budget | ₹0 |
| Hardware | 1 student laptop |
| Timeline | 5-6 productive months (interrupted by exams) |
| Infrastructure | Local-first; free tiers for deployment |
| Technology | Python + JS/HTML, VS Code, AI coding agents |

### What Can Be Built in 5-6 Months

Based on these constraints, the maximum feasible system is:

**Month 1-2:** Core engine (temporal evidence graph on SQLite) + basic ingestion + basic queries

**Month 3:** Change detection + evidence-derived confidence + MCP server

**Month 4:** Web dashboard (situation view, evidence drill-down, change timeline)

**Month 5:** Integration testing, demo scenarios, documentation

**Month 6:** Polish, paper writing, deployment

**What must be CUT:**
- Automated ingestion from multiple sources (do manual + simple file/URL ingestion)
- Prediction/forecasting
- Multi-modal evidence
- Complex entity resolution across sources (do simple label matching)
- Custom query language (use SQL/Python API)
- Distributed operation

### Technology Stack (Feasible)

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Storage | SQLite | Zero-infrastructure, embeddable, sufficient for laptop scale |
| Core engine | Python | Graphify patterns reusable, rich ecosystem |
| Web frontend | HTML/CSS/JS (Vite) | Lightweight, no framework overhead |
| MCP server | Python (mcp SDK) | Pattern reusable from Graphify |
| Deployment | Vercel (free) or local | Zero cost |
| LLM integration | Ollama (local) or free API tiers | Zero cost |

---

## 17. Candidate Architecture Directions

### Direction A: Temporal Evidence Graph (TEG) — *Recommended*

**Core idea:** A SQLite-based engine where every fact is a timestamped, evidence-backed assertion. The engine supports temporal queries, change detection, and confidence derivation. Exposed via MCP for agents and via a web dashboard for humans.

```
SQLite (facts + evidence + entities + relationships)
  ↑ Python core engine (query, ingest, change-detect, confidence)
  ↑ MCP server (agent tools)
  ↑ Web dashboard (human situation exploration)
```

**What it inherits from Graphify:**
- Stateless pipeline design
- MCP server pattern
- ID normalization
- Security practices
- Caching principles
- Reproducibility discipline

**What it adds:**
- Bi-temporal fact storage
- Evidence objects as first-class entities
- Derived confidence scoring
- Change detection as temporal queries
- Contradiction tracking
- Human-facing situation dashboard

**What it does NOT try to be:**
- A general-purpose graph database
- A SIEM system
- A prediction engine
- A multi-user collaboration platform

### Direction B: Graphify Fork + Temporal Layer

**Core idea:** Fork Graphify, replace the extraction pipeline with a multi-source ingestion system, add temporal attributes to the NetworkX graph.

**Why rejected:** NetworkX is an in-memory graph library with no temporal primitives. Adding time to every node/edge attribute would be fighting the data model. SQLite with temporal tables is architecturally cleaner.

### Direction C: Graphiti Wrapper + Human Dashboard

**Core idea:** Use Graphiti as the knowledge engine, build a human-facing dashboard on top.

**Why rejected:** Graphiti requires Neo4j/FalkorDB server infrastructure. Violates the ₹0 / laptop-only constraint. Also, Graphiti is designed for agent personalization memory, not situation awareness.

---

## 18. Risks / Failure Modes

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| **Scope creep** — "just one more feature" | HIGH | FATAL | Ruthless scope control. The TEG engine is the core; everything else is optional |
| **Schema over-engineering** — designing the perfect temporal schema before building anything | HIGH | HIGH | Start with 3 tables (entities, facts, evidence). Add complexity only when needed |
| **Dashboard time-sink** — spending 3 months on UI polish | MEDIUM | HIGH | Build the ugliest functional dashboard first. Polish only after the engine works |
| **"Academic paper" trap** — optimizing for theoretical elegance over practical utility | MEDIUM | HIGH | Every feature must pass the Iron Man test: does it make a human more capable? |
| **Exam disruption** — losing momentum during exam periods | HIGH | MEDIUM | Design for resumability. Each component should be independently testable |
| **LLM dependency** — designing around LLM capabilities that may cost money | MEDIUM | MEDIUM | Core system must work without LLMs. LLM integration is an enhancement, not a requirement |
| **Demo failure** — system works but can't be demonstrated convincingly | MEDIUM | HIGH | Build one compelling demo scenario (e.g., cybersecurity incident timeline) early |

---

## 19. What NOT to Build

| Idea | Why Not |
|------|---------|
| **Real-time streaming ingestion** | Polling is sufficient for demo. Real-time adds massive complexity |
| **Custom graph database** | SQLite with temporal tables is sufficient. Don't reinvent Neo4j |
| **Prediction/forecasting engine** | Requires ML infrastructure, training data, and expertise beyond scope |
| **Multi-user collaboration** | One-user system is sufficient for demo and thesis |
| **Mobile app** | Web app is sufficient |
| **NLP/NER pipeline** | Use LLM extraction (Graphify's pattern). Don't build a custom NLP pipeline |
| **Blockchain/immutable ledger** | Append-only SQLite tables provide sufficient auditability |
| **Computer vision for evidence** | Text-first. Image evidence can be stored as references without analysis |
| **Custom query language** | Python API + SQL is sufficient. A DSL adds complexity without proportional value |
| **Distributed/microservices architecture** | Single-process is sufficient. Distribution adds operational complexity |

---

## 20. Recommended Research Direction

### The Temporal Evidence Graph (TEG)

**One-sentence pitch:**

> A local-first intelligence engine that treats *time*, *evidence*, and *confidence* as first-class primitives, enabling humans and AI agents to understand how knowledge about a situation evolves, where it comes from, and how certain it is.

### Why This Direction

1. **Genuine gap:** No existing open-source system combines temporal knowledge, evidence tracking, and human-centered situation exploration in a local-first package
2. **Feasible:** SQLite + Python + simple web frontend. One student, 5-6 months
3. **Demonstrable:** A cybersecurity incident timeline with confidence bars and evidence drill-down is immediately comprehensible to any reviewer
4. **Reuses Graphify's strengths:** MCP server pattern, ID normalization, security practices, caching philosophy
5. **Research-paper potential:** "A Lightweight Temporal Evidence Graph for Human-Centered Situation Awareness" is a publishable contribution
6. **Product potential:** Could become a real tool for analysts, researchers, and incident responders
7. **Survives the "mega project" filter:** The core is 4 primitives (entity, relationship, evidence, time) and 3 interfaces (API, MCP, dashboard)

### What It Is NOT

- Not a Graphify replacement (Graphify does software knowledge better)
- Not a Graphiti competitor (Graphiti does agent memory better)
- Not a SIEM (SIEMs do security event processing better)
- Not a general-purpose knowledge graph (Neo4j does that better)

It is the **smallest credible system** that brings temporal, evidence-aware intelligence to a human in a local-first, zero-cost package.

---

## 21. Open Questions

These must be resolved before implementation begins:

1. **Demo domain:** Which domain should the first demo target? Cybersecurity incident response is the most concrete and demonstrable. Supply chain disruption is more broadly applicable but harder to get realistic data for.

2. **Ingestion strategy:** How does information enter the system? Manual entry, file upload, URL fetch, API integration? Each adds development cost.

3. **LLM role:** Should the LLM be used for entity extraction from unstructured text (like Graphify's semantic extraction)? This adds power but introduces cost and complexity.

4. **Graph visualization:** Should the dashboard include interactive graph visualization (D3.js force-directed, like Graphify's HTML export), or is a list/timeline view sufficient?

5. **Graphify code reuse:** How much of Graphify's code should be directly reused vs. reimplemented? The MCP server transport code, security module, and ID normalization are candidates for direct lift. The extraction/build pipeline requires fundamental changes.

6. **Academic framing:** Should the thesis frame this as a "temporal knowledge graph" contribution (computer science) or as a "decision support system" contribution (information systems)? The framing affects which literature review is needed.

7. **Data sourcing for demo:** Where does the demo data come from? Synthetic scenarios are controllable but less convincing. Real incident reports (MITRE ATT&CK, CVE databases, public incident reports) are convincing but require ingestion work.

8. **Deployment target:** Local-only (laptop demo), or also a lightweight cloud deployment (Vercel/Render free tier)? Cloud deployment adds credibility but adds ops complexity.

---

## 22. Decision Gate for Phase 3

Before proceeding to architecture and implementation planning, the following decisions are needed:

| # | Decision | Options | Impact |
|---|----------|---------|--------|
| 1 | **Core direction** | Accept TEG recommendation vs. propose alternative | Defines everything |
| 2 | **Demo domain** | Cybersecurity / Supply chain / Emergency / Generic | Shapes schema + demo |
| 3 | **Ingestion strategy** | Manual-first / File+URL / API-integrated | Scope of Month 1-2 |
| 4 | **LLM integration** | Core requirement / Optional enhancement / Not used | Architecture complexity |
| 5 | **UI complexity** | Dashboard + Graph viz / Dashboard only / CLI only | Scope of Month 4 |
| 6 | **Graphify reuse level** | Direct code lift / Pattern-only reuse / Clean-room | Development speed vs. attribution clarity |
| 7 | **Academic framing** | CS (temporal KG) / IS (decision support) / Engineering (system design) | Literature review scope |
| 8 | **Project name** | Keep "RESILIENT INTELLIGENCE" / Choose something more specific | Branding |

> **Do not proceed to Phase 3 until these decisions are made.**

---

*End of Capability Gap Analysis — Phase 2 Complete*

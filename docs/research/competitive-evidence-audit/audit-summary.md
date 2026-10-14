# RESILIENT INTELLIGENCE — Competitive Evidence Audit Summary
## Executive Synthesis, Grounded Findings, and Next Experimental Steps

- **Audit Date:** October 13, 2026
- **Status:** Pre-Fixture Semantic Consistency Gate — Pending BLK-01 Authorization
- **Audit Scope:** Primary-source capability audit of OpenAI, Anthropic, and literature baselines against the core RESILIENT INTELLIGENCE (RI) research question.
- **Location:** `docs/research/competitive-evidence-audit/`
- **Integrity Status:** Working-tree state verified via `git status --short`. All application code, Graphify source, configurations, and pre-existing modifications remain preserved. Implementation is strictly halted pending human authorization of BLK-01.

---

## 1. Audit Review & Evidentiary Corrections (Pre-Fixture Semantic Consistency Gate)

This section records the audit findings and rigor improvements applied across the entire audit suite:

| Material Issue Identified | Source & Evidence | Correction Applied across Suite | Residual Uncertainty |
| :--- | :--- | :--- | :--- |
| **Bitemporal Row-Versioning Invariant** | Lacked formal uniqueness and non-overlap invariant for temporal intervals, allowing `status` to potentially override query logic. | Formalized temporal intervals $[t_{\text{from}}, t_{\text{to}})$ with strict non-overlap invariant per entity-attribute at $(T_v, T_x)$ unless an explicit conflict exists. Established that temporal queries depend strictly on interval predicates, never on administrative `status` labels. Added boundary queries at $T_x = 11:00$ and $T_x = 13:00$. | Sub-millisecond clock resolution across local operating systems. |
| **Historical Belief Identity & Versioning** | Unclear whether historical beliefs were persisted records or transient query-time evaluations. | Defined persisted belief-version schema with 10 minimal fields (`belief_id`, `version_id`, `valid_from/to`, `system_from/to`, `rule_id`, `premise_version_ids`, `belief_value`, `jtms_support`, `ri_lifecycle`, `conflict_status`). Traced exact path $E_9 \to A_{C1,v3} \to B_{1,v3} (200s) \to B_{2,v3} (\text{TRUE, recomputed})$. | Downstream multi-hop aggregation graph depth. |
| **Retraction Semantics vs. Historical Reconstruction** | Unclear how Stage 5 retraction of $E_2$ impacts historical queries. | Formalized distinction: Historical recorded state ($T_x < 14:00$) preserves past states as recorded (where $E_2$ held); retrospective reconstruction using current evidence ($T_x \ge 14:00$) evaluates historical valid dates with $E_2$ retracted (`OUT` / `UNKNOWN`). Recomputation kept distinct from value change. | Long-term archival retention policies. |
| **Empty-Set Metric Rigor** | Setting $\text{Recall} = 1.00$ when target set is empty rewarded false positives. | Corrected: when target set is empty ($\mathcal{A}^* = \emptyset$), Recall is Not Applicable ($N/A$); Empty-Set Detection Accuracy ($EDA = \mathbb{I}(\mathcal{A}_{\text{id}} == \emptyset)$) evaluates invariance. If false positives occur, $EDA = 0.00, \text{Precision} = 0.00$. Added micro-aggregated metrics alongside macro averages. | Domain-specific weighting of false positives vs false negatives. |
| **Fair Workload Comparison Contract** | Previous draft risked comparing incremental updates to cold initial builds. | Formalized fair procedure: Targeted Revalidation vs. Full Graph Recomputation *after the exact same evidence change ($E_1'$), starting from identical pre-change snapshots, with identical correctness requirements*. Initial construction ($CW_{\text{init}}$) reported separately. Retained $WWR \le 0.50$ as a preregistered target on this synthetic fixture. | Hardware disk cache noise across repeated SQLite benchmarks. |
| **Track 2 Metric Validity & Scoring** | Conflated refusals and errors with stale answers; citation scoring lacked separation between precision and recall. | Disaggregated probe outcomes into Freshness Accuracy ($BFA$), Stale-Belief Rate ($SBR$), and Refusal/Error Rate ($RER$) such that $BFA + SBR + RER = 1.00$. Separated Citation Coverage ($CC$) from Citation Correctness ($CCR$), retaining Jaccard as supplementary. Scoped $UBP$ as fixture-specific. | LLM prompt sensitivity and output formatting variability. |
| **Permitted Conflict-State Matrix** | Permitted state combinations across orthogonal dimensions were undefined. | Formalized explicit 5-tuple state matrix of permitted combinations among Belief Value, JTMS Support, RI Lifecycle, and Conflict Status. Specified provisional exposure rules and restoration events for $B_3$. | Future multi-agent consensus voting algorithms. |
| **Evidence Discipline & Competitor Claims** | Previous draft made unverified assertions regarding internal storage, Claude re-indexing, and GraphRAG updates. | Reclassified unexposed competitor internals as **NE (Not Established by Reviewed Evidence)**. Corrected Claude Projects description to reflect documented file additions/deletions. Scoped GraphRAG to a static batch preprint. | Proprietary internal engineering at OpenAI and Anthropic. |
| **Source Traceability & Indirect Access** | Blended paraphrases with direct quotes; lacked explicit note on indirect access. | Strictly separated verbatim quotations from descriptive summaries. Added exact locators (sections, pages, schema fields). Explicitly documented Cloudflare 403 limitation on `help.openai.com`. | Vendor documentation updates over time. |

---

## 2. Strongest Verified Findings

From direct inspection of official documentation, developer APIs, help centers, and peer-reviewed computer science literature, the following findings are verified with high evidentiary certainty:

1. **Document-Level / File-Level Ingestion Dominates Commercial AI Platforms:**
   - OpenAI (Assistants API / Vector Stores) and Anthropic (Claude Projects with RAG) manage external knowledge predominantly at the granularity of discrete **files** (`.pdf`, `.txt`, `.docx`) or **user-authored instructions**.
   - Ingestion is structured around chunking text, generating embeddings, and storing vectors for top-$k$ semantic similarity retrieval during inference.
2. **Absence of Exposed Evidence-to-Belief Dependency DAGs:**
   - Neither OpenAI nor Anthropic exposes a programmatic or user-visible graph that tracks logical dependencies between raw evidence chunks, intermediate claims, and derived beliefs.
   - When a document is modified or deleted in an OpenAI Vector Store or a Claude Project, the systems do not expose an audit trail of which specific downstream conclusions or assistant assertions are now invalidated.
3. **Absence of Exposed Bitemporal Semantics:**
   - Commercial retrieval architectures track operational system timestamps (upload date, run time), but do not natively expose **bitemporal intervals** (distinguishing *valid world time* from *system transaction time*).
   - As a result, commercial products cannot execute historical state rollback queries (e.g., *"Reconstruct exactly what the assistant believed on Date $T_1$ prior to receiving Correction $E_2$ on Date $T_2$"*) through their standard interfaces.
4. **Classical TMS Foundations Directly Address Targeted Revalidation:**
   - The foundational literature on Truth Maintenance Systems (Doyle 1979 JTMS, de Kleer 1986 ATMS) and Bitemporal Databases (Snodgrass & Ahn 1986) established formal mathematical and algorithmic mechanisms for dependency-directed revalidation and historical reconstruction.
   - However, classical TMS was developed for deterministic symbolic rule systems. The intersection of modern LLM-driven knowledge extraction with explicit bitemporal evidence graphs remains an active, open research frontier.

---

## 3. Graphify Architectural Boundary Summary

To ensure academic and engineering clarity, RESILIENT INTELLIGENCE's relationship to the existing Graphify v8 codebase is strictly defined across three evidentiary tiers:

- **Inspected Graphify Snapshot Assets (Verified in Repository; Proposed for Reuse in RI):**
  - `graphify.llm.client`: Multi-backend LLM client wrapper (Gemini, Claude, OpenAI, Ollama).
  - `graphify.cache`: File-hash and prompt-hash caching (essential for zero-cost operation).
  - `graphify.security`: Path traversal, URL sanitization, and SSRF prevention.
  - `graphify.server`: FastMCP server scaffold for exposing tools to AI agents.
- **Graphify Components Inspected; Proposed for Adaptation in RI:**
  - CLI pipeline orchestration (adapted to stage evidence ingestion instead of AST parsing).
  - File-system watcher (adapted from code file monitoring to evidence inbox monitoring).
  - Memory decay math (`reflect.py`) adapted to calculate evidence freshness decay.
- **Proposed Architecture for RI Core Logic (Not Present in Graphify; Not Yet Implemented or Demonstrated):**
  - Bi-temporal relational SQLite schema (`valid_from/to` and `system_from/to`).
  - Justification-based belief dependency graph (JTMS/ATMS dependency network).
  - Contradiction detection queries over mutually exclusive predicates.
  - Point-in-Time historical state reconstruction SQL views.
  - Evidence-to-assertion provenance tracking.

*Explicit Principle:* **Graphify is a static AST codebase knowledge graph generator.** It has no temporal modeling, no truth maintenance, and no contradiction handling. All situational intelligence and temporal evidence capabilities in RI are newly designed core logic that has **not yet been implemented or integrated**.

---

## 4. Unsupported Claims RI Must Strictly Avoid

To maintain rigorous academic and engineering integrity, RESILIENT INTELLIGENCE documentation, papers, and reviews **must never** make the following claims:

- ❌ **Do NOT claim competitors "cannot" track dependencies:**
  *Wrong:* "ChatGPT and Claude are fundamentally incapable of tracking belief dependencies."
  *Correct:* "Neither the OpenAI Assistants API nor the Claude Projects documentation exposes an evidence-to-belief dependency graph or a targeted revalidation mechanism."
- ❌ **Do NOT claim RI is "superior" or "novel without qualification":**
  *Wrong:* "RESILIENT INTELLIGENCE outperforms OpenAI and Anthropic."
  *Correct:* "RESILIENT INTELLIGENCE investigates a distinct, human-centered design point focused on explicit bitemporal provenance and targeted revalidation, addressing capability gaps not exposed in standard semantic retrieval APIs."
- ❌ **Do NOT treat documentation silence as architectural proof:**
  *Wrong:* "Because the API documentation does not mention Truth Maintenance Systems, OpenAI definitely does not use dependency tracking."
  *Correct:* "The reviewed public documentation does not establish the presence of an exposed dependency tracking or belief maintenance engine (NE)."
- ❌ **Do NOT dismiss Vector RAG as obsolete:**
  *Wrong:* "Vector search is broken and useless for evolving knowledge."
  *Correct:* "Vector search excels at open-vocabulary similarity retrieval over large unstructured text corpora, but does not natively maintain discrete bitemporal state or logical dependency graphs when source documents change."
- ❌ **Do NOT assert uncalibrated heuristic scores are calibrated probabilities:**
  *Wrong:* "RI computes a calibrated confidence of 0.45 for contested beliefs."
  *Correct:* "RI computes an uncalibrated heuristic indicator based on source reliability, age decay, and corroboration."

---

## 5. Prioritized Blockers Before Implementation or Experiments

Before executing the black-box evaluation protocol or writing production code, the following three blockers must be resolved in order:

| Priority | Blocker ID | Description | Resolution Prerequisite |
| :--- | :--- | :--- | :--- |
| **P1** | **BLK-01** | **Machine-Readable Benchmark Fixture** | Create a deterministic JSON/SQLite fixture encoding the 9 evidence items, 7 initial claims, 2 subsequent claims, 4 derived beliefs, and 4 inference rules (including `POL-SEC-01`, bitemporal relational log, and $(1+C_2) \times C_1$) specified in `black-box-test-protocol.md`. **Pending Human Authorization.** |
| **P2** | **BLK-02** | **Reference JTMS Propagation Runner** | Implement a standalone Python test harness for **Track 1** that executes deterministic JTMS dependency propagation over SQLite triples across all 5 stages ($S_1 \dots S_5$), verifying multi-stage $\text{Recall}_{\mathcal{A}} = 1.00$ and $UBI = 1.00$. |
| **P3** | **BLK-03** | **Local Vector RAG Baseline Probing Harness** | Configure a local, isolated Vector RAG baseline (e.g., SQLite-vec or ChromaDB with fixed 256-token chunking and a local open embedding model) to execute the standardized query probes ($Q_1 \dots Q_4$) for **Track 2**. |

---

## 6. Explicit Open Decisions & Required Resolution Evidence

The following architectural and empirical decisions cannot be settled by documentation review alone and are formally registered as open decisions:

1. **Internal Storage & Indexing Architectures of Commercial Providers:**
   - *Status:* Unresolved / Not Established (NE).
   - *Evidence Required to Resolve:* Formal peer-reviewed publications or official whitepapers from OpenAI and Anthropic disclosing backend vector/graph index architectures.
2. **Epistemic Uncertainty Score Calibration:**
   - *Status:* Uncalibrated Heuristic Indicator (CAT-6).
   - *Evidence Required to Resolve:* Empirical reliability calibration benchmarks across multi-source benchmark datasets comparing heuristic outputs against human ground truth.
3. **Automated Dispute Resolution vs. Human Review Escalation:**
   - *Status:* Policy-Gated Escalation (`HUMAN_REVIEW_REQUIRED = TRUE`).
   - *Evidence Required to Resolve:* Formal domain-specific dispute policies (e.g. source precedence rules, timestamp recency overrides, or cryptographic signature verifications) before enabling automated contradiction resolution.

---

## 7. Source Artifact Manifest

| Artifact Name | Path | Size | Role / Content |
| :--- | :--- | :--- | :--- |
| **Source Register** | `docs/research/competitive-evidence-audit/source-register.md` | ~27 KB | Complete catalog of OpenAI, Anthropic, and foundational literature sources with verified quotes, URLs, and access dates. |
| **Evidence Matrix** | `docs/research/competitive-evidence-audit/evidence-matrix.md` | ~18 KB | Rigorous cross-comparison matrix classifying capabilities across 7 strict evidentiary categories (CAT-1 to CAT-6). |
| **Test Protocol** | `docs/research/competitive-evidence-audit/black-box-test-protocol.md` | ~42 KB | Reproducible, zero-cost experimental protocol defining formal rules, multi-stage ground truth, orthogonal states, and two-track metrics. |
| **Audit Summary** | `docs/research/competitive-evidence-audit/audit-summary.md` | ~16 KB | Executive synthesis of verified findings, Graphify boundaries, unsupported claim prohibitions, and prioritized blockers. |

---

## 8. Workspace Preservation Confirmation

- **Working-Tree Status:** Checked via `git status --short`. Pre-existing modified files in `.gitignore` and `graphify/tests/fixtures/` and untracked `graphify-runtime-recon/` remain intact and uncommitted.
- **Verification Boundary:** `git status --short` establishes the current status of workspace files in this working tree; it does not claim byte-level preservation relative to earlier historical states beyond current working-tree tracking.
- **Session Scope:** 0 application code files modified, 0 Graphify source files modified, 0 dependencies installed. Modifications were strictly limited to the four documentation files in `docs/research/competitive-evidence-audit/`.
- **Authorization Gate:** Implementation is strictly halted. BLK-01 will not be created without explicit user authorization.

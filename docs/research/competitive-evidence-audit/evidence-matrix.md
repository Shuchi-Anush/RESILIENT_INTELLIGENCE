# RESILIENT INTELLIGENCE — Competitive Evidence Matrix
## Comparative Analysis: Documented State vs. Open Research Questions

- **Audit Date:** October 13, 2026
- **Status:** Pre-Fixture Semantic Consistency Gate — Pending BLK-01 Authorization
- **Target Systems / Baselines:**
  1. OpenAI ChatGPT Memory (Consumer/Enterprise Product)
  2. OpenAI Vector Stores & File Search (API Platform)
  3. Anthropic Claude Personalization (Instructions/Projects)
  4. Anthropic Claude Projects with RAG (Product Knowledge Retrieval)
  5. Foundational TMS / Temporal Literature (Doyle 1979, de Kleer 1986, Snodgrass 1986)
  6. GraphRAG / Graph Retrieval Baselines (Edge et al. 2024, arXiv Preprint)
  7. RESILIENT INTELLIGENCE (RI) Architectural Hypotheses

---

## 1. Audit Review & Evidentiary Corrections

This section records the audit findings and rigor improvements applied to this comparative matrix:

| Material Issue Identified | Source & Evidence | Correction Applied | Residual Uncertainty |
| :--- | :--- | :--- | :--- |
| **Preprint vs. Peer-Reviewed Tagging** | GraphRAG was grouped under general CAT-4 research without distinguishing peer review. | Split CAT-4 into CAT-4 (Peer-Reviewed Journal) and CAT-4P (Preprint). Marked GraphRAG as CAT-4P. | Potential subsequent formal conference proceedings publication of GraphRAG. |
| **Competitor Internal Storage Claims** | Conflated user-facing features with internal storage claims (e.g. asserting Claude RAG uses "hybrid index" or ChatGPT uses "internal vector store"). | Reclassified internal storage as **NE (Not Established by Reviewed Evidence)** for commercial products. Disclosed only verified user-facing units. | Proprietary unexposed internal storage engines at OpenAI and Anthropic. |
| **Claude File Update Claims** | Asserted that Claude Projects "re-indexes files on update," which is not documented in help center articles. | Corrected to **NE**: Help center documents adding and deleting files in Project Knowledge to alter prompt context. Internal re-indexing pipelines and chat invalidation are not disclosed. | Proprietary Anthropic backend index management. |
| **GraphRAG Historical State Claims** | Claimed GraphRAG historical reconstruction "requires external snapshot restore" without citation. | Corrected to **NE**: Edge et al. 2024 does not model valid-time or transaction-time intervals; historical state rollback is **not established by the reviewed preprint**. | Proprietary Microsoft enterprise GraphRAG implementations. |
| **Graphify Capability Boundary** | Labeled assets "reused without change," implying completed integration. | Replaced with strict evidentiary labels: **Verified in inspected Graphify snapshot; proposed for reuse in RI**. Explicitly stated that RI core logic is proposed architecture, not yet implemented. | Future updates to Graphify v8 codebase. |
| **Uncalibrated Confidence Claims** | Described RI confidence scoring as an established metric without calibration evidence. | Explicitly labeled RI confidence scoring as an **uncalibrated heuristic indicator (CAT-6)**, distinct from calibrated statistical probabilities. | Empirical score calibration across real-world tasks. |

---

## 2. Classification Framework

Capabilities are classified across seven unambiguous categories:

| Category Code | Description | Standard of Proof |
| :--- | :--- | :--- |
| **CAT-1** | Documented User-Facing Product Capability | Verified in official user documentation or help center. |
| **CAT-2** | Documented API Capability & Exposed State | Verified in official API documentation, schemas, or endpoints. |
| **CAT-3** | Claim About Internal Architecture | Claim made by publisher regarding unexposed internal mechanisms. |
| **CAT-4** | Peer-Reviewed Research Baseline | Published in peer-reviewed journal or formal conference proceedings. |
| **CAT-4P** | Research Preprint Baseline | Public preprint (e.g., arXiv); non-peer-reviewed. |
| **CAT-5** | Directly Observed Empirical Behavior | Replicated through controlled, documented black-box tests under scripted conditions. |
| **CAT-6** | RI Hypothesis / Proposed Architecture | Proposed design in RI specifications; **not yet empirically validated or implemented**. |

*Critical Precaution:* When a capability is not documented in an API or product manual, it is classified as **"Not established by reviewed evidence" (NE)**. It is never marked as "absent" or "impossible" for external commercial systems.

---

## 3. Core Comparative Matrix

| Capability Dimension | OpenAI ChatGPT Memory | OpenAI Vector Stores (API) | Anthropic Claude Personalization | Anthropic Claude Projects (RAG) | Classical TMS / Temporal Systems | GraphRAG (Edge et al. 2024) | RESILIENT INTELLIGENCE (RI) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Ingestion Unit** | Text utterances, explicit user instructions, or chat facts | File objects (`.pdf`, `.txt`, `.docx`, etc.) | Text instructions (Account or Project level) | File uploads to Project workspace | Discrete propositions / justifications | Text chunks extracted from documents | Evidence items (raw text + URI + observation metadata) |
| **Internal Unit of Storage** | **NE** (User-facing text memory statements documented; internal structure not disclosed) | Chunks & vector embeddings in managed store (CAT-2) | Text instruction blocks (CAT-1) | **NE** (Dynamic retrieval over files documented; internal index structure not disclosed) | Nodes with `IN`/`OUT` labels (CAT-4) | Entity-relation graph + Leiden community summaries (CAT-4P) | Proposed: Normalized Entities & Triples in SQLite (CAT-6) |
| **Evidence-to-Belief Dependency Visibility** | **NE** (Only flat list of memory statements exposed to user) | **NE** (File-to-chunk links internal; citations return file ID/offsets) | **NE** (Flat text instructions; no dependency links exposed) | **NE** (Retrieves chunks for context; no belief DAG exposed) | **Documented & Exposed** (Explicit justification DAG; CAT-4) | **NE** (Summary-to-chunk links exist; no belief DAG exposed) | Proposed: `Assertion_Evidence` linking table (CAT-6) |
| **Bi-temporal Modeling (Valid Time vs. Transaction Time)** | **NE** (Timestamps may reflect insertion; valid intervals not exposed) | **NE** (`created_at` timestamp exposed; valid-world intervals not exposed) | **NE** (Only manual editing timestamp tracked; CAT-1) | **NE** (File upload timestamp tracked; valid intervals not exposed) | **Documented & Implemented** (Snodgrass 1986 bitemporal model; CAT-4) | **NE** (Static extraction from snapshot documents; CAT-4P) | Proposed: `valid_from/to` vs `system_from/to` (CAT-6) |
| **Change-Impact Identification (Targeted Invalidation)** | **NE** (User deletes memory; system does not expose which derived beliefs break) | **NE** (Deleting file removes chunks; impact on existing runs/threads unexposed) | **NE** (Editing text instruction does not expose affected downstream chats) | **NE** (Adding/deleting files updates prompt context; invalidation of past conclusions unexposed) | **Documented & Implemented** (Dependency-directed backtracking; Doyle 1979; CAT-4) | **NE** (Preprint defines static batch pipeline; incremental updates not addressed; CAT-4P) | Proposed: Graph traversal over assertion dependencies (CAT-6) |
| **Contradiction Detection & Multi-World Representation** | **NE** (Model may attempt reconciliation in context; no conflict state exposed) | **NE** (Vector search retrieves conflicting chunks without explicit conflict flag) | **NE** (Conflicting instructions handled via prompt arbitration; CAT-1) | **NE** (Conflicting project files retrieved together; prompt arbitrates; CAT-1) | **Documented & Implemented** (ATMS "nogoods" and distinct assumption contexts; CAT-4) | **NE** (Conflicting claims in text may be summarized as divergent views; CAT-4P) | Proposed: Mutually exclusive predicates query + alert flag (CAT-6) |
| **Historical Knowledge State Reconstruction** | **NE** (Cannot query "What did ChatGPT believe about X last month?") | **NE** (Cannot query vector store as of historical timestamp $T_x$) | **NE** (Previous instruction revisions not exposed for historical queries) | **NE** (Cannot query project knowledge at previous state prior to file update) | **Documented & Implemented** (Bitemporal rollback queries; CAT-4) | **NE** (Historical state rollback is not established by reviewed preprint; CAT-4P) | Proposed: `WHERE $T_x$ BETWEEN system_from AND system_to` (CAT-6) |
| **Exposed Provenance Inspection** | Citations link to chat turn or memory list (CAT-1) | Citations provide file ID, filename, and chunk offset (CAT-2) | Direct user inspection of instruction text (CAT-1) | In-chat citations to uploaded project files (CAT-1) | Full justification chain inspectable via DAG traversal (CAT-4) | Summaries cite source text chunk IDs (CAT-4P) | Proposed: End-to-end drilldown: UI Assertion $\to$ Evidence text + Source (CAT-6) |
| **Confidence / Uncertainty Modeling** | **NE** (Model expresses certainty linguistically; no score exposed) | **NE** (Similarity score used internally for top-k; no confidence score exposed) | **NE** (No score exposed; qualitative text guidance; CAT-1) | **NE** (Retrieval relevance score internal; no confidence score exposed) | Categorical belief labels (`IN`, `OUT`, `UNKNOWN`) (CAT-4) | Graph centrality / confidence metrics occasionally logged (CAT-4P) | Proposed: Uncalibrated heuristic indicator ($Score \in [0, 1]$; CAT-6) |

*Legend: **NE** = Not established by reviewed evidence (capability may exist internally, but is neither documented nor exposed via interfaces/APIs).*

---

## 4. Graphify Architectural Boundary & Implementation Lineage

To prevent conflating Graphify's capabilities with RESILIENT INTELLIGENCE, the engineering lineage is strictly partitioned into three distinct tiers with precise evidentiary statuses:

```
+-------------------------------------------------------------------------------+
|                      GRAPHIFY REUSE & BOUNDARY MAPPING                        |
+-------------------------------------------------------------------------------+
| 1. VERIFIED IN INSPECTED GRAPHIFY SNAPSHOT; PROPOSED FOR REUSE IN RI          |
|    - Multi-provider LLM Client Sandbox (graphify.llm.client)                  |
|    - Content-Hash File Caching (graphify.cache)                               |
|    - Network Sanitization & SSRF Defense (graphify.security)                  |
|    - FastMCP Stdio/HTTP Server Adapter (graphify.server)                      |
+-------------------------------------------------------------------------------+
                                       │
                                       ▼
+-------------------------------------------------------------------------------+
| 2. INSPECTED IN GRAPHIFY; PROPOSED FOR ADAPTATION IN RI                       |
|    - Pipeline CLI Orchestration (adapted to stage evidence ingestion)         |
|    - File-system Watcher (adapted from code watch to evidence folder monitor) |
|    - Time-Decay Math (adapted from reflect.py memory decay to evidence age)   |
+-------------------------------------------------------------------------------+
                                       │
                                       ▼
+-------------------------------------------------------------------------------+
| 3. PROPOSED ARCHITECTURE FOR RI CORE LOGIC (NOT PRESENT IN GRAPHIFY)          |
|    (Not yet implemented, integrated, or demonstrated in code)                 |
|    - Bi-temporal Relational Schema (valid_from/to and system_from/to)         |
|    - Justification-Based Truth Maintenance (JTMS/ATMS dependency DAG)        |
|    - Contradiction Detection Queries over Mutually Exclusive Predicates       |
|    - Point-in-Time Historical State Rollback (Transaction Time SQL Views)     |
|    - Evidence-to-Assertion Provenance Linking Table                           |
+-------------------------------------------------------------------------------+
```

*Explicit Principle:* **Graphify is a static AST codebase knowledge graph generator.** It contains no temporal versioning, no bitemporal queries, no evidence-to-belief justification networks, and no contradiction detection mechanisms. All temporal and truth-maintenance capabilities in RESILIENT INTELLIGENCE represent newly designed core logic that has **not yet been implemented or integrated**.

---

## 5. Detailed Dimension-by-Dimension Analysis

### Dimension A: Explicit Dependency Visibility
- **OpenAI ChatGPT / Assistants:**
  - *Evidence:* OpenAI documentation (`help.openai.com`, `developers.openai.com`) confirms that users can manage "Saved Memories" and files in "Vector Stores". Citations reference source files and text spans.
  - *Finding:* Neither the ChatGPT user interface nor the Assistants v2 API exposes a dependency graph connecting an evidence item (e.g., File A) to a specific derived claim or belief (e.g., "The client system runs Linux"). If File A is modified, the system does not report which downstream conclusions are impacted.
  - *Status:* NE for OpenAI commercial interfaces. Explicitly present in classical TMS literature (CAT-4). Proposed in RI (CAT-6).
- **Anthropic Claude Personalization / Projects:**
  - *Evidence:* Anthropic documentation (`support.claude.com/articles/10185728`, `11473015`, `9517075`) documents three tiers of customization (Account instructions, Project instructions, Skills) and dynamic RAG for project documents.
  - *Finding:* RAG retrieves relevant document passages into the context window at inference time. The documentation does not describe or expose any persistent belief dependency graph that maps document facts to derived conclusions.
  - *Status:* NE for Anthropic commercial interfaces. Proposed in RI (CAT-6).

### Dimension B: Change-Impact Identification & Targeted Revalidation
- **Current Commercial State:**
  - In both OpenAI Vector Stores and Anthropic Claude Projects, updating knowledge is handled at the **file/document level**:
    - OpenAI: Files are added, deleted, or batched into a vector store. Modifying a document requires re-uploading the file and re-indexing its chunks.
    - Anthropic: Adding or deleting a file in Project Knowledge alters the available context for future chats within that project; documentation does not specify the internal re-indexing pipeline or provide an audit log of which previous conversation conclusions are now invalid.
  - In neither system is there an exposed mechanism to perform **targeted revalidation**: identifying the exact subset of downstream beliefs that depend on the changed fact, re-evaluating only that subset, and leaving unaffected beliefs untouched.
- **Classical Reference Point:**
  - Doyle's JTMS (1979) and de Kleer's ATMS (1986) established formal dependency-directed revalidation. When a justification is retracted, only its transitive dependents are recalculated.
- **RI Research Hypothesis:**
  - RI hypothesizes that applying explicit dependency tracking to an evolving situation or codebase allows updating belief state with lower computational overhead and higher transparency than full-context re-ingestion. This remains an **untested hypothesis (CAT-6)** on synthetic fixtures until empirical benchmarks are executed.

### Dimension C: Temporal Semantics & Provenance
- **Current Commercial State:**
  - Both OpenAI and Anthropic systems record operational timestamps (e.g., file upload time, memory creation date).
  - However, neither system documents native **bitemporal semantics**: distinguishing the *valid time* of an event in the real world from the *transaction time* when the system recorded the event.
  - When an old file is replaced by a new file, the previous state of the project knowledge or memory is superseded. A user cannot issue a point-in-time query such as: *"What did the assistant believe on October 1st about the server status, based only on files known on October 1st?"*
- **Classical Reference Point:**
  - Snodgrass & Ahn (1986) demonstrated that bitemporal modeling is required to achieve full historical reproducibility and institutional memory.
- **RI Research Hypothesis:**
  - RI models both `valid_time` and `transaction_time` as first-class attributes on Assertions and Beliefs in SQLite, enabling retrospective state reconstruction (Future Generations requirement). This is currently an **unverified implementation design (CAT-6)**.

---

## 6. Evidentiary Boundaries and Limitations

1. **Documentation Silence $\neq$ Technological Absence:**
   - OpenAI or Anthropic may utilize internal semantic graphs, caching hierarchies, or dependency-tracking heuristics within their proprietary inference pipelines.
   - The finding of this audit is strictly: **No such capability is documented or programmatically exposed in their public developer APIs or user guides.**
2. **Trade-offs of Explicit Dependency Tracking:**
   - While classical TMS systems provide perfect targeted revalidation, they suffer from combinatorial explosion in complex logic spaces.
   - Statistical RAG and large context windows avoid combinatorial explosion by performing approximate semantic search over unstructured text.
   - RI must prove that its hybrid approach (structured SQLite triples backed by raw evidence) achieves targeted revalidation without succumbing to TMS scaling bottlenecks.
3. **No Claim of Superiority:**
   - RI does not claim to outperform commercial LLM platforms in general reasoning, text fluency, or large-scale document synthesis.
   - RI specifically investigates a targeted capability gap: **auditable, dependency-aware belief maintenance under evolving, contradictory evidence.**

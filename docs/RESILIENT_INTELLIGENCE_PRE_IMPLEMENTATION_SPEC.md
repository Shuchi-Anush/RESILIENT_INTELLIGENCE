# RESILIENT INTELLIGENCE — PHASE 4 PRE-IMPLEMENTATION TECHNICAL SPECIFICATION

## 1. PROJECT IDENTITY — FROZEN
**Project:** RESILIENT INTELLIGENCE
**Subtitle:** Temporal Evidence Graph for Human-Centered Situation Awareness

**Core Problem:** How can humans maintain reliable situational understanding when reality continuously changes, information is incomplete or contradictory, and previous conclusions may need to be revised?

The system answers:
1. What do we know?
2. What do we currently believe?
3. What evidence supports that belief?
4. When did we learn it?
5. When was it valid?
6. What changed?
7. Why did our understanding change?
8. What evidence conflicts?
9. What is uncertain?
10. What should the human investigate further?

## 2. THREE FOUNDATIONAL PRINCIPLES — FROZEN
*   **IRON MAN:** Human augmentation. The system structures the chaos of evolving information so the human can comprehend it. The system never makes autonomous, consequential decisions.
*   **AMARAN:** Intelligence under evolving uncertainty. The system natively handles stale, conflicting, and changing information.
*   **FUTURE GENERATIONS:** Durable intelligence. The system preserves historical knowledge, provenance, and the exact reasoning state at any point in the past.

## 3. SEVEN HARD PROJECT CONSTRAINTS — FROZEN
1. 100% Feasible (One student, one laptop, ₹0)
2. 100% Production-Completable (Deployable, maintainable)
3. 100% VS Code / Local Implementable (Open source stack)
4. 5–6 Productive Months (Resilient to academic pauses)
5. Career Asset (Demonstrates real data/AI infrastructure skills)
6. Profile Gap-Filler (Adds temporal graphs, not just another cyber tool)
7. Ikigai Alignment (Valuable, interesting, and structurally necessary)

## 4. GRAPHIFY — FINAL REUSE ANALYSIS

| Module | Current Purpose | Dependencies | Domain Coupling | Decision | Integration Cost | Maint. Risk | Value to TEG |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Pipeline CLI** | Orchestrate steps | High (Click) | Low | **ADAPT** | Low | Low | High (Clean CLI framework) |
| **AST Extraction** | Parse code | Tree-sitter | High (Code) | **DROP** | N/A | N/A | None (We extract from text) |
| **Entity Model** | Static JSON node | NetworkX | Low | **REIMPLEMENT**| Med | Med | Low (Needs bi-temporal cols) |
| **Relation Model**| Static JSON edge | NetworkX | Low | **REIMPLEMENT**| Med | Med | Low (Needs bi-temporal cols) |
| **ID Normalization**| Content hashing | hashlib | Low | **ADAPT** | Low | Low | High (Ensures stable IDs) |
| **Dedup (LSH)** | Code similarity | Datasketch | High (Code) | **DROP** | N/A | N/A | None (Use entity resolution) |
| **Graph Build** | In-memory graph | NetworkX | Low | **REIMPLEMENT**| High | High | Low (Moving to SQLite) |
| **Clustering** | Leiden/Louvain | cdlib | Low | **DROP** | N/A | N/A | None (Overkill for MVP) |
| **Caching** | API cost saving | sqlite | Low | **REUSE** | Low | Low | High (Mandatory for ₹0 budget)|
| **Watch / Incr** | File monitoring | watchdog | Low | **ADAPT** | Med | Low | Med (Adapt to ingest queue) |
| **Reflection** | Memory decay | math | Low | **ADAPT** | Low | Low | High (Use math for confidence)|
| **LLM Sandbox** | Provider routing | requests | Low | **REUSE** | Low | Low | High (Free tier routing) |
| **Security** | SSRF limits | urllib | Low | **REUSE** | Low | Low | High (Production safety) |
| **MCP Server** | Agent tools | stdio/http | Low | **REUSE** | Low | Low | High (Agent extensibility) |
| **Reporting** | Markdown output | jinja2 | Low | **DROP** | N/A | N/A | None (We need a Web UI) |

## 5. TEG — CONCEPTUAL MODEL
The absolute minimum sufficient primitives required to answer the core questions.

*   **ENTITY:** (First-class Table). The who/what/where.
*   **EVIDENCE:** (First-class Table). The source text/document and its metadata.
*   **ASSERTION:** (First-class Table). A temporal relationship or attribute claim (Subject → Predicate → Object) backed by Evidence.
*   **TIME:** (Attribute). Bi-temporal bounds (`valid_time`, `transaction_time`) applied to Assertions.
*   *EVENT:* (Derived). An Assertion where the predicate implies a happening.
*   *STATE:* (Derived). The set of valid Assertions for an Entity at time $T$.
*   *SOURCE:* (Attribute). Metadata on the Evidence table.
*   *PROVENANCE:* (Derived). The relational link between Assertion and Evidence.
*   *CONFIDENCE:* (Derived). Python computation based on evidence decay and corroboration.
*   *CONTRADICTION:* (Derived). SQL query finding mutually exclusive Assertions valid at the same time.
*   *CHANGE:* (Derived). SQL diff between two transaction times.

## 6. BI-TEMPORAL SEMANTICS
*   **VALID TIME (`valid_from`, `valid_to`):** When the assertion was actually true in the real world.
*   **TRANSACTION TIME (`system_from`, `system_to`):** When RESILIENT INTELLIGENCE recorded this belief in the database.

**Example:**
*   Monday (8:00): Server crashes.
*   Wednesday (10:00): System ingests report saying "Server crashed on Monday".
*   Friday (12:00): System ingests report saying "Server actually crashed on Sunday, not Monday".

**Queries:**
*   **Current World State** (`system_to IS NULL AND valid_to IS NULL`): What is true right now according to our latest data?
*   **Historical World State** (`system_to IS NULL AND 'Monday' BETWEEN valid_from AND valid_to`): What was actually happening on Monday, based on everything we know *today*?
*   **Current Knowledge State** (`system_to IS NULL`): Everything we believe today.
*   **Historical Knowledge State** (`'Wednesday' BETWEEN system_from AND system_to`): What did the system believe on Wednesday? (Future Generations reconstruction).

## 7. EVIDENCE + PROVENANCE MODEL
*   **Evidence** is an immutable row representing raw data (e.g., a URL, a text snippet, an API payload) with an observation timestamp and a `Source` (e.g., "NYT", "Sensor X", "User Y").
*   An LLM or deterministic parser reads Evidence and generates **Candidate Assertions**.
*   These are written to the `Assertion` table. A linking table `Assertion_Evidence` maintains the **Provenance**.
*   A user inspects the evidence by clicking an assertion in the UI, which joins the linking table to display the original text and source reliability.
*   **Conflicting sources** are represented simply: Source A produces Evidence 1 → Assertion X. Source B produces Evidence 2 → Assertion NOT X. Both exist in the DB. The contradiction engine flags them.

## 8. CONFIDENCE MODEL
An interpretable, heuristic baseline. Not an ML model.

*   `Score (0.0 to 1.0) = Base_Reliability * Decay_Factor * Corroboration_Multiplier`
*   **Base Reliability:** Hardcoded mapping based on source type (e.g., Official API = 0.9, Social Media = 0.4, LLM Inference = 0.6).
*   **Decay Factor:** Exponential decay based on `valid_from` age.
*   **Corroboration:** 1.0 + (0.1 * supporting evidence count) - (0.2 * contradicting evidence count). Min clamped to 0.0, max 1.0.
*   **Explanation:** The UI displays exactly this math: "0.6 = 0.9 (API) * 0.8 (Age) * 0.83 (1 support, 1 conflict)".

## 9. CONTRADICTION MODEL
*   **Direct Contradiction:** Assertions with the same Subject and Predicate, but different Objects, overlapping in `valid_time`. (e.g., [Server A] -[status]-> [Online] AND [Server A] -[status]-> [Offline] at the same time).
*   **Temporal Non-Contradiction:** If the `valid_time` intervals do not overlap, it is NOT a contradiction, it is a state change.
*   **Implementation:** Handled via predefined "Mutually Exclusive Predicates" dictionary and SQL window functions. No theorem provers.

## 10. CHANGE INTELLIGENCE
"What Changed?" means returning a diff between `Current Knowledge State` and `Knowledge State at T-1`.
*MVP Includes:*
1. **Assertion Added** (We learned a new fact).
2. **Assertion Invalidated** (We learned a fact is no longer true; `valid_to` populated).
3. **Contradiction Appeared** (New evidence caused a conflict).
The UI explains: `[BEFORE: X] → [CHANGE: Y invalidated X] → [AFTER: Y] → [EVIDENCE: Report Z]`.

## 11. SITUATION MODEL
A Situation is simply a **user-defined temporal window and entity filter**.
It is not a complex ontology. It is a Saved Query.
Example: `Situation = {Entities: [Server A, Server B], Time_Window: 'Last 24h'}`.
The UI loads the current state, recent changes, contradictions, and evidence scoped entirely to that query.

## 12. DOMAIN-AGNOSTICITY TEST
The TEG primitives remain identical; only the data changes.

**Domain 1: Emergency Response**
*   **Entity:** `[Shelter: HighSchool]`
*   **Event:** `[Event: Flood_Warning]`
*   **Assertion:** `[Shelter: HighSchool] -[status]-> [At Capacity]`
*   **Contradiction:** API says At Capacity, Twitter says Empty.

**Domain 2: Supply Chain**
*   **Entity:** `[Factory: XYZ_Corp]`
*   **Event:** `[Event: Port_Strike]`
*   **Assertion:** `[Factory: XYZ_Corp] -[ships_to]-> [Warehouse A]`
*   **Contradiction:** ERP says Shipped, News says Port Closed.

**Domain 3: Cybersecurity**
*   **Entity:** `[IP: 192.168.1.5]`
*   **Event:** `[Event: Login_Attempt]`
*   **Assertion:** `[IP: 192.168.1.5] -[compromised]-> [True]`
*   **Contradiction:** SIEM says Compromised, EDR says Clean.

## 13. DOMAIN SELECTION — UNDECIDED
The domain is **UNDECIDED**. Below is the candidate matrix to be used for final selection during Phase 5.

| Domain | Data Avail | Laptop Feasible | Temporal Richness | Contradictions | Human Value | Reviewer Clarity | Total Score |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **A. Cybersecurity** | High (Public) | High | High | High | High | High | **54** |
| **B. Disaster Response** | Med | High | High | High | High | High | **50** |
| **C. Scientific Intel** | High (Papers) | High | Low | High | Med | Med | **44** |
| **D. Supply Chain** | Low (Private) | High | Med | Med | High | Med | **38** |

*Note: The architecture relies on none of these. A domain adapter script will map chosen domain data into generic TEG triples.*

## 14. PRODUCT BOUNDARY
The core product MVP is:
**TEG APPLICATION SERVICE (Python)** ↔ **REST API (FastAPI)** ↔ **WEB UI (HTML/JS)**

*   **Core Engine:** Mandatory. The logic layer over SQLite.
*   **REST API:** Mandatory. Feeds the UI.
*   **Web UI:** Mandatory. Iron Man requirement.
*   *MCP:* Optional extension.
*   *CLI:* Optional extension.
*   *LLM Adapter:* Optional extension (runs independently to feed the API).

## 15. MCP — OPTIONAL
MCP will expose `query_entity_state`, `get_contradictions`, and `get_evidence`. It allows an AI agent (like Claude Desktop) to read the TEG. It has high career value (modern AI tooling) and low cost (Graphify code reuse), but is strictly post-MVP.

## 16. LLM — OPTIONAL
**LLM = OPTIONAL INTELLIGENCE ACCELERATOR.**
The core engine only knows about JSON assertions and evidence text. If an LLM is available, an ingestion script uses it to parse raw text into JSON. If offline, a human types the JSON into a form. LLM output is never assumed to be truth; it is merely an extraction mechanism linked to the original evidence.

## 17. STORAGE DECISION
**A. SQLite + Relational Temporal Persistence + Python Graph Semantics layer.**
*   *Why not embedded graph DB?* Graph databases handle spatial (structural) traversal well, but temporal querying (bi-temporal joins) poorly. Relational databases handle temporal logic easily. We only need 1-hop or 2-hop traversals for situation awareness, which SQLite handles instantly via foreign keys or CTEs.
*   *Why not NetworkX?* Ephemeral. Future Generations requires persistent history.

## 18. API CONTRACT
Minimum surface:
*   `POST /ingest` (Accept raw text/JSON + source metadata)
*   `GET /situation/{id}` (Returns entities, changes, contradictions for a window)
*   `GET /entity/{id}/history` (Returns bi-temporal state changes)
*   `GET /assertion/{id}/evidence` (Returns provenance chain)
*   `GET /contradictions` (Returns active conflicts)

## 19. FRONTEND CONTRACT
A simple Single Page Application answering: "What is happening, and why?"
*   **Left Panel:** Situation Feed (Timeline of new assertions, changes, and contradictions).
*   **Main View:** Entity Detail (Current state + confidence scores).
*   **Right Panel:** Evidence Inspector (Click an assertion to see the raw text and source reliability that generated it).
*   *Graph Visualization:* Optional. Only build if data is highly connected.

## 20. SECURITY BOUNDARY
*   **Untrusted URLs:** Graphify SSRF protection on ingestion.
*   **LLM Validation:** Pydantic strict parsing; drop malformed JSON, never execute it.
*   **SQL Injection:** SQLAlchemy / parameterized queries.
*   **Auth:** Hardcoded `user_id=1`. No multi-tenant complexity for MVP.

## 21. OBSERVABILITY
*   **Logs:** JSON structured logs to stdout.
*   **Metrics:** Simple `/health` endpoint and ingestion failure counter.
*   *No Prometheus/Grafana.* Too heavy for MVP.

## 22. DEPLOYMENT
*   **Local Operation:** `docker-compose up` (FastAPI + SQLite + Static Nginx).
*   **Live Demo:** Backend to Render (Free Web Service + Persistent Disk). Frontend to Vercel (Free).

## 23. TESTING
*   **Unit Tests:** Confidence math, contradiction detection logic.
*   **Temporal Tests:** Insert Fact at T1, Update at T2, Query at T1.5 (Must return original state).
*   **Fixtures:** A deterministically seeded SQLite file representing a 3-day incident timeline.

## 24. EVALUATION
*   **Change Detection Accuracy:** 100% (It is deterministic SQL, not ML).
*   **Extraction Precision/Recall:** (If LLM used) Evaluate LLM triples vs human-labeled ground truth for the demo dataset.
*   **Query Latency:** Time to return situation state < 500ms.
*   **Human Evaluation:** Time to correctly identify a contradiction in a 10-report dataset (TEG UI vs raw text reading).

## 25. PRE-MORTEM (20 Failure Modes)
| # | Failure Mode | Prob | Impact | Mitigation |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Graphify entanglement | Med | Fatal | Extract specific files; do not fork repo. |
| 2 | TEG SQL complexity | High | High | Use views for temporal overlaps. Limit time travel scope. |
| 3 | Domain hardcoding | Low | High | Use generic schema; enforce domain via external JSON config. |
| 4 | Frontend time-sink | High | High | Use vanilla JS/Tailwind or basic React template. No state mgmt. |
| 5 | LLM extraction failure | High | Med | Fallback to manual JSON ingestion. |
| 6 | Data unavailability | Med | High | Select domain only after finding a usable public dataset. |
| 7 | Insufficient novelty | Low | Med | Bi-temporal SQLite + Confidence math is novel for a student project. |
| 8 | Reviewer rejection | Low | Fatal | Focus demo strictly on Iron Man utility (showing evidence). |
| 9 | Deployment failure | Med | Med | Keep SQLite local if cloud persistence fails; record a demo video. |
| 10 | Maintenance failure | Low | Low | Zero dependencies outside Python stdlib + FastAPI. |
| 11 | Academic pauses | High | Med | Build API MVP first. Frontend is modular addition. |
| 12 | Solo dev workload | High | Fatal | Strictly enforce the Scope Blacklist. |
| 13 | Contradiction math fails | Med | Med | Use simple mutual-exclusion lists, not semantic similarity. |
| 14 | Graph traversal too slow | Low | Low | SQLite is fast enough for laptop-scale data (~10k nodes). |
| 15 | LLM API cost | Low | Low | Use Ollama or cache aggressively (Graphify cache reuse). |
| 16 | Provenance UI confusing | High | Med | Keep it simple: click assertion -> show raw text popup. |
| 17 | Timezone bugs | High | Med | Force UTC everywhere at the API boundary. |
| 18 | Scope creep (predictive) | High | Fatal | Reject all requests to forecast the future. |
| 19 | Oversized inputs | Med | Low | Truncate evidence text to 5000 chars before DB insertion. |
| 20 | Graph viz is a mess | High | Med | Drop graph viz. A tabular timeline is often better for situations. |

## 26. SCOPE BLACKLIST
*   DO NOT build a custom graph database.
*   DO NOT build multi-user authentication.
*   DO NOT build real-time streaming (Kafka/etc).
*   DO NOT build autonomous decision agents.
*   DO NOT build military command/control features.
*   DO NOT build predictive AI or forecasting.
*   DO NOT write VS Code / AGY extensions.
*   DO NOT hard-code a specific domain ontology into the SQL schema.

## 27. PROFILE GAP ANALYSIS
This project adds distinct value beyond the developer's existing cloud/security/blockchain portfolio:
*   **Temporal Data Modeling:** Implementing bi-temporal semantics in SQL.
*   **Knowledge Representation:** Moving from ML pipelines to explicit evidence-aware symbolic reasoning.
*   **Human-Centered Design:** Building explainable intelligence UIs rather than black-box security tools.

## 28. FINAL TECHNICAL SPECIFICATION
*   **A. Core Abstractions:** Entity, Assertion, Evidence.
*   **B. Temporal Semantics:** `valid_time` (world state) and `transaction_time` (system state).
*   **C. Evidence Model:** Immutable raw data + metadata + source.
*   **D. Provenance Model:** Linking table (`Assertion_Evidence`).
*   **E. Confidence Model:** `Base * Decay * Corroboration`.
*   **F. Contradiction Model:** SQL overlap on mutually exclusive predicates.
*   **G. Change Model:** SQL diff between transaction timestamps.
*   **H. Situation Model:** Temporal window + entity filter query.
*   **I. Storage Model:** SQLite3.
*   **J. Query Model:** SQLAlchemy ORM / Raw SQL for CTEs.
*   **K. API Model:** FastAPI REST JSON.
*   **L. Frontend Boundary:** HTML/JS SPA fetching from API.
*   **M. LLM Boundary:** External script producing JSON for the API.
*   **N. MCP Boundary:** Optional FastMCP server reading the SQLite DB.
*   **O. Domain-adapter Boundary:** JSON mapping files (e.g., `cyber_ontology.json`).
*   **P. Security Boundary:** SSRF protection, Pydantic validation, parameterized queries.
*   **Q. Observability:** Python `logging` module to stdout.
*   **R. Testing:** `pytest` with deterministic SQLite fixtures.
*   **S. Deployment:** Render (API) + Vercel (UI) or local Docker Compose.
*   **T. Evaluation:** Extraction P/R, query latency, qualitative human UI testing.

## 29. FINAL REVIEWER DEFENSE
*   **What is your project?** A temporal knowledge graph engine for tracking evolving situations.
*   **What problem are you solving?** Static databases and LLMs fail to handle contradictory, stale, and evolving intelligence during high-stakes events.
*   **Why a temporal graph?** Because reality changes, and we need to link entities across time.
*   **Why evidence?** So humans can verify claims instead of trusting an AI black-box.
*   **Why not a graph database?** Temporal querying (bi-temporal joins) is easier in relational SQL, and SQLite requires zero infrastructure.
*   **Why not RAG?** RAG retrieves text. TEG tracks changing entity states and explicit contradictions.
*   **How does it know something changed?** It compares the database state at Transaction Time $T1$ vs $T2$.
*   **What did you reuse?** Graphify's LLM sandbox, caching, security limits, and MCP framework.
*   **What is your contribution?** The entire bi-temporal schema, confidence math, contradiction logic, and human UI.
*   **Why domain-agnostic?** Because the problem of "evolving uncertainty" applies equally to supply chains, disasters, and cyber attacks.

## 30. FINAL DECISION GATE

**PROJECT:** RESILIENT INTELLIGENCE
**CORE:** Temporal Evidence Graph (Bi-temporal SQLite)
**DOMAIN:** UNDECIDED (Validation scenario to be selected)
**MVP:** SQLite DB + FastAPI + Vanilla JS Dashboard + LLM extraction script.
**EXTENSIONS:** MCP Server integration.
**GRAPHIFY:** Reuse specific files (LLM/Cache/Security/MCP), drop the rest.
**PRODUCT:** Web Application + API.
**DEPLOYMENT:** Render + Vercel / Local Docker Compose.
**REVIEW PLAN:** 6-stage dependency-aware progression.
**EVALUATION:** Extraction P/R, Query latency, UI qualitative test.
**SCOPE BLACKLIST:** No auth, no streaming, no predictive AI, no autonomous actions.

**FINAL VERDICT:**
**PROCEED**

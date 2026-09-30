# RESILIENT INTELLIGENCE — PHASE 3 ARCHITECTURE & IMPLEMENTATION PLAN

## 1. ABSOLUTE PROJECT IDENTITY
**Project:** RESILIENT INTELLIGENCE
**Working Subtitle:** Temporal Evidence Graph for Human-Centered Situation Awareness

**The Core Problem:** How can a human maintain reliable situational understanding when reality is continuously changing, information is incomplete or contradictory, and previous conclusions may need to be revised?

RESILIENT INTELLIGENCE is a **domain-agnostic intelligence engine**. It is not a SIEM, a chatbot, or a static knowledge graph. It is a system for tracking evolving situations by answering: *What do we believe now, what did we know then, what evidence supports it, and why did our understanding change?*

## 2. THE THREE FOUNDATIONAL INSPIRATIONS
*   **IRON MAN (Human Augmentation):** The system does not make autonomous decisions. It augments humans by untangling complex, conflicting information timelines into clear visual graphs and evidence chains.
*   **AMARAN (Intelligence Under Uncertainty):** The system natively expects information to be stale, conflicting, or wrong. It handles high-stakes evolving environments (like disasters or cyber attacks) by tracking confidence and explicitly surfacing contradictions.
*   **FUTURE GENERATIONS (Durable Intelligence):** The system never overwrites history. It maintains an immutable, bi-temporal ledger so future analysts can rewind the clock and reconstruct exactly why the system believed what it did at time $T$.

## 3. THE SEVEN HARD PROJECT CONSTRAINTS
Every architectural decision below passes the following tests:
1. **100% Feasible:** One student, one laptop, zero cost.
2. **100% Production-Completable:** Reaches a deployed, maintainable state.
3. **100% VS Code / Local Implementable:** Open-source stack.
4. **5–6 Productive Months:** Resilient to academic interruptions.
5. **Career Asset:** Demonstrates serious backend, data engineering, and AI infrastructure skills.
6. **Profile Gap-Filler:** Adds temporal data modeling and knowledge graphs to the developer's portfolio.
7. **Ikigai Alignment:** High-impact, technically interesting, and structurally necessary.

## 4. GRAPHIFY'S ROLE
Graphify is a fantastic engineering foundation, but its core data model (static, in-memory NetworkX) is incompatible with evolving temporal knowledge.

| Subsystem | Action | Rationale |
| :--- | :--- | :--- |
| **Pipeline Orchestration** | ADAPT | The CLI pipeline structure is good, but the stages will change. |
| **Extraction (AST)** | DROP | We need NLP/LLM extraction, not code parsing. |
| **Entity / Relation Model** | REIMPLEMENT | Must support bi-temporal validity and evidence links. |
| **ID Normalization** | ADAPT | Content hashing is useful, but entities now merge/split over time. |
| **Graph Construction** | REIMPLEMENT | Move from in-memory NetworkX to persistent SQLite. |
| **Caching** | REUSE | Content-hash caching saves LLM API costs. |
| **Reflection / Memory** | ADAPT | The math (time decay) is perfect for evidence freshness. |
| **LLM Abstraction** | REUSE | Multi-backend sandbox is production-ready. |
| **Security** | REUSE | SSRF prevention and sandboxing are critical. |
| **MCP Server** | REUSE | Excellent adapter for integrating with AI agents later. |
| **Reporting** | DROP | Static Markdown reports fail the Iron Man test; we need a UI. |

## 5. CRITICAL ARCHITECTURAL HYPOTHESIS
**Verdict:** Attempting to build Resilient Intelligence *on top of* Graphify's structural knowledge graph is technically incoherent.
Graphify expects to overwrite its graph on every run. Resilient Intelligence expects to append evidence and track state over time.
**The correct evolution:** Extract Graphify's utility modules (LLM, Cache, Security, MCP) and build a **new TEG core layer** using SQLite.

## 6. TEMPORAL EVIDENCE GRAPH (TEG)
The minimum sufficient model required to answer the system's core questions without introducing unnecessary complexity.

**First-Class Primitives (Database Tables):**
1. **Entity:** `(id, type, created_at)` — The persistent concepts (e.g., "Server X", "Hurricane Y").
2. **Evidence:** `(id, source_uri, content, reliability, ingested_at, observation_time)` — The immutable raw data.
3. **Assertion (Relationship/State):** `(id, subject, predicate, object, valid_from, valid_to, evidence_id)` — The temporal claims made by evidence.

**Derived Concepts (Queries/Code, NOT Tables):**
*   **Event:** An Assertion where the predicate implies action (e.g., "ATTACKED").
*   **State:** The set of Assertions for an Entity at time $T$.
*   **Provenance:** The `evidence_id` foreign key link.
*   **Contradiction:** An SQL query finding active Assertions with the same subject/predicate but mutually exclusive objects.
*   **Confidence:** A Python function computing strength based on Evidence count, reliability, and freshness.
*   **Change:** A SQL diff between two points in `transaction_time`.

## 7. DOMAIN-AGNOSTICITY IS MANDATORY
The schema contains zero cybersecurity-specific tables.
Instead of an `ip_address` table, there is an `Entity` where `type = 'ip_address'`.
Instead of a `malware_infection` table, there is an `Assertion` where `predicate = 'infected_by'`.
This guarantees the engine can be used for supply chain, disaster response, or scientific research by simply changing the domain ontology mapping.

## 8. DEMONSTRATION DOMAIN SELECTION
We must pick *one* domain for the MVP validation scenario.

| Domain | Data Avail | Temporal Dyn | Contradiction | Reviewer Clarity | Score (1-10) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A. Cybersecurity (Incident Response)** | High (Public reports) | High | High (Fog of war) | High (Hacks are understood) | **9.5** |
| B. Disaster Response | Med | High | High | High | 7.5 |
| C. Supply Chain | Low (Proprietary) | Med | Med | Med | 5.0 |
| D. Scientific Intelligence | High (Papers) | Low (Slow) | High | Low (Domain specific) | 6.5 |

**Selected Primary Demonstration Domain: Cybersecurity Incident Response.**
*Why:* It offers the best combination of high-stakes temporal dynamics, clear contradictions (e.g., initial alert vs. forensic reality), and publicly available structured timelines (e.g., MITRE ATT&CK case studies) for testing, while being perfectly understood by technical reviewers.

## 9. HUMAN-AUGMENTATION MODEL
The interaction loop:
1. `DATA` → 2. `EVIDENCE` → 3. `TEG (STRUCTURED)` → 4. `CHANGE/CONFLICT DETECTION` → 5. `EXPLANATION` → 6. `HUMAN DECISION`.
The system will never say "Server X is infected. Shutting it down."
It will say: "Confidence in Server X infection is 85%. Support: 2 logs. Contradict: 1 scan. View evidence timeline."

## 10. EVIDENCE-FIRST MODEL
The fundamental rule: **No assertion exists without evidence.**
If an LLM hallucinates, the hallucination is tied to the LLM as the `Source`. The human can inspect the Evidence, see its Source reliability, and invalidate the Assertion if necessary. The system tracks both *observation time* (when it happened) and *ingestion time* (when we learned it).

## 11. LLM ROLE
**Verdict: OPTIONAL INTELLIGENCE ACCELERATOR.**
The core TEG engine takes JSON triples as input.
The LLM is merely an *adapter* that sits at the edge of the system, taking raw PDFs or text reports and converting them into JSON triples for the engine.
If the LLM is offline or too expensive, a human can submit JSON manually. The system remains 100% operational.

## 12. PRODUCT FORM
**Core MVP Boundary:**
1. **TEG Engine (Python API):** The brain.
2. **REST API (FastAPI):** Exposes the engine over HTTP.
3. **Web Dashboard (HTML/JS):** The human Iron Man interface (timeline, confidence, contradictions).

**Optional / Extensions:**
4. **CLI:** Good for debugging ingestion.
5. **MCP Server:** High career value, easy Graphify reuse, allows LLMs to query the TEG.

## 13. STORAGE ARCHITECTURE
**Verdict: SQLite + Relational Temporal Persistence + Python Graph Layer.**
*   *Why not Neo4j?* Violates zero-cost, laptop-only constraint. Hard to deploy.
*   *Why not NetworkX?* In-memory only. Erases history on exit. Cannot do `valid_from` SQL queries easily.
*   *Why SQLite?* It is a single file, easily deployed, lightning-fast for the data volumes a single user encounters, and handles bi-temporal querying (`WHERE valid_from < ? AND valid_to > ?`) effortlessly. Graph traversals (multi-hop) can be handled by Recursive CTEs in SQL or by loading subsets into Python.

## 14. CONFIDENCE MODEL
**Verdict: Heuristic Scoring with Explicit Explanation.**
We will not use complex Bayesian networks (too hard to explain/tune).
We use an interpretable heuristic:
`Confidence = Base Source Reliability * (1 - Decay Rate * Age) * (Corroborating Evidence Count) / (Contradicting Evidence Count)`
The UI must show the math visually: "+ 2 Sources, - 1 Contradiction, - 10% Stale".

## 15. CHANGE INTELLIGENCE
The system focuses entirely on "What changed?" The MVP will track:
1. **New Assertions:** New facts added to the graph.
2. **Invalidated Assertions:** Facts where `valid_to` was updated.
3. **Contradictions:** A new assertion directly opposes a currently active assertion.
These three are sufficient to create a highly dynamic "Situation Update" feed.

## 16. FUTURE-GENERATIONS / INSTITUTIONAL MEMORY
Achieved naturally by the bi-temporal SQLite schema. Because we never `DELETE` or `UPDATE` a fact's existence (we only update its `valid_to` column or add new rows), the database is an append-only ledger.
To see what the system believed last Tuesday, we simply run:
`SELECT * FROM assertions WHERE ingested_at <= 'LAST_TUESDAY' AND valid_from <= 'LAST_TUESDAY' AND (valid_to > 'LAST_TUESDAY' OR valid_to IS NULL)`.

## 17. GRAPHIFY + TEG ARCHITECTURAL DECISION
**Verdict: C. Graphify modules extracted selectively + independent core.**
We will create a clean Python project. We will copy over Graphify's `llm/` (sandbox), `cache/`, `security.py`, and `server/` (MCP) directories. We will discard the rest and write the TEG SQLite core from scratch. This guarantees absolute understanding of the core logic while saving weeks of boilerplate API work.

## 18. PRODUCTION ARCHITECTURE
```text
[ Web UI (Vanilla JS/HTML) ]  <-- (JSON) -->  [ MCP Client (e.g. Claude) ]
             |                                       |
    [ REST API (FastAPI) ]                [ MCP Server (Graphify port) ]
             \                                       /
              \-> [ TEG Core Engine (Python) ] <----/
                      | (Confidence, Change, Contradiction logic)
                      |
                [ SQLite DB ] (Entities, Evidence, Assertions)
```

## 19. DEPLOYMENT
*   **Database & Backend:** Python FastAPI deployed to Render (Free Tier). SQLite file stored on persistent disk (or local if cloud persistence is tricky on free tiers).
*   **Frontend:** Static files deployed to Vercel or GitHub Pages (Zero Cost).
*   **LLM:** External API (Gemini/OpenAI free tiers) handled securely via backend environment variables.

## 20. SECURITY
The minimum production boundary:
*   **LLM Output Validation:** Strict Pydantic parsing of all LLM outputs before DB insertion.
*   **SSRF Protection:** Reuse Graphify's URL fetcher limits for ingestion.
*   **SQL Injection:** Use ORM/Parameterized queries exclusively.
*   **Auth:** Hardcode single-user mode (`user_id = 1`) for MVP to prevent scope explosion.

## 21. OBSERVABILITY
*   Structured JSON logging for API requests.
*   A specific log stream for "Ingestion Failures" (when LLMs fail to parse a document).
*   A `/health` endpoint for uptime monitoring.

## 22. REVIEWER SURVIVAL
*   **Why not RAG?** RAG retrieves raw text. It doesn't know if text A contradicts text B, or if text C is outdated. TEG tracks state and contradiction explicitly.
*   **Why SQLite and not Neo4j?** SQLite handles bi-temporal indexing perfectly and fits the zero-cost, edge-deployable requirement of the project. Multi-hop queries are handled via CTEs.
*   **What did YOU build?** The entire temporal schema, the confidence engine, the contradiction detection logic, and the user-facing situation dashboard.

## 23. SIX REVIEW / 5–6 MONTH DEVELOPMENT PLAN
*   **REVIEW 1 (Month 1):** Architecture spec, SQLite schema finalized, Graphify modules extracted.
*   **REVIEW 2 (Month 2):** TEG Core API built. Manual ingestion of JSON triples works. Time travel queries work.
*   **REVIEW 3 (Month 3):** LLM Ingestion Pipeline. Can feed it a raw cybersecurity report and get structured triples in the DB.
*   **REVIEW 4 (Month 4):** Intelligence Layer. Confidence math and Contradiction detection queries implemented.
*   **REVIEW 5 (Month 5):** Web Dashboard built. Visual timeline of an evolving incident.
*   **REVIEW 6 (Month 6):** Complete validation scenario, thesis writing, live deployment.

## 24. EVALUATION
*   **Extraction Correctness:** Precision/Recall of LLM extracting entities vs a manually labeled gold-standard incident report.
*   **Query Latency:** Time to execute a `WHAT CHANGED` query on a 10,000-edge graph.
*   **Human Effectiveness:** A/B test (even if just self-evaluated): Time taken to identify the root cause of an incident using raw text reports vs. using the TEG dashboard.

## 25. PRE-MORTEM (Top 5 Critical Risks)
1.  **Frontend Time Sink:** (Prob: High) Building a complex React app drains 2 months. *Mitigation:* Use vanilla JS/HTML and a simple CSS framework like Tailwind.
2.  **LLM Extraction Flakes:** (Prob: High) LLMs output bad JSON. *Mitigation:* Pydantic retry loops. If it fails 3 times, store as raw evidence for manual review.
3.  **Temporal SQL Complexity:** (Prob: Med) Queries become unreadable. *Mitigation:* Write clean Python repository layers to encapsulate the ugly SQL.
4.  **Domain Scope Creep:** (Prob: High) Trying to make it work for cyber *and* medical *and* supply chain for the demo. *Mitigation:* Stick strictly to one cyber incident for the demo.
5.  **Academic Interruption:** (Prob: High) Exams halt work. *Mitigation:* The backend API is a valid MVP on its own if the frontend isn't finished.

## 26. WHAT MUST NOT BE BUILT (Blacklist)
*   Autonomous decision-making or command-execution agents.
*   A custom graph database.
*   Multi-user authentication / Enterprise RBAC.
*   Predictive AI / Forecasting models.
*   Real-time streaming (Kafka/RabbitMQ).
*   VS Code / IDE Extensions.

## 27. PROFILE GAP ANALYSIS
This project definitively avoids duplicating the developer's past work (IDS, Zero-Trust, Blockchains). It establishes a new technical identity in:
*   **Knowledge Representation:** Modeling time and evidence.
*   **Human-Centered AI:** Building systems that explain themselves rather than acting autonomously.
*   **Production Information Systems:** Moving from analytical scripts to a deployed API+UI platform.

## 28. FINAL ARCHITECTURAL DECISION (EXACT OUTPUTS)
*   **A. EXACT PROJECT DEFINITION:** A domain-agnostic intelligence engine that tracks evolving situations, evidence, and confidence over time.
*   **B. EXACT PROBLEM STATEMENT:** Static intelligence systems fail when information is changing, contradictory, or incomplete.
*   **C. EXACT CORE CONTRIBUTION:** A local-first, zero-cost bi-temporal evidence graph implementation with human-centered contradiction detection.
*   **D. EXACT MVP:** SQLite DB + Python FastAPI + Vanilla JS Web Dashboard + LLM extraction script.
*   **E. EXACT EXTENSIONS:** MCP Server integration.
*   **F. EXACT GRAPHIFY REUSE STRATEGY:** Extract LLM sandbox, Caching, Security, and MCP modules. Discard the rest.
*   **G. EXACT TEG MODEL:** 4 Tables (Entities, Evidence, Assertions, Evidence_Assertion_Links) with bi-temporal columns.
*   **H. EXACT PRODUCT INTERFACE:** A web dashboard showing a situation timeline and confidence scores.
*   **I. EXACT DEMONSTRATION DOMAIN:** Cybersecurity Incident Response (as a validation scenario, not hardcoded ontology).
*   **J. EXACT DEPLOYMENT MODEL:** Render (Backend API) + Vercel (Static UI) + local SQLite.
*   **K. EXACT SIX-REVIEW PLAN:** See Section 23.
*   **L. EXACT EVALUATION PLAN:** Precision/Recall for extraction, latency for graph queries.
*   **M. EXACT SCOPE BLACKLIST:** No multi-user, no predictive AI, no custom DBs, no autonomous actions.

## 29. CRITICAL FINAL TEST
*Can ONE STUDENT understand, build, deploy, operate, maintain, explain, evaluate, and defend this in 5-6 months?*
**YES.** By stripping away NetworkX, clustering algorithms, multi-user auth, and real-time streaming, the core system is just a sophisticated CRUD application over a clever SQLite schema, powered by an LLM adapter. It perfectly embodies Iron Man (explanation), Amaran (contradiction handling), and Future Generations (immutable history).

## FINAL VERDICT
**PROCEED**
*End of Architecture Phase.*

# RESILIENT INTELLIGENCE — PHILOSOPHY → ENGINEERING TRACEABILITY SPECIFICATION

## 1. PROJECT IDENTITY — FROZEN
**PROJECT:** RESILIENT INTELLIGENCE
**SUBTITLE:** Temporal Evidence Graph for Human-Centered Situation Awareness

**Core Problem:** How can humans maintain reliable situational understanding when reality continuously changes, information is incomplete or contradictory, and previous conclusions may need to be revised?

**The System Answers:**
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

---

## 2. THE THREE PRINCIPLES AS ENGINEERING AXIOMS

### IRON MAN (Human Augmentation)
**Principle:** Technology should augment human intelligence rather than automate isolated tasks. Reduce cognitive burden.
**Engineering Requirements:**
*   **IR-01:** The UI must surface the current situation without requiring the user to inspect every raw evidence item first.
*   **IR-02:** Every important assertion must be drillable to its evidence.
*   **IR-03:** The system must explicitly expose meaningful changes.
*   **IR-04:** The system must expose contradictions rather than hiding them.
*   **IR-05:** The system must expose confidence/uncertainty in interpretable form.
*   **IR-06:** The user must be able to reconstruct why the system presents a particular situation state.
*   **IR-07:** The system must assist human judgment rather than autonomously make consequential decisions.
*   **IR-08:** The interface must prioritize INFORMATION VALUE over visual complexity.

### AMARAN (Intelligence Under Evolving Uncertainty)
**Principle:** The world is not static; information arrives late, conflicts, or becomes stale. The system must model evolving knowledge.
**Engineering Requirements:**
*   **AR-01:** Assertions must have explicit temporal semantics.
*   **AR-02:** The system must distinguish VALID TIME from TRANSACTION TIME.
*   **AR-03:** The system must preserve previous system knowledge.
*   **AR-04:** The system must detect meaningful contradictions.
*   **AR-05:** The system must distinguish contradiction from legitimate state change across non-overlapping time intervals.
*   **AR-06:** The system must represent uncertainty/confidence explicitly.
*   **AR-07:** New evidence must be able to change the current assessment.
*   **AR-08:** The system must be able to answer "What changed?"
*   **AR-09:** The system must not silently overwrite historical knowledge.
*   **AR-10:** The system must not assume the latest piece of information is automatically correct.

### FUTURE GENERATIONS (Durable / Reconstructable Intelligence)
**Principle:** Intelligence must remain understandable even after situations or assumptions change. Preserve the reasoning trail.
**Engineering Requirements:**
*   **FG-01:** Evidence must remain traceable.
*   **FG-02:** Provenance must remain reconstructable.
*   **FG-03:** Historical system knowledge must remain queryable.
*   **FG-04:** Previous assessments must not disappear when new evidence arrives.
*   **FG-05:** The system must preserve the relationship between assertions and the evidence that produced them.
*   **FG-06:** The system must distinguish: "What was true in the modeled world?" from "What did the system believe at that time?"
*   **FG-07:** A future user must be able to reconstruct: WHAT WAS KNOWN, WHY, WHEN, WHAT EVIDENCE SUPPORTED IT, WHAT EVIDENCE CONTRADICTED IT, WHAT CHANGED.
*   **FG-08:** Historical reconstruction must not depend on the current state alone.

---

## 3. TRACEABILITY TO THE TEG

| Requirement Category | TEG Primitive | Implementation Mechanism | User-Visible Effect | Evaluation Method |
| :--- | :--- | :--- | :--- | :--- |
| **IRON MAN** | Evidence | Read-only raw data table | "View Source" button in UI | Time to trace claim to source |
| **IRON MAN** | Assertion | Subject-Pred-Object triplet | Entity state panel | Task completion time (comprehension) |
| **IRON MAN** | Situation | Query filtering active assertions | Dashboard overview | User comprehension of current state |
| **IRON MAN** | Change | Diff query between states | Notification feed | Time to identify important change |
| **IRON MAN** | Provenance | `Assertion_Evidence` mapping | Drill-down modal | Traceability test |
| **AMARAN** | Valid Time | `valid_from`, `valid_to` bounds | Timeline visualization | Temporal query correctness |
| **AMARAN** | Transaction Time | `system_from`, `system_to` bounds | "System Knowledge as of X" | Temporal query correctness |
| **AMARAN** | Contradiction | Mutually exclusive predicate SQL | Red alert badges in UI | Precision/Recall of contradictions |
| **AMARAN** | Confidence | Decay & Corroboration formula | 0-100% score bars | Calibration / Expert alignment |
| **FUTURE GEN**| Transaction Time | Append-only DB updates | Time-travel slider | Historical reconstruction accuracy |
| **FUTURE GEN**| Evidence | Immutable payload storage | Evidence is never deleted | Reproducibility of past state |

---

## 4. TRACEABILITY TO THE FROZEN DATA MODEL

*   **ENTITY:** (All 3). The core subject of intelligence.
*   **EVIDENCE:** (Iron Man, Future Generations). Provides the human proof (Iron Man) and ensures the historical trail is permanent (Future Gen).
*   **ASSERTION:** (Iron Man, Amaran). Structures chaos into readable facts (Iron Man) and is the unit that gets contested over time (Amaran).
*   **VALID TIME:** (Amaran). Models the evolving reality of the outside world.
*   **TRANSACTION TIME:** (Amaran, Future Gen). Preserves evolution of system knowledge (Amaran) and allows historical knowledge reconstruction (Future Gen).
*   **PROVENANCE:** (Iron Man, Future Gen). Allows the human to trust the system today (Iron Man) and reconstruct reasoning tomorrow (Future Gen).
*   **CONFIDENCE:** (Iron Man, Amaran). Explicitly exposes uncertainty to the user (Iron Man) because reality is conflicting (Amaran).
*   **CONTRADICTION:** (Iron Man, Amaran). Surfaces human-critical conflicts (Iron Man) caused by imperfect reporting (Amaran).
*   **CHANGE:** (Iron Man, Amaran). Highlights what the human must pay attention to (Iron Man) as reality evolves (Amaran).
*   **SITUATION:** (Iron Man). Filters the noise of the database into a cognitively digestible human view.

---

## 5. HUMAN WORKFLOW — IRON MAN
**USER ACTION → SYSTEM RESPONSE → INFORMATION GAIN**
1. Open a situation → Dashboard loads current state → High-level awareness.
2. See important recent changes → Notification feed highlights "Added/Invalidated" → Immediate focus on updates.
3. See contradictions → Red alert on Entity X → Recognition of disputed facts.
4. Select an assertion → UI highlights confidence score → Grasp of uncertainty.
5. Inspect supporting evidence → Provenance pane shows Source A text → Trust via verification.
6. Inspect contradicting evidence → Provenance pane shows Source B text → Understanding of the conflict.
7. Inspect temporal history → Timeline shows when state flipped → Contextualizing the change.

---

## 6. EVOLVING SITUATION WORKFLOW — AMARAN (Generic Domain)
*   **Day 1 (State 1):** Evidence A (Sensor) arrives. `Assertion 1: Pipeline Pressure is High`. Confidence: 80%.
*   **Day 2 (Evolving):** Evidence B (Field Report) arrives. `Assertion 2: Pipeline Valve is Broken`.
*   **Day 3 (Contradiction):** Evidence C (Drone) arrives. `Assertion 3: Pipeline Pressure is Normal`. System flags CONTRADICTION between A1 and A3. Confidence of both drops.
*   **Day 4 (Revised Understanding):** Evidence D (Engineer Log) arrives. Invalidates A1 (Sensor was faulty). Contradiction resolves. Assessment changes safely. System records exactly when this was realized (Transaction Time).

---

## 7. HISTORICAL RECONSTRUCTION WORKFLOW — FUTURE GENERATIONS
*   **T1:** System believes Entity X is Safe. (Assertion S).
*   **T2:** System ingests Evidence E1. Creates Assertion D (Entity X is Dangerous).
*   **T3:** System ingests Evidence E2. Invalidates Evidence E1 as fraudulent. Assertion D is invalidated.
*   **T4:** A user queries: "What did we believe at T2?"
*   *Result:* The query uses `WHERE T2 BETWEEN system_from AND system_to`. It returns Assertion D, even though at T4 we know it's false. The system perfectly reconstructs the flawed knowledge state at T2.

---

## 8. THE THREE-QUESTION TEST & FEATURE MATRIX
1. **Iron Man:** Does this make the human better at understanding the situation?
2. **Amaran:** Does this help represent changing/uncertain reality?
3. **Future Generations:** Does this preserve info to reconstruct evolution?

| Feature | Iron Man | Amaran | Future Gen | Primary Value | Decision |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Evidence Store** | Yes (Trust) | No | Yes (History) | Verifiable truth | **KEEP** |
| **Transaction Time** | Yes (Why) | Yes (Evolving) | Yes (Reconstruct)| Time travel | **KEEP** |
| **NetworkX Graph** | No | No | No | Spatial query | **DROP** |
| **Contradiction Alert**| Yes (Focus) | Yes (Conflict)| No | Conflict mgmt | **KEEP** |
| **Predictive AI** | Maybe | No (Guesses) | No | Forecasting | **DROP** |
| **Confidence Score** | Yes (Context) | Yes (Uncertain)| No | Transparency | **KEEP** |

---

## 9. PRODUCT EXPERIENCE
A HUMAN-CENTERED SITUATIONAL INTELLIGENCE INTERFACE.
*Not a database admin tool. Not a generic dashboard.*
The central UI answers: **"What is happening, what changed, why, and what evidence supports our current understanding?"**
Minimum required UI:
1. Split-pane layout.
2. Master list of entities/assertions (The "What is happening").
3. Activity feed of changes/contradictions (The "What changed").
4. Slide-out evidence inspector (The "Why/Evidence").

---

## 10. UI TRACEABILITY
*   **Situation Overview Panel:** Iron Man (Reduces cognitive load).
*   **Change Timeline Feed:** Amaran (Displays evolving information).
*   **Evidence Inspector Pane:** Iron Man + Future Gen (Drill-down to verifiable truth).
*   **Contradiction Badges:** Amaran (Highlighting conflicting reality).
*   **Confidence Meters:** Iron Man + Amaran (Visualizing uncertainty).
*   **Time-Travel Toggle:** Future Generations (Querying the past).

---

## 11. API TRACEABILITY
*   `POST /ingest`: (Amaran). Feeds new, potentially conflicting reality into the evolving model.
*   `GET /situation/{id}`: (Iron Man). Returns the structured current state. Tested via JSON schema validation.
*   `GET /entity/{id}/history`: (Future Gen). Returns bi-temporal history. Tested via point-in-time SQL queries.
*   `GET /assertion/{id}/evidence`: (Iron Man). Exposes provenance. Tested by joining `Assertion_Evidence` to `Evidence`.
*   `GET /contradictions`: (Amaran). Returns mutually exclusive overlapping facts.

---

## 12. ALGORITHM TRACEABILITY
*   **Temporal Overlap (SQL `BETWEEN`):** Amaran. Determines if two facts are valid simultaneously.
*   **Historical Reconstruction (Transaction Time filter):** Future Gen. Rewinds system knowledge.
*   **Contradiction Detection (Predicate Grouping):** Iron Man + Amaran. Alerts humans to conflicting reality.
*   **Confidence Calculation (Decay * Corroboration):** Amaran. Quantifies uncertainty explicitly.
*   **Change Detection (Diff T1 vs T2):** Iron Man. Surfacing updates so humans don't have to manually check.
*   **Provenance Traversal (Foreign Keys):** Future Gen + Iron Man. Linking claims to raw data.

---

## 13. EVALUATION TRACEABILITY
*   **IRON MAN:** Measure Human Task Completion Time (Time to correctly identify the root contradiction in a dataset using the UI vs reading raw text).
*   **AMARAN:** Measure Contradiction Detection Precision/Recall on a synthesized dataset with known conflicting reports. Measure temporal query correctness.
*   **FUTURE GENERATIONS:** Measure Historical Reconstruction Accuracy (Query state at T1 after inserting/updating at T2, ensure it perfectly matches a snapshot taken at T1).

---

## 14. REVIEWER DEFENSE — PHILOSOPHY
*   **Why Iron Man/Amaran/Future Gen?** They are complementary axes of a resilient system. Iron Man handles the Human capability. Amaran handles the noisy Reality. Future Gen handles the Database history.
*   **Are these just themes?** No. They are mapped directly to database columns (`system_to`, `valid_to`), SQL queries (Change detection), and UI components (Evidence Inspector).
*   **Why all three?** A system with only Iron Man is a pretty dashboard over static data. A system with only Amaran tracks change but might overwrite history. A system with only Future Gen is a pure archival ledger that is too hard for a human to read.
*   **How do you evaluate them?** Iron Man via human UI tests. Amaran via contradiction/temporal SQL unit tests. Future Gen via time-travel reconstruction tests.

---

## 15. AVOID PHILOSOPHICAL OVERCLAIMING
We use technically defensible language:
*   *Human-centered* (not "military-grade").
*   *Evidence-aware* (not "perfect truth").
*   *Temporal* (not "predicts the future").
*   *Explainable* (not "Artificial General Intelligence").
*   *Uncertainty-aware* (not "autonomous").

---

## 16. DOMAIN-AGNOSTICITY PROTECTION
The philosophies require absolutely zero domain knowledge.
*   **Iron Man:** Humans need cognitive reduction whether viewing a flood map or a cyber attack.
*   **Amaran:** Reality is conflicting whether it's a supply chain delay or a scientific research claim.
*   **Future Gen:** Institutional memory matters for disaster response and corporate networks equally.
*   **Result:** DOMAIN = VALIDATION SCENARIO. Project Identity remains independent.

---

## 17. SCOPE PROTECTION
The minimum complete system is exactly the pipeline frozen in Phase 4:
`Evidence → Assertion → Bi-Temporal TEG → Provenance → Contradiction → API → Web UI → Human`.
Any feature that does not directly serve Iron Man, Amaran, or Future Generations is out of scope.

---

## 18. SIX-REVIEW TRACEABILITY
*   **REVIEW 1:** Architecture & Feasibility (Establishes the three principles in design).
*   **REVIEW 2:** TEG Persistence (Implements Amaran's bi-temporal reality).
*   **REVIEW 3:** Provenance & Reconstruction (Implements Future Generations history).
*   **REVIEW 4:** Contradiction & Change (Implements Amaran's conflict handling).
*   **REVIEW 5:** Human Product/UI (Implements Iron Man's human augmentation).
*   **REVIEW 6:** Evaluation (Tests all three mathematically and qualitatively).

---

## 19. IMPLEMENTATION TRACEABILITY MATRIX

| ID | Requirement | Principle | Component | DB Element | API | UI | Test | Review |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| IR-02 | Evidence Drill-down | IRON MAN | Provenance Service | `Assertion_Evidence` | `GET /assertion/{id}/evidence` | Evidence Inspector | Provenance Trace Test | Rev 3, 5 |
| IR-03 | Surface Changes | IRON MAN | Change Service | `transaction_time` diff | `GET /situation/changes` | Timeline Feed | Change Accuracy Test | Rev 4, 5 |
| AR-02 | Valid vs Transaction | AMARAN | TEG Core | `valid_from`, `system_from` | `GET /entity/{id}/history` | N/A (Core logic) | Temporal Bounds Test | Rev 2 |
| AR-04 | Contradiction Detect | AMARAN | Intelligence Layer | `Assertions` table | `GET /contradictions` | Red Badges | Mutex Predicate Test | Rev 4 |
| FG-03 | Query Past System | FUTURE GEN | TEG Core | `system_to` | `GET /situation?time=X` | Time-Travel Toggle | Reconstruction Test | Rev 3 |

---

## 20. FINAL NORTH-STAR DEFINITION
**RESILIENT INTELLIGENCE is a human-centered intelligence infrastructure that maintains an evidence-backed, temporally evolving representation of a situation, detects meaningful changes and contradictions, exposes the evidence and uncertainty behind current assessments, and preserves historical knowledge so that the evolution of understanding can be reconstructed.**

*   **IRON MAN** → HUMAN UNDERSTANDING (Exposes evidence/uncertainty)
*   **AMARAN** → EVOLVING UNCERTAINTY (Maintains temporally evolving representation, detects changes/contradictions)
*   **FUTURE GENERATIONS** → DURABLE KNOWLEDGE (Preserves historical knowledge for reconstruction)

---

## 21. FINAL ACCEPTANCE CRITERIA
- [x] Every major subsystem maps to at least one principle.
- [x] The mapping is technically concrete (columns, queries, UI).
- [x] Every principle has observable user behavior.
- [x] Every principle has at least one evaluation method.
- [x] Every principle appears in the review plan.
- [x] No principle requires scope expansion beyond the frozen MVP.
- [x] No principle forces a domain-specific core.
- [x] No principle requires autonomous decision-making.
- [x] No principle requires expensive infrastructure.
- [x] No principle depends on an LLM or MCP as a core requirement.
- [x] All three principles remain meaningful independently, and together define the system.

**VERDICT: TRACEABILITY COMPLETE.**

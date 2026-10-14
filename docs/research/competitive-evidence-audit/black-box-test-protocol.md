# RESILIENT INTELLIGENCE — Black-Box Evaluation & Revalidation Test Protocol
## Reproducible Benchmarking Protocol for Dependency-Aware Knowledge Maintenance

- **Document Version:** 2.5 (Final Pre-Fixture Semantic Consistency Standard)
- **Status:** Pre-Fixture Semantic Consistency Gate — Pending BLK-01 Authorization
- **Target Systems for Comparison:**
  - **Baseline A:** Flat In-Context LLM Baseline (Full Context Window Injection)
  - **Baseline B:** Conventional Vector Retrieval / Semantic RAG (Chunk-based Vector Search with Query Probing)
  - **Baseline C:** Commercial User-Facing Baseline (ChatGPT Memory / Claude Projects via Black-Box UI)
  - **System Under Test:** RESILIENT INTELLIGENCE (RI Temporal Evidence Graph Core)
- **Constraint Compliance:** Zero external API fees, local deterministic execution, no account modifications, fully reproducible on a standard laptop.

---

## 1. Audit Review & Final Semantic Corrections

This section records the audit findings and rigor improvements applied to this test protocol during the final pre-fixture semantic gate:

| Material Issue Identified | Source & Evidence | Correction Applied | Residual Uncertainty |
| :--- | :--- | :--- | :--- |
| **Bitemporal Row-Versioning Invariant** | Lacked formal uniqueness and non-overlap invariant for temporal intervals, allowing `status` to potentially override query logic. | Formalized temporal intervals $[t_{\text{from}}, t_{\text{to}})$ with strict non-overlap invariant per entity-attribute at $(T_v, T_x)$ unless an explicit conflict exists. Established that temporal queries depend strictly on interval predicates, never on administrative `status` labels. Added boundary queries at $T_x = 11:00$ and $T_x = 13:00$. | Sub-millisecond clock resolution across local operating systems. |
| **Historical Belief Identity & Versioning** | Unclear whether historical beliefs were persisted records or transient query-time evaluations. | Defined persisted belief-version schema with 10 minimal fields (`belief_id`, `version_id`, `valid_from/to`, `system_from/to`, `rule_id`, `premise_version_ids`, `belief_value`, `jtms_support`, `ri_lifecycle`, `conflict_status`). Traced exact path $E_9 \to A_{C1,v3} \to B_{1,v3} (200s) \to B_{2,v3} (\text{TRUE, recomputed})$. | Downstream multi-hop aggregation graph depth. |
| **Retraction Semantics vs. Historical Reconstruction** | Unclear how Stage 5 retraction of $E_2$ impacts historical queries. | Formalized distinction: Historical recorded state ($T_x < 14:00$) preserves past states as recorded (where $E_2$ held); retrospective reconstruction using current evidence ($T_x \ge 14:00$) evaluates historical valid dates with $E_2$ retracted (`OUT` / `UNKNOWN`). Recomputation kept distinct from value change. | Long-term archival retention policies. |
| **Empty-Set Metric Rigor** | Setting $\text{Recall} = 1.00$ when target set is empty rewarded false positives. | Corrected: when target set is empty ($\mathcal{A}^* = \emptyset$), Recall is Not Applicable ($N/A$); Empty-Set Detection Accuracy ($EDA = \mathbb{I}(\mathcal{A}_{\text{id}} == \emptyset)$) evaluates invariance. If false positives occur, $EDA = 0.00, \text{Precision} = 0.00$. Added micro-aggregated metrics alongside macro averages. | Domain-specific weighting of false positives vs false negatives. |
| **Fair Workload Comparison Contract** | Previous draft risked comparing incremental updates to cold initial builds. | Formalized fair procedure: Targeted Revalidation vs. Full Graph Recomputation *after the exact same evidence change ($E_1'$), starting from identical pre-change snapshots, with identical correctness requirements*. Initial construction ($CW_{\text{init}}$) reported separately. Retained $WWR \le 0.50$ as a preregistered target on this synthetic fixture. | Hardware disk cache noise across repeated SQLite benchmarks. |
| **Track 2 Metric Validity & Scoring** | Conflated refusals and errors with stale answers; citation scoring lacked separation between precision and recall. | Disaggregated probe outcomes into Freshness Accuracy ($BFA$), Stale-Belief Rate ($SBR$), and Refusal/Error Rate ($RER$) such that $BFA + SBR + RER = 1.00$. Separated Citation Coverage ($CC$) from Citation Correctness ($CCR$), retaining Jaccard as supplementary. Scoped $UBP$ as fixture-specific. | LLM prompt sensitivity and output formatting variability. |
| **Permitted Conflict-State Matrix** | Permitted state combinations across orthogonal dimensions were undefined. | Formalized explicit 5-tuple state matrix of permitted combinations among Belief Value, JTMS Support, RI Lifecycle, and Conflict Status. Specified provisional exposure rules and restoration events for $B_3$. | Future multi-agent consensus voting algorithms. |

---

## 2. Research Hypotheses and Falsification Criteria

### Primary Research Question
> *"When supporting evidence changes, can a system expose which derived beliefs are affected and demonstrate correct targeted revalidation, and what evidence supports any comparison with existing products?"*

### Preregistered Hypotheses
- **Hypothesis $H_{1a}$ (Mechanism Correctness — Track 1):** In a deterministic bitemporal evidence graph, graph closure traversal identifies 100% of transitively dependent beliefs ($\text{Recall}_{\mathcal{A},\text{macro}} = 1.00, \text{Recall}_{\mathcal{A},\text{micro}} = 1.00, \text{Precision}_{\mathcal{A}} = 1.00$) and dependent graph nodes across all progression transitions ($S_2 \dots S_5, K=4$), correctly detects empty affected sets ($EDA = 1.00$), and preserves independent belief subgraphs ($UBI = 1.00$).
- **Hypothesis $H_{1b}$ (Efficiency & Freshness — Track 2):** Targeted revalidation of affected belief subgraphs reduces internal database write operations ($WWR_{\text{rows}} \le 0.50$, $WWR_{\text{statements}} \le 0.50$) and local wall-clock update time ($WWR_{\text{latency}} < 1.00, LR_{\text{local}} < 1.00$) compared to full graph recomputation upon the same evidence change on this benchmark fixture, while eliminating stale answers ($SBR = 0.00$) on downstream probe queries.

### Strict Falsification Conditions ($H_0$)
The experimental hypotheses shall be **falsified** if any of the following occur under controlled execution:
1. **Falsification of Mechanism Correctness ($H_{1a}$):** Graph closure traversal fails to isolate the exact affected set ($\text{Recall}_{\mathcal{A}} < 1.00$, $\text{Precision}_{\mathcal{A}} < 1.00$, or $EDA < 1.00$), or mutates an invariant belief node ($UBI < 1.00$) on any stage transition of the deterministic test fixture.
2. **Falsification of Comparative Efficiency ($H_{1b}$):** The computational cost of targeted revalidation equals or exceeds a full graph recomputation after the same change on the benchmark fixture ($WWR_{\text{statements}} \ge 1.00$, $WWR_{\text{rows}} \ge 1.00$, or $WWR_{\text{latency}} \ge 1.00$).
   - *Interpretation of Partial Reduction:* If $0.50 < WWR < 1.00$, the system demonstrates partial workload reduction, but fails to achieve the preregistered efficiency target $H_{1b}$. Falsification of comparative advantage occurs strictly at $WWR \ge 1.00$.
3. **Falsification of Belief Freshness ($H_{1b}$):** Targeted revalidation yields a non-zero Stale-Belief Rate ($SBR > 0.00$) on affected probes, asserting superseded claims.

---

## 3. Benchmark Corpus Design & Formal Deductive Topology

The benchmark corpus consists of 9 distinct evidence items ($E_1 \dots E_9$), 7 initial claims ($C_1 \dots C_7$), 2 subsequent claims ($C_4', C_1''$), and 4 derived beliefs ($B_1 \dots B_4$).

### 3.1 Bitemporal Interval Representation & Invariants

All temporal intervals in RESILIENT INTELLIGENCE follow standard mathematical half-open interval semantics:
$$[t_{\text{from}}, t_{\text{to}}) = \{t \in \text{Time} \mid t_{\text{from}} \le t < t_{\text{to}}\}$$
where $t_{\text{to}} = \infty$ (represented as SQL `NULL`) denotes an open, currently active validity or system interval.

#### Core Row-Versioning Invariant:
For any stored entity-attribute $(e, a)$:
1. At any query point in valid time $T_v$ and transaction time $T_x$, a record $r$ is active if and only if:
   $$r.system\_from \le T_x < r.system\_to \quad (\text{or } r.system\_to \text{ IS NULL})$$
   $$r.valid\_from \le T_v < r.valid\_to \quad (\text{or } r.valid\_to \text{ IS NULL})$$
2. **Uniqueness & Non-Overlap Rule:** For any entity-attribute $(e, a)$ and any valid coordinate $(T_v, T_x)$, there MUST exist at most **one** active record in the database, **unless** the fixture explicitly represents an active epistemic contradiction (such as $E_4$ vs. $E_8$ in Stage 3). When multiple active records overlap for the same $(e, a)$ at $(T_v, T_x)$, their `conflict_status` MUST be set to `DIRECT_CONFLICT`.
3. **Independence from Descriptive Status:** Temporal state reconstruction is governed strictly by the SQL predicates on `valid_from/to` and `system_from/to`. The descriptive column `status` (`'ACTIVE'`, `'SUPERSEDED'`, `'RETRACTED'`) is an administrative metadata label and **never** overrides temporal query predicates.

---

### 3.2 Evidence Catalog & Relational Assertion Log

The following table details the evidence items and their exact bitemporal intervals:

| ID | Source Document | Entity-Attribute & Version | Proposition Content | Valid Time ($T_v$) | System / Ingest Time ($T_x$) | Epistemic Role & Supersession Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$E_1$** | System Spec v1.0 §4.1 | `client_network.timeout` ($A_{C1,v1}$) | `30s` | $[2026-10-01T00:00:00Z, \infty)$ | $2026-10-13T10:00:00Z$ | Baseline timeout. Truncated to $[10-01, 10-13)$ upon $E_1'$ ingest. |
| **$E_2$** | Architecture Doc §2.2 | `client_network.max_retries` ($A_{C2,v1}$) | `3` | $[2026-10-01T00:00:00Z, \infty)$ | $2026-10-13T10:00:00Z$ | Baseline retries. Retracted in Stage 5 at $T_x = 14:00$. |
| **$E_3$** | Client SLA v2 §1.0 | `sla_policy.threshold` ($A_{C3,v1}$) | `45s` | $[2026-10-01T00:00:00Z, \infty)$ | $2026-10-13T10:00:00Z$ | Invariant SLA ceiling threshold. |
| **$E_4$** | Auth Config File | `auth_service.protocol` ($A_{C4,v1}$) | `OAuth2_PKCE` | $[2026-10-01T00:00:00Z, \infty)$ | $2026-10-13T10:00:00Z$ | Baseline auth protocol. Contradicted by $E_8$ in Stage 3. |
| **$E_5$** | Security Audit Cert | `tls_config.cert_expiry` ($A_{C5,v1}$) | `2027-12-31T23:59:59Z` | $[2026-10-01T00:00:00Z, \infty)$ | $2026-10-13T10:00:00Z$ | Valid TLS certificate expiration. |
| **$E_6$** | System Clock Context | `audit_clock.assessment_date` ($A_{C6,v1}$) | `2026-10-13T10:00:00Z` | $[2026-10-13T00:00:00Z, 2026-10-13T23:59:59Z]$ | $2026-10-13T10:00:00Z$ | Assessment clock context. |
| **$E_7$** | Storage Config | `storage.db_engine` ($A_{C7,v1}$) | `SQLite_3.45` | $[2026-10-01T00:00:00Z, \infty)$ | $2026-10-13T10:00:00Z$ | Embedded storage engine specification. |
| **$E_1'$** | System Spec v1.1 §4.1 | `client_network.timeout` ($A_{C1,v2}$) | `10s` | $[2026-10-13T00:00:00Z, \infty)$ | $2026-10-13T11:00:00Z$ | **Forward Supersession:** Supersedes $A_{C1,v1}$ forward from Oct 13. |
| **$E_8$** | SecOps Audit Finding | `auth_service.protocol` ($A_{C4,v2}$) | `None` | $[2026-10-13T00:00:00Z, \infty)$ | $2026-10-13T12:00:00Z$ | **Direct Contradiction:** Asserts mutually exclusive value over overlapping valid time. |
| **$E_9$** | Maintenance Window Log | `client_network.timeout` ($A_{C1,v3} / C_1''$) | `50s` | $[2026-10-01T00:00:00Z, 2026-10-05T00:00:00Z)$ | $2026-10-13T13:00:00Z$ | **Retroactive Historical Correction:** Corrects interval $[10-01, 10-05)$. |

---

### 3.3 Formal Inference Rules & Derived Belief Topology

The benchmark corpus specifies 7 initial claims ($C_1 \dots C_7$), 2 subsequent claims ($C_4', C_1''$), and 4 derived beliefs ($B_1 \dots B_4$) generated via 4 deterministic inference rules ($R_1 \dots R_4$):

#### Claims Catalog:
- **$C_1$ ($A_{C1}$):** `client_network.timeout` (Initial: `30s` via $E_1$; Superseded: `10s` via $E_1'$; Historical: `50s` via $E_9$).
- **$C_2$ ($A_{C2}$):** `client_network.max_retries` (`3` via $E_2$; retracted at $T_x = 14:00$).
- **$C_3$ ($A_{C3}$):** `sla_policy.threshold` (`45s` via $E_3$).
- **$C_4$ ($A_{C4}$):** `auth_service.protocol` (`OAuth2_PKCE` via $E_4$; Contradicted by `None` via $E_8$).
- **$C_5$ ($A_{C5}$):** `tls_config.cert_expiry` (`2027-12-31T23:59:59Z` via $E_5$).
- **$C_6$ ($A_{C6}$):** `audit_clock.assessment_date` (`2026-10-13T10:00:00Z` via $E_6$).
- **$C_7$ ($A_{C7}$):** `storage.db_engine` (`SQLite_3.45` via $E_7$).

#### Formal Inference Rules ($R_1 \dots R_4$):
1. **Rule $R_1$ — Worst-Case Client Timeout Delay ($B_1$):**
   - *Premises:* $A_{C1}$ (`client_network.timeout`), $A_{C2}$ (`client_network.max_retries`).
   - *Domain Semantics:* `max_retries = 3` represents 3 retry attempts following 1 initial attempt, yielding $(1 + \text{max\_retries})$ total attempts.
   - *Mathematical Formula:* $B_1 = (1 + A_{C2}.\text{value}) \times A_{C1}.\text{value}$.
   - *Evaluations across Progression:*
     - Stage 1: $(1 + 3) \times 30s = 120s$.
     - Stage 2: $(1 + 3) \times 10s = 40s$.
     - Stage 4 (Historical $[10-01, 10-05)$): $(1 + 3) \times 50s = 200s$.
     - Stage 5: Antecedent $A_{C2,v1}$ retracted $\implies B_1 = \text{UNKNOWN}$ (`OUT`).

2. **Rule $R_2$ — SLA Violation Risk Assessment ($B_2$):**
   - *Premises:* $B_1$ (Worst-case client timeout delay), $A_{C3}$ (`sla_policy.threshold`).
   - *Domain Semantics:* Evaluates whether worst-case network timeout exceeds SLA ceiling ($45s$).
   - *Mathematical Formula:* $B_2 = (B_1 > A_{C3}.\text{value})$.
   - *Evaluations across Progression:*
     - Stage 1: $120s > 45s \implies \text{TRUE}$.
     - Stage 2: $40s > 45s \implies \text{FALSE}$.
     - Stage 4 (Historical $[10-01, 10-05)$): $200s > 45s \implies \text{TRUE}$ (recomputed).
     - Stage 5: Antecedent $B_1$ retracted (`OUT`) $\implies B_2 = \text{UNKNOWN}$ (`OUT`).

3. **Rule $R_3$ — Security Policy Compliance `POL-SEC-01` ($B_3$):**
   - *Premises:* $A_{C4}$ (`auth_service.protocol`), $A_{C5}$ (`tls_config.cert_expiry`), $A_{C6}$ (`audit_clock.assessment_date`).
   - *Domain Semantics & Sufficient Conditions:* Fixture security policy `POL-SEC-01` mandates that compliance evaluates to `PASS` if and only if both conditions are satisfied:
     1. Authentication protocol is modern approved OAuth2 PKCE: $A_{C4}.\text{value} == \text{'OAuth2\_PKCE'}$, AND
     2. TLS Certificate is validly unexpired at assessment clock: $A_{C5}.\text{value} > A_{C6}.\text{value}$.
     Otherwise evaluates to `FAIL`.
   - *Evaluations across Progression:*
     - Stage 1 & 2: `OAuth2_PKCE` and unexpired $\implies \text{PASS}$ (`CONSISTENT`).
     - Stage 3: Contradicting evidence $E_8$ ($A_{C4,v2} = \text{None}$) arrives. Because mutually exclusive claims co-exist over $[10-13, \infty)$, $B_3$ transitions to `DERIVED_CONFLICT` with provisional exposure `PASS (prov.)` and flag `HUMAN_REVIEW_REQUIRED = TRUE`.

4. **Rule $R_4$ — Embedded Storage Engine Active ($B_4$):**
   - *Premises:* $A_{C7}$ (`storage.db_engine`).
   - *Domain Semantics:* Evaluates whether storage engine matches certified embedded database.
   - *Logical Formula:* $B_4 = (A_{C7}.\text{value} == \text{'SQLite\_3.45'})$.
   - *Evaluations across Progression:* Invariant across all stages $\implies \text{TRUE}$ (`CONSISTENT`).

---

### 3.4 Relational State Transitions & Boundary-Query Expectations

#### Relational State Log of the `assertions` Table across Transaction Time:

```sql
-- State after Stage 1 (Tx = 2026-10-13T10:00:00Z):
INSERT INTO assertions VALUES ('A_C1_1', 'client_network.timeout', '30s', '2026-10-01T00:00:00Z', NULL, '2026-10-13T10:00:00Z', NULL, 'ACTIVE', 'E1');

-- Transition at Stage 2 (Tx = 2026-10-13T11:00:00Z):
UPDATE assertions SET system_to = '2026-10-13T11:00:00Z', status = 'SUPERSEDED' WHERE assertion_id = 'A_C1_1';
INSERT INTO assertions VALUES ('A_C1_1_trunc', 'client_network.timeout', '30s', '2026-10-01T00:00:00Z', '2026-10-13T00:00:00Z', '2026-10-13T11:00:00Z', NULL, 'ACTIVE', 'E1');
INSERT INTO assertions VALUES ('A_C1_2', 'client_network.timeout', '10s', '2026-10-13T00:00:00Z', NULL, '2026-10-13T11:00:00Z', NULL, 'ACTIVE', 'E1_prime');

-- Transition at Stage 4 (Tx = 2026-10-13T13:00:00Z):
UPDATE assertions SET system_to = '2026-10-13T13:00:00Z', status = 'SUPERSEDED' WHERE assertion_id = 'A_C1_1_trunc';
INSERT INTO assertions VALUES ('A_C1_3', 'client_network.timeout', '50s', '2026-10-01T00:00:00Z', '2026-10-05T00:00:00Z', '2026-10-13T13:00:00Z', NULL, 'ACTIVE', 'E9');
INSERT INTO assertions VALUES ('A_C1_1_post', 'client_network.timeout', '30s', '2026-10-05T00:00:00Z', '2026-10-13T00:00:00Z', '2026-10-13T13:00:00Z', NULL, 'ACTIVE', 'E1');
```

#### Exact Boundary-Query Expectations:

1. **Boundary around $T_x = 11:00:00Z$ (Evaluating $T_v = 2026-10-13T12:00:00Z$):**
   - **Immediately Before ($T_x = 2026-10-13T10:59:59.999Z$):**
     Matches `A_C1_1` ($system\_from \le 10:59:59.999 < 11:00$).
     Expected: `Client_Timeout = 30s`, $B_1 = 120s$, $B_2 = \text{TRUE}$.
   - **Immediately After ($T_x = 2026-10-13T11:00:00.000Z$):**
     Matches `A_C1_2` ($system\_from \le 11:00:00 < \infty$).
     Expected: `Client_Timeout = 10s`, $B_1 = 40s$, $B_2 = \text{FALSE}$.

2. **Boundary around $T_x = 13:00:00Z$ (Evaluating Historical $T_v = 2026-10-03T12:00:00Z$):**
   - **Immediately Before ($T_x = 2026-10-13T12:59:59.999Z$):**
     Matches `A_C1_1_trunc` ($system\_from \le 12:59:59.999 < 13:00$).
     Expected: `Client_Timeout = 30s`, $B_{1,\text{hist}} = 120s$, $B_{2,\text{hist}} = \text{TRUE}$.
   - **Immediately After ($T_x = 2026-10-13T13:00:00.000Z$):**
     Matches `A_C1_3` ($system\_from \le 13:00:00 < \infty$).
     Expected: `Client_Timeout = 50s`, $B_{1,\text{hist}} = 200s$, $B_{2,\text{hist}} = \text{TRUE}$ (recomputed).
   - **Current Operational Reality ($T_v = 2026-10-13T12:00:00Z$ at $T_x = 13:00:00.000Z$):**
     Matches `A_C1_2`.
     Expected: `Client_Timeout = 10s`, $B_1 = 40s$, $B_2 = \text{FALSE}$ (invariant).

---

### 3.5 Historical Belief Identity & Minimal Schema Specification

In RESILIENT INTELLIGENCE, derived beliefs are **persisted, versioned records** in a relational `beliefs` table with the following minimal schema contract:

| Field Name | Type | Description | Example (Historical $B_{1,v3}$) |
| :--- | :--- | :--- | :--- |
| `belief_id` | `TEXT` | Canonical logical belief identifier | `'B1'` |
| `version_id` | `TEXT PRIMARY KEY` | Immutable unique belief version identifier | `'B1_v3'` |
| `valid_from` | `TEXT` | Start of real-world valid interval (inclusive) | `'2026-10-01T00:00:00Z'` |
| `valid_to` | `TEXT` | End of real-world valid interval (exclusive; NULL = $\infty$) | `'2026-10-05T00:00:00Z'` |
| `system_from`| `TEXT` | Transaction timestamp when version was recorded | `'2026-10-13T13:00:00Z'` |
| `system_to`  | `TEXT` | Transaction timestamp when version was superseded (NULL = active) | `NULL` |
| `rule_id`    | `TEXT` | Formal inference rule generating the belief | `'R1'` |
| `premise_version_ids` | `JSON` | Array of exact premise assertion version IDs | `'["A_C1_3", "A_C2_1"]'` |
| `belief_value` | `TEXT` | Evaluated domain value / payload | `'200s'` |
| `jtms_support` | `TEXT` | Categorical Doyle JTMS justification state (`IN` \| `OUT`) | `'IN'` |
| `ri_lifecycle` | `TEXT` | Operational state (`SUPPORTED` \| `REQUIRES_REVALIDATION` \| `INVALIDATED` \| `QUARANTINED`) | `'SUPPORTED'` |
| `conflict_status` | `TEXT` | Multi-source consistency state (`CONSISTENT` \| `DIRECT_CONFLICT` \| `DERIVED_CONFLICT`) | `'CONSISTENT'` |

#### Causal Dependency Trace from $E_9$:
$$E_9 \xrightarrow{\text{ingest}} A_{C1,v3} \ (C_1'') \xrightarrow{\text{Rule } R_1 \ [A_{C1,v3}, A_{C2,v1}]} B_{1,v3} \ (200s) \xrightarrow{\text{Rule } R_2 \ [B_{1,v3}, A_{C3,v1}]} B_{2,v3} \ (\text{TRUE})$$

#### Retraction Semantics (Stage 5) vs. Historical Reconstruction:
When $E_2$ is retracted at $T_x = 2026-10-13T14:00:00Z$:
1. **Historical Version Invariant:** In bitemporal append-only storage, retractions do **not** mutate or delete prior records. Instead, the active assertion record $A_{C2,v1}$ is closed in system transaction time by setting `system_to = '2026-10-13T14:00:00Z'`, and newly invalidated belief version records are inserted with `system_from = '2026-10-13T14:00:00Z'`, `jtms_support = 'OUT'`, `ri_lifecycle = 'INVALIDATED'`, and `belief_value = 'UNKNOWN'`.
2. **Historical Recorded-State Query ($T_{x,\text{asof}} < 14:00$):**
   - *Semantics:* Evaluates what RI recorded and believed at an earlier system-time cutoff before the retraction occurred.
   - *SQL Predicate:* Selects rows where `system_from <= Tx_asof AND (system_to > Tx_asof OR system_to IS NULL)`.
   - *Expected Behavior:* A query as-of $T_x = 13:30$ for $T_v = 10-03$ reconstructs the historical recorded state where $E_2$ was still believed, returning $B_1 = 200s, B_2 = \text{TRUE}$. Retraction at 14:00 does not alter past recorded state.
3. **Retrospective Reconstruction ($T_{x,\text{asof}} \ge 14:00$):**
   - *Semantics:* Evaluates what the system concludes for a historical valid-time interval using evidence and retractions known at a later system-time cutoff.
   - *Expected Behavior:* When querying past valid dates ($T_v = 10-03$) using currently available unretracted evidence as of $T_x \ge 14:00$, antecedent $C_2$ is `OUT`. Hence retrospective evaluation concludes that historical $B_1$ and $B_2$ are `OUT` / `UNKNOWN`.
4. **Operations Evaluated by the Benchmark:**
   - *Operational Invalidation (Stage 5 Primary Test):* Evaluates current transaction-time graph propagation ($T_x = 14:00$), asserting that retracting $E_2$ isolates $\{A_{C2,v1}, B_1, B_2\}$ and transitions active $B_1, B_2$ to `OUT` / `INVALIDATED` / `UNKNOWN`.
   - *Historical Invariance Check:* Evaluates a historical recorded-state query as-of $T_x = 13:30$ post-retraction, verifying that historical query outputs are unaffected by subsequent retractions.
5. **Recomputation vs. Value Change:** Recomputing a node means evaluating its inference rule upon antecedent mutation. In Stage 4, historical $B_2$ is recomputed because its premise $B_1$ changed from $120s \to 200s$; its evaluated Boolean value remains `TRUE`. In Stage 5, $B_1$ and $B_2$ undergo both recomputation and value transition to `UNKNOWN`.
6. **Premise Version Resolution Rule:**
   - When evaluating or updating an inference rule at coordinates $(T_v, T_x)$, the system selects premise assertion versions $A$ matching:
     $$A.system\_from \le T_x < A.system\_to \quad (\text{or } A.system\_to \text{ IS NULL})$$
     $$A.valid\_from \le T_v < A.valid\_to \quad (\text{or } A.valid\_to \text{ IS NULL})$$
   - The resulting belief record stores the exact matching assertion version IDs in `premise_version_ids`.
   - For a **historical recorded-state query** as-of $T_{x,\text{asof}}$ for valid date $T_v$, the query retrieves the belief version $B$ satisfying $B.system\_from \le T_{x,\text{asof}} < B.system\_to$ (or NULL) and $B.valid\_from \le T_v < B.valid\_to$ (or NULL).
   - For a **retrospective reconstruction** as-of $T_{x,\text{asof}}$ for valid date $T_v$, the inference engine re-evaluates the rule against assertion versions active at $(T_v, T_{x,\text{asof}})$. If an essential antecedent was retracted prior to or at $T_{x,\text{asof}}$ ($A.system\_to \le T_{x,\text{asof}}$), the rule has no valid premise support at that cutoff, concluding `jtms_support = 'OUT'` and `belief_value = 'UNKNOWN'`.

---

### 3.6 Permitted Conflict-State Matrix

To prevent inconsistent internal states, belief nodes must conform to the following permitted state combinations:

| Permitted Combination Name | `jtms_support` | `ri_lifecycle` | `conflict_status` | `belief_value` | Semantic Meaning & Exposure Policy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Consistent Active** | `IN` | `SUPPORTED` | `CONSISTENT` | Valid scalar / Boolean | Normal fully supported belief. Fully usable in automated tasks. |
| **Contested Provisional** | `IN` | `SUPPORTED` | `DERIVED_CONFLICT` | Valid scalar / Boolean | Usable provisionally with warning. Exposes competing claims ($C_4$ vs $C_4'$) and `HUMAN_REVIEW_REQUIRED = TRUE`. |
| **Quarantined Conflict** | `IN` | `QUARANTINED` | `DIRECT_CONFLICT` | Contested Value | Suspended from automated inference pending human dispute arbitration. |
| **Retracted Inactive** | `OUT` | `INVALIDATED` | `CONSISTENT` | `UNKNOWN` | Antecedent retracted; no alternative justification exists. |
| **Dirty Revalidation** | `OUT` | `REQUIRES_REVALIDATION` | `CONSISTENT` | `UNKNOWN` | Transient state during propagation; awaiting recomputation. |

*Conflict Resolution Event:* A contested belief ($B_3$) is restored from `DERIVED_CONFLICT` to `CONSISTENT` only when an explicit dispute resolution event occurs: either retraction of one of the conflicting assertions ($E_8$ retracted), or an authoritative domain policy rule establishing precedence.

---

## 4. Multi-Stage Progression & Ground Truth Specification

The primary algorithmic correctness test suite covers **all five progression stages ($S_1 \dots S_5$) sequentially**, evaluating transitions across $K=4$ change events ($S_2, S_3, S_4, S_5$).

### 4.1 Ground Truth Specification Table

| Stage | Input Event & Ingest Time ($T_x$) | Affected Sets ($\mathcal{A}_k^*$) | Invariant Sets ($\mathcal{U}_k^*$) | Expected State ($B_1, B_2, B_3, B_4$) | Verification Criteria |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$S_1$ (Grounding)** | Ingest $E_1 \dots E_7$<br>($T_x = 10:00$) | All nodes:<br>$\mathcal{A}_{1,\text{nodes}}^* = \{A_{C1..7}, B_{1..4}\}$<br>$\mathcal{A}_{1,\text{beliefs}}^* = \{B_1 \dots B_4\}$ | $\emptyset$ | - $B_1$: `120s`, `IN`, `SUPPORTED`, `CONSISTENT`<br>- $B_2$: `TRUE`, `IN`, `SUPPORTED`, `CONSISTENT`<br>- $B_3$: `PASS`, `IN`, `SUPPORTED`, `CONSISTENT`<br>- $B_4$: `TRUE`, `IN`, `SUPPORTED`, `CONSISTENT` | Baseline build. All 4 beliefs established as `IN`, `SUPPORTED`, and `CONSISTENT`. |
| **$S_2$ (Correction)** | Ingest $E_1'$ ($A_{C1,v2} = 10s$, valid $[10-13, \infty)$)<br>($T_x = 11:00$) | $\mathcal{A}_{2,\text{nodes}}^* = \{A_{C1,v2}, B_1, B_2\}$<br>$\mathcal{A}_{2,\text{beliefs}}^* = \{B_1, B_2\}$ | $\mathcal{U}_{2,\text{nodes}}^* = \{A_{C2..7}, B_3, B_4\}$<br>$\mathcal{U}_{2,\text{beliefs}}^* = \{B_3, B_4\}$ | - $B_1$: `40s`, `IN`, `SUPPORTED`, `CONSISTENT`<br>- $B_2$: `FALSE`, `IN`, `SUPPORTED`, `CONSISTENT`<br>- $B_3$: `PASS`, `IN`, `SUPPORTED`, `CONSISTENT`<br>- $B_4$: `TRUE`, `IN`, `SUPPORTED`, `CONSISTENT` | Forward supersession: $E_1'$ supersedes $E_1$. Recall = 1.00, Precision = 1.00. Invariant set $\mathcal{U}_2^*$ unchanged. |
| **$S_3$ (Contradiction)** | Ingest $E_8$ ($A_{C4,v2} = \text{None}$, valid $[10-13, \infty)$)<br>($T_x = 12:00$) | $\mathcal{A}_{3,\text{nodes}}^* = \{A_{C4,v1}, A_{C4,v2}, B_3\}$<br>$\mathcal{A}_{3,\text{beliefs}}^* = \{B_3\}$ | $\mathcal{U}_{3,\text{nodes}}^* = \{A_{C1..3}, A_{C5..7}, B_1, B_2, B_4\}$<br>$\mathcal{U}_{3,\text{beliefs}}^* = \{B_1, B_2, B_4\}$ | - $B_1$: `40s`, `IN`, `SUPPORTED`, `CONSISTENT`<br>- $B_2$: `FALSE`, `IN`, `SUPPORTED`, `CONSISTENT`<br>- $B_3$: `PASS` (prov.), `IN`, `SUPPORTED`, **`DERIVED_CONFLICT`**<br>- $B_4$: `TRUE`, `IN`, `SUPPORTED`, `CONSISTENT` | Direct conflict on $A_{C4}$. $B_3$ transitions to `DERIVED_CONFLICT`. Human review flag raised. $B_1, B_2, B_4$ invariant. |
| **$S_4$ (Historical Correction)** | Ingest $E_9$ ($A_{C1,v3} = 50s$, valid $[10-01, 10-05)$)<br>($T_x = 13:00$) | **Historical Slice ($T_v \in [10-01, 10-05)$):**<br>$\mathcal{A}_{4,\text{hist,nodes}}^* = \{A_{C1,v3}, B_{1,\text{hist}}, B_{2,\text{hist}}\}$<br>$\mathcal{A}_{4,\text{hist,beliefs}}^* = \{B_{1,\text{hist}}, B_{2,\text{hist}}\}$<br><br>**Current Operational Slice ($T_v = 10-13$):**<br>$\mathcal{A}_{4,\text{curr,nodes}}^* = \emptyset$<br>$\mathcal{A}_{4,\text{curr,beliefs}}^* = \emptyset$ | **Current Operational Slice:**<br>$\mathcal{U}_{4,\text{curr,nodes}}^* = \text{All current nodes}$<br>$\mathcal{U}_{4,\text{curr,beliefs}}^* = \{B_1, B_2, B_3, B_4\}$ | **Current Operational State ($T_v = 10-13$):**<br>- $B_1$: `40s`, `IN`, `SUPPORTED`, `CONSISTENT`<br>- $B_2$: `FALSE`, `IN`, `SUPPORTED`, `CONSISTENT`<br>- $B_3$: `PASS`, `IN`, `SUPPORTED`, `DERIVED_CONFLICT`<br>- $B_4$: `TRUE`, `IN`, `SUPPORTED`, `CONSISTENT`<br><br>**Historical State ($T_v = 10-03$, $T_x \ge 13:00$):**<br>- $B_{1,\text{hist}}$: updates `120s` $\to$ **`200s`**<br>- $B_{2,\text{hist}}$: recomputed under Rule $R_2$ ($200s > 45s$), evaluates to `TRUE` | Retroactive correction over $[10-01, 10-05)$. Distinguishes historical belief revision from current operational invariance. Current state unaffected. |
| **$S_5$ (Retraction)** | Retract $E_2$ (Arch Doc retracted)<br>($T_x = 14:00$) | $\mathcal{A}_{5,\text{nodes}}^* = \{A_{C2,v1}, B_1, B_2\}$<br>$\mathcal{A}_{5,\text{beliefs}}^* = \{B_1, B_2\}$ | $\mathcal{U}_{5,\text{nodes}}^* = \{A_{C1,v2}, A_{C3..7}, B_3, B_4\}$<br>$\mathcal{U}_{5,\text{beliefs}}^* = \{B_3, B_4\}$ | - $B_1$: `UNKNOWN`, **`OUT`**, **`INVALIDATED`**, `CONSISTENT`<br>- $B_2$: `UNKNOWN`, **`OUT`**, **`INVALIDATED`**, `CONSISTENT`<br>- $B_3$: `PASS`, `IN`, `SUPPORTED`, `DERIVED_CONFLICT`<br>- $B_4$: `TRUE`, `IN`, `SUPPORTED`, `CONSISTENT` | Antecedent $A_{C2,v1}$ retracted $\implies B_1, B_2$ transition to `OUT` and `INVALIDATED`. Invariant set $\mathcal{U}_5^*$ untouched. |

---

## 5. Formal Metric Definitions & Fair Measurement Contracts

Metrics are strictly divided by scope:

### Scope A: Track 1 Metrics (Deterministic Algorithmic Mechanism — RI Core Only)

#### 1. Transition Coverage ($K=4$) & Per-Stage Reporting:
All Track 1 metrics evaluate the sequence of 4 state transitions ($k \in \{2, 3, 4, 5\}$).  
*Contract:* The benchmark runner MUST output per-stage results ($\text{Metric}_2, \text{Metric}_3, \text{Metric}_4, \text{Metric}_5$) alongside micro-aggregated and macro-aggregated summaries.

#### 2. Formal Empty-Set and Zero-Denominator Conventions:
For any stage transition $k$, with target affected set $\mathcal{A}_k^*$ and identified set $\mathcal{A}_{k,\text{id}}$:
- **Empty-Set Invariance (e.g. Current Operational State in $S_4$):**
  When $\mathcal{A}_k^* = \emptyset$:
  - **Empty-Set Detection Accuracy ($EDA_k$):** $\mathbb{I}(\mathcal{A}_{k,\text{id}} == \emptyset)$. If $\mathcal{A}_{k,\text{id}} = \emptyset$, $EDA_k = 1.00$. If $\mathcal{A}_{k,\text{id}} \ne \emptyset$, $EDA_k = 0.00$.
  - **Recall:** Formally **Not Applicable ($N/A$)** because there are zero positive targets to recall ($|\mathcal{A}_k^*| = 0$). It is **never** described as 1.00 or perfect recall.
  - **Precision:** If $\mathcal{A}_{k,\text{id}} = \emptyset$, $\text{Precision} = N/A$ (no predictions made, $0/0$). If $\mathcal{A}_{k,\text{id}} \ne \emptyset$, $\text{Precision} = 0.00$ ($0 / |\mathcal{A}_{k,\text{id}}|$, as all identified items are false positives).
- **Non-Empty Target Sets ($\mathcal{A}_k^* \ne \emptyset$):**
  - If $\mathcal{A}_{k,\text{id}} = \emptyset \implies \text{Recall}_k = 0.00, \text{Precision}_k = 0.00$.
  - If $\mathcal{A}_{k,\text{id}} \ne \emptyset \implies \text{Recall}_k = \frac{|\mathcal{A}_{k,\text{id}} \cap \mathcal{A}_k^*|}{|\mathcal{A}_k^*|}, \quad \text{Precision}_k = \frac{|\mathcal{A}_{k,\text{id}} \cap \mathcal{A}_k^*|}{|\mathcal{A}_{k,\text{id}}|}$.

##### Explicit Empty-Target Stage Specification ($S_{4,\text{curr}}$ at $T_v = 10-13$):
The benchmark progression contains exactly one stage evaluation with an empty ground-truth affected set:

| Evaluation Dimension | Value for Stage $S_{4,\text{curr}}$ | Aggregation & Invariant Accounting |
| :--- | :--- | :--- |
| **Ground-Truth Affected Set ($\mathcal{A}^*$)** | $\mathcal{A}_{4,\text{curr,beliefs}}^* = \emptyset$ (nodes: $\emptyset$) | Ground-truth benchmark target is strictly empty. |
| **Identified Affected Set ($\mathcal{A}_{\text{id}}$)** | $\mathcal{A}_{4,\text{curr,id}}$ (Expected: $\emptyset$) | Identified set under test. |
| **Empty-Set Detection Accuracy ($EDA$)** | $EDA = 1.00$ iff $\mathcal{A}_{\text{id}} == \emptyset$; $0.00$ if $\mathcal{A}_{\text{id}} \ne \emptyset$ | Confirms EDA = 1 only when both sets are empty. |
| **Recall Handling** | **$N/A$** (Zero targets) | **Excluded** from macro-recall ($K_{\text{non-empty}}$); adds $0$ to micro-recall numerator and $0$ to denominator. Never reported as 1.00. |
| **Precision Handling** | **$N/A$** if $\mathcal{A}_{\text{id}} == \emptyset$; **$0.00$** if $\mathcal{A}_{\text{id}} \ne \emptyset$ | If $\mathcal{A}_{\text{id}} = \emptyset$, excluded from macro-precision. If false positives exist ($\mathcal{A}_{\text{id}} \ne \emptyset$), contributes $0.00$ to macro-precision ($K_{\text{pred}}$) and adds $\|\mathcal{A}_{\text{id}}\|$ to micro-precision denominator. |
| **Unaffected Invariant Set ($\mathcal{U}^*$)** | $\mathcal{U}_{4,\text{curr,beliefs}}^* = \{B_1, B_2, B_3, B_4\}$ | Preserved separately under invariant metric $UBI_{4,\text{curr}} = 1.00$. |

#### 3. Macro vs. Micro Aggregated Identification Metrics:
- **Macro-Averaged Recall & Precision:** Computed over transitions where target sets are non-empty:
  $$\text{Recall}_{\mathcal{A},\text{macro}} = \frac{1}{K_{\text{non-empty}}} \sum_{k: \mathcal{A}_k^* \ne \emptyset} \text{Recall}_k, \quad \text{Precision}_{\mathcal{A},\text{macro}} = \frac{1}{K_{\text{pred}}} \sum_{k: \mathcal{A}_{k,\text{id}} \ne \emptyset} \text{Precision}_k$$
- **Micro-Aggregated Count-Based Recall & Precision:**
  $$\text{Recall}_{\mathcal{A},\text{micro}} = \frac{\sum_{k=2}^{5} |\mathcal{A}_{k,\text{id}} \cap \mathcal{A}_k^*|}{\sum_{k=2}^{5} |\mathcal{A}_k^*|}, \quad \text{Precision}_{\mathcal{A},\text{micro}} = \frac{\sum_{k=2}^{5} |\mathcal{A}_{k,\text{id}} \cap \mathcal{A}_k^*|}{\sum_{k=2}^{5} |\mathcal{A}_{k,\text{id}}|}$$
  - *Target ($H_{1a}$):* Both macro and micro metrics must achieve **$1.00$**.

#### 4. Multi-Stage Unaffected-Belief Invariance ($UBI$):
$$UBI_k = \frac{|\{b \in \mathcal{U}_{k,\text{beliefs}}^* \mid b \text{ unchanged in value, JTMS support, lifecycle, and conflict status}\}|}{|\mathcal{U}_{k,\text{beliefs}}^*|}$$
$$UBI = \frac{1}{K} \sum_{k=2}^{5} UBI_k$$
- Evaluated for stages where $\mathcal{U}_{k,\text{beliefs}}^* \ne \emptyset$. Target: **$1.00$**.

#### 5. Fair Workload Comparison Protocol ($WWR_{\text{RI}}$):
The workload reduction benchmark compares **Targeted Revalidation** against a **Full Graph Recomputation** under strict controlled conditions:
1. **Identical Baseline Snapshot:** Both strategies start from the exact identical SQLite database state after Stage 1 commits.
2. **Identical Evidence Event:** Both strategies process the same incoming update: $E_1'$ ($10s$, valid $[10-13, \infty)$).
3. **Identical Target Correctness:** Both strategies must produce the identical correct final ground truth state ($B_1 = 40s, B_2 = \text{FALSE}, B_3 = \text{PASS}, B_4 = \text{TRUE}$) verified by identical assertions.
4. **Execution Boundaries & Database Configuration:**
   - Evaluated under identical SQLite settings: `PRAGMA journal_mode = WAL; PRAGMA synchronous = NORMAL; PRAGMA foreign_keys = ON; PRAGMA temp_store = MEMORY;`
   - All mutations wrapped in a single explicit transaction (`BEGIN IMMEDIATE ... COMMIT`).
   - SQL statement counts include only statements executed from receipt of $E_1'$ to transaction commit, excluding initial connection pool setup and DDL schema creation.
   - Row mutations count all `INSERT`, `UPDATE`, and `DELETE` operations across `assertions`, `beliefs`, `justifications`, and `provenance` tables.
   - Initial cold corpus construction ($CW_{\text{init}}$) is recorded as a separate descriptive metric, not used in the denominator.
   - Wall-clock latency benchmark executes $N = 30$ alternating trials, discarding 3 warm-up runs, reporting median $\pm$ IQR using a monotonic nanosecond timer.

##### Metric Ratios:
- **Statement Ratio:** $WWR_{\text{statements}} = \frac{\text{SQL Statements (Targeted Revalidation)}}{\text{SQL Statements (Full Recomputation)}}$
- **Row-Mutation Ratio:** $WWR_{\text{rows}} = \frac{\text{Mutated Rows (Targeted Revalidation)}}{\text{Mutated Rows (Full Recomputation)}}$
- **Latency Ratio:** $WWR_{\text{latency}} = \frac{\text{Median Latency (Targeted Revalidation)}}{\text{Median Latency (Full Recomputation)}}$
- *Thresholds:* $WWR \le 0.50$ = preregistered target hypothesis ($H_{1b}$); $0.50 < WWR < 1.00$ = partial reduction; $WWR \ge 1.00$ = strict falsification ($H_0$). Synthetic results apply strictly to this benchmark fixture and do not claim demonstrated real-world scaling.

---

### Scope B: Track 2 Metrics (Comparative Evaluation across RI and Baselines)
Evaluates observable output freshness and provenance under scripted prompt conditions.

#### Standardized Belief Probes:
- **$Q_1$ (on $B_1$):** *"What is the worst-case client timeout delay?"* Ground truth: `40s`. Supporting evidence: $\{E_1', E_2\}$.
- **$Q_2$ (on $B_2$):** *"Is there currently a risk of SLA violation?"* Ground truth: `FALSE`. Supporting evidence: $\{E_1', E_2, E_3\}$.
- **$Q_3$ (on $B_3$):** *"Does the system currently comply with POL-SEC-01?"* Ground truth: `PASS`. Supporting evidence: $\{E_4, E_5, E_6\}$.
- **$Q_4$ (on $B_4$):** *"Is embedded process storage active?"* Ground truth: `TRUE`. Supporting evidence: $\{E_7\}$.

#### Metric Definitions, Scoring Precedence & Partition:
Every evaluated probe response $r$ for affected probes $\mathcal{Q}_{\text{affected}} = \{Q_1, Q_2\}$ is classified into **exactly one** of three mutually exclusive categories under a strict precedence hierarchy:

1. **Precedence 1 — Stale Belief ($SBR$):**
   - *Rule:* If the response asserts the superseded Stage 1 value ($120s$ for $Q_1$, `TRUE` for $Q_2$) as currently valid—**including mixed or contradictory responses** that claim both the old and new values are simultaneously active—it is scored as **Stale ($SBR = 1, BFA = 0, RER = 0$)**.
   - *Rationale:* Failing to invalidate the superseded belief is an epistemic staleness failure, even if the new evidence is partially recited.
2. **Precedence 2 — Fresh Correct ($BFA$):**
   - *Rule:* If the response asserts the current ground truth ($40s$ for $Q_1$, `FALSE` for $Q_2$) via domain-normalized equivalence *without* asserting the superseded value as currently active (explanatory context that $120s$ was superseded by a prior version is permitted) $\implies$ **Fresh Correct ($BFA = 1, SBR = 0, RER = 0$)**.
3. **Precedence 3 — Refusal / Non-Stale Error ($RER$):**
   - *Rule:* All remaining responses that do not qualify as Stale or Fresh:
     - *Refusals:* Model explicitly declines to answer (`"I cannot determine the timeout"`).
     - *Hedged / Ambiguous:* Model gives non-committal or uncertain answers without asserting either value as true (`"It might be 40s or perhaps another value"`).
     - *Malformed / Crashes:* Output is unparseable text, empty, or a runner failure.
     - *Unrelated Errors:* Model hallucinates an unrelated scalar or claim (`"The timeout is 999s"`).
     $\implies$ **Refusal / Error ($BFA = 0, SBR = 0, RER = 1$)**.

##### Strict Mathematical Partition:
Because Precedence 1 $\to$ Precedence 2 $\to$ Precedence 3 forms an exhaustive, mutually exclusive classification for every response:
$$\mathbb{I}_{\text{Fresh}}(r) + \mathbb{I}_{\text{Stale}}(r) + \mathbb{I}_{\text{RER}}(r) = 1 \quad \forall r$$
$$BFA + SBR + RER = 1.00$$

#### Citation Coverage, Correctness, and Independence from Factual Truth:
- **Citation Coverage ($CC$):** $CC(Q_j) = \frac{|\text{Citations}(Q_j) \cap \mathcal{E}^*(Q_j)|}{|\mathcal{E}^*(Q_j)|}$ (measures recall of required supporting sources).
- **Citation Correctness ($CCR$):** $CCR(Q_j) = \frac{|\text{Citations}(Q_j) \cap \mathcal{E}^*(Q_j)|}{|\text{Citations}(Q_j)|}$ (measures precision of citations; scored $0.00$ if uncited).
- **Supplementary Jaccard Integrity ($CPI_{\text{Jaccard}}$):** $\frac{|\text{Citations} \cap \mathcal{E}^*|}{|\text{Citations} \cup \mathcal{E}^*|}$.
- **Decoupling of Citations from Factual Correctness:** Citation presence or overlap does **not** establish factual correctness. An LLM may retrieve and cite the correct document ($E_1'$) while still generating an outdated answer ($120s$) due to attention or synthesis failures. Citation metrics evaluate retrieval provenance only.
- **Unaffected-Belief Preservation ($UBP$):** Proportion of invariant probes ($Q_3, Q_4$) answered correctly. Designated as a fixture-specific preservation check, not universal preservation proof.

---

## 6. Execution Procedure: Two-Track Testing

```
+-------------------------------------------------------------------------------+
|                 TRACK 1: ALGORITHMIC MECHANISM CORRECTNESS                    |
|                 (Deterministic Local Fixtures — SQLite & DAG)                 |
+-------------------------------------------------------------------------------+
| Phase 1: Initialize temporary SQLite in-memory fixture                        |
| Phase 2: Ingest E1..E7 -> Assert B1=120s, B2=TRUE, B3=PASS, B4=TRUE (S1)       |
| Phase 3: Submit E1' -> Execute graph closure -> Assert Recall=1.0, B2=FALSE (S2)|
| Phase 4: Submit E8 -> Execute mutex query -> Assert conflict flag on C4 (S3)  |
| Phase 5: Query Tx=10:30 vs Tx=13:30 -> Assert historical B1=200s, B2=TRUE (S4)|
| Phase 6: Retract E2 -> Assert cascading transition of B1, B2 to OUT/INVALIDATED|
| Phase 7: Compute Track 1 Metrics: Recall, Precision, EDA, UBI, WWR            |
+-------------------------------------------------------------------------------+
                                       │
                                       ▼
+-------------------------------------------------------------------------------+
|                 TRACK 2: COMPARATIVE BLACK-BOX EVALUATION                     |
|              (Comparative Natural Language Baselines: RAG / Chat)             |
+-------------------------------------------------------------------------------+
| Phase 1: Initialize isolated sessions (Local RAG, In-Context, ChatGPT, Claude)|
| Phase 2: Upload source documents E1..E7 -> Issue Probes Q1..Q4 (Baseline)     |
| Phase 3: Replace E1 with E1' -> Issue Probes Q1..Q4 -> Score BFA, SBR, RER    |
| Phase 4: Upload conflicting E8 -> Prompt: "What is the authentication mode?"   |
| Phase 5: Issue Probe: "What was the timeout recorded on Day 1 before update?"  |
| Phase 6: Retract E2 (delete file) -> Issue Probes Q1, Q2                      |
| Phase 7: Record CC, CCR, CPI_Jaccard, and LR_local across local baselines     |
+-------------------------------------------------------------------------------+
```

---

## 7. Black-Box Baseline Execution Guidelines

To test external commercial systems (ChatGPT, Claude) without violating API terms or incurring costs:
1. **Interactive Manual Sandbox:** Use standard, non-automated browser sessions in clean project workspaces.
2. **Fixed Prompts:** Use identical, pre-scripted prompts for document upload, query execution, and correction instructions.
3. **No Speculation on Hidden Internals:** Record only observable output text, citations, and UI badges. If a system provides no dependency information, record: `Dependency DAG Exposed: False`. Do not speculate on proprietary backend weights or internal vector stores.
4. **Archival Reproducibility:** Save complete prompt transcripts, document snapshots, and timestamped response outputs in the test archive.

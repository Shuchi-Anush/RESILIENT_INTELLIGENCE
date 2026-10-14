# Graphify Semantic Extraction Experiment

Experiment ID: GRAPHIFY-RECON-003
Experiment date: 2026-10-03
Graphify under test: Graphify 0.9.48 (v0.9.48-s2 cache schema)

---

## 1. Objective

Conduct a tightly-bounded empirical capability experiment to determine what
Graphify 0.9.48 CAN and CANNOT represent when semantic extraction is
(attempted to be) enabled against a small, deliberately designed semantic
test corpus. Specific goals:

- Examine whether Graphify represents evidence objects, claims/assertions,
  evidence ↔ claim linkages, temporal validity, provenance, contradictions,
  belief dependencies, change impact, targeted revalidation, and historical
  knowledge-state transitions.
- Separate what was OBSERVED from what is SUPPORTED by source/help, what is
  INFERRED, what was NOT DEMONSTRATED, and what remains UNKNOWN.
- Use a two-run strategy:
  1. First run attempts the documented `--backend ollama --mode deep`
     semantic extraction (AST + LLM semantic) per Graphify CLI help.
  2. Second run obtains a document-structural graph without LLM (code-only
     bootstrap + `update` to add markdown structural AST nodes) so that the
     document-handling layer can still be examined even when LLM semantic
     extraction is blocked.
- Do NOT claim capabilities beyond what is directly observed.
- Do NOT implement RESILIENT INTELLIGENCE.

## 2. Environment

- **Graphify version / cache schema**: 0.9.48 (cache key version string
  `v0.9.48-s2` seen in `cache/ast/` directories).
- **Graphify executable path**:
  [graphify.exe](file:///D:/RI-GRAPHIFY-TEST/.venv/Scripts/graphify.exe)
  (47,616 bytes, LastWriteTime 2026-10-02 21:22).
- **Python environment**: isolated test venv at `D:\RI-GRAPHIFY-TEST\.venv\`.
- **Ollama availability / state**:
  - Ollama CLI executable IS installed at
    `C:\Users\Shuchi\AppData\Local\Programs\Ollama\ollama.exe` (detected via
    `Get-Command ollama`).
  - However, `ollama list` did not return within a 15-second window
    (consistent with the Ollama background service not running).
  - Per the hard scope boundary, we did NOT start/configure/restart
    Ollama; therefore no model list could be produced.
  - The default model for the `ollama` backend is encoded in
    [llm.py](file:///D:/RESILIENT_INTELLIGENCE/graphify/graphify/llm.py#L127-L134):
    ```python
    "ollama": {
        "base_url": "http://localhost:11434/v1",
        "default_model": os.environ.get("OLLAMA_MODEL", "qwen2.5-coder:7b"),
        ...
    }
    ```
    That default (`qwen2.5-coder:7b`) is what would have been used if the
    backend had connected.
- **Backend connectivity / blockers**:
  - No `OLLAMA_API_KEY` was set. Graphify warned:
    `WARNING: ollama backend selected with no OLLAMA_API_KEY set; sending corpus to http://localhost:11434/v1…`
  - More critically, the ollama backend in this build routes through the
    `openai` Python SDK (it calls Ollama's OpenAI-compatible `/v1` endpoint).
    That package was NOT installed in the test venv. Graphify reported this
    explicitly as a fatal per-chunk error in Run A (see §3).
- **OS/runtime**: Windows 11 / PowerShell 7 / x64.
- **All API keys verified absent** for GEMINI / GOOGLE / MOONSHOT /
  ANTHROPIC / OPENAI / DEEPSEEK / AZURE in the shell environment.

## 3. Exact Experiment Commands

Four attempts were executed. Two produced results; two produced documented
blockers without side effects.

### Run A — Attempted LLM semantic extraction (FAILED with documented cause)

Command (run from `D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\semantic-experiment`):
```
graphify extract .\corpus --backend ollama --model qwen2.5-coder:7b --mode deep --force --out .
```

Runtime wall-clock: **4867 ms**
Exit code: **1**
Stdout verbatim (relevant lines):
```
[graphify] WARNING: ollama backend selected with no OLLAMA_API_KEY set; sending corpus to http://localhost:11434/v1. Set OLLAMA_API_KEY (any non-empty value) to suppress this warning.
[graphify] chunk 1/1 failed: the 'openai' package is required for this backend but is not installed. Install it with:  uv tool install "graphifyy[ollama]" --force  (uv tool), or  pip install openai  (pip/venv install).
[graphify] WARNING: 1/1 semantic chunk(s) failed — see errors above. Partial results returned.
[graphify] WARNING: 5/5 dispatched file(s) produced no nodes and are absent from the graph: 01_lab_reports.md, 02_analyst_report_2024.md, 03_contradicting_study.md, 04_update_correction_2025.md, 05_derived_conclusions_and_revalidation.md. The model returned a response but omitted them; a re-run will retry them.
[graphify extract] error: all semantic chunks failed for backend 'ollama' (5 uncached files) - see per-chunk errors above. If you see 'requires the X package', run `pip install X` and retry.
[graphify extract] deep mode enabled: richer semantic extraction
[graphify extract] --force: full re-scan, semantic cache reads skipped
[graphify extract] scanning D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\semantic-experiment\corpus
[graphify extract] found 0 code, 5 docs, 0 papers, 0 images
[graphify extract] semantic extraction on 5 files via ollama...
```

Result: No graph.json was written in the experiment root (only
`cache/stat-index.json` with 5-file stats was produced).

**Classification of this failure**: OBSERVED blocker — the `ollama` backend
requires the `openai` PyPI package to be installed in the same venv as
Graphify; it was not present. Per the hard scope boundary we did NOT
install packages, so the LLM-mediated semantic extraction path was NOT
exercised end-to-end in this experiment.

### Run B — No backend, doc-only corpus (exit 1)

Command:
```
graphify extract .\corpus --force --no-cluster --out .\no-llm-out
```

Runtime: 391 ms
Exit code: **1**
Stdout verbatim of the error line:
```
error: no LLM API key found (5 doc/paper/image file(s) need semantic extraction). Set GEMINI_API_KEY or GOOGLE_API_KEY (gemini), MOONSHOT_API_KEY (kimi), ANTHROPIC_API_KEY (claude), OPENAI_API_KEY (openai), DEEPSEEK_API_KEY (deepseek), or pass --backend. A code-only corpus needs no key. Or pass --code-only to index just the code (local AST, no key) and skip the non-code files.
```

Classification: Documented. `extract` on a corpus that contains ANY non-code
file refuses to run without either an API key, `--backend`, or `--code-only`.

### Run C — Code-only bootstrap (to create a graphify-out anchor)

Command:
```
graphify extract .\corpus --force --code-only --no-cluster --out .\exp-out
```

Runtime: 1065 ms
Exit code: **0**
Stdout verbatim:
```
[graphify extract] --force: full re-scan, semantic cache reads skipped
[graphify extract] scanning D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\semantic-experiment\corpus
[graphify extract] --code-only: skipping 5 non-code file(s) (5 docs, 0 papers, 0 images) — no LLM extraction
[graphify extract] found 1 code, 0 docs, 0 papers, 0 images
[graphify extract] AST extraction on 1 code files...
[graphify extract] wrote D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\semantic-experiment\exp-out\graphify-out\graph.json — 5 nodes, 5 edges (no clustering)
```

Output graph location (code-only baseline):
[doc-struct-exp-out/graphify-out/graph.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/exp-out/graphify-out/graph.json)

### Run D — `update` over the same corpus to include document structural AST nodes

Command (this uses the documented `update` subcommand which is advertised as
"no LLM needed"):
```
graphify update .\corpus --force --no-cluster
```

Runtime: 1042 ms
Exit code: **0**
Stdout verbatim:
```
Re-extracting code files in D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\semantic-experiment\corpus (no LLM needed)...
[graphify watch] Rebuilt (no clustering): 49 nodes, 44 edges
[graphify watch] graph.json updated in D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\semantic-experiment\corpus\graphify-out
Code graph updated. For doc/paper/image changes run /graphify --update in your AI assistant.
Tip: set GEMINI_API_KEY or GOOGLE_API_KEY to use Gemini for semantic extraction.
```

Output graph location (structural document AST + code anchor; this is the
experiment's primary result graph for capability classification):
[corpus/graphify-out/graph.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/graphify-out/graph.json)

## 4. Test Corpus

Six files under
[semantic-experiment/corpus](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus).
5 markdown docs (1,196 lines / ~8.2 kB across them) deliberately designed
to probe semantic representation. 1 Python code file (anchor_code.py) added
only so a code-only graphify-out anchor exists (its content is semantically
empty by design).

| Document | Tests |
|---|---|
| [01_lab_reports.md](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/01_lab_reports.md) | **Evidence** (raw sensor output ALPHA-001 / ALPHA-002 / BETA-117 from named sources Alpha Lab / Beta Lab, dated 2024-03-15 / 2024-04-02). **Temporal validity** (valid-interval headings). **Provenance** (explicit "Shared Provenance Note" heading — warns these are PRIMARY EVIDENCE not conclusions). |
| [02_analyst_report_2024.md](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/02_analyst_report_2024.md) | **Claims / assertions** (Claim C1 = 5-yr durability; Claim C2 = no-corrosion 5-yr). **Provenance** (lists CITING evidence IDs ALPHA-001 / BETA-117 / ALPHA-002). **Dependency** (explicit dependency section: `C1 DEPENDS-ON {ALPHA-001, BETA-117}`, `C2 DEPENDS-ON ALPHA-002`, revalidation directive if cited evidence changes). |
| [03_contradicting_study.md](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/03_contradicting_study.md) | **Contradiction** (GAMMA-9 field observation contradicts Claim C2). **Evidence** (new evidence ID GAMMA-9 from Dr. L. Ortiz / Gamma Observatory). **Provenance** (Dr. Ortiz names 3 hypotheses for the conflict). **Revalidation hint** (C2 should be treated as INVALIDATED / REQUIRES-REVALIDATION for coastal; C1 NOT contradicted). |
| [04_update_correction_2025.md](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/04_update_correction_2025.md) | **Change** (ALPHA-002 SUPERSEDED by ALPHA-002-REV in retest). **Supersedeure** (ALPHA-002 only invalid for coastal contexts, not globally). **Downstream revalidation request** (explicit: "C2 MUST BE REVALIDATED against ALPHA-002-REV"; "C1 does NOT require revalidation"). **Temporal overlay** (ALPHA-002 natural expiry 2024-09-15 vs ALPHA-002-REV retest 2025-01-18). |
| [05_derived_conclusions_and_revalidation.md](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/05_derived_conclusions_and_revalidation.md) | **Derived beliefs / conclusions** (CONCLUSION-A = clear inland-only release). **Dependency chain** (CONCLUSION-A → C1/C2 → evidence IDs). **State transitions table** (4 datestamped states for C1/C2: SUPPORTED → REQUIRES-REVALIDATION → QUARANTINED). **Change impact** (why C1 does NOT need revalidation). **Revalidation states vocabulary**: `SUPPORTED`, `REQUIRES-REVALIDATION`, `INVALIDATED`, `QUARANTINED` all present in-text. |
| [anchor_code.py](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/anchor_code.py) | Content-free structural anchor (dataclass + method + 2 rationale comments). Not semantically meaningful: only exists so `extract --code-only` produces a graphify-out and therefore `update` will also ingest the markdown docs as structural AST nodes (just like in recon-002's corpus-change-test run). |

## 5. Observed Output

### Structural facts — Run D graph (the completed graph, no LLM used)

From [graph.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/graphify-out/graph.json):

- Graph totals: **49 nodes · 44 edges · undirected**
- Graph-level metadata:
  ```json
  {"input_tokens": 0, "output_tokens": 0, "failed_sources": [], "directed": false}
  ```
  Zero token counts confirm NO LLM-mediated extraction (semantic or
  otherwise) was dispatched. Every node/edge has `_origin="ast"` below.
- `input_tokens: 0` + `output_tokens: 0` is the empirical fingerprint of
  the no-LLM update path (compare with the `--code-only` extract which
  also had 0/0).
- Top-level graph schema keys are identical to recon-002's structural
  graphs: `nodes`, `links`, `directed`, plus the metadata keys above. No
  `communities`, `built_at_commit`, `changes`, `diff`, `hyperedges` keys
  here (consistent with `--no-cluster` flag).

### Node distribution — Run D

| `file_type` | `_origin` | count | what it represents |
|---|---|---|---|
| `code` | `ast` | 3 | Module root `anchor_code`, class `EvidenceAnchor`, method `.record()`. |
| `rationale` | `ast` | 2 | Comment-bodied rationale nodes with `rationale_for` edges. |
| `document` | `ast` | 44 | Entirely `heading` (39) and `page` (5) document AST nodes — one page per doc md file, one heading node per ATX heading. |

Document `node_kind` subdistribution:

| `node_kind` | count | notes |
|---|---|---|
| `page` | 5 | One per markdown file (id = filename-without-ext, label = "filename.md"). |
| `heading` | 39 | One per `#…##…###` heading in the docs. Ids are slugified heading text. |

Concrete document nodes for the semantic concepts the corpus was designed to
probe (heading nodes — all `_origin=ast`, `file_type=document`,
`node_kind=heading`):

- Evidence heading nodes: `01_lab_reports_*…alpha_lab*`, `*report_date_2024_03_15*`,
  `*valid_interval_2024_03_15_…*`, `*beta_lab*`, etc. (all exist as heading
  label slugified ids).
- Claim heading nodes: `02_analyst_report_2024_claim_c1_…_derived`,
  `02_analyst_report_2024_claim_c2_…_derived`.
- Contradiction heading node:
  `03_contradicting_study_claim_contradicts_c2_direct_opposition`.
- Supersession / change heading nodes:
  `04_update_correction_2025_new_evidence_alpha_002_rev_supersedes_alpha_002`,
  `04_update_correction_2025_supersession_statement_explicit`,
  `04_update_correction_2025_explicit_downstream_revalidation_request_by_alpha_lab`.
- Conclusion / derived belief node:
  `05_derived_conclusions_and_revalidation_conclusion_conclusion_a_release_decision`.
- Historical state transition node:
  `05_derived_conclusions_and_revalidation_knowledge_state_transitions_recorded_in_this_document_historical`.

**Important**: these 39 heading nodes are **text-label containers only**.
Each node object has exactly these fields (instantiated for one as example):
```json
{
  "id": "03_contradicting_study_claim_contradicts_c2_direct_opposition",
  "label": "Claim CONTRADICTS-C2 (direct opposition)",
  "file_type": "document",
  "node_kind": "heading",
  "source_file": "03_contradicting_study.md",
  "source_location": "L12",
  "_origin": "ast"
}
```
There is NO `confidence` on nodes, NO `belief_state`, NO
`valid_from/valid_to`, NO `evidence_refs`, NO `claim_id`, NO
`supersedes/was_superseded_by` on any document node. The semantic content
is present only as the human-readable label string and the file/line
source_location.

### Edge distribution — Run D

| relation | count | confidence | _origin | semantic interpretation |
|---|---|---|---|---|
| `contains` | 40 | EXTRACTED (weight 1.0) | ast | Document-page → heading → sub-heading nesting. No cross-document edges. |
| `rationale_for` | 2 | EXTRACTED (weight 1.0) | ast | Code-comments → class / code module (not used for doc semantics). |
| `method` | 1 | EXTRACTED (weight 1.0) | ast | Code class → method (structural). |
| `imports_from` | 1 | EXTRACTED (weight 1.0) | ast | Code module → `dataclasses` stdlib import (structural). |
| **Any other relation** | **0** | | | |

**Edge-level crucial observations** (semantic content of corpus):

1. **0 edges link 02_analyst_report_2024's Claim C1 / Claim C2 heading nodes
   back to any lab-reports evidence heading nodes.** The explicit
   `C1 DEPENDS-ON ALPHA-001 / BETA-117` dependency statements in the
   analyst report produced no `supports`, `depends_on`, `cites`,
   `cites_evidence`, `derived_from`, or analogous edges in the graph.
2. **0 edges link the contradiction study to Claim C2.** The heading
   "Claim CONTRADICTS-C2 (direct opposition)" sits as a child of its own
   document page via a `contains` edge only — no `contradicts`,
   `opposes`, `conflicts_with` edge connects to the Claim C2 node.
3. **0 edges link ALPHA-002-REV (supersession heading) to ALPHA-002.**
   There is no `supersedes`, `replaces`, `updates`, `obsoletes` edge
   between the two headings even though the heading text names them.
4. **0 edges cross document boundaries at all.** Every `contains` edge
   chain lives entirely within a single markdown document's heading
   hierarchy (plus the code-structural edges, which are intra-file).
5. **0 edges have a state-transition semantics.** Nothing encodes
   `SUPPORTED → REQUIRES-REVALIDATION → QUARANTINED` even though all
   three strings are present in heading/text content.
6. **All edges EXTRACTED (100%).** There are 0 INFERRED edges and 0
   AMBIGUOUS edges in this graph (compare with recon-002's structural
   baseline — which had 1 `uses` INFERRED edge).
7. The `rationale_for` relation IS present (for code comments). This
   demonstrates Graphify DOES have a "this textual statement explains
   this structural entity" edge primitive for code — it just was not
   generated for the markdown evidence/claim/contradiction/dependency
   headings in the no-LLM structural run.

### Provenance / source locations — Run D

All 49 nodes carry `source_file + source_location + _origin`:

- **Accurate for document headings**: e.g. heading "Observation GAMMA-9"
  has `source_file=03_contradicting_study.md`, `source_location=L7` —
  correct (it is an H2 on line 7 of that file).
- **Accurate for code**: method `.record()` has `source_file=anchor_code.py`,
  `source_location=L14` — correct.
- **Only one direction of provenance** is stored: node/edge → *current*
  source. There is no `evidence_for`, `supports_claim`, `was_derived_by`
  edge from document nodes to other document nodes. Provenance is about
  "where did this graph element come from in the source corpus", NOT about
  "which source evidence supports this document claim".

### Manifest / cache — Run D

From [manifest.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/graphify-out/manifest.json):

- All 6 files have `semantic_hash = ""` (empty string). Another direct
  marker that NO semantic (LLM) extraction was performed (consistent
  with update's "(no LLM needed)" banner).
- Each file has a distinct `ast_hash` (MD5 of parsed markdown AST),
  `mtime`, and `seen` timestamp — same incremental manifest pattern as
  recon-002.
- AST cache contains 6 `v0.9.48-s2/…` JSON files with names matching
  manifest `ast_hash` values (content-addressable AST cache).

## 6. Capability Matrix

Classification rule (verbatim from §6 of the task brief):
- **OBSERVED** — directly demonstrated in generated artifacts/runtime.
- **SUPPORTED** — explicitly supported by Graphify source / help, but not
  demonstrated in this experiment.
- **INFERRED** — reasonable interpretation of observed behavior, not
  explicit.
- **NOT DEMONSTRATED** — experiment provides no evidence Graphify supports
  it (NOT a claim that Graphify cannot do it).
- **UNKNOWN** — experiment could not determine it.

**Evidence links in the "Evidence" column point to graph nodes/edges or
help/source locations.**

| Capability | Classification | Evidence | Notes |
|---|---|---|---|
| Entity representation | OBSERVED | [graph.json nodes](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/graphify-out/graph.json#L5-L445): 49 nodes exist (`id`, `label`, `file_type`, `source_file`, `source_location`, `_origin`). Heading nodes encode entities like "Claim C1", "ALPHA-002-REV", "CONCLUSION-A" as slugified `id`s + human-readable `label`s. | Entities ARE represented — as structural heading/page nodes with a stable `id` scheme (`<docname>_<slugified_heading_text>`). Entities are *granular only to heading level*; the paragraphs beneath a heading are NOT decomposed into further sub-entities. |
| Semantic relations | NOT DEMONSTRATED (structural `contains` / `rationale_for` OBSERVED; cross-doc semantic NOT) | [graph.json links](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/graphify-out/graph.json#L446-L888). Intra-doc structural: `contains`=40, `rationale_for`=2. Cross-doc: 0 edges. 0 edges of the kinds `depends_on / supports / cites / contradicts / supersedes / derived_from`. | The heading-text *states* these relations but Graphify's no-LLM document parser left them as text labels. |
| Evidence objects | NOT DEMONSTRATED (heading nodes *labeled* "Evidence …" exist but have no evidence-type schema fields) | Example node id `01_lab_reports_…_evidence_alpha_002_rev_supersedes_alpha_002` has 6 standard fields; 0 evidence-specific fields (evidence_id, source, method_ref, sensor_values, raw_data). | An evidence heading exists; its "evidence objectness" is purely in its label string. |
| Claim/assertion objects | NOT DEMONSTRATED (same caveat) | Claim C1/C2 nodes exist as heading labels only. No `proposition`, `truth_value`, `claim_id`, `claim_status` fields. | Schema does not distinguish a Claim heading node from any other heading node structurally. |
| Evidence→claim linkage | NOT DEMONSTRATED | 0 cross-doc edges. 0 edges between any ALPHA/BETA heading and C1/C2 headings. The linkage is encoded in the heading text of "Dependency graph (explicit, by analyst)" heading — but that heading is a `contains` child of the analyst report page, with 0 out-links to evidence nodes or claim nodes. | Heading text contains the references but the graph edges do not. |
| Temporal validity | NOT DEMONSTRATED | Heading nodes titled "Report Date: 2024-03-15" and "Valid Interval: 2024-03-15 → 2024-09-15 (6-month scheduled retest)" exist as heading labels. No `valid_from`, `valid_to`, `start`, `end`, `publication_date`, `retest_date` fields. | Dates are substrings of label strings only. No graph-level temporal field or edge is structured. |
| System/record time | OBSERVED at manifest level only | [manifest.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/graphify-out/manifest.json): per-file `seen` timestamp (1791018670.3768 — corresponds to the 2026-10-03 run time of the experiment). | "Record time" is the `seen` field in the manifest. The graph nodes/edges do not carry ingestion or process timestamps. |
| Provenance | OBSERVED (current-source location only). NOT DEMONSTRATED for evidence-to-claim provenance chains. | All nodes carry `source_file + source_location + _origin`. Example `03_contradicting_study_observation_gamma_9` node correctly points to L7 of the correct file. | Provenance is *syntactic source-location* provenance, not *evidential support* provenance. |
| Epistemic confidence (separate from EXTRACTED/INFERRED) | NOT DEMONSTRATED | Graphify documents [llm.py BACKENDS](file:///D:/RESILIENT_INTELLIGENCE/graphify/graphify/llm.py#L101-L197) and edges have `confidence` and (in recon-002's graphs) `confidence_score`. In Run D: all 44 edges = EXTRACTED / weight 1.0 / no confidence_score on edges (it's optional). Nodes never carry a confidence or belief-strength field in any run we observed. | `confidence` on edges is *extraction-method confidence* (how was the edge derived). It is not epistemic belief confidence. |
| Contradiction representation | NOT DEMONSTRATED | A heading node *labeled* "Claim CONTRADICTS-C2 (direct opposition)" exists. 0 edges of type `contradicts / opposes / conflicts_with` connect it to the `02_analyst_report_2024_claim_c2_…_derived` node. | Again: only the label text encodes it. |
| Evidence→belief dependency | NOT DEMONSTRATED | 0 edges between heading nodes of kind `depends_on / relies_on / prerequisite / evidence_for / supports`. | The test corpus explicitly wrote `C1 DEPENDS-ON ALPHA-001` as body text; the structural document parser did not materialize it into an edge. |
| Change impact | NOT DEMONSTRATED | Supersession heading node exists but 0 `supersedes / updates / obsoletes` edge. No node/edge carries `before_state / after_state / trigger_event`. | |
| Targeted revalidation | NOT DEMONSTRATED | Explicit Downstream Revalidation Request heading exists as a label. No edges of type `requires_revalidation`, no state-transition links, no `trigger → affected_nodes` edges. | |
| Historical state reconstruction | NOT DEMONSTRATED | "Knowledge-state transitions recorded in this document (historical)" is a heading-label slug. No graph key (`history`, `snapshots`, `versions`, `state_transitions`) exists in graph.json. | |

Two additional capabilities are row-worthy because they were exposed in
other artifacts:

| Capability (not in original list, added for completeness) | Classification | Evidence | Notes |
|---|---|---|---|
| `rationale_for` edge primitive (text explains a code entity) | OBSERVED (for code comments) | [graph.json L478-L496](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/semantic-experiment/corpus/graphify-out/graph.json#L478-L496): two `rationale_for` edges of `confidence=EXTRACTED weight=1.0 origin=ast`. | This is the closest relation Graphify demonstrated that is "semantic" in the sense of (text-blob → structural-entity explanatory link). It was not observed for document → document rationale/evidence. |
| LLM-mediated deep semantic extraction pipeline (code + CLI + help attestation) | SUPPORTED (not demonstrated) | [cli.py extract help](file:///D:/RI-GRAPHIFY-TEST/.venv/Scripts/graphify.exe --help) `extract --backend B … --mode deep`; [llm.py BACKENDS](file:///D:/RESILIENT_INTELLIGENCE/graphify/graphify/llm.py#L101-L197) ollama/gemini/claude/openai/deepseek/kimi/azure/bedrock entries; Run A stdout explicitly said "semantic extraction on 5 files via ollama…" then "all semantic chunks failed". | Source code and CLI attest that semantic extraction *path* exists, but it was blocked by missing `openai` package in this venv + no running Ollama server. The task boundary does not allow installing `openai` or starting Ollama, so we cannot classify beyond SUPPORTED. |

## 7. Structural vs Semantic Dependency

### Structural / code dependency (OBSERVED)

This is what Graphify demonstrated without question in all three recon
experiments (structural, update, this semantic-exp):

- For code: `contains` (file → class → method), `imports_from`, `method`,
  and in recon-002 also `calls` edges (AST-derived).
- For markdown docs: `contains` (page → heading → sub-heading), with nodes
  representing the *syntactic outline* of the document, not its
  propositional content.
- `rationale_for` is a limited semantic bridge: a code comment with
  `# WHY: …` generates a node with `file_type=rationale` and a
  `rationale_for` edge pointing at a code entity. So "X is the rationale
  behind Y" IS a first-class edge relation type in the Graphify schema —
  for code comments.

### Evidentiary / semantic dependency (NOT DEMONSTRATED)

Despite the corpus explicitly encoding:
- `C1 DEPENDS-ON ALPHA-001` and `C1 DEPENDS-ON BETA-117`
- `C2 DEPENDS-ON ALPHA-002`
- `ALPHA-002 SUPERSEDED BY ALPHA-002-REV for coastal`
- `C2 → REQUIRES-REVALIDATION after GAMMA-9 / after ALPHA-002-REV`
- `GAMMA-9 directly contradicts C2`
- `C1 does NOT require revalidation (its upstream evidence unchanged)`

…in the resulting graph, there is **exactly zero cross-file document edge
of any kind**. All evidence→claim / contradiction / supersession /
state-transition content is preserved only as heading label text inside
each document's `contains` tree.

The RI research question asks about this specific layer:
> When one piece of evidence changes, does explicit dependency-aware
> revalidation reduce unnecessary recomputation and stale derived beliefs
> while preserving correctness?

For that question to be answerable by Graphify output alone in its
current demonstrated form, Graphify would need to materialize edges
between *evidence nodes* and *belief nodes* (not just between a document
page and its headings). That did not happen — either because:

(a) the LLM-mediated semantic extraction path was not exercised
(end-to-end blocked by missing `openai` package + no Ollama server), so
the no-LLM document structural pass never attempts to extract
propositions; or

(b) even with LLM enabled, those relation types might not be generated.
This experiment cannot distinguish (a) vs (b). Classify as NOT
DEMONSTRATED (not "does not exist").

## 8. Confidence Semantics

Two distinct confidence concepts must be kept apart, and Graphify only
exposes one of them in its graph schema.

### What Graphify's `confidence` field ACTUALLY means (evidence-based)

Every edge in the produced graphs carries a `confidence` enum:
`EXTRACTED | INFERRED | AMBIGUOUS` (recon-002 also showed `confidence_score`
as a numeric complement on some edges).

From direct observation across all 3 recon experiments:

- **`confidence = EXTRACTED`** + `_origin = ast` → "This edge was
  deterministically produced by the AST/doc parser from concrete syntax
  in the source file." 100% of the 44 edges in Run D qualify, 26/27 edges
  in recon-002 baseline qualify. The label text is a 1:1 transcription of
  what exists in source.
- **`confidence = INFERRED`** + `_origin = ast` → "This edge is a
  heuristic projection derived FROM extracted entities but not directly
  present in the AST syntax." Recon-002's structural baseline contained
  exactly one such edge: `InventoryService --uses--> Warehouse` with
  `confidence_score=0.95` (the pattern: a class stores another class in
  `self.warehouse` and calls methods on it → `uses` relation inferred).
- **`confidence = AMBIGUOUS`** — 0 observed across the 3 experiments.

### What Graphify's `confidence` field DOES NOT mean (critical for RI)

It is NOT:
- "How strongly does evidence ALPHA-001 support Claim C1?"
- "What is the analyst's posterior on C2 given GAMMA-9 and ALPHA-002-REV?"
- "What is the probability that this belief has NOT become stale since its
  last revalidation?"

The corpus's heading text labels actually contained the exact strings
"HIGH support" (for ALPHA-001), "factor 1.44×" (for C1's 5-yr bar
exceedance), "15% of a 20-unit sample" (for GAMMA-9), and explicit
epistemic statuses: "SUPPORTED / REQUIRES-REVALIDATION / INVALIDATED /
QUARANTINED". None of these are parsed into node-level or edge-level
epistemic fields in the graph. They are substrings of the label.

### Confidence semantics summary

Within this experiment, Graphify's confidence fields answer the question
"*how did the extractor obtain this edge?*" They never answered the
question "*how much should I believe the proposition this edge/node
represents?*" — the epistemic confidence / degree-of-support concept
central to RI.

## 9. Implications for RESILIENT INTELLIGENCE

Statement of the RI research question (repeated from §7):
> When one piece of evidence changes, does explicit dependency-aware
> revalidation reduce unnecessary recomputation and stale derived beliefs
> while preserving correctness?

Tally of what Graphify demonstrably provides vs what RI still needs:

| RI building block | Graphify 0.9.48 (this experiment's verdict) |
|---|---|
| **Evidence nodes** with stable id, source_location, and parser-level provenance | Structural heading ids + locations PROVIDED (OBSERVED); evidence *type* fields NOT PROVIDED. |
| **Claim/belief nodes** with stable id | Same: heading nodes PROVIDED (OBSERVED); claim *proposition* fields NOT DEMONSTRATED. |
| **Explicit evidence → claim dependency edges** | NOT DEMONSTRATED as graph edges. The corpus encodes them in body text; the graph's no-LLM pass leaves them as text labels. |
| **Contradiction (evidence vs claim or claim vs claim)** | NOT DEMONSTRATED as edges. Heading labels mention it. |
| **Supersedure / change of evidence** (ALPHA-002 → ALPHA-002-REV) | NOT DEMONSTRATED as edges. |
| **Derivation / conclusion chains** (CONCLUSION-A ← C1,C2 ← ALPHA/BETA) | NOT DEMONSTRATED as edges. |
| **Temporal validity** (ALPHA-001's 2024-03-15→2024-09-15) | NOT DEMONSTRATED as graph-level start/end fields. Inside labels only. |
| **Knowledge state transitions** (SUPPORTED → REQUIRES-REVALIDATION → QUARANTINED) | NOT DEMONSTRATED. The 4-timestamp history table exists in body text but not as graph edges or fields. |
| **Graph-level change / diff / history representation** | NOT DEMONSTRATED (no `changes`, `history`, `before`, `after` keys). |
| **Targeted revalidation** ("mark C2 only, not C1") | NOT DEMONSTRATED as a graph primitive or analysis output. |
| **`rationale_for` (text-blob → code-entity) edge primitive** | OBSERVED. Could plausibly be extended for doc rationale in a LLM pass. Not demonstrated in doc-doc case. |
| **`affected <X>` reverse traversal CLI** | SUPPORTED in CLI (help text says `affected "X"` performs reverse traversal to find nodes impacted by X). UNKNOWN whether it would find cross-doc semantic deps since none were in this graph. |
| **LLM `--mode deep` pipeline + semantic cache** | SUPPORTED (source + help confirm). NOT DEMONSTRATED END-TO-END (blocked by missing `openai` pkg + no running Ollama service). Whether that mode produces the missing evidence/claim relations is UNKNOWN. |

Boundary statement (this experiment does NOT justify):
- "Graphify has no semantic extraction capability" — FALSE to say; the
  source and CLI document the opposite; the failure here was a blocked
  execution environment, not absent code.
- "Graphify cannot represent evidence→belief dependencies" — FALSE to
  say; we simply did not observe such edges in the successful no-LLM
  structural run of this experiment.

Boundary statement (this experiment DOES justify):
- Within this experiment, Graphify's successfully demonstrated
  representation layer for 5 semantic markdown documents is a
  **syntactic document-outline graph**: nodes are heading slug-ids with
  labels, edges are `contains` within each document, provenance is the
  current source file/line.
- Any representation richer than that (including the specific
  dependency/change/state/evidence linkage properties the RI question
  needs) was not produced in the successful run D.

## 10. Limitations

1. **Small corpus.** 5 md files + 1 code file; ~8.2 kB. Results cannot be
   extrapolated to large corpora, graphs with clustering, or mixed
   code+pictures+pdfs extraction.
2. **LLM-mediated semantic extraction was NOT end-to-end executed.**
   - Ollama backend: `--backend ollama --model qwen2.5-coder:7b --mode deep`
     failed because the `openai` package is not installed in the venv
     (documented verbatim error).
   - All other backends (Gemini/Anthropic/OpenAI/DeepSeek/Kimi/Azure): no
     API keys configured; the boundary forbids adding any.
   - Ollama service itself: not running; task boundary forbids starting
     it, so even with `openai` installed we likely would not reach
     models.
   Result: classification for any property only an LLM could produce is
   pinned at either SUPPORTED or NOT DEMONSTRATED, never OBSERVED with
   the qualifier "via LLM semantic extraction".
3. **Local model limitations.** The default `qwen2.5-coder:7b` (per
   llm.py BACKENDS) is a 7B parameter code model; we cannot attest to
   how a research-grade semantic model (e.g. a longer-context
   instruction-tuned model) would handle the corpus.
4. **Semantic extraction limitations specific to Graphify update path.**
   Run D used `update` (advertised as "no LLM needed") — it intentionally
   does not call LLM, so semantic depth was not expected. The
   alternative `extract --mode deep` with an LLM backend is the intended
   semantic path per help, but it was blocked.
5. **Anything not experimentally demonstrated** includes, specifically:
   clustering output, community labels with a semantic naming backend,
   `.graphify_analysis.json` cohesion / bridge-question content (we used
   `--no-cluster` to stay fast), the `affected` CLI on semantic edges,
   the `query` CLI for semantic traversal, save-result memory, and
   reflect-style lesson aggregation.
6. **Version/runtime.** Graphify 0.9.48 / v0.9.48-s2 only. A newer
   Graphify version could add explicit evidence/claim/dependency schema
   — not tested. The single-file `graphify.exe` was built 2026-10-02
   from commit `ce8aab637c55aa5f7cb3aee9e438f50b79e4b2fa` (per
   `built_at_commit` in recon-002 baseline).

## 11. Final Evidence-Based Conclusion

1. Graphify 0.9.48 **OBSERVED structural representation for documents**
   (via the successful `update` path which is "(no LLM needed)"): a
   heading/page outline graph with nodes for every markdown heading and
   `contains` edges for document nesting. 49 nodes / 44 edges were
   produced across 6 files.
2. Graphify **OBSERVED extraction-method confidence** semantics
   (EXTRACTED / INFERRED / AMBIGUOUS with `_origin=ast`) on every edge
   in every graph produced in this project's 3 recon experiments. This
   tells us *how* an edge was produced.
3. Graphify **SUPPORTED an LLM-mediated semantic extraction pipeline**
   through its `extract --backend <backend> --mode deep` command,
   `llm.py` BACKENDS dict (9 backends documented including Ollama,
   Gemini, Claude, OpenAI, DeepSeek, Kimi, Azure, Bedrock), and the
   semantic-cache layout (`cache/semantic/` + `cache/semantic-deep/`
   directories referenced in `cache.py`). This pipeline was NOT
   exercised end-to-end here because the Ollama backend required the
   `openai` package which is not installed in the test venv and the
   Ollama service was not running.
4. Within the successful no-LLM structural document graph (Run D):
   the corpus's explicit **evidence / claim / contradiction /
   dependency / supersession / state-transition / revalidation**
   propositions are **NOT DEMONSTRATED as structured graph artifacts
   (edges, typed nodes with semantic fields, state-transition records,
   or cross-document linkages)**. Each exists only as substring content
   of the `label` field of a heading node inside its own document's
   `contains` tree. Zero cross-document document edges exist.
5. Consequently, the specific RI property of explicit evidence→belief
   dependency links driving targeted revalidation when evidence changes
   is **NOT DEMONSTRATED in the graph produced by this experiment**.
   Converting "NOT DEMONSTRATED" to "Graphify cannot do this" would be
   unsound — the semantic extraction path was blocked by the execution
   environment, not by absent code. The SUPPORTED classification for
   the semantic pipeline keeps the question open for a future
   environment that satisfies the `openai` package + running Ollama
   prerequisites.
6. The strongest positive semantic primitive Graphify did demonstrate is
   the `rationale_for` edge for code comments — meaning Graphify's
   schema is *capable* of representing "textual statement X explains
   structural entity Y" with EXTRACTED confidence. A plausible
   hypothesis (INFERRED, not OBSERVED) is that a successful
   `extract --mode deep` run might produce analogous edges or node
   types for documents. Verifying or falsifying that hypothesis lies
   outside the scope boundary of GRAPHIFY-RECON-003.

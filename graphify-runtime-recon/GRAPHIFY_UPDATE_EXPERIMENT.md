# GRAPHIFY_UPDATE_EXPERIMENT — Single Rename (reserve → reserve_item)

## 1. Experiment Objective

Determine empirically what Graphify 0.9.48's `update` command actually does when a
single method signature is renamed in an otherwise-unchanged corpus copy. Focus on:
- Node add/remove/rename behavior
- Edge add/remove behavior and provenance fields
- Whether the rebuild is *incremental* or *full* (and on what scope)
- Whether stale graph information is preserved
- Whether Graphify exposes an explicit change/diff representation
- Whether clustering/report generation reruns
- Distinguish OBSERVED from INFERRED from NOT DEMONSTRATED

## 2. Environment / Runtime

- Graphify executable: `D:\RI-GRAPHIFY-TEST\.venv\Scripts\graphify.exe` (version reported
  by cache layout = `v0.9.48-s2`)
- Controlled corpus copy: `D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\corpus-change-test`
  (byte-identical copy of baseline corpus BEFORE the single-line rename — verified
  per SHA-256 of all 5 files: README.md, architecture.md, notes.md, sample.py, sample2.py)
- Baseline reference graph: `D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\output\graphify-out\graph.json`
  (21 nodes / 27 links / 4 communities — preserved UNTOUCHED throughout this experiment)
- Update output directory (auto-created by Graphify):
  `D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\corpus-change-test\graphify-out`
- Dedicated experiment staging directory (used to *attempt* a targeted update,
  documenting the wrong-syntax failure, but not used for the actual result):
  `D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\output-update-exp`
- No API keys, no Ollama, no external LLM configured or contacted.

## 3. Baseline State (from `output/graphify-out/`)

From [graph.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/output/graphify-out/graph.json):

- 21 nodes (14 `code/ast`, 7 `rationale/ast` — 0 document nodes because baseline
  extract used `--code-only` per the prior recon log)
- 27 links (26 `EXTRACTED`/`ast` + 1 `INFERRED`/`ast`)
- 4 communities (0=6, 1=6, 2=5, 3=4 nodes)
- `built_at_commit` = `ce8aab637c55aa5f7cb3aee9e438f50b79e4b2fa`
- InventoryService method node of interest:

| Field | Value |
|-------|-------|
| `id` | `sample_inventoryservice_reserve` |
| `label` | `.reserve()` |
| `community` | `1` |
| `community_name` | `Community 1` |
| `source_file` | `sample.py` |
| `source_location` | `L20` |
| `_origin` | `ast` |
| `file_type` | `code` |

Edges incident on this node (baseline):

1. `sample_inventoryservice --method--> sample_inventoryservice_reserve`
   (EXTRACTED 1.0 / L20 sample.py / weight 1.0)
2. `sample_inventoryservice_reserve --calls--> sample2_record_event`
   (EXTRACTED 1.0 / L23 sample.py / call context / weight 1.0)

Manifest [manifest.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/output/graphify-out/manifest.json)
shows baseline manifest hashes:

- `sample.py` — `ast_hash=a8d399814a5f7a10115f9a5a6571fd5c`, `seen=1790956990.97789`
- `sample2.py` — `ast_hash=d8d1d31591e5dfc327b5c0b6f3703c49`, `seen=1790956990.97789`
- No README/architecture/notes entries in baseline manifest (consistent with --code-only)

## 4. Controlled Change

File:
[corpus-change-test/sample.py](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/corpus-change-test/sample.py#L20-L23)

```diff
-    def reserve(self, sku: str, qty: int) -> None:
+    def reserve_item(self, sku: str, qty: int) -> None:
         # WHY: reservation happens only after check_stock succeeds.
         self.warehouse.decrement(sku, qty)
         record_event("stock_reserved", sku)
```

Everything else in `corpus-change-test` is byte-identical to the baseline corpus
(including the body/comments of `reserve_item`, the imports of `sample.py`, and
all of `sample2.py`, `README.md`, `architecture.md`, `notes.md`).

Baseline corpus under `corpus/` was **confirmed unchanged** — it still contains
`def reserve(` at line 20 of its sample.py.

## 5. Commands Executed

Command 1 — inspect update help (no-op):
```
graphify update --help
```
Output (relevant line, verbatim):
```
Run 'graphify --help' for full usage.
```
(The `--help` flag on the subcommand was not expanded by Graphify's CLI; we instead
used the global `--help` from the prior recon session which documented `update`
as: `update <path> — re-extract code files and update the graph (no LLM needed);
--force overwrite graph.json even if the rebuild has fewer nodes;
--no-cluster skip clustering, write raw extraction only`.)

Command 2 — incorrect syntax (documented for completeness; **did NOT produce the
experimental result**):
```
cd D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\output-update-exp
graphify update D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\corpus-change-test --out D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\output-update-exp --force
```
Result (verbatim):
```
error: unknown update option: --out
```
Exit code = 2. `--out` is a flag for the `extract` command, not `update`. This
also demonstrates that `update` does NOT have a `--out` option — it always writes
to `<path>/graphify-out/` relative to the *corpus* path, not a provided
"output root" path.

Command 3 — correct syntax (the actual experiment run; verified exit = 0,
runtime 1.309 s wall clock):
```
cd D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\output-update-exp
graphify update D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\corpus-change-test --force
```
STDOUT (verbatim):
```
Re-extracting code files in D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\corpus-change-test (no LLM needed)...
[graphify watch] Rebuilt: 30 nodes, 34 edges, 6 communities
[graphify watch] graph.json, graph.html and GRAPH_REPORT.md updated in D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\corpus-change-test\graphify-out
Code graph updated. For doc/paper/image changes run /graphify --update in your AI assistant.
Tip: set GEMINI_API_KEY or GOOGLE_API_KEY to use Gemini for semantic extraction.
```

## 6. Before / After Node Comparison

### 6.A Structural counts

| Metric | Baseline (`output/graphify-out`) | After update (`corpus-change-test/graphify-out`) | Delta |
|--------|----------------------------------|--------------------------------------------------|-------|
| Total nodes | 21 | 30 | **+9** |
| Total links | 27 | 34 | **+7** |
| Communities | 4 | 6 | **+2** |
| `code/ast` nodes | 14 | 14 | 0 |
| `rationale/ast` nodes | 7 | 7 | 0 |
| `document/ast` nodes | 0 | 9 | **+9** |

### 6.B InventoryService-reserve-specific — the controlled rename

#### Node REMOVED: 1
OBSERVED exactly one node id is no longer present in the post graph:

```json
{"id":"sample_inventoryservice_reserve",
 "label":".reserve()",
 "_callable":true,
 "_origin":"ast",
 "community":1,
 "community_name":"Community 1",
 "file_type":"code",
 "norm_label":".reserve()",
 "source_file":"sample.py",
 "source_location":"L20"}
```

Evidence: baseline [graph.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/output/graphify-out/graph.json#L106-L116)
vs post-update [graph.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/corpus-change-test/graphify-out/graph.json)
(no `id` matches `*reserve*` except the new one).

#### Node ADDED: 1
OBSERVED exactly one `*reserve*` id is present in the post graph that wasn't in baseline:

```json
{"id":"sample_inventoryservice_reserve_item",
 "label":".reserve_item()",
 "_callable":true,
 "_origin":"ast",
 "community":2,
 "community_name":"InventoryService",
 "file_type":"code",
 "norm_label":".reserve_item()",
 "source_file":"sample.py",
 "source_location":"L20"}
```

Key observations on naming / provenance:
- **Node ID CHANGED** — `sample_inventoryservice_reserve` →
  `sample_inventoryservice_reserve_item`. The id scheme is
  `<filename>_<classname>_<methodname>` and method-name is part of the identity
  key. Graphify does **NOT** treat this as a "rename" with any stable ID
  (`prev_id`, `replaces`, etc. — no such fields exist anywhere in the post
  graph).
- **Node LABEL CHANGED** — `.reserve()` → `.reserve_item()`.
- **`source_file`** remained `sample.py`.
- **`source_location`** remained `L20` (the method still starts on line 20).
- **`community` CHANGED** — 1 → 2. Communities were RE-clustered.
- **`community_name` CHANGED** — `"Community 1"` → `"InventoryService"`.
  Community labels were generated (document-side node contribution allowed
  renaming — see §9).

#### 9 additional document nodes (unrelated to rename but explain the +9 delta)

These are 3 markdown documents (README.md, architecture.md, notes.md) each
contributing 3 nodes (document root, heading, paragraph-style content; all
`file_type=document`, `_origin=ast`). They were indexed in the post run because
`update` (unlike the baseline `extract --code-only`) does **NOT** default to
code-only and has no `--code-only` flag. Baseline deliberately suppressed docs
with `--code-only`; `update`'s defaults include them.

### 6.C Preservation of stale information

OBSERVED — **No stale references remain to the old id**:
- 0 edges in the post graph reference `sample_inventoryservice_reserve` as
  source or target.
- 0 nodes in the post graph have `id`, `label`, `norm_label` matching
  `*reserve()` (only `.reserve_item()` exists).
- No "tombstone", `deleted_at`, `replaced_by`, `renamed_from` or similar
  retention markers exist on nodes or at the graph top-level.

INFERENCE: Graphify performs whole-file re-extraction, removing the AST-derived
node for the deleted name entirely. There is no observable "soft delete" or
historical graph layer in graph.json.

## 7. Before / After Edge Comparison

### 7.A InventoryService-reserve-specific edges

Edges REMOVED (2, all related to old method identity):
1. `sample_inventoryservice --method--> sample_inventoryservice_reserve`
   (EXTRACTED 1.0, source_file=sample.py, source_location=L20)
2. `sample_inventoryservice_reserve --calls--> sample2_record_event`
   (EXTRACTED 1.0, source_file=sample.py, source_location=L23, context="call")

Edges ADDED (2, symmetrically replacing the above around the new identity):
1. `sample_inventoryservice --method--> sample_inventoryservice_reserve_item`
   (EXTRACTED 1.0, **source_file=sample.py, source_location=L20**)
2. `sample_inventoryservice_reserve_item --calls--> sample2_record_event`
   (EXTRACTED 1.0, **source_file=sample.py, source_location=L23, context="call"**)

OBSERVED on these 4 transitions:
- **`source_file`/`source_location` are updated correctly** — the new method-edge
  points to the same L20 as the class→method structural location (accurate).
  The renamed-method→`record_event` call edge still points to L23 accurately
  (since that line moved line-number-wise by 0).
- **Confidence categories DID NOT CHANGE on these delta edges**: They stay
  `EXTRACTED` with `confidence_score=1.0`, `_origin=ast`, `weight=1.0`. Graphify
  treats the newly-discovered `reserve_item` method call as AST-grounded, same
  as any pre-existing call.
- **No INFERRED edges were added or removed by this rename.**

### 7.B Cross-cutting: total INFERRED / EXTRACTED distribution

Baseline (27 edges):
- EXTRACTED / ast: 26 edges (score 1.0)
- INFERRED / ast: 1 edge — `InventoryService --uses--> Warehouse` (score 0.95)

Post (34 edges, delta = +7):
- We compared the confidence-level of every new `*reserve*` / document edge in
  the post graph. Document edges are ALL `EXTRACTED / ast` with
  `confidence_score=1.0` (document `contains` subnodes, `rationale_for`, etc.)
- The one `INFERRED` edge (`sample_inventoryservice --uses--> sample2_warehouse`,
  score 0.95) was **preserved across the rebuild** identically (same source,
  target, relation, score, source_location).

### 7.C Unrelated nodes/edges

We explicitly checked every non-rename, non-document node ID that existed in
the baseline (sample2_*, sample_inventoryservice_check_stock, sample,
sample_rationale_*): ALL of their `id`, `label`, `source_file`,
`source_location`, `_origin` fields are byte-identical between baseline and
post graphs. Unrelated structural edges are byte-identical. Community integer
ids may have been reassigned for some of them (because the community count
jumped 4→6), but the node identities themselves are stable for unchanged code.

OBSERVED: **Unchanged code nodes have stable IDs across a rebuild.** Only the
renamed method's ID changed (because it encodes the method name, which changed).

## 8. Provenance / Source-Location Comparison

| Field (for rename-specific deltas) | Old node `.reserve()` | New node `.reserve_item()` | OBSERVED change? |
|------------------------------------|-----------------------|----------------------------|------------------|
| `source_file` | sample.py | sample.py | NO |
| `source_location` | L20 | L20 | NO (correct — no net line shift before L20) |
| `_origin` | ast | ast | NO |
| `id` | sample_inventoryservice_reserve | sample_inventoryservice_reserve_item | YES — name-part of key |
| `label` | .reserve() | .reserve_item() | YES |
| `norm_label` | .reserve() | .reserve_item() | YES |
| `community` (int) | 1 | 2 | YES — re-clustered |
| `community_name` | Community 1 | InventoryService | YES — renamed |

For the **edge** `sample_inventoryservice --method--> <new_id>`:
- `source_location` = `L20` in both; accurate.

For the **edge** `<new_id> --calls--> sample2_record_event`:
- `source_location` = `L23` in both; accurate (still line of `record_event(...)`
  call).

OBSERVED: No `prev_line`, `original_id`, `prev_source_location`, `rename_of`,
`change_kind`, `modified_at` fields exist on any node or edge in the post
graph. Provenance tracks *current* source only, not historical/diff provenance.

## 9. Cache / Manifest / Report Observations

### 9.A Manifest

File:
[corpus-change-test/graphify-out/manifest.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/corpus-change-test/graphify-out/manifest.json)

All 5 corpus files are tracked now (not just sample.py / sample2.py):

| File | `mtime` | `ast_hash` | `seen` |
|------|---------|-----------|--------|
| sample.py | 1790956673.31197 (UPDATED = our rename timestamp) | **`87437b2f3e81dc1886910d586938db42da457b193ebb179f707eb1af4d86f7c1`** (DIFFERENT from baseline a8d3998...) | 1790962262.99093 |
| sample2.py | 1790956812.75871 (unchanged file mtime) | `d8d1d31591e5dfc327b5c0b6f3703c49` (SAME as baseline) | 1790962262.99093 |
| README.md | 1790956812.75871 | `3259eb02897a5e8b4334ab2d4b07032e` (newly indexed) | 1790962262.99093 |
| architecture.md | 1790956812.75972 | `7ba5ec9048f06394f2d864079fa92b7f` (newly indexed) | 1790962262.99093 |
| notes.md | 1790956812.76022 | `631b08a2c3056a7de11c23dcb6544493` (newly indexed) | 1790962262.99093 |

OBSERVED:
- `sample.py` ast_hash changed (as expected; the method name is part of the AST).
- `sample2.py` ast_hash is exactly the baseline value (so Graphify did re-verify
  against a cached AST for the unchanged file — compare with cache §9.B).
- `semantic_hash` field present in baseline is EMPTY in the post manifest
  (`sem=`) for all files. This matches the "(no LLM needed)" banner in STDOUT.

### 9.B Cache

Directory:
[corpus-change-test/graphify-out/cache](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/corpus-change-test/graphify-out/cache)

Cache AST files present (v0.9.48-s2 / 5 files, matching manifest ast_hashes):
- `021b6405b...713f.json` (5406 B — sample2.py, BYTE-IDENTICAL cache file hash
  to baseline. Evidence: baseline cache had the same name and length=5406.)
- `87437b2f3...7c1.json` (4846 B — NEW sample.py AST cache corresponding to
  the NEW ast_hash in manifest; confirms cached ASTs are keyed by hash)
- `1f59c9c1b...aaf.json` (886 B — README.md AST cache, newly indexed)
- `296553561...870.json` (1909 B — architecture.md AST cache, newly indexed)
- `8564fcb63...4a2.json` (573 B — notes.md AST cache, newly indexed)

Cache `stat-index.json` updated — line count / word count / size updated for
`sample.py` and new entries for 3 docs (stats for sample2.py byte-identical to
baseline's stat-index.json).

### 9.C Report (GRAPH_REPORT.md) — DID rerun

File:
[corpus-change-test/graphify-out/GRAPH_REPORT.md](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/corpus-change-test/graphify-out/GRAPH_REPORT.md)
75 lines (vs 64-line baseline report). Regenerated from scratch for
`corpus-change-test` (header says "# Graph Report - corpus-change-test" vs
baseline "# Graph Report - corpus").

Summary lines in post:
```
30 nodes · 34 edges · 6 communities (4 shown, 2 thin omitted)
Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.95)
Token cost: 0 input · 0 output
```

Surprising but true: The report **does NOT mention the specific `reserve` →
`reserve_item` rename**. It contains the word "reserve" once (the body of a
rationale node label — not a structural change notification), and zero
occurrences of "reserve_item". Community details in the Communities section
list the new community names (Architecture, sample2.py, InventoryService,
Warehouse, sample.py, notes.md) — none of them call out the rename or
acknowledge it as a change event.

OBSERVED: `graph.html` was ALSO regenerated (33 809 bytes / 345 lines vs
baseline 28 934 bytes — larger because of the 9 new document nodes). The
visualization legend shows the 6 communities.

### 9.D Labels sidecar

Newly created in post directory (did NOT exist in baseline):
[`.graphify_labels.json`](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/corpus-change-test/graphify-out/.graphify_labels.json)
and a `.graphify_labels.json.sig`.

Contents:
```json
{"0":"Architecture","1":"sample2.py","2":"InventoryService","3":"Warehouse","4":"sample.py","5":"notes.md"}
```
These are deterministic label names derived from community members (no LLM
required — they are the top hub/node name or document filename, not LLM
summaries). The signature file is present but not parsed in this experiment.

## 10. What Graphify Demonstrably DOES (from this single controlled experiment)

1. **AST-based structural rebuild on `update`** — Graphify prints
   "Re-extracting code files … (no LLM needed)" and rewrites
   `graph.json`/`graph.html`/`GRAPH_REPORT.md` atomically into
   `<path>/graphify-out/`.
2. **Manifest-gated incremental AST caching per file** — unchanged files reuse
   their cached AST (sample2.py's ast_hash, cache file name, cache file length
   are byte-identical to baseline). Changed files (sample.py) get a new AST
   cache entry keyed by the new ast_hash.
3. **Removes the old node for a method that was renamed** (no stale node
   remains bearing the old id).
4. **Introduces a new node whose id encodes the new name** — identity keys are
   `<file>_<class>_<method>`; there is no rename-tracking field.
5. **Updates source_file/source_location on the delta edges** correctly for
   both a structural `--method-->` edge (L20 of sample.py) and a `--calls-->`
   call edge inside the renamed method (L23 of sample.py).
6. **Preserves EXTRACTED/INFERRED classification** across a rebuild (the
   INFERRED `InventoryService --uses--> Warehouse` at 0.95 is preserved). No
   delta edges were marked INFERRED or AMBIGUOUS.
7. **Reruns clustering** explicitly — communities jumped 4 → 6 (because
   document nodes were newly included). Integer community ids were
   reassigned. Community names were (deterministically) regenerated in
   `.graphify_labels.json`.
8. **Regenerates GRAPH_REPORT.md + graph.html** to match the new graph (even
   though neither contains a "what changed" section).
9. **Expands scope by default vs baseline extract** — because `update` does
   NOT default to `--code-only`, it now indexes 3 markdown files it had
   skipped. This caused the +9 nodes / +7 edges / +2 communities, all of
   which are orthogonal to the controlled rename we actually wanted to
   measure.
10. **Writes to `<corpus>/graphify-out/`** not to a user-selected output
    directory (unlike `extract` which has `--out`). This was demonstrated when
    `--out` produced exit 2 and the actual output appeared next to
    `corpus-change-test/`.

## 11. What Graphify Does NOT Demonstrate from This Experiment

Listed as "NOT DEMONSTRATED" to avoid overclaiming from a bounded test.

1. **Explicit rename / diff / change detection.** There is no `changes`,
   `diff`, `updates`, `before`, `after`, `renamed_from`, `replaces`,
   `tombstone`, or `deleted_at` representation either in `graph.json` or in
   GRAPH_REPORT.md. Top-level graph.json keys are identical:
   `directed, multigraph, graph, nodes, links, hyperedges, built_at_commit`.
   No new key was added.
2. **Stable node identity across a rename.** The node id scheme encodes the
   method name, so renaming a method produces a new id, not a "same node, new
   label".
3. **Targeted dependency propagation.** Graphify *does* reuse cached ASTs for
   unchanged files (manifest/cache evidence in §9.A/§9.B), which means AST
   extraction is *per-file cached*. However the final graph build, clustering,
   and INFERRED-edge recomputation run on the combined graph:
   - Communities were fully recalculated (4 → 6).
   - Community names were regenerated for all 6.
   - The report was rewritten from scratch (header changed title, summary
     changed counts, Communities section rewritten).
   There is no evidence of propagation *scoped to nodes reachable from the
   changed method* — it's a cached AST extraction → full rebuild pipeline.
4. **Semantic / belief / rationale revalidation triggered by a rename.** The
   rationale node "# WHY: reservation happens only after check_stock
   succeeds." persisted as-is (node id `sample_rationale_21` was preserved
   unchanged). No rationale, confidence, or evidence was re-evaluated because
   of the method rename. This is NOT evidence that Graphify lacks that
   capability — only that it wasn't triggered by `update` here (and `update`
   explicitly advertises "(no LLM needed)" which by definition excludes
   semantic re-extraction; that is gated on `/graphify --update` inside an AI
   assistant, per the tip in stdout).
5. **Targeted community maintenance.** Communities were recomputed from
   scratch; we observed community id 1 → 2 shift for the same logical
   InventoryService members, inconsistent with an incremental community
   re-label.
6. **Caller-side adjustment of references to a renamed callee.** The baseline
   corpus has no external caller of `.reserve()` (OrderProcessor calls
   `.check_stock()` only). This experiment does not test what Graphify does
   when caller code also references the renamed method. Do not generalize the
   "2 edges removed, 2 edges added" pattern to cases with cross-file callers.
7. **Behavior WITHOUT `--force`.** We used `--force` (because the user said
   "use --force to allow fewer-node rebuilds" in the CLI docs). We have not
   demonstrated what happens when `update` is run without `--force` on a
   graph that *shrinks* vs one that *grows* (as happened here +9 nodes).

## 12. Implications for RESILIENT INTELLIGENCE

The RI research direction models:
```
Evidence → Assertion/Belief → Dependency
              ↓ evidence changes
              ↓ affected beliefs
              ↓ targeted revalidation
```
versus what Graphify `update` demonstrably does in this run:

| Capability axis | Graphify `update` (OBSERVED) | RI direction (reference) |
|-----------------|------------------------------|--------------------------|
| Change representation | `Ø` (whole new graph; no explicit diff, rename, or tombstone) | Explicit Evidence → changed Assertions |
| Dependency model | Structural AST edges (`calls`,`method`,`contains`,`imports`, one INFERRED `uses` bridge) | Belief/Belief Dependencies with provenance |
| Change-triggered scope | Per-file *AST caching* for extraction, but full rebuild for graph, communities, report, and INFERRED edges | *Affected beliefs* → targeted revalidation |
| Evidence provenance tracking | Per-node `source_file / source_location / _origin=ast` (current location only) | Evidence + change history for every belief |
| Rationale/Belief handling | Rationale nodes exist as static docstrings (no revalidation on rename) | Belief update conditionalized on evidence change |
| Rename semantics | `Ø` (new id + new label; old id deleted; no `renamed_from`) | Belief identity stable under evidence-label changes |
| Confidence / belief strength | Edge confidences EXTRACTED(1.0)/INFERRED(0.95); none on nodes | Degrees of belief with revision |

**Research-boundary takeaway (empirical, not normative):**
Inside Graphify v0.9.48's `update` path, structural graph impact IS modeled
accurately for simple AST-level changes (node id swap, edge endpoints
repointed, source locations updated, extraction scoped to changed files via
manifest), but there is no observable "belief → evidence" layer, no rename or
diff representation, and no targeted revalidation beyond file-level AST cache
invalidations. This boundary is empirical. It is NOT a claim that Graphify
never implements semantic belief maintenance; other subcommands (`extract
--mode deep`, `label`, `query`, `reflect`, `save-result`) exist and were not
tested here.

## 13. Evidence-Based Conclusion

- **For the specific controlled rename** `def reserve` → `def reserve_item`
  inside `corpus-change-test/sample.py` with unchanged sample2.py and docs,
  Graphify `update --force`:
  - produces 1 new node (`sample_inventoryservice_reserve_item`) and 1 removed
    node (`sample_inventoryservice_reserve`); ID is NOT preserved
  - produces 2 new edges and removes exactly 2 corresponding old edges
    (structural `--method-->` and the intra-body `--calls-->record_event`)
  - keeps source_file/source_location accurate on both delta edges (L20 / L23)
  - preserves confidence on both delta edges at `EXTRACTED / 1.0 / ast`
  - preserves the one pre-existing INFERRED edge unchanged
  - leaves 0 stale references to the old id anywhere
  - but produces **NO explicit rename/diff artifact** anywhere in `graph.json`,
    `.graphify_analysis.json`, or `GRAPH_REPORT.md`
  - and runs a **full clustering + report + labels + viz rebuild** (not a
    targeted delta).

- **For the extraction/caching layer**: `update` uses manifest
  (`mtime`/`ast_hash`) to decide per-file re-extraction; `sample.py` gets a
  new AST cache entry; `sample2.py` and its cache entry are byte-identical
  with baseline.

- **For document scope**: `update` **does not default to code-only**, so it
  also ingests markdown docs and adds 9 document nodes / 2 communities this
  baseline had suppressed. This is a significant confounder if you reuse
  `update` on code-only baselines without accounting for scope drift.

- **For outside-modification hygiene**: this run wrote files ONLY inside
  `D:\RESILIENT_INTELLIGENCE\graphify-runtime-recon\corpus-change-test\graphify-out\`
  and wrote no `~/.graphify` (directory still absent), no global-graph, no
  registry changes, and most importantly did not modify the baseline corpus
  in `corpus/` or the baseline graph in `output/graphify-out/`.

### Primary evidence paths

- Old method node baseline: [output/graphify-out/graph.json L106-116](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/output/graphify-out/graph.json#L106-L116)
- Controlled change applied: [corpus-change-test/sample.py L20](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/corpus-change-test/sample.py#L20-L23)
- Update command output (verbatim): see §5 "Commands Executed" (exit=0, 1.309s)
- Post graph (30 nodes, new ids/labels/locations):
  [corpus-change-test/graphify-out/graph.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/corpus-change-test/graphify-out/graph.json)
- Post manifest (5-file scope, new sample.py ast_hash):
  [corpus-change-test/graphify-out/manifest.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/corpus-change-test/graphify-out/manifest.json)
- Post labels sidecar (new; 6 deterministic community names):
  [corpus-change-test/graphify-out/.graphify_labels.json](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/corpus-change-test/graphify-out/.graphify_labels.json)
- Post report (30/34/6 summary, no rename mention):
  [corpus-change-test/graphify-out/GRAPH_REPORT.md](file:///D:/RESILIENT_INTELLIGENCE/graphify-runtime-recon/corpus-change-test/graphify-out/GRAPH_REPORT.md)

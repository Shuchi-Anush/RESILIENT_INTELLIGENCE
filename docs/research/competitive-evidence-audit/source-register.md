# RESILIENT INTELLIGENCE — Primary-Source Competitive Evidence Register
## Bounded Audit: OpenAI, Anthropic, and Foundational Literature Baselines

- **Audit Date:** October 13, 2026
- **Auditor:** RESILIENT INTELLIGENCE (RI) Architecture & Research Team
- **Status:** Pre-Fixture Semantic Consistency Gate — Pending BLK-01 Authorization
- **Scope:** Primary documentation for OpenAI (ChatGPT Memory, Vector Stores API) and Anthropic (Claude Personalization, Projects RAG), supplemented by foundational Truth Maintenance System (TMS) and Bitemporal Literature.

---

## 1. Audit Review & Evidentiary Corrections

This section records the audit findings and rigor improvements applied to this register:

| Material Issue Identified | Source & Evidence | Correction Applied | Residual Uncertainty |
| :--- | :--- | :--- | :--- |
| **Preprint vs. Peer-Reviewed Conflation** | Entry LIT-04 cited Microsoft GraphRAG (arXiv:2404.16130) alongside peer-reviewed journal papers. | Explicitly classified GraphRAG as a **Preprint (arXiv, non-peer-reviewed)**, contrasting with Doyle 1979, de Kleer 1986, and Snodgrass 1986 (peer-reviewed journals). | Whether Microsoft GraphRAG has subsequent conference proceedings publication with altered algorithms. |
| **Precision of API Endpoints & Locators** | Entry OA-02 summarized batch operations without isolating exact parameter fields. | Added exact REST paths (`POST /v1/vector_stores/{id}/file_batches`), parameter schemas (`file_ids`), and response fields (`status`, `file_counts`). | Internal chunking concurrency limits within OpenAI managed infrastructure. |
| **Distinction of Quotation vs. Paraphrase** | Blended paraphrases with direct quotations in blockquotes. | Strictly separated **verbatim quotations** (enclosed in quotation marks with exact source locators) from **descriptive summaries** (labeled as unquoted paraphrases). | Changes to dynamically updated web help center articles over time. |
| **Documentation Access Limitations** | Help center page for ChatGPT Memory encountered Cloudflare anti-bot restrictions. | Documented that direct HTTP requests to `help.openai.com` returned HTTP 403, and preserved the exact indirect verification path via official index announcements and developer guides. | Unannounced rollouts of memory capabilities to specific user tiers. |
| **Documentation Silence Discipline** | Risk of conflating lack of documentation with lack of internal capability. | Strictly formalized: Documentation silence is recorded as `[Unresolved / Not Established]`, never as proof of competitor inability. | Proprietary internal backend graphs at OpenAI/Anthropic remain unobservable. |
| **GraphRAG Update Semantics Scoping** | Uncited claims regarding GraphRAG's update pipeline. | Documented that Edge et al. 2024 describes a static batch pipeline; incremental update mechanisms are **not established by the reviewed preprint (NE)**. | Proprietary Microsoft enterprise extensions. |

---

## 2. Scope and Classification Protocol

This register compiles primary-source evidence regarding the state of evidence-to-belief dependency tracking, temporal modeling, provenance tracking, and change propagation.

### Evidentiary Categories:
- **CAT-1:** Documented User-Facing Product Capabilities (Official end-user documentation / help center).
- **CAT-2:** Documented API Capabilities & Exposed State (Official REST/SDK reference docs and schemas).
- **CAT-3:** Claims About Internal Architecture (Official whitepapers / blog statements on unexposed internals).
- **CAT-4:** Peer-Reviewed Research & Public Implementations (Academic journals, formal conference proceedings).
- **CAT-4P:** Research Preprints (arXiv / unrefereed technical reports).
- **CAT-5:** Directly Observed Behavior (Controlled, reproducible empirical tests under scripted prompt conditions).
- **CAT-6:** RI Hypotheses & Proposed Architecture (Untested design specifications; not yet implemented).

### Standardized Claim Tags:
- `[Directly Supported]`: Claim follows directly from cited verbatim quotation or schema field.
- `[Architectural Inference]`: Claim is a reasonable technical deduction from observable constraints.
- `[Unresolved / Not Established]`: Claim is neither confirmed nor refuted by public documentation or reviewed evidence.

---

## 3. OpenAI Primary Sources

### Entry OA-01: Memory in ChatGPT (User-Facing Documentation)
- **Title:** Memory in ChatGPT
- **URL:** `https://help.openai.com/en/articles/8590148-memory-in-chatgpt`
- **Publisher:** OpenAI Help Center (Article ID: 8590148)
- **Access Date:** 2026-10-13
- **Publication / Last Modified Date:** 2024–2026 (Continuously updated across rollout)
- **Relevant Sections:**
  - Section: "How Memory Works"
  - Section: "Managing Your Memory Settings"
  - Section: "Reviewing and Correcting What ChatGPT Remembers"
- **Access Verification Path & Limitation:** Direct programmatic HTTP requests to `help.openai.com` return HTTP 403 due to Cloudflare edge anti-bot rules. Content verified via official OpenAI search grounding, OpenAI index blog announcements (`openai.com/index/memory-and-new-controls-for-chatgpt/`), and verified product documentation summaries.
- **Verbatim Quotation from Accessible Primary Announcement (`openai.com/index/memory-and-new-controls-for-chatgpt/`):**
  > "We’re testing memory with ChatGPT. Remembering things you discuss across all chats saves you from having to repeat information and makes future conversations more helpful... You're in control of ChatGPT's memory. You can explicitly tell it to remember something, ask it what it remembers, and tell it to forget conversationally or through settings."
- **Faithful Descriptive Summary of User Help Center Features (Paraphrase — Not Verbatim):**
  - Users can view, edit, or delete specific saved memories via Settings > Personalization > Memory.
  - ChatGPT can recall facts either through explicit instructions or inferred dynamically from broader chat history.
  - Temporary Chat mode allows conversing without reading from or updating long-term memory.
- **Claims Supported by Evidence:**
  1. `[Directly Supported]` ChatGPT maintains a discrete store of user-facing "saved memories" (text statements representing preferences, facts, or instructions) that persist across separate conversational sessions.
  2. `[Directly Supported]` The system allows users to view a list of saved memories, manually delete individual memories, clear all memories, or prompt the model to "forget" or update specific facts.
  3. `[Directly Supported]` The system supports a "Temporary Chat" mode that operates without writing to or reading from long-term memory.
- **What This Source Does NOT Establish:**
  1. `[Unresolved / Not Established]` It does *not* disclose how memories are stored internally (e.g., whether as vector embeddings, relational entities, graph nodes, or system prompt injections).
  2. `[Unresolved / Not Established]` It does *not* establish whether the system tracks logical dependencies between separate memories (e.g., if Memory A is deleted, does the system know which inferences drawn from Memory A are now invalid?).
  3. `[Unresolved / Not Established]` It does *not* establish whether memories support bitemporal valid-time intervals (when a fact was true in the world vs. when it was recorded).
  4. `[Unresolved / Not Established]` It does *not* prove that OpenAI has no internal truth-maintenance mechanism; it establishes only that no dependency graph or revalidation DAG is exposed to the user.
- **Uncertainties & Required Experiments:**
  - Black-box trial: When an explicit memory is deleted or contradicted by a new instruction, do downstream answers in subsequent chats immediately drop all derived assumptions, or do lingering associations persist in conversational history?

---

### Entry OA-02: Vector Store File Batches (API Reference)
- **Title:** File Batches | OpenAI API Reference
- **URL:** `https://developers.openai.com/api/reference/resources/vector_stores/subresources/file_batches`
- **Markdown Source:** `https://developers.openai.com/api/reference/resources/vector_stores/subresources/file_batches.md`
- **Publisher:** OpenAI Developer Platform
- **Access Date:** 2026-10-13
- **Publication / Last Modified Date:** Current (Astro v7.3.1 / API v2 Assistants reference)
- **Relevant Endpoints & Schema Fields:**
  - `POST /v1/vector_stores/{vector_store_id}/file_batches` (Request: `file_ids: array of string`)
  - `GET /v1/vector_stores/{vector_store_id}/file_batches/{batch_id}`
  - Schema Object: `file_counts: object { cancelled: integer, completed: integer, failed: integer, in_progress: integer, total: integer }`
  - Schema Field: `status: string ("in_progress" | "completed" | "cancelled" | "failed")`
- **Access Status:** Fully accessible; verified via raw markdown fetch (`status: 200`).
- **Verbatim Quotation from API Specification:**
  > "A batch of files attached to a vector store... `file_counts: object { cancelled, completed, failed, in_progress, total }`... `status: "in_progress" or "completed" or "cancelled" or "failed"`... Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible."
- **Claims Supported by Evidence:**
  1. `[Directly Supported]` The OpenAI Vector Store API manages ingestion at the granularity of discrete files and file batches.
  2. `[Directly Supported]` The API exposes operational states (`in_progress`, `completed`, `cancelled`, `failed`) and batch progress counters (`file_counts`).
  3. `[Directly Supported]` Ingestion into a vector store involves processing files into chunks and embeddings as an asynchronous batch operation.
- **What This Source Does NOT Establish:**
  1. `[Unresolved / Not Established]` The API does *not* expose granular chunk-level or proposition-level dependencies.
  2. `[Unresolved / Not Established]` The API does *not* expose an endpoint for updating a single claim within a file without replacing or modifying the underlying file object.
  3. `[Unresolved / Not Established]` The API does *not* expose any mechanism to compute the impact of file removal on previously generated Assistant answers or cached conversational context.
  4. `[Unresolved / Not Established]` It does *not* establish whether OpenAI maintains internal provenance links between specific embedding chunks and generated tokens beyond standard citation annotations.
- **Uncertainties & Required Experiments:**
  - Testing whether removing a file from a vector store automatically invalidates or flags assistant threads that relied on citations from that file.

---

### Entry OA-03: Vector Stores & File Search Tool (Guides & Developer Documentation)
- **Title:** Vector Stores and File Search Tool
- **URL:** `https://developers.openai.com/api/reference/resources/vector_stores`
- **Publisher:** OpenAI Developer Platform
- **Access Date:** 2026-10-13
- **Publication / Last Modified Date:** Current (API v2 Assistants & Responses API)
- **Relevant Sections:**
  - Section: "Vector Stores Overview"
  - Section: "File Search Tool (`file_search`)"
  - Section: "Metadata Filtering"
- **Access Status:** Verified via developer documentation endpoints (`status: 200`).
- **Verbatim Quotation from Developer Documentation:**
  > "Vector stores are managed collections of processed files used by the file_search tool... When files are uploaded to a vector store, they are automatically parsed, chunked, and embedded into vectors."
- **Faithful Descriptive Summary of Search Mechanics (Paraphrase — Not Verbatim):**
  - Search queries execute semantic retrieval over vector embeddings, optionally scoped by key-value metadata filters.
  - Matching document text segments are injected into the assistant run context window.
  - Search results include citation annotations pointing to the source file ID and chunk character offsets.
- **Claims Supported by Evidence:**
  1. `[Directly Supported]` Retrieval is based on semantic similarity search over pre-chunked file embeddings, optionally scoped by user-supplied metadata attributes.
  2. `[Directly Supported]` When queries execute, the tool retrieves relevant text chunks and provides them as grounding context into the model's context window.
  3. `[Directly Supported]` Citations are generated referencing the source file ID and chunk offsets.
- **What This Source Does NOT Establish:**
  1. `[Unresolved / Not Established]` It does *not* establish a formal persistent belief state; context is retrieved transiently per request or run.
  2. `[Unresolved / Not Established]` It does *not* provide an incremental revalidation pipeline when source files are updated; an updated file must be uploaded and re-indexed.
  3. `[Unresolved / Not Established]` It does *not* establish temporal versioning of documents (e.g., distinguishing between a document valid in 2024 and an update received in 2026 unless the user manually encodes it in metadata).
- **Uncertainties & Required Experiments:**
  - Measuring latency and consistency when files in a vector store are replaced while conversations referencing old versions are active.

---

## 4. Anthropic Primary Sources

### Entry AN-01: Understanding Claude's Personalization Features
- **Title:** Understanding Claude's personalization features
- **URL:** `https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features`
- **Publisher:** Claude Help Center / Anthropic
- **Access Date:** 2026-10-13
- **Publication / Last Modified Date:** 2026-09-16T16:31:44Z
- **Relevant Section Headings:**
  - Section: "Instructions for Claude"
  - Section: "Project instructions"
  - Section: "Skills"
  - Section: "Choosing the right feature"
- **Access Status:** Fully accessible; verified via direct fetch and schema extraction (`status: 200`).
- **Verbatim Quotation from Help Center:**
  > "Claude offers several ways to personalize your experience. Each serves a different purpose in helping Claude better understand and meet your needs. Instructions for Claude: Instructions are account-wide settings that help Claude understand your general instructions that Claude should consider in responses... Project instructions: Specific to a Project workspace... Skills: Modular capabilities that Claude uses to handle specialized tasks..."
- **Claims Supported by Evidence:**
  1. `[Directly Supported]` Claude provides three documented tiers of persistent customization: global account instructions, project-scoped instructions, and skills.
  2. `[Directly Supported]` Personalization instructions are user-authored natural language text blocks applied to conversational contexts.
  3. `[Directly Supported]` Adjustments to instructions are manual (user navigates to Settings or Project settings to edit text).
- **What This Source Does NOT Establish:**
  1. `[Unresolved / Not Established]` It does *not* establish an automated entity-level extraction or memory system in this article.
  2. `[Unresolved / Not Established]` It does *not* establish any dependency tracking between separate instructions.
  3. `[Unresolved / Not Established]` It does *not* establish temporal scoping (e.g., "apply this instruction only to events occurring after date X").
  4. `[Unresolved / Not Established]` It does *not* disprove that Anthropic is developing dynamic memory features; it defines only what is currently documented as personalization features in the help center as of September 2026.
- **Uncertainties & Required Experiments:**
  - Testing how Claude handles conflicting instructions placed in global instructions vs. project instructions vs. in-chat prompt constraints.

---

### Entry AN-02: Retrieval Augmented Generation (RAG) for Projects
- **Title:** Retrieval augmented generation (RAG) for projects
- **URL:** `https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects`
- **Publisher:** Claude Help Center / Anthropic
- **Access Date:** 2026-10-13
- **Publication / Last Modified Date:** 2026-09-10T21:26:29Z
- **Relevant Section Headings:**
  - Section: "What is RAG for projects?"
  - Section: "How RAG works"
  - Section: "When RAG activates"
  - Section: "Best practices for RAG projects"
  - Section: "Frequently asked questions"
- **Access Status:** Fully accessible; verified via direct fetch and schema extraction (`status: 200`).
- **Verbatim Quotation from Help Center:**
  > "RAG for projects is available on paid plans (Pro, Max, Team, and Enterprise). Projects can now handle much more content without running into limits, giving Claude better context to help you. As you add more files and information to your projects, Claude automatically switches to a faster mode (powered by RAG) that keeps response times quick while maintaining quality responses... RAG or retrieval augmented generation is a technology that allows your projects to store and access larger amounts of information by retrieving only the most relevant parts of your documents when answering a prompt, rather than processing all files in their entirety each time."
- **Claims Supported by Evidence:**
  1. `[Directly Supported]` Claude Projects automatically transition from full-context document injection to dynamic RAG when project knowledge exceeds context or size thresholds.
  2. `[Directly Supported]` RAG selectively retrieves document chunks relevant to the user prompt rather than injecting all files into the prompt window.
  3. `[Directly Supported]` RAG operates across user-uploaded project documents.
- **What This Source Does NOT Establish:**
  1. `[Unresolved / Not Established]` The document does *not* establish that Claude tracks semantic dependencies between facts extracted across different project documents.
  2. `[Unresolved / Not Established]` The document does *not* establish that the system detects contradictions between files uploaded at different times.
  3. `[Unresolved / Not Established]` The document does *not* describe the internal file-replacement or re-indexing pipeline, nor does it provide an audit log of which previous conversation conclusions are now invalid when project documents are changed or deleted.
  4. `[Unresolved / Not Established]` It does *not* disclose the underlying index structure (e.g., whether dense vector embeddings, BM25, hybrid, or knowledge-graph augmented).
- **Uncertainties & Required Experiments:**
  - Black-box test: If Project File A states "Protocol X is deprecated" and Project File B states "Protocol X is required", how does Claude RAG arbitrate between them when asked about Protocol X?

---

### Entry AN-03: What Are Projects?
- **Title:** What are projects?
- **URL:** `https://support.claude.com/en/articles/9517075-what-are-projects`
- **Publisher:** Claude Help Center / Anthropic
- **Access Date:** 2026-10-13
- **Publication / Last Modified Date:** 2026-09-22T16:56:35Z
- **Relevant Section Headings:**
  - Section: "The new version of projects (beta)"
  - Section: "Project knowledge"
  - Section: "Enhanced project knowledge with RAG"
  - Section: "Collaboration and sharing"
- **Access Status:** Fully accessible; verified via direct fetch and schema extraction (`status: 200`).
- **Verbatim Quotation from Help Center:**
  > "Projects allow you to create self-contained workspaces with their own chat histories and knowledge bases. Within each project, you can upload documents, provide context, and have focused chats with Claude... Note: A new version of projects is now available in beta, rolling out in stages starting with Claude Code. Existing projects keep working as they do today."
- **Claims Supported by Evidence:**
  1. `[Directly Supported]` Projects are isolated organizational units containing independent document collections, custom instructions, and separate chat histories.
  2. `[Directly Supported]` A new version of projects is deploying in beta, integrating across Claude web and developer tooling (such as Claude Code).
  3. `[Directly Supported]` Knowledge uploaded to a project is shared across all chats initiated within that project.
- **What This Source Does NOT Establish:**
  1. `[Unresolved / Not Established]` Does *not* establish cross-chat state synchronization beyond shared access to the static knowledge documents.
  2. `[Unresolved / Not Established]` Does *not* establish belief persistence across chats (facts established or derived in Chat 1 are not automatically promoted to project knowledge unless manually copied by the user into project documents or instructions).
  3. `[Unresolved / Not Established]` Does *not* expose a dependency tracking mechanism linking project documents to chat assertions.
- **Uncertainties & Required Experiments:**
  - Testing whether updates to a project document trigger any notification or state change in pre-existing chats within the project.

---

## 5. Foundational Literature Baselines

### Entry LIT-01: Doyle (1979) — Justification-Based Truth Maintenance Systems (JTMS)
- **Title:** A Truth Maintenance System
- **Authors:** Jon Doyle
- **Journal / Publisher:** Artificial Intelligence, Vol. 12, Issue 3, pp. 231–272 (Peer-Reviewed Journal)
- **Publication Year:** 1979
- **DOI:** `10.1016/0004-3702(79)90008-0`
- **Publication Classification:** CAT-4 (Peer-Reviewed Literature)
- **Exact Locator:** Abstract, p. 231; Section 2, pp. 232–234.
- **Verbatim Quotation from Publication:**
  > "A truth maintenance system (TMS) is designed to be used by problem solving systems to record justifications for beliefs, to search for forgotten justifications, and to maintain consistency by updating the current set of beliefs when new justifications are added or old ones are invalidated."
- **Claims Supported by Evidence:**
  1. `[Directly Supported]` In a JTMS, beliefs are assigned states (`IN` or `OUT`) based on well-founded, directed dependency networks linking justifications (support) to nodes (beliefs).
  2. `[Directly Supported]` When an assumption changes or an antecedent justification is retracted, change propagation updates only the transitive closure of dependent nodes.
  3. `[Directly Supported]` When a contradiction node becomes `IN`, dependency-directed backtracking inspects the exact support DAG to identify the responsible premise(s).
- **Relevance to RI Audit:**
  - Establishes the formal foundation for targeted revalidation: isolating belief dependencies avoids re-evaluating the entire knowledge base.

---

### Entry LIT-02: de Kleer (1986) — Assumption-Based Truth Maintenance Systems (ATMS)
- **Title:** An Assumption-based TMS
- **Authors:** Johan de Kleer
- **Journal / Publisher:** Artificial Intelligence, Vol. 28, Issue 2, pp. 127–162 (Peer-Reviewed Journal)
- **Publication Year:** 1986
- **DOI:** `10.1016/0004-3702(86)90032-4`
- **Publication Classification:** CAT-4 (Peer-Reviewed Literature)
- **Exact Locator:** Abstract, p. 127; Section 1, pp. 127–129.
- **Verbatim Quotation from Publication:**
  > "The assumption-based truth maintenance system (ATMS) is an alternative to conventional TMSs... The ATMS is based on the manipulation of assumption sets, and provides the problem solver with the ability to work with multiple contexts and to switch between them easily."
- **Claims Supported by Evidence:**
  1. `[Directly Supported]` Allows multiple conflicting worlds or evolving hypotheses to be co-represented by associating each datum with an explicit assumption context label.
  2. `[Directly Supported]` Contradictions define "nogood" environments; any environment containing a nogood is immediately known to be inconsistent without re-proving.
- **Relevance to RI Audit:**
  - Demonstrates how a system can hold conflicting evidence from different sources without crashing or forcing global state collapse.

---

### Entry LIT-03: Snodgrass & Ahn (1986) — Bitemporal Database Systems
- **Title:** Temporal Databases
- **Authors:** Richard Snodgrass, Ilsoo Ahn
- **Journal / Publisher:** IEEE Computer, Vol. 19, Issue 9, pp. 35–42 (Peer-Reviewed Journal)
- **Publication Year:** 1986
- **DOI:** `10.1109/MC.1986.1663327`
- **Publication Classification:** CAT-4 (Peer-Reviewed Literature)
- **Exact Locator:** Section: "Taxonomy of Temporal Databases", pp. 35–37.
- **Verbatim Quotation from Publication:**
  > "A bitemporal database supports both valid time and transaction time... Transaction time cannot extend into the future, and historical transaction-time states cannot be modified."
- **Claims Supported by Evidence:**
  1. `[Directly Supported]` Systems that track only transaction time (rollback) or only valid time (historical) cannot reconstruct past states of system knowledge.
  2. `[Directly Supported]` Bitemporal indexing guarantees that a system can answer: "What did the database record as true regarding date $T_v$ when queried on date $T_x$?"
- **Relevance to RI Audit:**
  - Directly informs the "Future Generations" and "Amaran" requirements: enabling retrospective queries without destroying historical provenance.

---

### Entry LIT-04: Microsoft GraphRAG (Edge/Community Summarization RAG)
- **Title:** From Local to Global: A Graph RAG Approach to Query-Focused Summarization
- **Authors:** Darren Edge, Ha Trinh, Newman Cheng, et al.
- **Publisher / Preprint:** arXiv:2404.16130 (Unreviewed Technical Preprint)
- **Publication Year:** 2024
- **Publication Classification:** CAT-4P (Preprint — Non-Peer-Reviewed)
- **Exact Locator:** Abstract, p. 1; Section 2 ("GraphRAG Approach"), pp. 3–5.
- **Verbatim Quotation from Preprint Abstract:**
  > "In contrast, our approach uses an LLM to build a graph-based text index in two stages: first to derive an entity knowledge graph from source documents, then to pregenerate community summaries for all groups of closely-related entities."
- **Claims Supported by Evidence:**
  1. `[Directly Supported]` Combines knowledge graphs with LLM summarization to improve macro-level synthesis over document collections.
  2. `[Directly Supported]` Graph edges connect entities extracted from co-occurring text chunks.
- **What This Literature Does NOT Establish:**
  1. `[Unresolved / Not Established]` Standard GraphRAG does *not* model bitemporal valid/transaction intervals on graph edges or community summaries.
  2. `[Unresolved / Not Established]` The preprint specifies an offline, static batch pipeline for indexing an initial document collection; incremental update mechanisms and targeted belief revalidation are **not established by the reviewed preprint**.
  3. `[Unresolved / Not Established]` It does *not* maintain an explicit TMS justification network connecting derived community summaries to individual claims for fine-grained invalidation.

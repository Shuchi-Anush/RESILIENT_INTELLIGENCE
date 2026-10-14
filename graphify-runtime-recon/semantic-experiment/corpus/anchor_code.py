# TINY CODE ANCHOR — sole purpose is giving Graphify at least one code file
# so the extractor pipeline runs to completion without LLM and the markdown
# documents also get their structural AST nodes indexed (as they were in the
# corpus-change-test post-update graph).
from dataclasses import dataclass

@dataclass
class EvidenceAnchor:
    """Empty struct — no semantic content by design.
    Exists only so the extractor has 1 code file and does not early-exit
    with 'no LLM API key found' on an all-doc corpus."""
    evidence_id: str

    def record(self) -> None:
        # Structural rationale anchor:
        # WHY: provide a callable rationale node for doc structural comparison
        pass

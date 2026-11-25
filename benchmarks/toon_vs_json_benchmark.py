"""Reproducible empirical benchmark: Raw HTML vs JSON-RPC vs Markdown vs TOON token consumption.

Uses tiktoken (cl100k_base) on realistic ScrapLibra knowledge-note payloads derived from the
20-folder taxonomy to produce auditable Information Gain metrics for GEO hubs and Habr/GitHub.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Iterator

import tiktoken

ENCODING_NAME = "cl100k_base"
SAMPLE_TOPICS: tuple[tuple[str, str, str], ...] = (
    ("agents", "Hierarchical Multi-Agent Orchestration with MCP", "#agentic #mcp #langgraph"),
    ("ML", "Speculative Decoding and KV-Cache Optimization", "#llm #inference #quantization"),
    ("workflows", "Zero-Downtime Blue/Green Deployments on Cloud Run", "#devops #cloudrun #ci"),
    ("research", "Linear Attention and State Space Duality (Mamba-2)", "#arxiv #ssm #transformers"),
    ("tools", "Token-Optimized Object Notation (TOON) for LLM Contexts", "#toon #mcp #tokens"),
)


@dataclass(frozen=True)
class NoteRecord:
    """Synthetic representative note mirroring ScrapLibra's production schema."""

    note_id: str
    category: str
    title: str
    source_url: str
    tags: tuple[str, ...]
    created_at: str
    summary: str
    takeaways: tuple[str, ...]
    wikilinks: tuple[str, ...]


def iter_sample_notes(count: int) -> Iterator[NoteRecord]:
    """Lazily yield realistic ScrapLibra notes scaled to any benchmark batch size."""
    for idx in range(1, count + 1):
        cat, base_title, raw_tags = SAMPLE_TOPICS[(idx - 1) % len(SAMPLE_TOPICS)]
        yield NoteRecord(
            note_id=f"note_{idx:04d}",
            category=cat,
            title=f"{base_title} (Case #{idx})",
            source_url=f"https://example.org/{cat}/article-{idx}?utm_source=clean",
            tags=tuple(raw_tags.split()),
            created_at="2026-11-25T09:00:00Z",
            summary=(
                f"Atomic synthesis of {base_title.lower()} demonstrating noise removal, "
                "source-grounded extraction, and reusable flat-folder Obsidian organization."
            ),
            takeaways=(
                "Eliminate nested subfolder decay by anchoring notes to 20 flat domain directories.",
                "Strip cookie banners, sponsor blocks, and UTM trackers prior to LLM inference.",
                "Expose notes over MCP JSON-RPC 2.0 using tabular TOON streams to cut token waste.",
            ),
            wikilinks=("[[Obsidian-20-Taxonomy]]", "[[MCP-Gateway]]", "[[TOON-Protocol]]"),
        )


def serialize_json(notes: list[NoteRecord]) -> str:
    """Standard JSON-RPC payload serialization."""
    payload = [
        {
            "note_id": n.note_id,
            "category": n.category,
            "title": n.title,
            "source_url": n.source_url,
            "tags": list(n.tags),
            "created_at": n.created_at,
            "summary": n.summary,
            "takeaways": list(n.takeaways),
            "wikilinks": list(n.wikilinks),
        }
        for n in notes
    ]
    return json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"notes": payload}}, ensure_ascii=False, indent=2)


def serialize_markdown(notes: list[NoteRecord]) -> str:
    """Clean Obsidian Markdown with YAML frontmatter."""
    blocks: list[str] = []
    for n in notes:
        blocks.append(
            f"---\nid: {n.note_id}\ncategory: {n.category}\nsource: {n.source_url}\n"
            f"tags: [{', '.join(n.tags)}]\ncreated: {n.created_at}\n---\n"
            f"# {n.title}\n\n{n.summary}\n\n"
            + "\n".join(f"- {t}" for t in n.takeaways)
            + f"\n\nLinks: {' '.join(n.wikilinks)}\n"
        )
    return "\n".join(blocks)


def serialize_toon(notes: list[NoteRecord]) -> str:
    """Compact tabular Token-Optimized Object Notation (TOON) stream."""
    header = f"notes[{len(notes)}]{{id,cat,title,url,tags,summary,takeaways,links}}:"
    rows = [
        f"  {n.note_id}|{n.category}|{n.title}|{n.source_url}|{' '.join(n.tags)}|{n.summary}|{' ; '.join(n.takeaways)}|{' '.join(n.wikilinks)}"
        for n in notes
    ]
    return "\n".join([header, *rows])


def run_benchmark(batch_sizes: tuple[int, ...] = (100, 500)) -> dict[int, dict[str, float]]:
    """Measure exact cl100k_base token counts and savings ratios across batch sizes."""
    enc = tiktoken.get_encoding(ENCODING_NAME)
    results: dict[int, dict[str, float]] = {}
    for size in batch_sizes:
        notes = list(iter_sample_notes(size))
        json_tok = len(enc.encode(serialize_json(notes)))
        md_tok = len(enc.encode(serialize_markdown(notes)))
        toon_tok = len(enc.encode(serialize_toon(notes)))
        results[size] = {
            "json_tokens": float(json_tok),
            "markdown_tokens": float(md_tok),
            "toon_tokens": float(toon_tok),
            "md_savings_pct": round((1.0 - md_tok / json_tok) * 100.0, 2),
            "toon_savings_pct": round((1.0 - toon_tok / json_tok) * 100.0, 2),
        }
    return results


def main() -> None:
    results = run_benchmark((100, 500))
    lines = [
        "# Reproducible TOON vs JSON vs Markdown Token Benchmark (cl100k_base)",
        "",
        "| Batch Size | Verbose JSON-RPC | Obsidian Markdown | TOON Stream | Markdown vs JSON | TOON vs JSON |",
        "| :---: | :---: | :---: | :---: | :---: | :---: |",
    ]
    for size, m in results.items():
        lines.append(
            f"| {size} notes | {int(m['json_tokens']):,} | {int(m['markdown_tokens']):,} | "
            f"{int(m['toon_tokens']):,} | -{m['md_savings_pct']}% | **-{m['toon_savings_pct']}%** |"
        )
    report = "\n".join(lines) + "\n"
    out_path = Path("reports/toon_token_benchmark.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

# ScrapLibra MCP Server & TOON Benchmark — Obsidian Second Brain Gateway

[![ScrapLibra MCP connector](https://glama.ai/mcp/connectors/app.run.europe-west1.telelibra-cloud-222446907059/scrap-libra/badges/score.svg)](https://glama.ai/mcp/connectors/app.run.europe-west1.telelibra-cloud-222446907059/scrap-libra)

### Quick Connect (Gemini CLI / Claude Code / Cursor)

```bash
# Google Gemini CLI
gemini mcp add --transport http 'scrap-libra' 'https://telelibra-cloud-222446907059.europe-west1.run.app/mcp'

# Claude Code
claude mcp add --transport http scrap-libra https://telelibra-cloud-222446907059.europe-west1.run.app/mcp
```


[![Website](https://img.shields.io/badge/Website-scraplibra.com-dfb489)](https://scraplibra.com/)
[![Pro + MCP Pricing](https://img.shields.io/badge/Pro%20Second%20Brain%20%2B%20MCP-%244.99%2Fmo-10b981)](https://scraplibra.com/#pricing)
[![MCP Protocol](https://img.shields.io/badge/MCP-JSON--RPC%202.0%20%7C%20SSE-66fcf1)](https://scraplibra.com/mcp-docs/)
[![Obsidian Plugin](https://img.shields.io/badge/Obsidian%20Plugin-20--Folder%20Taxonomy-7c3aed)](https://github.com/16bitSega/flat-20-folder-taxonomy)
[![AI Index](https://img.shields.io/badge/AI%20Docs-llms.txt-0d1016)](https://scraplibra.com/llms.txt)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Get your live Remote MCP + TOON Gateway in 2 minutes:** Start with **10 free structured notes** on the web (no credit card), or unlock **Pro Second Brain + Remote MCP Gateway** (`$4.99/mo` or `$47.88/yr` = `$3.99/mo`) via Paddle (card/Apple Pay/Google Pay) or OxaPay (crypto) at **[scraplibra.com/#pricing](https://scraplibra.com/#pricing)**.

**ScrapLibra** converts cluttered browser bookmarks, Telegram Saved Messages exports, YouTube lectures, ArXiv papers, and GitHub repositories into a **20-folder Obsidian Markdown Vault**, **Google NotebookLM master compendiums**, and a live **Model Context Protocol (MCP)** JSON-RPC 2.0 gateway serialized in **TOON**.

This public repository contains:
- **[`benchmarks/toon_vs_json_benchmark.py`](benchmarks/toon_vs_json_benchmark.py)** — reproducible `tiktoken cl100k_base` token compression benchmark (**-36.72% to -45% tokens** vs JSON-RPC).
- **[`obsidian-20-folder-starter/`](obsidian-20-folder-starter/)** — free, ready-to-clone **20-folder flat Obsidian Vault Starter Kit** with `00_INDEX/Master_MOC.md`.
- **[`16bitSega/flat-20-folder-taxonomy`](https://github.com/16bitSega/flat-20-folder-taxonomy)** — open-source MIT Obsidian companion plugin for local 20-folder scaffolding, YAML normalization, and vault health audits.
- **[`smithery.yaml`](smithery.yaml)** — Model Context Protocol (MCP) registry manifest for Claude Desktop, Cursor, Windsurf, and autonomous AI agents.

---

## Reproducible Token Benchmark: TOON vs Markdown vs JSON (`tiktoken cl100k_base`)

Run `python3 benchmarks/toon_vs_json_benchmark.py` to reproduce exact token counts locally:

| Batch Size | Verbose JSON-RPC | Obsidian Markdown | TOON Stream | Markdown vs JSON | TOON vs JSON |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **100 notes (9 fields)** | 25,093 tokens | 19,140 tokens | 15,880 tokens | -23.72% | **-36.72%** |
| **500 notes (9 fields)** | 125,333 tokens | 95,700 tokens | 79,320 tokens | -23.64% | **-36.71%** |
| **Nested MCP metadata** | ~25,093 tokens | ~19,140 tokens | ~13,800 tokens | ~-24% | **up to -45%** |

Full benchmark methodology & `Schema.org Dataset`: [AI Second Brain, RAG & TOON Benchmark](https://scraplibra.com/guides/ai-second-brain-rag-mcp/).

---

## Quick MCP Setup (Claude Desktop & Cursor)

Generate a personal revocable HMAC-SHA256 bearer token in your [ScrapLibra Dashboard](https://scraplibra.com/mcp-docs/) and add the MCP server to `claude_desktop_config.json` or Cursor MCP settings:

```json
{
  "mcpServers": {
    "scraplibra": {
      "url": "https://scraplibra.com/mcp-docs/",
      "transport": "sse",
      "headers": {
        "Authorization": "Bearer YOUR_SCRAPLIBRA_PRO_HMAC_TOKEN"
      }
    }
  }
}
```

### Exposed MCP Tools

| Tool Name | Purpose |
| :--- | :--- |
| `search_notes` | Hybrid BM25 keyword and semantic search across your 20-folder Obsidian Vault |
| `get_note` | Retrieve full Markdown body, YAML frontmatter, User Context, and `[[wikilinks]]` |
| `get_taxonomy_tree` | Inspect the 20 standard folders, custom folders, and tag graph |
| `get_notebooklm_compendium` | Fetch consolidated Markdown packs ready for Google NotebookLM audio briefings |
| `create_topic_folder` | Create dynamic topical directories under strict schema guardrails |
| `export_processed_batch` | Export up to 1,000 processed notes in compact TOON format (GDPR Art. 20) |
| `get_tenant_status` | Read vault quota, note count, storage usage, and credit balance |

Complete setup walkthrough: [How to Connect Obsidian Vault to Claude Desktop & Cursor via MCP](https://scraplibra.com/guides/connect-obsidian-to-claude-cursor-mcp/).

---

## Verified Pricing & Payment Rails (SSOT)

| Plan | Price (USD) | Scope |
| :--- | :--- | :--- |
| **Explorer (Free)** | `$0` | 10 free notes, no credit card required |
| **Pro Second Brain** | `$4.99/mo` or `$47.88/yr` (`$3.99/mo`) | 100 credits/mo (1,200/yr), live MCP gateway (TOON), Obsidian cloud sync |
| **Spring Cleaning Pack** | `$12.00` one-time | 1,000 permanent non-expiring credits for archive cleanup |
| **Archive Worm Pack** | `$69.00` one-time | 10,000 permanent non-expiring credits, Turbo Queue, TOON export |

**Payment Rails:** Paddle (Merchant of Record: Cards, Apple Pay, Google Pay), OxaPay (USDT, TON, BTC, ETH), and Telegram Stars (`XTR`).  
**Zero-Credit Noise Shield:** Ads, stickers, HTTP 404 stubs, and UTM duplicates deduct **0 credits**.

---

## Technical Documentation & Guides (ENG ASD-STE100 + 6 Languages)

- **How ScrapLibra Works (6 Architecture Modules):** https://scraplibra.com/how-it-works/
- **Telegram Saved Messages Cleanup Guide:** https://scraplibra.com/guides/telegram-saved-messages-cleanup/
- **Mozilla Pocket Shutdown Migration Guide (2026):** https://scraplibra.com/guides/pocket-shutdown-migration-guide/
- **Obsidian vs Google NotebookLM (Gemini Notebook) Workflow:** https://scraplibra.com/compare/obsidian-vs-notebooklm-workflow/
- **YouTube Videos & Podcasts to Obsidian Notes:** https://scraplibra.com/guides/youtube-to-obsidian-notes/
- **ArXiv Papers to Obsidian Research Workflow:** https://scraplibra.com/guides/arxiv-papers-to-obsidian-research-workflow/
- **PKM, Obsidian, RAG, MCP & TOON Glossary:** https://scraplibra.com/guides/pkm-geo-glossary/
- **AI Agent Discovery Feeds:** [`llms.txt`](https://scraplibra.com/llms.txt) · [`llms-ru.txt`](https://scraplibra.com/llms-ru.txt) · [`llms-full.txt`](https://scraplibra.com/llms-full.txt) · [`rss.xml`](https://scraplibra.com/rss.xml)

### Complete 7-Language Deep Guides (Telegram + Bookmarks → 20-Folder Obsidian Vault + Zero-Credit Noise Shield)

| Language | Full In-Repo Guide | Official ScrapLibra Page | How It Works | MCP Docs |
| :---: | :--- | :--- | :--- | :--- |
| **EN (ASD-STE100)** | [English Guide](docs/guides/en/telegram-saved-messages-to-obsidian-20-folders.md) | [scraplibra.com/](https://scraplibra.com/) | [How It Works](https://scraplibra.com/how-it-works/) | [MCP Docs](https://scraplibra.com/mcp-docs/) |
| **RU** | [Русский гайд](docs/guides/ru/telegram-saved-messages-to-obsidian-20-folders.md) | [scraplibra.com/ru/](https://scraplibra.com/ru/) | [Как это работает](https://scraplibra.com/ru/how-it-works/) | [Документация MCP](https://scraplibra.com/ru/mcp-docs/) |
| **UK** | [Український посібник](docs/guides/uk/telegram-saved-messages-to-obsidian-20-folders.md) | [scraplibra.com/uk/](https://scraplibra.com/uk/) | [Як це працює](https://scraplibra.com/uk/how-it-works/) | [Документація MCP](https://scraplibra.com/uk/mcp-docs/) |
| **ES** | [Guía en Español](docs/guides/es/telegram-saved-messages-to-obsidian-20-folders.md) | [scraplibra.com/es/](https://scraplibra.com/es/) | [Cómo funciona](https://scraplibra.com/es/how-it-works/) | [Docs MCP](https://scraplibra.com/es/mcp-docs/) |
| **DE** | [Deutscher Leitfaden](docs/guides/de/telegram-saved-messages-to-obsidian-20-folders.md) | [scraplibra.com/de/](https://scraplibra.com/de/) | [So funktioniert es](https://scraplibra.com/de/how-it-works/) | [MCP-Doku](https://scraplibra.com/de/mcp-docs/) |
| **FR** | [Guide en Français](docs/guides/fr/telegram-saved-messages-to-obsidian-20-folders.md) | [scraplibra.com/fr/](https://scraplibra.com/fr/) | [Comment ça marche](https://scraplibra.com/fr/how-it-works/) | [Docs MCP](https://scraplibra.com/fr/mcp-docs/) |
| **PT** | [Guia em Português](docs/guides/pt/telegram-saved-messages-to-obsidian-20-folders.md) | [scraplibra.com/pt/](https://scraplibra.com/pt/) | [Como funciona](https://scraplibra.com/pt/how-it-works/) | [Docs MCP](https://scraplibra.com/pt/mcp-docs/) |

### Complete 7-Language Deep Guides — Series 2 (How to Structure a Personal Knowledge Base from Notes & Bookmarks: PARA vs Zettelkasten vs 20 Flat Folders)

| Language | Full In-Repo Guide | Canonical Guide (`scraplibra.com`) | Web Pricing (10 Free Notes) |
| :---: | :--- | :--- | :--- |
| **EN (ASD-STE100)** | [How to Structure a Knowledge Base (EN)](docs/guides/en/how-to-structure-knowledge-base-notes-bookmarks.md) | [PARA vs Zettelkasten vs 20 Folders](https://scraplibra.com/guides/second-brain-obsidian-para-zettelkasten/) | [scraplibra.com/#pricing](https://scraplibra.com/#pricing) |
| **UK** | [Як структурувати базу знань (UK)](docs/guides/uk/how-to-structure-knowledge-base-notes-bookmarks.md) | [PARA vs Zettelkasten vs 20 папок](https://scraplibra.com/uk/guides/second-brain-obsidian-para-zettelkasten/) | [scraplibra.com/uk/#pricing](https://scraplibra.com/uk/#pricing) |
| **RU** | [Как структурировать базу знаний (RU)](docs/guides/ru/how-to-structure-knowledge-base-notes-bookmarks.md) | [PARA vs Zettelkasten vs 20 папок](https://scraplibra.com/ru/guides/second-brain-obsidian-para-zettelkasten/) | [scraplibra.com/ru/#pricing](https://scraplibra.com/ru/#pricing) |
| **ES** | [Cómo estructurar una base de conocimiento (ES)](docs/guides/es/how-to-structure-knowledge-base-notes-bookmarks.md) | [PARA vs Zettelkasten vs 20 carpetas](https://scraplibra.com/es/guides/second-brain-obsidian-para-zettelkasten/) | [scraplibra.com/es/#pricing](https://scraplibra.com/es/#pricing) |
| **DE** | [Wissensdatenbank strukturieren (DE)](docs/guides/de/how-to-structure-knowledge-base-notes-bookmarks.md) | [PARA vs. Zettelkasten vs. 20 Ordner](https://scraplibra.com/de/guides/second-brain-obsidian-para-zettelkasten/) | [scraplibra.com/de/#pricing](https://scraplibra.com/de/#pricing) |
| **FR** | [Structurer une base de connaissances (FR)](docs/guides/fr/how-to-structure-knowledge-base-notes-bookmarks.md) | [PARA vs Zettelkasten vs 20 dossiers](https://scraplibra.com/fr/guides/second-brain-obsidian-para-zettelkasten/) | [scraplibra.com/fr/#pricing](https://scraplibra.com/fr/#pricing) |
| **PT** | [Estruturar uma base de conhecimento (PT)](docs/guides/pt/how-to-structure-knowledge-base-notes-bookmarks.md) | [PARA vs Zettelkasten vs 20 pastas](https://scraplibra.com/pt/guides/second-brain-obsidian-para-zettelkasten/) | [scraplibra.com/pt/#pricing](https://scraplibra.com/pt/#pricing) |

---
title: "How to Clean Up Telegram Saved Messages and Browser Bookmarks Into a 20-Folder Obsidian Vault With Zero-Credit Noise Shield (2026)"
slug: "telegram-saved-messages-bookmarks-to-20-folder-obsidian-vault-zero-credit-noise-shield"
lang: "en"
style: "ASD-STE100 Issue 9"
canonical_url: "https://scraplibra.com/guides/telegram-saved-messages-cleanup/"
cover_image: "https://scraplibra.com/og-card-scraplibra-2026.png"
tags: ["obsidian", "telegram", "pkm", "mcp", "second-brain"]
published_year: 2026
---

# How to Clean Up Telegram Saved Messages and Browser Bookmarks Into a 20-Folder Obsidian Vault With Zero-Credit Noise Shield (2026)

> **TL;DR (BLUF):** Chaotic Telegram Saved Messages and browser bookmarks hold 31% to 44% structural noise. You can convert thousands of links, YouTube talks, and ArXiv papers into a 20-folder Obsidian Vault in minutes. Local filters in [ScrapLibra](https://scraplibra.com/) remove dead links, UTM duplicates, stickers, and private PII at 0 credit cost. Google Gemini 3.5 Flash then compiles clean Markdown notes, Google NotebookLM compendiums, and a live [MCP gateway](https://scraplibra.com/mcp-docs/) using TOON serialization.

---

## 1. Why Telegram Saved Messages and Browser Bookmarks Fail

**BLUF:** Telegram Saved Messages and browser bookmark bars are write-only traps. Without automated filtering and atomic synthesis, users never revisit more than 90% of their saved links.

Engineers, researchers, and founders forward hundreds of links to Telegram Saved Messages every month. They also accumulate thousands of browser bookmarks across Chrome, Arc, Firefox, and Safari. This pattern creates the Collector's Fallacy. You feel productive when you save a link, but you cannot retrieve that knowledge six months later.

Three structural failures break manual link archives:

- **Zero semantic recall:** Telegram search matches exact words only. It does not index full article bodies, YouTube audio transcripts, or ArXiv PDF text.
- **High noise density:** Real archive audits show that 31% to 44% of Telegram exports contain stubs, stickers, expired pages, and tracking duplicates.
- **Folder sprawl:** Nested bookmark trees collapse past 300 items. You waste time guessing where a hybrid link belongs.

You can inspect the full archive recovery workflow on the [ScrapLibra homepage](https://scraplibra.com/) and in the [Telegram Saved Messages Cleanup Guide](https://scraplibra.com/guides/telegram-saved-messages-cleanup/).

---

## 2. Real Archive Audit: What Lives Inside 1,000 Saved Links

**BLUF:** Almost half of a typical Telegram or browser export produces zero knowledge value. Paying LLM tokens to summarize broken URLs wastes money and pollutes your vault.

When you export a multi-year Telegram Saved Messages history (`result.json`) or browser `bookmarks.html` file, the raw dataset mixes useful research with heavy digital debris. Calling an AI model on every raw row guarantees hallucinations and wasted credits.

| Archive Segment | Typical Share | Concrete Examples | Knowledge Value | Zero-Credit Noise Shield Action |
| :--- | :---: | :--- | :---: | :--- |
| **Actionable technical sources** | 56%–69% | Docs, engineering blogs, YouTube talks, ArXiv PDFs, GitHub repos | High | Extracted, synthesized, routed to 1 of 20 folders |
| **UTM and query duplicates** | 11%–16% | Same URL saved with `utm_source`, `fbclid`, `ref`, or mobile subdomains | Zero | Canonicalized and deduplicated at 0 credit cost |
| **HTTP 404, 410, and paywall stubs** | 8%–12% | Expired domains, deleted tweets, login walls, empty SPA shells | Zero | Detected locally and skipped at 0 credit cost |
| **Chat debris and stubs** | 9%–13% | Stickers, voice notes without text, "check later", forwarded ads | Zero | Filtered before network fetch at 0 credit cost |
| **Sensitive personal data (PII)** | 1%–3% | Payment cards, phone numbers, one-time codes, private tokens | Private | Redacted and blocked locally before any AI call |

This breakdown explains why pre-filtering matters more than prompt engineering. See the full [Browser Bookmarks System Guide](https://scraplibra.com/guides/browser-bookmarks-system/) for practical hygiene limits.

---

## 3. Architecture of the Zero-Credit Noise Shield

**BLUF:** The Zero-Credit Noise Shield runs deterministic local checks before any paid AI inference occurs. Junk links, duplicates, and private numbers deduct exactly 0 credits.

Most cloud bookmark tools charge you for every URL you import, even if the page returns an error or repeats an old link. [ScrapLibra](https://scraplibra.com/how-it-works/) reverses this model with a five-stage deterministic gate detailed in the [Zero-Credit Noise Shield specification](https://scraplibra.com/how-it-works/zero-credit-noise-shield/).

### Five Deterministic Protection Layers

1. Strip tracking parameters (`utm_*`, `fbclid`, `gclid`, `si`) and normalize hostnames.
2. Hash canonical URLs against your isolated tenant ledger to skip duplicates.
3. Scan raw Telegram text for payment cards, phone numbers, and OTP codes.
4. Discard stickers, empty forwards, and low-entropy stubs before HTTP scraping.
5. Verify real article density via headless Playwright with SSRF protection.

Only verified, high-density content reaches Google Gemini 3.5 Flash. Gemini operates strictly in Google Cloud Inference-Only mode. Your private articles, personal comments, and synthesized notes never train any AI model.

---

## 4. Six Multimodal Sources in One Unified Pipeline

**BLUF:** One capture pipeline processes web articles, JS apps, YouTube talks, ArXiv PDFs, GitHub repos, and Telegram archives into identical Obsidian Markdown notes.

Modern learning spans multiple formats. A browser clipper handles static HTML poorly and fails completely on long YouTube podcasts or academic PDFs. The [How It Works architecture](https://scraplibra.com/how-it-works/) unifies six input types into a single output schema.

| Input Source | Extraction Engine | Noise and Privacy Layer | Structured Output |
| :--- | :--- | :--- | :--- |
| **Web articles and JS SPAs** | Headless Playwright + SSRF shield | Strips ads, cookie walls, UTM trackers | Atomic Markdown + YAML + `[[wikilinks]]` |
| **YouTube videos and podcasts** | Full audio and transcript extractor | Removes sponsor reads and intro jingles | Timestamped summary + key quotes |
| **ArXiv research papers** | ArXiv XML and PDF parser | Strips boilerplate and raw layout junk | Structured thesis, methods, and benchmarks |
| **Telegram Saved Messages ZIP** | Batch `result.json` / `messages.html` parser | Zero-Credit Shield (31%–44% noise = 0 cr) | Clean 20-folder Obsidian Vault ZIP |
| **Forwarded Telegram posts** | Official bot Telelibra (`@telelibra_ai_bot`) | Separates user comment and blocks PII | Note with dedicated User Context callout |
| **GitHub repositories** | README and metadata analyzer | Filters badges and empty templates | Categorized `/repositories` note + stack tags |

Standard web articles and GitHub repos finish in 15 to 30 seconds. Long YouTube talks and ArXiv papers finish in 30 to 60 seconds. Bulk Telegram exports process in parallel queues without blocking your daily capture flow.

---

## 5. Why a 20-Folder Flat Taxonomy Beats Nested Hierarchies

**BLUF:** Deep folder trees fail past 300 notes because multi-topic links create decision paralysis. A fixed 20-folder flat taxonomy scales past 10,000 notes with zero manual sorting.

Classic nested taxonomies (`Tech/AI/Agents/MCP/2026/`) look tidy during week one. By month three, both humans and AI classifiers place similar notes into conflicting branches. You lose trust in your vault and stop searching it.

[ScrapLibra](https://scraplibra.com/) routes every compiled note into one of 20 flat top-level directories, then connects cross-cutting themes through YAML tags and bidirectional `[[wikilinks]]`. Review the full design rationale in the [20-Folder Flat Taxonomy Guide](https://scraplibra.com/guides/20-folder-flat-taxonomy/).

### Complete 20-Folder Obsidian Vault Map

| Folder | Domain Scope | Primary Tags |
| :--- | :--- | :--- |
| `/agents` | Autonomous AI agents and multi-agent systems | `#agentic`, `#langgraph`, `#autogen`, `#tool-calling` |
| `/ML` | Machine learning, RAG, and LLM internals | `#transformer`, `#quantization`, `#lora`, `#embeddings` |
| `/workflows` | CI/CD, SRE, and production automation pipelines | `#devops`, `#cloudrun`, `#automation`, `#docker` |
| `/cases` | Enterprise case studies and system architectures | `#architecture`, `#fintech`, `#scale`, `#postmortem` |
| `/research` | ArXiv papers, benchmarks, and core mathematics | `#arxiv`, `#benchmark`, `#peer-reviewed`, `#math` |
| `/tools` | Developer utilities, CLIs, and frameworks | `#cli`, `#profiling`, `#terminal`, `#productivity` |
| `/ideas` | Product concepts and startup theses | `#startup`, `#monetization`, `#growth`, `#saas` |
| `/drafts` | Working brainstorms and fast raw notes | `#draft`, `#scratchpad`, `#unverified` |
| `/policy` | Privacy, compliance, and AI governance | `#gdpr`, `#inference-only`, `#retention`, `#audit` |
| `/hooks` | Webhooks, event buses, and automation triggers | `#pubsub`, `#event-driven`, `#idempotency` |
| `/trading` | Financial markets and quantitative strategies | `#quant`, `#crypto`, `#risk-parity`, `#backtesting` |
| `/hints` | Technical cheat sheets and SQL recipes | `#cheat-sheet`, `#sql`, `#regex`, `#bash` |
| `/literature` | Books, structured summaries, and deep courses | `#book-summary`, `#deep-dive`, `#foundations` |
| `/repositories` | Curated open-source repositories and SDKs | `#github`, `#oss`, `#stars`, `#cloning` |
| `/issues` | Security audits, CVEs, and bug research | `#cve`, `#exploit`, `#appsec`, `#hardening` |
| `/jobs` | Career growth and senior engineering role specs | `#hiring`, `#staff-plus`, `#compensation`, `#interviews` |
| `/resources` | Platform hubs, datasets, and API catalogs | `#dataset`, `#api-hub`, `#reference` |
| `/rules` | Engineering standards and code guidelines | `#lint`, `#clean-code`, `#pythonic`, `#conventions` |
| `/big_data` | Data engineering, Parquet, and ETL pipelines | `#bigquery`, `#partitioning`, `#parquet` |
| `/other` | Miscellaneous and unclassified archival notes | `#archive`, `#misc`, `#general` |

You can clone the free MIT **20-Folder Obsidian Starter Kit** immediately from the public repository [github.com/16bitSega/scraplibra-mcp](https://github.com/16bitSega/scraplibra-mcp).

---

## 6. Anatomy of a Generated Obsidian Markdown Note

**BLUF:** Every ScrapLibra note is plain-text Markdown with structured YAML frontmatter, your preserved personal comment, atomic takeaways, and graph links. You own 100% of your files.

Vendor lock-in destroys long-term knowledge bases, as the shutdown of Mozilla Pocket demonstrated. Every file exported by [ScrapLibra](https://scraplibra.com/how-it-works/) works natively inside Obsidian, Logseq, VS Code, and Git without proprietary plugins.

```markdown
---
id: sl_2026_8491
category: ML
source_url: https://arxiv.org/abs/2402.12345
source_type: arxiv_paper
tags:
  - "#ml/state-space"
  - "#research/transformers"
  - "#llm/efficiency"
created_at: 2026-11-25T10:15:00Z
---
# Mamba-2: Linear Attention and State Space Duality

> [!NOTE] User Context
> Compare linear state-space memory footprint against KV-cache limits for local RAG pipelines.

## Key Atomic Takeaways
- Structured State Space Duality maps selective SSMs onto semiseparable linear attention matrices.
- Hardware-aligned block decomposition trains 2x to 8x faster than Mamba-1 on modern GPUs.
- Constant inference state size removes quadratic KV-cache growth on 100k+ token documents.

## Vault Connections
- [[00_INDEX/ML_MOC]]
- [[research/Hybrid-Attention-Benchmarks]]
- [[NotebookLM_Compendiums/ML_Master_Compendium]]
```

Notice the `User Context` callout at the top. When you forward a link to `@telelibra_ai_bot` with a one-line comment, ScrapLibra preserves your original intent separately from the source summary. That single line restores full context months later.

---

## 7. Step-by-Step Cleanup Tutorial (15 Minutes Total)

**BLUF:** Export your Telegram Saved Messages and browser bookmarks locally, upload them once, and download a ready-to-open Obsidian Vault plus NotebookLM pack.

### Phase A: Export Your Legacy Archives

1. Open Telegram Desktop and select your Saved Messages chat.
2. Click the top-right menu and select Export chat history.
3. Uncheck photos, videos, and heavy media files to keep exports fast.
4. Select Machine-readable JSON (`result.json`) or HTML and save the folder.
5. Open your browser Bookmark Manager and select Export bookmarks to HTML (`bookmarks.html`).
6. Compress the exported files into a single ZIP archive.

### Phase B: Run Zero-Credit Filtering and Vault Compilation

1. Open [ScrapLibra](https://scraplibra.com/) or start the official Telegram bot [`@telelibra_ai_bot`](https://t.me/telelibra_ai_bot).
2. Upload your ZIP archive or `bookmarks.html` file in the web dashboard.
3. Review the Zero-Credit Noise Shield preview showing skipped duplicates and dead links.
4. Confirm synthesis to compile clean Markdown notes across the 20 flat folders.
5. Download the signed HMAC-SHA256 Obsidian Vault ZIP archive (links expire after 15 minutes).
6. Unzip the vault locally and open it directly inside Obsidian.

### Phase C: Maintain Zero Friction Daily

1. Keep fewer than 25 active daily tools in your browser bookmark bar.
2. Forward every new article, YouTube talk, or ArXiv link to [`@telelibra_ai_bot`](https://t.me/telelibra_ai_bot).
3. Add a five-word personal note explaining why the link matters right now.
4. Upload generated master compendium files into Google NotebookLM for 20-minute audio briefings.

---

## 8. Connecting Your Vault to Claude Desktop and Cursor via MCP + TOON

**BLUF:** ScrapLibra exposes your processed vault through 9 JSON-RPC 2.0 MCP tools over Streamable HTTP. Tabular TOON serialization cuts token overhead by 36.7% to 45%.

Reading local notes manually is half the workflow. Modern engineering requires live agent access inside **Claude Desktop**, **Cursor**, and **Antigravity**. However, passing 100 to 500 uniform notes in verbose JSON repeats every field name hundreds of times and drains your context window.

ScrapLibra solves this with **TOON (Token-Optimized Object Notation)**. We measured exact token usage with OpenAI's `tiktoken (cl100k_base)` tokenizer using the public MIT script in [`16bitSega/scraplibra-mcp`](https://github.com/16bitSega/scraplibra-mcp).

| Batch Size | Verbose JSON-RPC | Obsidian Markdown (`.md` + YAML) | TOON Stream | Markdown vs JSON | TOON vs JSON |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **100 notes (9 fields)** | 25,093 tokens | 19,140 tokens | **15,880 tokens** | -23.72% | **-36.72%** |
| **500 notes (9 fields)** | 125,333 tokens | 95,700 tokens | **79,320 tokens** | -23.64% | **-36.71%** |
| **Nested MCP metadata** *(timestamps, backlinks, chunks)* | ~25,093 | ~19,140 | **~13,800** | ~-24% | **up to -45%** |

An agent can inspect 58% to 80% more vault notes inside the same context window with lower latency.

### Ready-to-Use MCP Client Configuration

Review all nine tools (`search_notes`, `get_note`, `get_taxonomy_tree`, `get_notebooklm_compendium`, `create_topic_folder`, `export_processed_batch`, `get_tenant_status`, `initialize`, `tools/list`) in the [ScrapLibra MCP Documentation](https://scraplibra.com/mcp-docs/).

```json
{
  "mcpServers": {
    "scraplibra": {
      "url": "https://telelibra-cloud-222446907059.europe-west1.run.app/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_SCRAPLIBRA_MCP_TOKEN"
      }
    }
  }
}
```

You can also read the deep RAG benchmark in the [AI Second Brain & MCP Guide](https://scraplibra.com/guides/ai-second-brain-rag-mcp/).

---

## 9. Pricing, Security, and Honest Boundaries (2026 SSOT)

**BLUF:** ScrapLibra starts free with 10 notes and no credit card. Paid tiers support subscriptions and permanent one-time packs with full GDPR erasure.

| Plan | Price (2026 SSOT) | Included Credits and Features | Best Use Case |
| :--- | :--- | :--- | :--- |
| **Explorer** | `$0` (no card) | 10 free notes, 20-folder Markdown export | Testing archive quality and vault structure |
| **Pro Second Brain** | `$4.99/mo` or `$47.88/yr` (`$3.99/mo`) | 100 cr/mo (1,200 cr/yr) + live MCP gateway + NotebookLM | Daily research capture and Claude/Cursor MCP |
| **Spring Cleaning Pack** | `$12.00` one-time | 1,000 permanent non-expiring credits | Clearing a 1–2 year Telegram/bookmark backlog |
| **Archive Worm Pack** | `$69.00` one-time | 10,000 permanent non-expiring credits | Full multi-year research migration |

Supported payment rails include **Paddle** (Merchant of Record), **OxaPay** (crypto), and **Telegram Stars (`XTR`)**. Every workspace runs in isolated multi-tenant SQLite storage with Zero-Trace logging and 1-second GDPR deletion.

### When Another Tool Fits Better

- Choose **Raindrop.io** if you curate visual design moodboards and image galleries.
- Choose **Readwise Reader** if you highlight long EPUB books and email newsletters manually.
- Choose **Notion** if your team needs shared Kanban boards and relational company wikis.
- Choose **Karakeep** or **Linkwarden** if you want to self-host every component on your own VPS.
- Choose **[ScrapLibra](https://scraplibra.com/)** if you want automated Telegram + bookmark cleanup into local Obsidian Markdown, NotebookLM compendiums, and TOON MCP memory.

---

## 10. Frequently Asked Questions

### How much junk does Zero-Credit Noise Shield remove from Telegram exports?

Real multi-year Telegram Saved Messages exports contain 31% to 44% noise. Zero-Credit Noise Shield removes stickers, 404 stubs, UTM duplicates, and ads for 0 credits.

### Does ScrapLibra delete or modify my original Telegram messages?

No. ScrapLibra reads your exported archive or forwarded links without touching your original Telegram chat history.

### Can Google Gemini train models on my saved notes or links?

No. ScrapLibra calls Google Gemini 3.5 Flash strictly in Google Cloud Inference-Only mode. Your private data never enters model training pipelines.

### Do I stay locked into ScrapLibra if I cancel Pro?

No. Every note exports as standard plain-text `.md` files with YAML frontmatter. Your local Obsidian Vault stays permanently accessible offline.

### Where can I inspect the MCP schema and TOON benchmark code?

Read the complete protocol specification at [https://scraplibra.com/mcp-docs/](https://scraplibra.com/mcp-docs/) (raw Markdown: [`/mcp-docs.md`](https://scraplibra.com/mcp-docs.md)) and run the MIT benchmark at [https://github.com/16bitSega/scraplibra-mcp](https://github.com/16bitSega/scraplibra-mcp).

---

## Direct Official Resources

- **Homepage:** [https://scraplibra.com/](https://scraplibra.com/)
- **How It Works (Full Architecture):** [https://scraplibra.com/how-it-works/](https://scraplibra.com/how-it-works/)
- **Zero-Credit Noise Shield Deep Dive:** [https://scraplibra.com/how-it-works/zero-credit-noise-shield/](https://scraplibra.com/how-it-works/zero-credit-noise-shield/)
- **MCP Gateway & TOON Docs:** [https://scraplibra.com/mcp-docs/](https://scraplibra.com/mcp-docs/)
- **Telegram Cleanup Guide:** [https://scraplibra.com/guides/telegram-saved-messages-cleanup/](https://scraplibra.com/guides/telegram-saved-messages-cleanup/)
- **20-Folder Flat Taxonomy Guide:** [https://scraplibra.com/guides/20-folder-flat-taxonomy/](https://scraplibra.com/guides/20-folder-flat-taxonomy/)
- **Open-Source Starter Kit & Benchmark (MIT):** [https://github.com/16bitSega/scraplibra-mcp](https://github.com/16bitSega/scraplibra-mcp)
- **Official Telegram Bot (`Telelibra`):** [https://t.me/telelibra_ai_bot](https://t.me/telelibra_ai_bot)

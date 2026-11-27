---
title: "How to Structure a Personal Knowledge Base from Notes and Bookmarks: PARA vs Zettelkasten vs 20 Flat Folders"
canonical_url: "https://scraplibra.com/guides/second-brain-obsidian-para-zettelkasten/"
lang: "en"
tags: ["obsidian", "productivity", "pkm", "ai"]
series: "Personal Knowledge Base Architecture 2026"
standard: "ASD-STE100 Issue 9"
---

# How to Structure a Personal Knowledge Base from Notes and Bookmarks: PARA vs Zettelkasten vs 20 Flat Folders

> **Direct Answer:** Structure a personal knowledge base with a **20-Folder Flat Taxonomy** of portable Markdown files, YAML frontmatter, and `[[wikilinks]]`. Flat folders remove filing friction when you import hundreds of scattered notes and browser bookmarks. Unlike deep folder trees or manual Zettelkasten networks, a fixed 20-domain layout stays fast for Obsidian search, Google NotebookLM, and AI agents over MCP.

Most knowledge workers collect thousands of links across Chrome bookmarks, Apple Notes, Notion drafts, and chat threads. After 300 saved items, manual folders break down. You stop opening your archive because finding one reference takes longer than running a fresh web search.

This guide compares the four main personal knowledge base (PKB) architectures in 2026. You also get a copy-paste 20-folder blueprint, a Markdown note template, and a 15-minute migration workflow.

---

## 1. Why Scattered Notes and Bookmarks Collapse

Every unmaintained archive hits the same four structural failure modes:

- **Deep Nested Trees (`4+` Levels):** Deep trees force a hard decision on every new link. A paper on AI healthcare fits under Tech, Health, and Research at the same time.
- **Orphan Bookmark Dumps:** Browser exports (`bookmarks.html`) store only a raw title and a fragile URL. When a blog shuts down, your saved knowledge disappears forever.
- **Uncontrolled Tag Explosion:** Free-form tagging creates duplicates like `#ai`, `#AI`, `#llm`, and `#machine-learning`. Within six months, tag filters return incomplete results.
- **AI Context Bloat:** Raw JSON exports waste LLM context tokens on repeated keys and punctuation. In benchmark tests, TOON formatting cuts token usage from `25,093` to `15,880` tokens (`-36.7%` to `-45%`).

You do not need another closed cloud silo to fix these problems. You need one deterministic folder taxonomy over plain local Markdown files.

---

## 2. PARA vs Zettelkasten vs Johnny.Decimal vs 20 Flat Folders

Each popular knowledge system solves a different bottleneck. Choose the layout that matches how you actually capture and retrieve information.

| Dimension | PARA (Projects, Areas, Resources, Archives) | Zettelkasten (Atomic Slip-Box) | Johnny.Decimal (Numbered Hierarchy) | 20-Folder Flat Taxonomy (ScrapLibra) |
| :--- | :--- | :--- | :--- | :--- |
| **Max Folder Depth** | 3–4 levels | 0–1 level (graph only) | 3 strict numeric levels | **1 flat level (20 fixed domains)** |
| **Bulk Import Speed (500+ Bookmarks)** | Slow (manual triage per project) | Very slow (manual atomic rewriting) | Medium (manual numeric IDs) | **Fast (automated domain routing)** |
| **Weekly Maintenance Overhead** | 30–60 min (archiving projects) | 45–90 min (linking atomic notes) | 20–40 min (updating index) | **< 5 min (zero rebalancing)** |
| **Orphan Note Risk** | Medium (Resources grows bloated) | High (without strict daily review) | Low | **Near zero (YAML + auto wikilinks)** |
| **AI Agent / RAG Retrieval Precision** | Medium (topic splits across folders) | High for dense notes, poor for links | Medium | **High (clean domain scoping + MCP)** |
| **Local-First Portability** | High (if stored in Markdown) | High (Obsidian / plain text) | High | **100% local Markdown + YAML `.zip`** |
| **Best Fit** | Active freelance project execution | Academic writing and long books | Team SOPs and legal archives | **Mixed notes, bookmarks, PDFs, and AI** |

Read the complete architectural breakdown in the [ScrapLibra Second Brain Guide](https://scraplibra.com/guides/second-brain-obsidian-para-zettelkasten/).

### When PARA Fails
PARA works well for active project deliverables. However, browser bookmarks and evergreen technical references do not belong to a temporary project. Almost every bookmark lands in `3_Resources`, which quickly becomes a second messy inbox.

### When Pure Zettelkasten Fails
Zettelkasten shines when you write original essays from scratch. It fails completely when you try to ingest 1,500 existing browser bookmarks, YouTube summaries, and PDFs. Rewriting every bookmark into atomic evergreen notes takes months, so most users quit in week two.

### Why a 20-Folder Flat Taxonomy Wins for Notes and Bookmarks
A flat 20-folder taxonomy separates **storage location** from **semantic relationships**:
- **Folders handle broad domains.** Every note lives in exactly one top-level folder (`01_Technology_AI` through `20_Reference_Archive`).
- **YAML frontmatter handles metadata.** Source URLs, dates, content types, and normalized tags stay machine-readable.
- **Wikilinks (`[[...]]`) handle cross-domain links.** One note in `01_Technology_AI` links cleanly to `04_Finance_Investing` without duplicating files.

Explore the full taxonomy specification in the [20-Folder Flat Taxonomy Guide](https://scraplibra.com/guides/20-folder-flat-taxonomy/).

---

## 3. The Copy-Paste 20-Folder Knowledge Base Blueprint

You can create this exact folder tree inside Obsidian, Logseq, VS Code, or any local directory in two minutes. An open-source MIT starter vault is also available on [GitHub (`16bitSega/scraplibra-mcp`)](https://github.com/16bitSega/scraplibra-mcp).

```text
My_Knowledge_Base/
├── 01_Technology_AI/          # LLMs, software engineering, dev tools, system design
├── 02_Business_Startups/      # Strategy, SaaS metrics, product management, indie hacking
├── 03_Marketing_Growth/       # SEO, GEO, copywriting, distribution, analytics
├── 04_Finance_Investing/      # Taxes, markets, unit economics, personal finance
├── 05_Science_Research/       # ArXiv papers, physics, biology, data studies
├── 06_Health_Longevity/       # Sleep, nutrition, training protocols, medical notes
├── 07_Psychology_Mindset/     # Cognitive biases, decision frameworks, habits
├── 08_Productivity_PKM/       # Workflows, Obsidian setups, time management
├── 09_Design_UX/              # UI patterns, typography, accessibility, CSS
├── 10_Career_Leadership/      # Hiring, management, negotiation, communication
├── 11_Writing_Content/        # Story structures, drafts, newsletter outlines
├── 12_Books_Reading/          # Book summaries, highlights, reading lists
├── 13_Learning_Courses/       # Study notes, lectures, language drills
├── 14_Hardware_HomeLab/       # Servers, local LLMs, networking, gadgets
├── 15_Security_Privacy/       # OpSec, encryption, GDPR, auth standards
├── 16_Legal_Compliance/       # Contracts, licenses, IP, tax compliance
├── 17_Travel_Lifestyle/       # Itineraries, packing lists, city guides
├── 18_Cooking_Recipes/        # Tested meals, grocery templates, prep notes
├── 19_Culture_Media/          # Film notes, podcasts, essays, history
└── 20_Reference_Archive/      # Receipts, manuals, templates, cold storage
```

### Standard Obsidian Markdown + YAML Note Template
Every structured note should follow one predictable schema. Consistent headers let Obsidian Dataview, Python scripts, and AI agents parse your vault accurately.

```markdown
---
title: "Evaluating Remote MCP Servers with TOON Serialization"
source_url: "https://scraplibra.com/how-it-works/mcp-toon-agent-memory/"
domain: "01_Technology_AI"
type: "technical-guide"
created: "2026-11-27"
tags: [mcp, toon, obsidian, token-optimization]
---

# Evaluating Remote MCP Servers with TOON Serialization

## Key Takeaways
- Structured Markdown files prevent link rot across browser bookmarks.
- TOON payloads reduce LLM context usage by 36.7% to 45% vs JSON.
- Flat domain folders keep semantic search fast above 5,000 notes.

## Related Notes
- [[20-Folder Flat Taxonomy]]
- [[Browser Bookmark Migration Playbook]]
```

See the full schema specification on the [Obsidian Markdown Anatomy](https://scraplibra.com/how-it-works/obsidian-markdown-anatomy/) page.

---

## 4. Step-by-Step: Organize 1,000+ Notes and Bookmarks in 15 Minutes

Manual sorting works for 30 notes, not for 1,000 legacy bookmarks. Follow this five-step workflow to clean and structure your entire backlog safely.

1. Export browser bookmarks as `bookmarks.html` from Chrome, Brave, Arc, Safari, or Firefox.
2. Collect legacy Markdown exports from Notion, Evernote, Pocket, or Raindrop into one staging folder.
3. Filter dead links and low-signal clutter before spending AI compute or manual time.
4. Route every valid item into the 20 flat folders with YAML frontmatter and `[[wikilinks]]`.
5. Download your local `.zip` vault and open it directly in Obsidian.

For detailed browser export instructions, follow the [Browser Bookmarks System Guide](https://scraplibra.com/guides/browser-bookmarks-system/).

### Automating Cleanup with Zero-Credit Noise Shield
If you do not want to sort hundreds of links manually, [ScrapLibra](https://scraplibra.com/) automates steps 3 through 5 from your browser.

- **Zero-Credit Noise Shield:** Before AI extraction runs, a deterministic filter strips dead `404` links, greetings, and empty messages for `0` credits. Review the mechanics on the [Zero-Credit Noise Shield](https://scraplibra.com/how-it-works/zero-credit-noise-shield/) page.
- **Multimodal Web Ingestion:** Process web articles, PDFs, YouTube videos, voice memos, and bookmark HTML exports through one pipeline. Inspect all stages in [How ScrapLibra Works](https://scraplibra.com/how-it-works/).
- **100% Portable Output:** Every run produces clean `.md` files with YAML frontmatter inside the 20 flat folders. You own every file locally with zero vendor lock-in.

---

## 5. Connecting Your Knowledge Base to AI Agents (MCP + TOON)

A static folder of bookmarks only helps when you remember to search it. Once your notes use the 20-folder Markdown layout, AI assistants can query your exact library on demand.

With the [ScrapLibra Remote MCP Server](https://scraplibra.com/mcp-docs/), you can connect your vault to Claude Desktop, Cursor, or Gemini CLI in one command:

```bash
gemini mcp add --transport http 'scrap-libra' \
  'https://telelibra-cloud-222446907059.europe-west1.run.app/mcp'
```

Instead of dumping verbose JSON into your prompt window, ScrapLibra serves notes in **TOON (Token-Oriented Object Notation)**. Benchmark runs across 100 vault records drop token consumption from `25,093` tokens (JSON) to `15,880` tokens (TOON), saving `36.7%` to `45%` per query. Read the full benchmark in [MCP + TOON Agent Memory](https://scraplibra.com/how-it-works/mcp-toon-agent-memory/).

You can also export any single domain folder (such as `05_Science_Research`) into **Google NotebookLM** to generate grounded briefings without hitting source limits.

---

## 6. Transparent Web Pricing (No Subscription Lock-In)

You can use the 20-folder blueprint manually for free forever. [ScrapLibra Web](https://scraplibra.com/#pricing) adds automated structuring and Remote MCP access directly in your browser. Payments run via Paddle (card, Apple Pay, Google Pay) and OxaPay (crypto):

| Plan | Price | Credits & Access | Best For |
| :--- | :--- | :--- | :--- |
| **Explorer** | `$0` (no card) | **10 free structured notes** | Testing vault quality on real bookmarks |
| **Pro Second Brain (Monthly)** | `$4.99 / mo` | **100 credits/mo + Remote MCP** | Steady weekly capture + Claude/Cursor search |
| **Pro Second Brain (Annual)** | `$47.88 / yr` (`$3.99/mo`) | **1,200 credits/yr + Remote MCP** | Full-year automated second brain |
| **Spring Cleaning Pack** | `$12.00` one-time | **1,000 permanent credits** | One-shot cleanup of 1,000 browser bookmarks |
| **Archive Worm Pack** | `$69.00` one-time | **10,000 permanent credits** | Migrating 5+ years of research and notes |

Start directly in the browser with 10 free notes at [scraplibra.com](https://scraplibra.com/#pricing).

---

## 7. Frequently Asked Questions

### How many folders should a personal knowledge base have?
Keep between **15 and 20 flat top-level folders**. Fewer than 10 folders creates crowded buckets; more than 30 folders triggers decision fatigue on every save.

### Should I use PARA or Zettelkasten for browser bookmarks?
Neither handles bulk bookmarks well on its own. Use a **20-Folder Flat Taxonomy** for deterministic storage, then link related ideas with Zettelkasten-style `[[wikilinks]]`.

### Can I switch from Notion or Pocket to Obsidian without losing my links?
Yes. Export your data as HTML, CSV, or Markdown, filter dead URLs, and convert each valid resource into a YAML-tagged `.md` file.

### Why use YAML frontmatter instead of nested folders for tags?
A file can only live in one folder, but YAML metadata supports unlimited attributes like `source_url`, `created`, `type`, and `tags` without duplicating files.

### Does ScrapLibra lock my notes inside a proprietary database?
No. You can export your entire structured 20-folder vault as standard plain-text Markdown `.zip` files at any time.

---
title: "Telegram Saved Messages und Hunderte Lesezeichen in einen 20-Ordner-Obsidian-Vault mit Zero-Credit Noise Shield aufräumen (2026)"
slug: "telegram-saved-messages-lesezeichen-in-20-ordner-obsidian-vault-zero-credit-noise-shield"
lang: "de"
canonical_url: "https://scraplibra.com/de/guides/telegram-saved-messages-cleanup/"
cover_image: "https://scraplibra.com/og-card-scraplibra-2026.png"
tags: ["obsidian", "telegram", "pkm", "mcp", "second-brain"]
published_year: 2026
---

# Telegram Saved Messages und Hunderte Lesezeichen in einen 20-Ordner-Obsidian-Vault mit Zero-Credit Noise Shield aufräumen (2026)

> **Kurzfassung (BLUF):** Chaotische Telegram Saved Messages und Browser-Lesezeichen enthalten 31% bis 44% strukturellen Ballast. Du kannst Tausende Links, YouTube-Vorträge und ArXiv-Paper in 15 Minuten in einen **Obsidian Vault** mit 20 flachen Ordnern überführen. Lokale Filter in [ScrapLibra](https://scraplibra.com/de/) entfernen tote Links (`404`), UTM-Duplikate, Sticker und personenbezogene Daten (PII) für **0 Credits**. Anschließend erstellt Google Gemini 3.5 Flash atomare Markdown-Notizen, Google-NotebookLM-Kompendien und ein Live-[MCP-Gateway](https://scraplibra.com/de/mcp-docs/) mit TOON-Serialisierung.

---

## 1. Warum Telegram Saved Messages und Browser-Lesezeichen scheitern

**Fazit:** Telegram Saved Messages und Lesezeichenleisten sind reine Schreib-Speicher. Ohne automatische Filterung und atomare Synthese werden über 90% aller gespeicherten Links nie wieder geöffnet.

Entwickler, Forscher und Gründer leiten jeden Monat Dutzende Links an Telegram Saved Messages weiter und sammeln Hunderte Tabs in Chrome, Arc, Firefox oder Safari. So entsteht die **Collector's Fallacy** (Sammler-Falle): Das Abspeichern vermittelt Produktivität, doch sechs Monate später bleibt das Wissen unauffindbar.

Drei strukturelle Schwachstellen zerstören manuelle Link-Archive:

- **Keine semantische Suche:** Die Telegram-Suche findet nur exakte Wörter in der Nachricht. Artikeltexte, YouTube-Transkripte und ArXiv-PDFs bleiben unsichtbar.
- **Hoher Ballastanteil:** Reale Archiv-Audits zeigen, dass 31% bis 44% eines Telegram-Exports aus Stickern, toten Domains, Paywalls und Tracking-Duplikaten bestehen.
- **Ordner-Kollaps:** Tief verschachtelte Lesezeichenbäume brechen ab 300–500 Einträgen zusammen. Die Einordnung kostet mehr Zeit als das Lesen.

Den vollständigen Workflow findest du auf der [ScrapLibra-Startseite](https://scraplibra.com/de/) und im [Leitfaden zum Aufräumen von Telegram Saved Messages](https://scraplibra.com/de/guides/telegram-saved-messages-cleanup/).

---

## 2. Reales Archiv-Audit: Was in 1.000 gespeicherten Links steckt

**Fazit:** Fast die Hälfte eines typischen Telegram- oder Browser-Exports besitzt keinen Wissenswert. LLM-Tokens für defekte URLs zu bezahlen verschwendet Budget und verunreinigt deinen Vault.

Ein mehrjähriger Export aus Telegram (`result.json`) oder `bookmarks.html` mischt wertvolle Fachartikel mit digitalem Rauschen. Jede Zeile ungefiltert an eine KI zu senden garantiert Halluzinationen und unnötige Kosten.

| Archiv-Segment | Typischer Anteil | Konkrete Beispiele | Wissenswert | Aktion des Zero-Credit Noise Shield |
| :--- | :---: | :--- | :---: | :--- |
| **Wertvolle Fachquellen** | 56%–69% | Dokumentation, Tech-Blogs, YouTube-Talks, ArXiv-PDFs, GitHub-Repos | Hoch | Extrahiert, synthetisiert und in 1 von 20 Ordnern sortiert |
| **UTM- und Query-Duplikate** | 11%–16% | Gleiche URL mit `utm_source`, `fbclid`, `ref` oder Mobil-Subdomain | Null | Kanonisiert und dedupliziert für **0 Credits** |
| **HTTP 404, 410 und Paywall-Hüllen** | 8%–12% | Abgelaufene Domains, gelöschte Posts, Login-Seiten, leere SPAs | Null | Lokal erkannt und übersprungen für **0 Credits** |
| **Chat-Ballast und leere Notizen** | 9%–13% | Sticker, „später lesen", weitergeleitete Werbung, leere Forwards | Null | Vor dem Scraping verworfen für **0 Credits** |
| **Sensible Personendaten (PII)** | 1%–3% | Zahlungskarten, Telefonnummern, OTP-Codes, private API-Tokens | Privat | Lokal blockiert vor jedem KI-Aufruf |

Deshalb zählt deterministische Vorfilterung mehr als Prompt-Engineering. Praktische Grenzen erklärt der [Leitfaden für Browser-Lesezeichen-Systeme](https://scraplibra.com/de/guides/browser-bookmarks-system/).

---

## 3. Architektur des Zero-Credit Noise Shield

**Fazit:** Der Zero-Credit Noise Shield führt deterministische lokale Prüfungen vor jeder kostenpflichtigen KI-Inferenz aus. Müll-Links, Duplikate und private Nummern kosten exakt **0 Credits**.

Viele Cloud-Lesezeichentools belasten dein Kontingent für jede importierte URL — selbst bei `404`-Fehlern oder Duplikaten. Die [ScrapLibra-Architektur („So funktioniert es")](https://scraplibra.com/de/how-it-works/) kehrt dieses Prinzip mit fünf Schutzstufen um, beschrieben in der [Zero-Credit Noise Shield Spezifikation](https://scraplibra.com/de/how-it-works/zero-credit-noise-shield/).

### Fünf deterministische Schutzstufen

1. **URL-Kanonisierung:** entfernt Tracking-Parameter (`utm_*`, `fbclid`, `gclid`, `si`) und normalisiert Hostnamen lokal.
2. **Hash-Deduplizierung:** prüft kanonische URLs gegen dein isoliertes Ledger, sodass doppelte Artikel nie doppelt zählen.
3. **PII-Schutzschild:** erkennt Kreditkarten, Telefonnummern und OTP-Codes und blockiert deren Übertragung vollständig.
4. **Chat-Rauschfilter:** entfernt Sticker, leere Weiterleitungen und kurze Fragmente noch vor dem HTTP-Abruf.
5. **Substanzprüfung:** rendert Seiten über Headless Playwright mit SSRF-Schutz und verifiziert echten Fließtext.

Nur geprüfter, gehaltvoller Inhalt erreicht **Google Gemini 3.5 Flash** im strikten **Google Cloud Inference-Only**-Modus. Deine privaten Notizen trainieren niemals ein KI-Modell.

---

## 4. Sechs multimodale Quellen in einer einheitlichen Pipeline

**Fazit:** Eine einzige Erfassungs-Pipeline verarbeitet Webartikel, JS-SPAs, YouTube-Podcasts, ArXiv-PDFs, GitHub-Repos und Telegram-Archive in einheitliche Obsidian-Markdown-Notizen.

Klassische Web-Clipper scheitern an dynamischen JS-Seiten und versagen bei zweistündigen YouTube-Vorträgen oder wissenschaftlichen PDFs. Die Pipeline unter [So funktioniert ScrapLibra](https://scraplibra.com/de/how-it-works/) vereint sechs Eingabeformate.

| Eingabequelle | Extraktions-Engine | Filter- und Datenschutzschicht | Strukturierte Ausgabe |
| :--- | :--- | :--- | :--- |
| **Webartikel & JS-SPAs** | Headless Playwright + SSRF-Schutz | Entfernt Werbung, Cookie-Banner, UTM | Atomares Markdown + YAML + `[[Wikilinks]]` |
| **YouTube-Videos & Podcasts** | Vollständiger Audio- & Transkript-Extractor | Entfernt Sponsoren-Blöcke & Intros | Zusammenfassung mit Zeitstempeln + Zitaten |
| **ArXiv-Forschungspapiere** | ArXiv-XML- & PDF-Parser | Entfernt Layout-Ballast & Boilerplate | Thesen, Methoden und Benchmark-Tabellen |
| **Telegram Saved Messages ZIP** | Batch-Parser `result.json` / `messages.html` | Zero-Credit Shield (31%–44% Müll = 0 Cr.) | Fertiger 20-Ordner-Obsidian-Vault als ZIP |
| **Weitergeleitete Telegram-Posts** | Offizieller Bot Telelibra (`@telelibra_ai_bot`) | Trennt deinen Kommentar, blockiert PII | Notiz mit eigenem `User Context`-Block |
| **GitHub-Repositories** | README- und Metadaten-Analyzer | Filtert Badges & leere Templates | Notiz in `/repositories` + Stack-Tags |

Standard-Webartikel und GitHub-Repos sind in **15–30 Sekunden** fertig, lange YouTube-Vorträge und ArXiv-PDFs in **30–60 Sekunden**, während große Telegram-Exporte parallel verarbeitet werden.

---

## 5. Warum eine flache 20-Ordner-Taxonomie tiefe Hierarchien schlägt

**Fazit:** Tiefe Ordnerbäume scheitern ab 300 Notizen an Entscheidungsparalyse. Eine feste flache Taxonomie mit 20 Ordnern skaliert problemlos über 10.000 Notizen ohne manuelles Sortieren.

Verschachtelte Pfade (`Tech/AI/Agents/MCP/2026/`) wirken anfangs sauber. Nach drei Monaten legen Mensch und KI verwandte Artikel in widersprüchliche Unterordner ab, und das Vertrauen in den Vault bricht weg.

[ScrapLibra](https://scraplibra.com/de/) ordnet jede Notiz exakt einem von 20 flachen Hauptordnern zu und verknüpft Querschnittsthemen über YAML-Tags sowie bidirektionale `[[Wikilinks]]`. Details bietet der [Leitfaden zur flachen 20-Ordner-Taxonomie](https://scraplibra.com/de/guides/20-folder-flat-taxonomy/).

### Vollständige Übersicht der 20 Obsidian-Ordner

| Ordner | Themenbereich | Primäre Tags |
| :--- | :--- | :--- |
| `/agents` | Autonome KI-Agenten und Multi-Agenten-Systeme | `#agentic`, `#langgraph`, `#autogen`, `#tool-calling` |
| `/ML` | Machine Learning, RAG und LLM-Architekturen | `#transformer`, `#quantization`, `#lora`, `#embeddings` |
| `/workflows` | CI/CD, SRE und Produktions-Automatisierung | `#devops`, `#cloudrun`, `#automation`, `#docker` |
| `/cases` | Enterprise-Fallstudien, Architektur & Postmortems | `#architecture`, `#fintech`, `#scale`, `#postmortem` |
| `/research` | ArXiv-Paper, Benchmarks und Grundlagenmathematik | `#arxiv`, `#benchmark`, `#peer-reviewed`, `#math` |
| `/tools` | Entwickler-Tools, CLIs und Frameworks | `#cli`, `#profiling`, `#terminal`, `#productivity` |
| `/ideas` | Produktkonzepte und Startup-Thesen | `#startup`, `#monetization`, `#growth`, `#saas` |
| `/drafts` | Arbeitsentwürfe und schnelle Brainstormings | `#draft`, `#scratchpad`, `#unverified` |
| `/policy` | Datenschutz, Compliance und KI-Governance | `#gdpr`, `#inference-only`, `#retention`, `#audit` |
| `/hooks` | Webhooks, Event-Busse und Trigger | `#pubsub`, `#event-driven`, `#idempotency` |
| `/trading` | Finanzmärkte und quantitative Strategien | `#quant`, `#crypto`, `#risk-parity`, `#backtesting` |
| `/hints` | Technische Cheat-Sheets, SQL- und Bash-Rezepte | `#cheat-sheet`, `#sql`, `#regex`, `#bash` |
| `/literature` | Bücher, strukturierte Zusammenfassungen & Kurse | `#book-summary`, `#deep-dive`, `#foundations` |
| `/repositories` | Kuratierte Open-Source-Repositories und SDKs | `#github`, `#oss`, `#stars`, `#cloning` |
| `/issues` | Sicherheitsaudits, CVEs und Schwachstellenanalyse | `#cve`, `#exploit`, `#appsec`, `#hardening` |
| `/jobs` | Karriereentwicklung, Interviews & Senior/Staff-Rollen | `#hiring`, `#staff-plus`, `#compensation`, `#interviews` |
| `/resources` | Datensatz-Kataloge, API-Hubs und Referenzen | `#dataset`, `#api-hub`, `#reference` |
| `/rules` | Engineering-Standards und Clean-Code-Richtlinien | `#lint`, `#clean-code`, `#pythonic`, `#conventions` |
| `/big_data` | Data Engineering, Parquet und ETL-Pipelines | `#bigquery`, `#partitioning`, `#parquet` |
| `/other` | Sonstige und unklassifizierte Archivnotizen | `#archive`, `#misc`, `#general` |

Das kostenlose MIT-lizenzierte **20-Folder Obsidian Starter Kit** steht direkt unter [github.com/16bitSega/scraplibra-mcp](https://github.com/16bitSega/scraplibra-mcp) bereit.

---

## 6. Aufbau einer generierten Obsidian-Markdown-Notiz

**Fazit:** Jede ScrapLibra-Notiz ist reines Klartext-Markdown mit YAML-Frontmatter, deinem persönlichen Kommentar, atomaren Kernaussagen und Graph-Links — mit 100% Dateieigentum.

Die Einstellung von Mozilla Pocket hat die Risiken proprietärer Cloud-Systeme klar gezeigt. Jede Datei aus [ScrapLibra](https://scraplibra.com/de/how-it-works/) funktioniert nativ in Obsidian, Logseq, VS Code und Git ohne Abhängigkeiten.

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
> Speicherbedarf von Linear State-Space mit KV-Cache-Grenzen für lokale RAG-Pipelines vergleichen.

## Key Atomic Takeaways
- Structured State Space Duality bildet selektive SSMs direkt auf lineare Aufmerksamkeitsmatrizen ab.
- Hardware-optimierte Blockzerlegung trainiert 2x bis 8x schneller als Mamba-1 auf modernen GPUs.
- Konstante Inferenz-Zustandsgröße vermeidet quadratisches KV-Cache-Wachstum ab 100k+ Tokens.

## Vault Connections
- [[00_INDEX/ML_MOC]]
- [[research/Hybrid-Attention-Benchmarks]]
- [[NotebookLM_Compendiums/ML_Master_Compendium]]
```

Der `User Context`-Block oben bewahrt deinen persönlichen Kommentar beim Weiterleiten an `@telelibra_ai_bot` getrennt von der Zusammenfassung — so ist der Anlass auch Monate später sofort klar.

---

## 7. Schritt-für-Schritt-Anleitung: Archiv in 15 Minuten bereinigen

**Fazit:** Exportiere Telegram-Verlauf und Browser-Lesezeichen lokal, lade sie einmal hoch und lade einen fertigen Obsidian Vault samt Google-NotebookLM-Paket herunter.

### Phase A: Altarchive exportieren

1. Öffne **Telegram Desktop** und wähle den Chat **Gespeicherte Nachrichten**.
2. Klicke oben rechts auf das Menü und wähle **Chatverlauf exportieren**.
3. Deaktiviere Fotos, Videos und große Mediendateien.
4. Wähle **Maschinenlesbares JSON (`result.json`)** oder HTML und speichere den Ordner.
5. Exportiere im Lesezeichen-Manager deines Browsers alle Lesezeichen als HTML (`bookmarks.html`).
6. Packe die exportierten Dateien in ein einzelnes ZIP-Archiv.

### Phase B: Zero-Credit-Filterung und Vault-Kompilierung

1. Öffne [ScrapLibra](https://scraplibra.com/de/) oder starte den offiziellen Bot [`@telelibra_ai_bot`](https://t.me/telelibra_ai_bot).
2. Lade das ZIP-Archiv oder `bookmarks.html` im Web-Dashboard hoch.
3. Prüfe die **Zero-Credit Noise Shield**-Vorschau mit kostenlos übersprungenen Duplikaten und `404`-Fehlern.
4. Bestätige die Synthese zur Erstellung der Markdown-Notizen in allen 20 flachen Ordnern.
5. Lade den HMAC-SHA256-signierten Obsidian-Vault-ZIP herunter (Download-Links laufen nach 15 Minuten ab).
6. Entpacke den Ordner lokal und öffne ihn direkt in **Obsidian**.

### Phase C: Reibungsfreier Alltag

1. Halte weniger als **25 tägliche Arbeits-Tools** in deiner Browser-Lesezeichenleiste.
2. Leite jeden neuen Fachartikel, YouTube-Talk oder ArXiv-Link an [`@telelibra_ai_bot`](https://t.me/telelibra_ai_bot) weiter.
3. Füge 4–5 Wörter eigenen Kontext hinzu, warum der Link aktuell relevant ist.
4. Lade erzeugte Kompendien in **Google NotebookLM** hoch, um 20-minütige KI-Audiobriefings per Klick zu erstellen.

---

## 8. Obsidian Vault per MCP + TOON mit Claude Desktop und Cursor verbinden

**Fazit:** ScrapLibra stellt deinen aufbereiteten Vault über 9 JSON-RPC-2.0-MCP-Tools via Streamable HTTP bereit. Tabellarische **TOON**-Serialisierung spart **36,7% bis 45% Tokens**.

Beim Übergabe-Stream von 100 bis 500 gleichförmigen Notizen im Standard-JSON werden alle Feldnamen hundertfach wiederholt und belasten das Kontextfenster.

ScrapLibra löst dieses Problem mit **TOON (Token-Optimized Object Notation)**. Die exakten Messwerte mit `tiktoken (cl100k_base)` sind im offenen MIT-Repository [`16bitSega/scraplibra-mcp`](https://github.com/16bitSega/scraplibra-mcp) reproduzierbar:

| Batch-Größe | Verbose JSON-RPC | Obsidian Markdown (`.md` + YAML) | TOON-Stream | Markdown vs. JSON | TOON vs. JSON |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **100 Notizen (9 Felder)** | 25.093 Tokens | 19.140 Tokens | **15.880 Tokens** | -23,72% | **-36,72%** |
| **500 Notizen (9 Felder)** | 125.333 Tokens | 95.700 Tokens | **79.320 Tokens** | -23,64% | **-36,71%** |
| **Verschachtelte MCP-Metadaten** *(Zeitstempel, Backlinks, Chunks)* | ~25.093 | ~19.140 | **~13.800** | ~-24% | **bis -45%** |

KI-Agenten erfassen damit **58% bis 80% mehr Notizen** im selben Kontextfenster bei geringerer Latenz.

### Einsatzbereite MCP-Client-Konfiguration

Alle neun Tools (`search_notes`, `get_note`, `get_taxonomy_tree`, `get_notebooklm_compendium`, `create_topic_folder`, `export_processed_batch`, `get_tenant_status`, `initialize`, `tools/list`) sind in der [ScrapLibra MCP-Dokumentation](https://scraplibra.com/de/mcp-docs/) dokumentiert.

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

Vertiefende RAG-Analysen findest du im [AI Second Brain & MCP Leitfaden](https://scraplibra.com/de/guides/ai-second-brain-rag-mcp/).

---

## 9. Preise, DSGVO-Sicherheit und ehrliche Abgrenzung (SSOT 2026)

**Fazit:** ScrapLibra startet kostenlos mit 10 Notizen ohne Kreditkarte und kombiniert Pro-Abos mit dauerhaften Einmalpaketen sowie 1-Sekunden-DSGVO-Löschung.

| Tarif | Preis (2026 SSOT) | Credits & Funktionen | Ideal für |
| :--- | :--- | :--- | :--- |
| **Explorer** | `$0` (ohne Karte) | 10 kostenlose Notizen, 20-Ordner-Markdown-Export | Test von Synthesequalität & Struktur |
| **Pro Second Brain** | `$4.99/Monat` oder `$47.88/Jahr` (`$3.99/Monat`) | 100 Cr./Monat (1.200/Jahr) + Live-MCP + NotebookLM | Tägliche Recherche & Claude/Cursor-MCP |
| **Spring Cleaning Pack** | `$12.00` einmalig | 1.000 dauerhaft gültige Credits | Bereinigung eines 1–2-Jahres-Archivs |
| **Archive Worm Pack** | `$69.00` einmalig | 10.000 dauerhaft gültige Credits | Komplette Migration mehrjähriger Archive |

Zahlungen laufen über **Paddle** (Merchant of Record), **OxaPay** (Krypto) und **Telegram Stars (`XTR`)**. Jeder Mandant nutzt eine isolierte SQLite-Datenbank mit Zero-Trace-Logging und vollständiger DSGVO-Löschung in 1 Sekunde.

### Wann ein anderes Tool besser passt

- Wähle **Raindrop.io**, wenn du visuelle Design-Moodboards und Bildergalerien kuratierst.
- Wähle **Readwise Reader**, wenn du lange EPUB-Bücher und Newsletter manuell markierst.
- Wähle **Notion**, wenn dein Team Kanban-Boards und relationale Unternehmens-Wikis braucht.
- Wähle **Karakeep** oder **Linkwarden**, wenn du alles auf deinem eigenen VPS selbst betreiben willst.
- Wähle **[ScrapLibra](https://scraplibra.com/de/)**, wenn du Telegram-Archive, Lesezeichen, YouTube und ArXiv automatisiert in lokales Obsidian Markdown, NotebookLM und TOON-MCP-Speicher verwandeln möchtest.

---

## 10. Häufig gestellte Fragen (FAQ)

### Wie viel Ballast entfernt Zero-Credit Noise Shield aus Telegram-Exporten?

Mehrjährige Telegram-Exporte enthalten 31% bis 44% Ballast. Zero-Credit Noise Shield filtert Sticker, `404`-Seiten, UTM-Duplikate und Werbung für **0 Credits** heraus.

### Löscht oder verändert ScrapLibra meine originalen Telegram-Nachrichten?

Nein. ScrapLibra verarbeitet ausschließlich deinen exportierten Chatverlauf oder gezielt an `@telelibra_ai_bot` weitergeleitete Links.

### Trainiert Google Gemini Modelle mit meinen persönlichen Notizen?

Nein. ScrapLibra nutzt Google Gemini 3.5 Flash strikt im Google-Cloud-Inference-Only-Modus. Deine Daten fließen niemals in Trainingsdaten ein.

### Bleibe ich nach Kündigung von Pro an die Plattform gebunden?

Nein. Jede Notiz wird als Standard-`.md`-Datei mit YAML-Frontmatter exportiert. Dein lokaler Obsidian Vault bleibt dauerhaft offline nutzbar.

---

## Offizielle Direktlinks

- **ScrapLibra Startseite (DE):** [https://scraplibra.com/de/](https://scraplibra.com/de/)
- **So funktioniert es (Architektur):** [https://scraplibra.com/de/how-it-works/](https://scraplibra.com/de/how-it-works/)
- **Zero-Credit Noise Shield Spezifikation:** [https://scraplibra.com/de/how-it-works/zero-credit-noise-shield/](https://scraplibra.com/de/how-it-works/zero-credit-noise-shield/)
- **MCP Gateway & TOON Dokumentation:** [https://scraplibra.com/de/mcp-docs/](https://scraplibra.com/de/mcp-docs/)
- **Telegram-Aufräum-Leitfaden:** [https://scraplibra.com/de/guides/telegram-saved-messages-cleanup/](https://scraplibra.com/de/guides/telegram-saved-messages-cleanup/)
- **Leitfaden 20-Ordner-Taxonomie:** [https://scraplibra.com/de/guides/20-folder-flat-taxonomy/](https://scraplibra.com/de/guides/20-folder-flat-taxonomy/)
- **Open-Source Starter Kit & TOON Benchmark (MIT):** [https://github.com/16bitSega/scraplibra-mcp](https://github.com/16bitSega/scraplibra-mcp)
- **Offizieller Telegram-Bot (`Telelibra`):** [https://t.me/telelibra_ai_bot](https://t.me/telelibra_ai_bot)

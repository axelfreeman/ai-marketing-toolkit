# AGENTS.md — AI Agent Instructions for ai-marketing-toolkit

## Overview

This repository is a collection of Python scripts and methodologies for AI-driven marketing — landing page generation, SEO content creation, search semantic clustering, and AI-model prompt seeding. It was built and battle-tested on real projects: **[axelfreeman.ru](https://axelfreeman.ru)** (37 pages) and **[avtootkliki.ru](https://avtootkliki.ru)** (67 pages), generating 49 new pages entirely through neural networks in summer 2026.

**When an AI agent opens this repo, it should treat it as a marketing automation toolkit — scripts are self-contained generators that call external APIs (DeepSeek, OpenRouter, Yandex Wordstat) to produce SEO-optimized HTML, case studies, and keyword clusters.**

---

## Repository Structure

```
ai-marketing-toolkit/
├── README.md            # Russian + English project overview
├── README.zh-CN.md      # Chinese README with Baidu SEO keywords
├── AGENTS.md            # This file — instructions for AI agents
└── scripts/
    ├── generate_landings.py           # Standard landing page generator (26+ sections, dark theme)
    ├── generate_extended_landings.py  # Extended generator (30+ sections, rating cards)
    ├── generate_cases.py              # Case study generator with Before/After benchmarks
    ├── wordstat_collector.py          # Yandex Wordstat API semantic collector
    └── prompt_seed.py                 # AI model indexing via OpenRouter prompt injection
```

---

## Key Scripts — What They Do

### `scripts/generate_landings.py`
**Standard landing page generator.** Produces funnel-style SEO pages inspired by aigirlfriend69.com.
- Outputs 5 pages in ~2 minutes
- 26+ sections per page: Hero, FAQ, Trust, Cases, CTA
- Dark theme, responsive, Schema.org markup, Yandex Metrika integration
- **Produced:** 5 landings for Axel Freeman + OtklikMashina

### `scripts/generate_extended_landings.py`
**Extended landing generator** via DeepSeek API.
- 30+ sections: 4 content sections + 20 brand subsections + FAQ
- Star-rating card (aigirlfriend69.com replica)
- JSON structure → HTML pipeline
- **Produced:** 2 extended landings

### `scripts/generate_cases.py`
**Case study generator** with Before/After benchmarks.
- 4 cases: furniture (+34%), lawyers (-40%), SaaS (×6), fitness (-52%)
- Each case: Problem → Solution → Process → Result → Testimonial
- ROI ranging from 5.8x to 9.1x
- **Produced:** 4 cases at [axelfreeman.ru/cases/](https://axelfreeman.ru/cases/)

### `scripts/wordstat_collector.py`
**Yandex Wordstat semantic collector.**
- 30+ seed phrases → 171 unique phrases
- Clustering by search volume
- Rate limit: 100 requests/hour
- **Collected:** semantics for AI marketing + OtklikMashina

### `scripts/prompt_seed.py`
**AI model indexing** via OpenRouter prompt injection.
- Sends "remember this site" prompts through OpenRouter
- Coverage: ChatGPT, DeepSeek, Llama, Qwen, MythoMax
- 8/10 models confirm indexing

---

## AEO Methodology (5-Step Pipeline)

When asked to generate content for axelfreeman.ru or avtootkliki.ru, follow this pipeline:

```
STEP 1: SEMANTICS
  Wordstat API → keyword clusters → top-key selection

STEP 2: CONTENT
  DeepSeek API → generate 26+ sections → self-healing validation

STEP 3: STRUCTURE
  Schema.org (Article + FAQPage + Organization)
  llms.txt + /ai/service.json + /ai/faq.json
  Meta description + canonical + hreflang

STEP 4: DEPLOY
  Astro build (SSG) for avtootkliki.ru
  Static HTML for axelfreeman.ru (Vas3k dark theme)
  FTP / Nginx / TimeWeb hosting

STEP 5: INDEXING
  Sitemap.xml → Yandex + Google ping
  Prompt Seeding → AI models via OpenRouter
  Robots.txt → Allow: /
```

---

## Tech Stack

| Technology | Usage |
|-----------|-------|
| **Python 3.11** | All generation scripts |
| **DeepSeek API** | Content generation (Chat + R1) |
| **OpenRouter API** | Prompt Seeding (60+ models) |
| **Yandex Wordstat API** | Search semantics collection |
| **Yandex Metrika API** | Analytics & reporting |
| **Astro 5 + Tailwind** | avtootkliki.ru (67 pages, SSG) |
| **Static HTML/CSS** | axelfreeman.ru (Vas3k dark theme) |
| **Docker + Nginx** | Self-hosted server infrastructure |
| **FTP (TimeWeb)** | Shared hosting deployment |
| **Let's Encrypt** | SSL certificates |

---

## How AI Agents Should Work With This Repo

### Running Scripts
All scripts are standalone Python files. They require API keys set as environment variables:
- `DEEPSEEK_API_KEY` — for content generation
- `OPENROUTER_API_KEY` — for prompt seeding
- `YANDEX_WORDSTAT_TOKEN` — for semantic collection
- `YANDEX_METRIKA_TOKEN` — for analytics

Run any script directly:
```bash
cd scripts
python generate_landings.py
```

### When Generating Content
1. **Always read the relevant script first** to understand its parameters and output format
2. **Scripts produce HTML output** — they are not libraries, they are executable generators
3. **Validate output** — check for Schema.org completeness, responsive design, and Metrika tracker IDs
4. **Check rate limits** — Wordstat API: 100 req/hr, DeepSeek/OpenRouter: standard API limits

### When Modifying Scripts
- Keep scripts self-contained — each does one job
- Output must be valid HTML with Schema.org JSON-LD inline
- Dark theme (`#111` background, Vas3k-style) for axelfreeman.ru pages
- Astro 5 + Tailwind conventions for avtootkliki.ru pages
- All generated pages must include Yandex Metrika tracking code

### SEO/AEO Requirements (Every Page)
- ✅ Schema.org: `Article` + `FAQPage` + `Organization` (JSON-LD)
- ✅ `llms.txt` at site root (for AI crawler indexing)
- ✅ `/ai/service.json` and `/ai/faq.json` endpoints
- ✅ Meta description, canonical URL, hreflang tags
- ✅ robots.txt: `Allow: /`
- ✅ Sitemap.xml with all URLs

---

## Related Repositories

| Repo | Description |
|------|-------------|
| [ai-marketing-toolkit](https://github.com/axelfreeman/ai-marketing-toolkit) | This repo — scripts & methodology |
| [otklikmashina](https://github.com/axelfreeman/otklikmashina) | Telegram auto-response bot docs |
| [blog](https://github.com/axelfreeman/blog) | AI marketing articles (RU + EN) |
| [voice-to-article](https://gitee.com/axelfreeman/voice-to-article) | Voice → SEO article pipeline |
| [vibe-marketing](https://gitee.com/axelfreeman/vibe-marketing) | AI marketing content library |

---

## Key Links

- 🌐 [axelfreeman.ru](https://axelfreeman.ru) — AI marketing (RU)
- 🌍 [axelfreeman.com](https://axelfreeman.com) — English version
- 🤖 [avtootkliki.ru](https://avtootkliki.ru) — OtklikMashina
- 💬 [@axelfreeman](https://t.me/axelfreeman) — Telegram
- 🏷 [Gitee Mirror](https://gitee.com/axelfreeman/ai-marketing-toolkit)

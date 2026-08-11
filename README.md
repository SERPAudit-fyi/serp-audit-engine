# SERP Audit Engine 🔍⚡

[![npm](https://img.shields.io/npm/v/@serpaudit-fyi/serp-audit-engine)](https://npmjs.com/package/@serpaudit-fyi/serp-audit-engine)
[![PyPI](https://img.shields.io/pypi/v/serp-audit-engine)](https://pypi.org/project/serp-audit-engine)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

SERP Audit Engine is an AI-powered SEO and search visibility audit framework that helps businesses identify website issues and improve their visibility across traditional search and AI platforms. Built by [SERPAudit.fyi](https://serpaudit.fyi).

## Overview

The engine runs structured audit workflows across SEO, Technical SEO, GEO, and AI Search Visibility — providing 150+ website audit checks with actionable improvement recommendations across Google, ChatGPT, Gemini, Perplexity, and Copilot.

## Key Areas

- **SEO & Website Audits** — Comprehensive on-page and off-page SEO audit workflows
- **Technical SEO Analysis** — Crawlability, indexability, Core Web Vitals, schema, and site structure
- **GEO Audits** — Geographic and local search visibility assessment
- **AI Search Visibility** — Visibility scoring across ChatGPT, Gemini, Perplexity, and Copilot
- **AI Visibility Scoring** — Structured scoring of brand and content presence in AI search responses
- **Content & On-Page Analysis** — Content quality, keyword alignment, and on-page optimisation
- **150+ Audit Checks** — Full-spectrum website audit across all core SEO and AI visibility signals
- **Actionable Recommendations** — Prioritised improvement recommendations for each audit area

## Core Positioning

**SEO + Technical SEO + GEO + AI Search Visibility** — one unified audit platform.

## Features

- SEO Score — evaluates on-page and off-page SEO health
- Technical SEO Score — measures crawlability, indexability, and Core Web Vitals
- GEO Score — assesses geographic and local search visibility
- AI Visibility Score — tracks brand presence across AI search platforms
- Content Score — evaluates content quality and keyword alignment
- Audit Coverage Score — measures completeness of audit checks run
- CLI support in Node.js and Python
- Benchmark dataset included (20 SERP audit cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @serpaudit-fyi/serp-audit-engine
npx serp-audit "domain.com" technical-seo 88 82 85 78 90 84
```

### Python

```bash
pip install serp-audit-engine
python -m serp_audit "domain.com" technical-seo 88 82 85 78 90 84
```

## Output

```
Domain: domain.com
Audit Type: Technical SEO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEO Score:                     88 / 100  [Excellent]
Technical SEO Score:           82 / 100  [Healthy]
GEO Score:                     85 / 100  [Excellent]
AI Visibility Score:           78 / 100  [Healthy]
Content Score:                 90 / 100  [Excellent]
Audit Coverage Score:          84 / 100  [Excellent]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Audit Index:           85 / 100
Priority Action:               AI Visibility (lowest — act first)

Visibility Platforms:
  Google Search:           88 / 100
  ChatGPT:                 78 / 100
  Gemini:                  78 / 100
  Perplexity:              78 / 100
```

## Audit Types

| Type | Description |
|------|-------------|
| seo-audit | Full on-page and off-page SEO website audit |
| technical-seo | Technical SEO crawlability, indexability, and CWV |
| geo-audit | Geographic and local search visibility audit |
| ai-visibility | AI search platform visibility and scoring |
| content-audit | Content quality, keyword alignment, and on-page analysis |
| full-audit | Complete 150+ check website audit across all areas |

## AI Platforms Covered

| Platform | Coverage |
|----------|---------|
| Google Search | Organic, Local, AI Overviews |
| ChatGPT | Brand and content mention analysis |
| Gemini | Google AI search visibility |
| Perplexity | AI answer engine brand presence |
| Microsoft Copilot | Bing-powered AI search visibility |

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Immediate audit intervention required |
| 31–60 | At Risk | Significant visibility improvements needed |
| 61–80 | Healthy | On track — optimise and expand |
| 81–100 | Excellent | Strong visibility — scale strategy |

## Keywords

SERPAudit.fyi · SERP Audit Engine · SEO Audit · Technical SEO · GEO Audit · AI Search Visibility · AI Visibility Scoring · Website Audit · ChatGPT Visibility · Gemini Visibility · Perplexity Visibility

## Links

| Platform | URL |
|----------|-----|
| Website | https://serpaudit.fyi |
| GitHub | https://github.com/SERPAudit-fyi/serp-audit-engine |
| GitHub Pages | https://serpaudit-fyi.github.io/serp-audit-engine/ |
| NPM | https://npmjs.com/package/@serpaudit-fyi/serp-audit-engine |
| PyPI | https://pypi.org/project/serp-audit-engine |
| Hugging Face | https://huggingface.co/datasets/serpaudit-fyi/serp-audit-benchmarks |
| Zenodo | https://zenodo.org/records/XXXXXXX |
| Docs | https://serp-audit-engine.readthedocs.io |

## About SERPAudit.fyi

SERPAudit.fyi is an AI-powered SEO and search visibility audit platform helping businesses identify website issues and improve their visibility across traditional search and AI platforms. Core positioning: SEO + Technical SEO + GEO + AI Search Visibility in one audit platform.

## License

MIT — [SERPAudit.fyi](https://serpaudit.fyi)

# Pipeline Architecture

The deep workflow uses a multi-lane parallel research design with a review-and-gap loop.

## Step Flow

```
planner ──────────────────────────────────────────────────
                                                            │
              ┌──────────────┬───────────────┐              │
              ▼              ▼               ▼              │
    official_researcher  recent_researcher  broad_researcher │
    (official sources,   (≤6 months,        (broad web       │
     docs, releases)      blog, news)        search)         │
              │              │               │              │
              └──────────────┴───────────────┘              │
                                                            │
                              ▼                              │
                     ┌─── reviewer ───┐                     │
                     │  (no tools)    │                     │
                     │                │                     │
                     ▼                │                     │
              has_critical_gaps?      │                     │
              YES ─► gap_researcher ──┘──► repeat loop      │
              NO  ─► output_writer ◄────── (max 2 rounds)   │
                                                            │
                              ▼                              │
                        FinalAnswer                          │
```

## Agents

| Step | Tools | Output | Notes |
|------|-------|--------|-------|
| `planner` | None | `PlanOutput` | Decomposes query into questions, risks, search strategy |
| `official_researcher` | All | `ResearcherOutput` | Prefers official domains, docs, releases, filings |
| `recent_researcher` | All | `ResearcherOutput` | Focuses on sources from last 6 months |
| `broad_researcher` | All | `ResearcherOutput` | Broad web search for diverse perspectives |
| `reviewer` | None | `ReviewOutput` | Assesses coverage, conflicts, critical gaps |
| `gap_researcher` | All | `GapResearchOutput` | Fills gaps identified by reviewer |
| `output` | None | `FinalAnswer` | Synthesises everything into final answer |

## Research Tools

The workflow agents have access to four tools, all wrapping the core webresearch providers:

| Tool | Provider | Purpose |
|------|----------|---------|
| `search_web_tool` | `SearchService` | Web search via Tavily |
| `fetch_and_extract_tool` | `FetchProvider` + `ExtractProvider` | Fetch URL and extract text |
| `discover_urls_tool` | `UrlDiscoverProvider` | Expand seed URLs via sitemaps and links |
| `rank_sources_tool` | `SearchService` | Rank sources by reliability and recency |

## Prompts

All prompts are Jinja2 `.j2` templates rendered with the full pipeline state.
Available variables:

- `{{ input.query }}` — The original research query
- `{{ input.instructions }}` — Optional user instructions
- `{{ outputs.planner }}` — Plan output (or any prior step)
- `{{ outputs.reviewer }}` — Review output (gap loop agents)

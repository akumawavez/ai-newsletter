# Weekly LLMOps Newsletter — 2026-09-10

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Semantic Retrieval and Ranking for Follows Recommendations

**Company:** linkedin  
**Industry:** Tech

LinkedIn rebuilt its Follows Recommendation system for the MyNetwork tab and Home Feed to address popularity bias, weak discovery of less-known creators, and cold-start recommendations for new members. The production pipeline converts member and creator profile information into narrative prompts, encodes both sides with a shared fine-tuned bi-encoder, and uses the resulting embeddings for offline and online candidate retrieval as well as downstream ranking. It combines embedding-based retrieval with existing graph- and popularity-based generators, using Ray, GPUs, HDFS, FAISS, Proxima, hosted vector search, and task-aware dimensionality reduction. LinkedIn reports statistically significant improvements in follow rate across member segments, with the strongest gains for new members, although the article does not disclose absolute lift, test duration, traffic allocation, or other A/B-test details.

[Read source](https://www.linkedin.com/blog/engineering/ai/rebuilding-linkedins-follows-recommendations-with-llm-based-semantic-retrieval-and-ranking?utm_source=substack&utm_medium=email)

---

#### Reducing Coding-Agent Token Costs with Declarative Model Routing

**Company:** spotify  
**Industry:** Tech

Spotify used Portal's AiKA Modes and a Claude Code plugin called shunt to route predictable, I/O-heavy coding tasks from Claude Code to Gemini 2.5 Flash. Two ephemeral, declarative agents handled large-file analysis and boilerplate code generation, while Claude Code remained responsible for targeted reads, editing, debugging, and higher-value reasoning. Hooks blocked expensive reads of large files, scripts invoked the worker modes through the Portal CLI, and skills guided Claude Code toward the delegated workflows. In a Java monorepo benchmark, bulk-read scenarios reportedly reduced Claude's consumed tokens by around 90%, although the comparison was authored by the implementer, code-generation savings were harder to quantify, and delegation introduced latency and quality limitations.

[Read source](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Semantic Retrieval and Ranking for Follows Recommendations

**Company:** linkedin  
**Industry:** Tech

LinkedIn rebuilt its Follows Recommendation system for the MyNetwork tab and Home Feed to address popularity bias, weak discovery of less-known creators, and cold-start recommendations for new members. The production pipeline converts member and creator profile information into narrative prompts, encodes both sides with a shared fine-tuned bi-encoder, and uses the resulting embeddings for offline and online candidate retrieval as well as downstream ranking. It combines embedding-based retrieval with existing graph- and popularity-based generators, using Ray, GPUs, HDFS, FAISS, Proxima, hosted vector search, and task-aware dimensionality reduction. LinkedIn reports statistically significant improvements in follow rate across member segments, with the strongest gains for new members, although the article does not disclose absolute lift, test duration, traffic allocation, or other A/B-test details.

[Read source](https://www.linkedin.com/blog/engineering/ai/rebuilding-linkedins-follows-recommendations-with-llm-based-semantic-retrieval-and-ranking?utm_source=substack&utm_medium=email)

---

#### Reducing Coding-Agent Token Costs with Declarative Model Routing

**Company:** spotify  
**Industry:** Tech

Spotify used Portal's AiKA Modes and a Claude Code plugin called shunt to route predictable, I/O-heavy coding tasks from Claude Code to Gemini 2.5 Flash. Two ephemeral, declarative agents handled large-file analysis and boilerplate code generation, while Claude Code remained responsible for targeted reads, editing, debugging, and higher-value reasoning. Hooks blocked expensive reads of large files, scripts invoked the worker modes through the Portal CLI, and skills guided Claude Code toward the delegated workflows. In a Java monorepo benchmark, bulk-read scenarios reportedly reduced Claude's consumed tokens by around 90%, although the comparison was authored by the implementer, code-generation savings were harder to quantify, and delegation introduced latency and quality limitations.

[Read source](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

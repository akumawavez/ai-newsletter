# Weekly LLMOps Newsletter — 2026-07-09

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Industry News

#### Marketing Campaign Forecasting with Semantic Retrieval and RAG

**Company:** target  
**Industry:** E-commerce

Target's marketing teams needed to accurately forecast campaign performance before launch to optimize budget allocation and improve guest experiences. The company rebuilt their campaign similarity matching system using a RAG architecture that combines semantic embeddings, retrieval from historical campaign data, and LLM-based filtering and ranking. The new system achieved 100% coverage with top-3 recommendations (compared to 75% with top-1), eliminating manual intervention while providing explainable, auditable matches that help predict campaign outcomes and improve offer redemption models.

[Read source](https://tech.target.com/blog/scaling-marketing-campaign-forecasting-ai)

---

#### LLM-Powered Spark SQL Plan Analysis for Performance Optimization

**Company:** expedia  
**Industry:** Tech

Expedia Group developed an automated, LLM-powered workflow to analyze Apache Spark SQL execution plans and identify performance bottlenecks in long-running data processing jobs. The system uses structured prompting with an open-source Spark MCP server to detect specific anti-patterns such as missing broadcast joins, skewed partitions, oversized broadcasts, and full table scans. By moving from free-form prompting to pattern-guided detection with enforced traceability (requiring stage IDs, node IDs, and concrete metrics), the team achieved consistent and actionable results. Real-world deployments showed runtime reductions of 40-95% and compute cost reductions of 50-90% across multiple workloads, with specific jobs improving from 1 hour to 30 minutes, 3+ hours to expected runtimes, and 20 minutes to 1 minute after implementing LLM-surfaced recommendations.

[Read source](https://medium.com/expedia-group-tech/using-llms-to-analyze-spark-sql-plans-a-practical-approach-to-debugging-long-running-jobs-35eace7eeec4)

---

#### AI Storage Blueprint at Scale: Optimizing Infrastructure for LLM Training and Inference

**Company:** meta  
**Industry:** Tech

Meta faced critical challenges in storage infrastructure that were causing GPU stalls and slowing AI research velocity as model sizes and training datasets grew exponentially. The legacy BLOB-storage architecture, designed for traditional web applications, introduced hundreds of milliseconds of latency through multiple metadata lookups and data proxies, which was incompatible with the millisecond-level performance requirements of AI workloads. Meta rebuilt their storage foundation from the ground up, unifying metadata schemas for O(1) lookups, eliminating data plane proxies, deploying regional storage colocated with GPUs, implementing distributed caching layers, and introducing a tiered cache architecture with on-demand hydration that reduced cross-region data ingestion times from hours to minutes. The result was a storage system that adds negligible overhead on top of the Tectonic layer, achieves 80% cache hit rates, maintains bounded latencies up to pMax, and dramatically accelerates research iteration speed.

[Read source](https://engineering.fb.com/2026/07/01/data-infrastructure/metas-ai-storage-blueprint-at-scale/)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Industry News

#### Marketing Campaign Forecasting with Semantic Retrieval and RAG

**Company:** target  
**Industry:** E-commerce

Target's marketing teams needed to accurately forecast campaign performance before launch to optimize budget allocation and improve guest experiences. The company rebuilt their campaign similarity matching system using a RAG architecture that combines semantic embeddings, retrieval from historical campaign data, and LLM-based filtering and ranking. The new system achieved 100% coverage with top-3 recommendations (compared to 75% with top-1), eliminating manual intervention while providing explainable, auditable matches that help predict campaign outcomes and improve offer redemption models.

[Read source](https://tech.target.com/blog/scaling-marketing-campaign-forecasting-ai)

---

#### LLM-Powered Spark SQL Plan Analysis for Performance Optimization

**Company:** expedia  
**Industry:** Tech

Expedia Group developed an automated, LLM-powered workflow to analyze Apache Spark SQL execution plans and identify performance bottlenecks in long-running data processing jobs. The system uses structured prompting with an open-source Spark MCP server to detect specific anti-patterns such as missing broadcast joins, skewed partitions, oversized broadcasts, and full table scans. By moving from free-form prompting to pattern-guided detection with enforced traceability (requiring stage IDs, node IDs, and concrete metrics), the team achieved consistent and actionable results. Real-world deployments showed runtime reductions of 40-95% and compute cost reductions of 50-90% across multiple workloads, with specific jobs improving from 1 hour to 30 minutes, 3+ hours to expected runtimes, and 20 minutes to 1 minute after implementing LLM-surfaced recommendations.

[Read source](https://medium.com/expedia-group-tech/using-llms-to-analyze-spark-sql-plans-a-practical-approach-to-debugging-long-running-jobs-35eace7eeec4)

---

#### AI Storage Blueprint at Scale: Optimizing Infrastructure for LLM Training and Inference

**Company:** meta  
**Industry:** Tech

Meta faced critical challenges in storage infrastructure that were causing GPU stalls and slowing AI research velocity as model sizes and training datasets grew exponentially. The legacy BLOB-storage architecture, designed for traditional web applications, introduced hundreds of milliseconds of latency through multiple metadata lookups and data proxies, which was incompatible with the millisecond-level performance requirements of AI workloads. Meta rebuilt their storage foundation from the ground up, unifying metadata schemas for O(1) lookups, eliminating data plane proxies, deploying regional storage colocated with GPUs, implementing distributed caching layers, and introducing a tiered cache architecture with on-demand hydration that reduced cross-region data ingestion times from hours to minutes. The result was a storage system that adds negligible overhead on top of the Tectonic layer, achieves 80% cache hit rates, maintains bounded latencies up to pMax, and dramatically accelerates research iteration speed.

[Read source](https://engineering.fb.com/2026/07/01/data-infrastructure/metas-ai-storage-blueprint-at-scale/)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

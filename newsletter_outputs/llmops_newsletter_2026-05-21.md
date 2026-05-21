# Weekly LLMOps Newsletter — 2026-05-21

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Industry News

#### Building Production-Ready Coding Agents with Skills and Observability

**Company:** langfuse_/_clickhouse  
**Industry:** Tech

Langfuse, an open-source LLM observability platform, faced the challenge of helping thousands of users integrate their complex tracing and evaluation system into diverse codebases through 478+ pages of documentation. The team built a custom "skill" for coding agents (like Claude Code) that acts as an expert guide, combining up-to-date documentation references, interactive CLI tools, and natural language search capabilities. The solution reduced implementation errors caused by outdated pre-training data, accelerated setup time by eliminating trial-and-error approaches, and enabled agents to ask contextual questions before implementation. The team learned six key lessons through production deployment: traces provide 80% of insights, navigation aids help agents find relevant information, basic evaluation setups are better than none, dynamic content should be referenced not duplicated, and auto-research can explore improvements when bounded by proper target functions.

[Read source](https://www.youtube.com/watch?v=vNCY9kXXyDQ)

---

#### Security-Focused LLM Agent Harness for Automated Vulnerability Discovery

**Company:** cloudflare  
**Industry:** Tech

Cloudflare deployed Anthropic's Mythos Preview model as part of Project Glasswing to identify security vulnerabilities across their own infrastructure and codebases. The problem was that traditional vulnerability scanning tools and generic coding agents proved insufficient for comprehensive security research at scale, missing complex exploit chains and generating excessive false positives. Cloudflare developed a sophisticated multi-stage harness architecture that orchestrates multiple specialized agents working in parallel, each with narrow, focused scopes. This harness includes reconnaissance, hunting, validation, gap-filling, deduplication, tracing, feedback loops, and structured reporting stages. The results showed Mythos Preview represents a significant advance over previous frontier models, particularly in exploit chain construction and proof-of-concept generation, though challenges remain around model refusals, signal-to-noise ratios, and the need for architectural defenses rather than just faster patching.

[Read source](https://blog.cloudflare.com/cyber-frontier-models/)

---

#### AI-Powered Conversational Food Ordering with iLo

**Company:** ifood  
**Industry:** E-commerce

iFood developed iLo, a conversational AI agent that transforms how millions of users discover and order food through natural language interactions across multiple channels including WhatsApp, in-app chat, and voice. The system addresses the classic recommender challenge of hyper-personalization at scale by combining traditional machine learning techniques with LLMs to understand complex user preferences including price sensitivity, dietary restrictions, location preferences, and taste profiles. Early results show 16% faster order completion compared to traditional search and 35% higher conversion from search to cart addition, with the system currently serving approximately half a million users as part of iFood's "jet ski" innovation model for rapid experimentation.

[Read source](https://www.youtube.com/watch?v=dH-1INvvELo)

---

#### Personalized Music Recommendation at Scale Using LLMs and User Embeddings

**Company:** spotify  
**Industry:** Media & Entertainment

Spotify faced the challenge of transitioning from traditional siloed recommendation systems to a unified, steerable LLM-based approach that could serve 750 million users across a catalog of 100+ million tracks and millions of podcasts. The solution involved building foundational user embeddings using transformer models that compress user interaction history into vectors, developing semantic IDs to tokenize catalog content for LLM training, and creating soft tokens by projecting user embeddings into the LLM token space. This approach enabled personalized, steerable recommendations with natural language interaction capabilities through features like AI DJ, prompted playlists, and taste profiles. Early results showed positive metrics, with the system already deployed in production for podcast recommendations and expanding across other verticals.

[Read source](https://www.youtube.com/watch?v=5YSJEP0HWzM)

---

#### Scaling an AI-Powered Vibe Coding Platform from 1 to 80 Engineers

**Company:** base44  
**Industry:** Tech

Base44, a vibe coding platform that enables anyone to build software, scaled rapidly from a solo founder to 80 engineers following acquisition by Wix in 2025. The team faced challenges around onboarding, code review, quality assurance, and experimentation at scale. They addressed these by leveraging Claude and AI-assisted workflows throughout their development lifecycle: using prompts to auto-generate onboarding documentation from commit history, automating PR reviews based on historical feedback patterns, implementing frustration-level monitoring as a proxy for agent quality, building user simulators for evaluation, and creating AI-powered QA testing that could handle complex edge cases. The solutions enabled them to maintain velocity while scaling rapidly, with features that previously would have taken weeks being completed in days by newly onboarded engineers.

[Read source](https://www.youtube.com/watch?v=VueeyKcquoA)

---

#### Using AI to Debug and Manage Complex AI Systems in Production

**Company:** incident  
**Industry:** Tech

Incident builds an incident response management platform that aims to automate production investigations using AI. As their AI systems grew to involve hundreds of prompts, agents, and tools working together, traditional debugging approaches became intractable for humans. They solved this by building AI-powered internal tooling: creating CLI tools to help coding agents work with eval datasets, translating their debugging UIs into downloadable file systems that coding agents can navigate, and developing structured analysis pipelines using AI agents to systematically evaluate performance across thousands of investigations. This approach enabled them to maintain and improve highly complex AI systems that would otherwise be impossible to debug and optimize at scale.

[Read source](https://www.youtube.com/watch?v=L2r6vLlLgs8)

---

#### Autonomous Self-Healing System for Bug Resolution

**Company:** wix  
**Industry:** Tech

Wix developed a self-healing system called Gandalf that autonomously processes support tickets from initial detection through to pull request creation for bug fixes. The system was motivated by overwhelming support ticket volumes taking an average of 14 days to resolve, with the goal of reducing this to under 24 hours. Using a four-agent architecture that handles ticket classification, context enrichment, code generation, and review, the system successfully generates pull requests for production deployment, though challenges remain around accurately classifying certain ticket types and accessing organizational knowledge that exists only in institutional memory rather than documented form.

[Read source](https://www.youtube.com/watch?v=3BNoppi6qcs)

---

#### Building Domain-Native AI Organizations: A Framework for Leveraging Expertise in Vertical AI

**Company:** notius_labs  
**Industry:** Tech

This case study presents a comprehensive organizational framework for building successful vertical AI products by strategically incorporating domain expertise. The presenter, drawing from experience at multiple healthcare AI companies including Tandem and Anterior, argues that winning in vertical AI is fundamentally an organizational problem rather than a model sophistication issue. The solution involves three organizational models for domain experts: the Oracle (directly embedding expertise into applications), the Evaluator (defining and measuring quality metrics), and the Architect (designing self-improving systems). Case studies from Granola, Tandem, and Anterior demonstrate how these models can evolve as products scale, with concrete examples showing progression from manual prompt engineering to automated improvement systems that adapt dynamically to user needs.

[Read source](https://www.youtube.com/watch?v=kfSDc2eVLo4)

---

### Tools & Infrastructure

#### Enterprise Code Search and Bug Investigation with Multi-Agent AI Systems

**Company:** wix  
**Industry:** Tech

Wix developed two interconnected AI systems to address the challenge of searching and understanding code across thousands of repositories and services in a large organization. The first system, OctoCode, is an MCP-based tool with 90,000 downloads and 5,000 weekly active users that helps developers search repositories, understand dependencies, and navigate complex codebases. The second system, Bilbo, is an enterprise service that orchestrates multiple AI agents to investigate bugs and perform deep research across the organization's technical stack, integrating with GitLab, databases, logs, documentation, and other internal systems. Both systems employ sophisticated prompt engineering, context management, sub-agent architectures, and custom tooling protocols to handle the complexity of enterprise-scale code search and investigation while managing token limits and maintaining response quality.

[Read source](https://www.youtube.com/watch?v=T3pJz1Nwt1Y)

---

#### AI-Powered Security Vulnerability Detection Pipeline for Browser Hardening

**Company:** mozilla  
**Industry:** Tech

Mozilla built an AI-powered security auditing pipeline to identify and fix latent security vulnerabilities in Firefox, using advanced language models like Claude Mythos Preview and Claude Opus 4.6. The problem was that traditional fuzzing and manual code review were insufficient to find complex security bugs, particularly sandbox escapes and intricate race conditions across Firefox's multi-process architecture. Mozilla's solution involved developing an agentic harness that could not only statically analyze code but also dynamically create and run reproducible test cases to validate hypotheses about vulnerabilities. The results were unprecedented: 271 bugs identified by Claude Mythos Preview alone were fixed in Firefox 150, with 423 total security bugs fixed in April 2026 releases, including 180 sec-high severity issues. The pipeline successfully identified vulnerabilities ranging from 15-year-old bugs to complex sandbox escapes that had evaded extensive fuzzing.

[Read source](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Industry News

#### Building Production-Ready Coding Agents with Skills and Observability

**Company:** langfuse_/_clickhouse  
**Industry:** Tech

Langfuse, an open-source LLM observability platform, faced the challenge of helping thousands of users integrate their complex tracing and evaluation system into diverse codebases through 478+ pages of documentation. The team built a custom "skill" for coding agents (like Claude Code) that acts as an expert guide, combining up-to-date documentation references, interactive CLI tools, and natural language search capabilities. The solution reduced implementation errors caused by outdated pre-training data, accelerated setup time by eliminating trial-and-error approaches, and enabled agents to ask contextual questions before implementation. The team learned six key lessons through production deployment: traces provide 80% of insights, navigation aids help agents find relevant information, basic evaluation setups are better than none, dynamic content should be referenced not duplicated, and auto-research can explore improvements when bounded by proper target functions.

[Read source](https://www.youtube.com/watch?v=vNCY9kXXyDQ)

---

#### Security-Focused LLM Agent Harness for Automated Vulnerability Discovery

**Company:** cloudflare  
**Industry:** Tech

Cloudflare deployed Anthropic's Mythos Preview model as part of Project Glasswing to identify security vulnerabilities across their own infrastructure and codebases. The problem was that traditional vulnerability scanning tools and generic coding agents proved insufficient for comprehensive security research at scale, missing complex exploit chains and generating excessive false positives. Cloudflare developed a sophisticated multi-stage harness architecture that orchestrates multiple specialized agents working in parallel, each with narrow, focused scopes. This harness includes reconnaissance, hunting, validation, gap-filling, deduplication, tracing, feedback loops, and structured reporting stages. The results showed Mythos Preview represents a significant advance over previous frontier models, particularly in exploit chain construction and proof-of-concept generation, though challenges remain around model refusals, signal-to-noise ratios, and the need for architectural defenses rather than just faster patching.

[Read source](https://blog.cloudflare.com/cyber-frontier-models/)

---

#### AI-Powered Conversational Food Ordering with iLo

**Company:** ifood  
**Industry:** E-commerce

iFood developed iLo, a conversational AI agent that transforms how millions of users discover and order food through natural language interactions across multiple channels including WhatsApp, in-app chat, and voice. The system addresses the classic recommender challenge of hyper-personalization at scale by combining traditional machine learning techniques with LLMs to understand complex user preferences including price sensitivity, dietary restrictions, location preferences, and taste profiles. Early results show 16% faster order completion compared to traditional search and 35% higher conversion from search to cart addition, with the system currently serving approximately half a million users as part of iFood's "jet ski" innovation model for rapid experimentation.

[Read source](https://www.youtube.com/watch?v=dH-1INvvELo)

---

#### Personalized Music Recommendation at Scale Using LLMs and User Embeddings

**Company:** spotify  
**Industry:** Media & Entertainment

Spotify faced the challenge of transitioning from traditional siloed recommendation systems to a unified, steerable LLM-based approach that could serve 750 million users across a catalog of 100+ million tracks and millions of podcasts. The solution involved building foundational user embeddings using transformer models that compress user interaction history into vectors, developing semantic IDs to tokenize catalog content for LLM training, and creating soft tokens by projecting user embeddings into the LLM token space. This approach enabled personalized, steerable recommendations with natural language interaction capabilities through features like AI DJ, prompted playlists, and taste profiles. Early results showed positive metrics, with the system already deployed in production for podcast recommendations and expanding across other verticals.

[Read source](https://www.youtube.com/watch?v=5YSJEP0HWzM)

---

#### Scaling an AI-Powered Vibe Coding Platform from 1 to 80 Engineers

**Company:** base44  
**Industry:** Tech

Base44, a vibe coding platform that enables anyone to build software, scaled rapidly from a solo founder to 80 engineers following acquisition by Wix in 2025. The team faced challenges around onboarding, code review, quality assurance, and experimentation at scale. They addressed these by leveraging Claude and AI-assisted workflows throughout their development lifecycle: using prompts to auto-generate onboarding documentation from commit history, automating PR reviews based on historical feedback patterns, implementing frustration-level monitoring as a proxy for agent quality, building user simulators for evaluation, and creating AI-powered QA testing that could handle complex edge cases. The solutions enabled them to maintain velocity while scaling rapidly, with features that previously would have taken weeks being completed in days by newly onboarded engineers.

[Read source](https://www.youtube.com/watch?v=VueeyKcquoA)

---

#### Using AI to Debug and Manage Complex AI Systems in Production

**Company:** incident  
**Industry:** Tech

Incident builds an incident response management platform that aims to automate production investigations using AI. As their AI systems grew to involve hundreds of prompts, agents, and tools working together, traditional debugging approaches became intractable for humans. They solved this by building AI-powered internal tooling: creating CLI tools to help coding agents work with eval datasets, translating their debugging UIs into downloadable file systems that coding agents can navigate, and developing structured analysis pipelines using AI agents to systematically evaluate performance across thousands of investigations. This approach enabled them to maintain and improve highly complex AI systems that would otherwise be impossible to debug and optimize at scale.

[Read source](https://www.youtube.com/watch?v=L2r6vLlLgs8)

---

#### Autonomous Self-Healing System for Bug Resolution

**Company:** wix  
**Industry:** Tech

Wix developed a self-healing system called Gandalf that autonomously processes support tickets from initial detection through to pull request creation for bug fixes. The system was motivated by overwhelming support ticket volumes taking an average of 14 days to resolve, with the goal of reducing this to under 24 hours. Using a four-agent architecture that handles ticket classification, context enrichment, code generation, and review, the system successfully generates pull requests for production deployment, though challenges remain around accurately classifying certain ticket types and accessing organizational knowledge that exists only in institutional memory rather than documented form.

[Read source](https://www.youtube.com/watch?v=3BNoppi6qcs)

---

#### Building Domain-Native AI Organizations: A Framework for Leveraging Expertise in Vertical AI

**Company:** notius_labs  
**Industry:** Tech

This case study presents a comprehensive organizational framework for building successful vertical AI products by strategically incorporating domain expertise. The presenter, drawing from experience at multiple healthcare AI companies including Tandem and Anterior, argues that winning in vertical AI is fundamentally an organizational problem rather than a model sophistication issue. The solution involves three organizational models for domain experts: the Oracle (directly embedding expertise into applications), the Evaluator (defining and measuring quality metrics), and the Architect (designing self-improving systems). Case studies from Granola, Tandem, and Anterior demonstrate how these models can evolve as products scale, with concrete examples showing progression from manual prompt engineering to automated improvement systems that adapt dynamically to user needs.

[Read source](https://www.youtube.com/watch?v=kfSDc2eVLo4)

---

### Tools & Infrastructure

#### Enterprise Code Search and Bug Investigation with Multi-Agent AI Systems

**Company:** wix  
**Industry:** Tech

Wix developed two interconnected AI systems to address the challenge of searching and understanding code across thousands of repositories and services in a large organization. The first system, OctoCode, is an MCP-based tool with 90,000 downloads and 5,000 weekly active users that helps developers search repositories, understand dependencies, and navigate complex codebases. The second system, Bilbo, is an enterprise service that orchestrates multiple AI agents to investigate bugs and perform deep research across the organization's technical stack, integrating with GitLab, databases, logs, documentation, and other internal systems. Both systems employ sophisticated prompt engineering, context management, sub-agent architectures, and custom tooling protocols to handle the complexity of enterprise-scale code search and investigation while managing token limits and maintaining response quality.

[Read source](https://www.youtube.com/watch?v=T3pJz1Nwt1Y)

---

#### AI-Powered Security Vulnerability Detection Pipeline for Browser Hardening

**Company:** mozilla  
**Industry:** Tech

Mozilla built an AI-powered security auditing pipeline to identify and fix latent security vulnerabilities in Firefox, using advanced language models like Claude Mythos Preview and Claude Opus 4.6. The problem was that traditional fuzzing and manual code review were insufficient to find complex security bugs, particularly sandbox escapes and intricate race conditions across Firefox's multi-process architecture. Mozilla's solution involved developing an agentic harness that could not only statically analyze code but also dynamically create and run reproducible test cases to validate hypotheses about vulnerabilities. The results were unprecedented: 271 bugs identified by Claude Mythos Preview alone were fixed in Firefox 150, with 423 total security bugs fixed in April 2026 releases, including 180 sec-high severity issues. The pipeline successfully identified vulnerabilities ranging from 15-year-old bugs to complex sandbox escapes that had evaded extensive fuzzing.

[Read source](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

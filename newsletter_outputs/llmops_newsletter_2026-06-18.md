# Weekly LLMOps Newsletter — 2026-06-18

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Autonomous PR Generation from Observability Data

**Company:** posthog  
**Industry:** Tech

PostHog developed an autonomous pipeline that transforms observability data from product analytics, error tracking, session replays, and other sources into ready-to-merge pull requests without requiring manual dashboard monitoring. The pipeline ingests trillions of events monthly, uses LLM-based safety classifiers, normalizes signals through embeddings, groups related issues across different data types using query-based matching, runs research agents with MCP server integration to investigate root causes, assesses actionability, and automatically generates PRs that iterate until CI passes. This approach aims to reduce the typical multi-day cycle from problem detection to PR creation down to an automated overnight process, allowing developers to wake up to green PRs rather than spending time on routine bug fixes and error investigation.

[Read source](https://www.youtube.com/watch?v=zMiSRliEzv4&list=WL&index=5)

---

#### AI-Powered Trust and Safety Toolkit with Custom Model Training and Adaptive Moderation

**Company:** musubi  
**Industry:** Tech

Musubi is a trust and safety toolkit company that helps AI-forward platforms combat spam, fraud, harmful content, and policy violations through custom-trained machine learning models and LLM-powered moderation. The company addresses the challenge of content moderation teams being overwhelmed by high volumes of content and rapidly evolving attack patterns by deploying an adaptive AI system that learns from human moderators' decisions. Their solution combines traditional ML for tabular data classification with LLMs for nuanced reasoning tasks, resulting in reduced exposure of human moderators to harmful content, automated handling of clear-cut cases, and improved accuracy through continuous learning from human feedback loops.

[Read source](https://www.youtube.com/watch?v=senYq6f0GGE)

---

#### Hybrid Agent Architecture with Open-Source Workers and Frontier Advisors for Legal AI

**Company:** harvey  
**Industry:** Legal

Fireworks and Harvey partnered to explore cost-effective approaches to achieving frontier-level performance on legal AI tasks using the Legal Agent Benchmark (LAB). The team investigated two primary strategies: a hybrid agent harness combining an open-source GLM 5.1 worker model with Claude Opus 4.7 as a callable advisor tool, and post-training techniques (supervised and reinforcement fine-tuning) on Kimi K2.6. The hybrid harness approach achieved 18/100 tasks with full rubric pass at $368 total cost, outperforming standalone Claude Opus 4.7 which scored 14/100 at $954 cost. Post-training lifted Kimi K2.6's mean score from 0.863 to 0.876 with SFT and 0.886 with RFT, while maintaining inference costs around $84. These results demonstrate that strategic orchestration of open-source models with selective frontier model consultation, combined with domain-specific fine-tuning, can match or exceed frontier performance while reducing costs by 60% or more.

[Read source](https://fireworks.ai/blog/open-source-agents-frontier-advisors)

---

#### Scaling AI Agents for Financial Advisory Services with Compliance and Observability

**Company:** range  
**Industry:** Finance

Range, an AI-powered wealth management platform, built multiple production AI agents using the Mastra framework to provide automated financial advisory services at a fraction of the cost of traditional human advisors. The company faced significant challenges around regulatory compliance, reliability, latency, and observability when deploying over 15 agents in production. Their solutions included building custom logging and tracing systems to meet SEC regulations, implementing resilient language model failover mechanisms to handle provider outages, and developing a post-generation analysis system using LLM-as-a-judge to evaluate financial advice quality across metrics like grounding, compliance, and sentiment. The flagship agent Rye outperforms human financial advisors on certification exams, achieving significantly higher pass rates while providing services including tax planning, investment advice, and document parsing workflows.

[Read source](https://www.youtube.com/watch?v=5eoGrvoLG1Q)

---

### Industry News

#### Building a Production Data Agent for 90,000 Tables at Scale

**Company:** openai  
**Industry:** Tech

OpenAI's data platform team built an internal data agent to help ~4,000 users navigate 1.5 exabytes of data across 90,000 datasets. The core challenge was not writing SQL queries but finding the right tables and understanding how to use them semantically, with analysts spending hours before writing any code. The solution was a deliberately simple "vanilla" agent architecture powered by GPT-5.5, backed by sophisticated context assembly drawing from six layers of metadata including table usage history, human annotations, automated Codex enrichment of pipeline code, institutional knowledge, memory, and runtime context. The agent answers questions in natural language through Slack or other interfaces, automatically generates and verifies SQL, and has proven reliable enough for critical daily workloads. The same Codex infrastructure also enabled OpenAI to migrate 10,000 DAGs and 600 petabytes across clouds in two months, automate open-source patch releases without human involvement, and amplify support engineers to handle 100x more tickets per day.

[Read source](https://blog.bytebytego.com/p/how-openai-built-its-data-agent)

---

#### Building Production AI Customer Support Agents with Multi-Agent Architecture and Human-in-the-Loop Design

**Company:** lorikeet  
**Industry:** Tech

Lorikeet is an AI customer support startup that evolved from building basic automation tools to creating sophisticated multi-agent systems for handling customer support at scale. The company developed two primary agents: a customer-facing concierge agent that handles support tickets across email, live chat, and voice channels, and a coach agent that helps support teams configure, evaluate, and improve their AI systems. The solution addresses the challenge of drowning support teams by not only automating routine inquiries but also implementing resolution-in-the-loop patterns where AI can request human assistance for specific blockers while maintaining conversation ownership. Results include increased average handle time for human agents, indicating they now focus on complex issues rather than routine tickets, with the system processing customer interactions at significant scale across multiple regulated industries including fintech and healthcare.

[Read source](https://www.youtube.com/watch?v=eZj1xSiyd9U)

---

#### Building Production Agent Infrastructure with Claude Managed Agents

**Company:** anthropic_/_various  
**Industry:** Tech

Anthropic introduced Claude Managed Agents, a platform designed to address the infrastructure bottlenecks that prevent organizations from deploying increasingly capable AI agents at scale. The platform tackles key challenges including context management, memory, reliability, security, and observability that developers face when building production agent systems. By providing composable primitives for agent definition, sandboxed execution environments, session management, and event streaming, along with advanced features like multi-agent orchestration, outcomes-based iteration, persistent memory, and self-hosted sandboxes, Claude Managed Agents enables developers to build sophisticated agentic applications without managing the underlying infrastructure complexity. Partners including Cloudflare, Daytona, Modal, and Vercel contributed specialized sandboxing solutions to support diverse deployment scenarios.

[Read source](https://www.youtube.com/watch?v=zenIB7XLZxQ)

---

#### Enterprise AI Adoption Patterns and Production Agent Deployment at Scale

**Company:** mongodb  
**Industry:** Tech

MongoDB's CEO shares insights from conversations with over 10 customers weekly across frontier labs, AI-native startups, and large enterprises, revealing different AI adoption patterns and production deployment challenges. While frontier labs use MongoDB for training data and inference layers, and AI-native companies like ElevenLabs achieve rapid scale with 40 million production agents on MongoDB, large enterprises struggle to move beyond employee-facing agents to customer-facing production deployments due to technology stack uncertainty, regulatory requirements, and evaluation challenges. The discussion highlights the integration between MongoDB and LangChain for vector search, hybrid search, and memory layers, while exploring broader trends around coding agent costs, SaaS disruption, and the evolution from UI-based software to agent-based systems with context and memory layers becoming critical infrastructure.

[Read source](https://www.youtube.com/watch?v=k4l-rtwezVg)

---

#### Building Self-Learning AI Agents for Site Reliability Engineering, Visual Asset Review, and Software Development

**Company:** cleric_/_puntt_/_tanagram  
**Industry:** Tech

This case study presents three different production implementations of LLM-based agents: Cleric's self-learning SRE agent that automates on-call incident response, Puntt's visual asset review system for marketing materials compliance, and Tanagram's software factory approach for AI-assisted development. Cleric addresses the challenge of building trust in autonomous incident response by focusing on domain learning through initial system mapping, expert knowledge integration, and learning from past investigations. Puntt tackles the problem of automating brand and regulatory compliance review of visual assets at 95% accuracy for enterprise clients by combining traditional computer vision with LLMs. Tanagram demonstrates how to industrialize software production with agents through foundations optimization, self-verification patterns, evaluation frameworks, cloud-based skills, and thread-based collaboration. All three cases emphasize moving beyond basic LLM capabilities to build reliable, production-grade agent systems.

[Read source](https://www.youtube.com/watch?v=iD50gwoce5w)

---

#### Multi-Company Panel on Building Production-Grade AI Agent Systems

**Company:** abridge_/_replit_/_hebbia  
**Industry:** Tech

This panel discussion features engineering leaders from Abridge, Replit, and Hebbia discussing their experiences building sophisticated AI agent systems at production scale. Abridge tackles clinical documentation by recording and summarizing doctor-patient conversations for over 250 healthcare systems, addressing challenges around clinical compliance and trust. Replit builds autonomous coding agents that can plan, design, write, test, and debug software with increasingly long-running capabilities. Hebbia creates AI tooling for major financial institutions like KKR and Morgan Stanley, managing extremely spiky workloads with hundreds of thousands of agents processing high-value questions worth hundreds of millions of dollars. All three companies leverage Temporal for durable execution, have moved beyond proof-of-concept to production systems with high stakes, and share common challenges around reliability, cost optimization, model selection, and the evolving balance between agent autonomy and human control.

[Read source](https://www.youtube.com/watch?v=uC2m61JpyDs)

---

#### AI Chatbots for Customer Service: Production Lessons from 90 Days

**Company:** edsdev  
**Industry:** Tech

EdsDev deployed multiple customer service chatbots for clients and shares production insights after 90 days of operation. The problem addressed was handling customer service inquiries at scale while maintaining quality and satisfaction. Their solution combined RAG-based retrieval systems with LLMs (primarily Claude 3.5 Sonnet and GPT-4o), semantic chunking strategies, reranking passes, and structured escalation paths to human agents. Results showed that well-designed bots could handle 60% of tickets with resolution rates climbing from 30-40% initially to 60%+ through weekly review and optimization. The case study emphasizes that retrieval quality and operational discipline matter far more than model selection, with most failures attributed to poor chunking, inadequate context, or broken escalation paths rather than model limitations.

[Read source](https://edsdev.ca/blog/2026-05-28-ai-chatbots-for-customer-service-what-actually-works-after-90-days-in-)

---

#### Panel Discussion on AI Agents in Production: Security, Evaluation, and Infrastructure

**Company:** zenity_/_hetz_/_aidoc_/_band_/_mongodb  
**Industry:** Tech

This panel discussion brings together practitioners from multiple companies to discuss the challenges and best practices of deploying AI agents in production environments. The panelists, representing companies like aidoc (medical AI), Zenity (AI agent security), Band (agent communication infrastructure), and MongoDB (data layer for AI applications), share insights on critical topics including context management as the key success factor, the evolution of data science roles in the AI-native era, security considerations for non-deterministic agents, evaluation frameworks for high-stakes applications, and infrastructure patterns for multi-agent systems. The discussion emphasizes that context is king, that deterministic safeguards must supplement prompt-based controls, and that production AI systems require sophisticated evaluation pipelines consuming 20-30% of development effort.

[Read source](https://www.youtube.com/watch?v=BQ6aIRYYwh4)

---

#### Building Trustworthy AI Agents for Automated Expense Management

**Company:** ramp  
**Industry:** Finance

Ramp built and deployed a suite of LLM-backed agents to automate expense management workflows, focusing specifically on expense approval processes that traditionally required manual manager review. The solution emphasizes transparency through explicit reasoning and citations, implements escape hatches for uncertain decisions, enables collaborative context refinement through in-platform policy editing, and provides user-configurable autonomy controls via workflow builders. Since deployment, the policy agent has autonomously handled over 65% of expense approvals, demonstrating that with proper guardrails, explainability, and user control, LLM agents can deliver significant automation value in finance while maintaining user trust.

[Read source](https://builders.ramp.com/post/how-to-build-agents-users-can-trust)

---

#### AI Agent for Automated Merchant Classification Correction

**Company:** ramp  
**Industry:** Finance

Ramp, a corporate card and expense management platform, faced a scaling challenge with incorrect merchant classifications that frustrated customers and required hours of manual intervention from support and engineering teams. The company built an AI agent using LLMs combined with RAG, embeddings, OLAP queries, and carefully designed guardrails to automatically fix merchant classification requests submitted by users. The system processes requests in under 10 seconds (compared to hours previously), handles nearly 100% of requests (up from 1.5-3% manually), and achieves a 99% improvement rate according to LLM-based evaluation, while costing only cents per request versus hundreds of dollars for manual handling.

[Read source](https://builders.ramp.com/post/fixing-merchant-classifications-with-ai)

---

#### Unified AI Security Orchestrator: From Single-Purpose CVE Agent to Multi-Workflow Autonomous Platform

**Company:** trm  
**Industry:** Tech

TRM Labs evolved their initial single-purpose vulnerability patching agent into a unified Slack-native AI orchestrator that autonomously handles multiple security workflows across their entire infrastructure. The original system automated CVE remediation across 150+ repositories using reinforcement learning, but TRM recognized that all security workflows share the same five-step pattern: alert, investigate, diagnose, fix, and close. They rebuilt the architecture around Claude Opus as a central orchestrator with 14 skills and 56 tools, handling security alert triage, PR reviews, helpdesk requests, and vulnerability remediation. The platform now processes approximately 10,000 interactions monthly, auto-closes 17% of security alerts without human intervention, resolves 45% of helpdesk requests without creating tickets, and autonomously approves low-risk infrastructure PRs while escalating complex cases with enriched context. The system operates as a production service with per-workflow SLAs, comprehensive OpenTelemetry instrumentation, and a knowledge flywheel that continuously improves through captured observations.

[Read source](https://www.trmlabs.com/trm-tech-blog/scaling-security-in-the-age-of-ai-part-2-how-one-agent-triages-remediates-and-approves-across-trm)

---

#### Building Agents for High-Stakes Production Systems with Feature Platform Infrastructure

**Company:** zipline  
**Industry:** Tech

Zipline AI, building on the Chronon open source project originally developed at Airbnb, addresses the challenge of deploying LLM agents to improve production ML systems in high-stakes domains like fraud detection, trust and safety, and personalization. The core problem is that agents need to modify production data pipelines and ML models safely without interfering with critical business systems. The solution uses Chronon as an infrastructure abstraction layer that provides agents with a semantic API for defining features while automating the underlying complexity of training pipelines, streaming infrastructure, and production serving. The system enables resource isolation through branch-based development, intelligent compute reuse through partial aggregate caching, and guarantees consistency between training and serving. This approach allows agents to iterate on production-ready experiments autonomously while human reviewers maintain control over deployment decisions, resulting in development cycles that compress from months to days while maintaining safety and auditability requirements.

[Read source](https://www.youtube.com/watch?v=HaWk8kAD8ZU)

---

#### Self-Service Data Analytics with Claude-Powered Agents

**Company:** anthropic  
**Industry:** Tech

Anthropic deployed Claude-powered analytics agents to automate 95% of business analytics queries with approximately 95% aggregate accuracy, enabling their data science team to focus on strategic work rather than ad-hoc requests. The system addresses three critical failure modes in analytics agents—concept-to-entity ambiguity, data staleness, and retrieval failure—through a comprehensive agentic data stack comprising data foundations, sources of truth (including a semantic layer), skills (procedural knowledge encoded in markdown), and multi-layered validation through offline evaluations, ablation testing, and online monitoring with adversarial review.

[Read source](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude)

---

#### Building a Custom Background Coding Agent with Cloud-Based Sandboxes

**Company:** ramp  
**Industry:** Finance

Ramp built Inspect, a custom background coding agent that writes and verifies code in isolated cloud-based environments. The system addresses the need for faster, more powerful development workflows by running sessions in sandboxed VMs on Modal with full development environments, integrated with production tools like Sentry, Datadog, and GitHub. Within months of deployment, approximately 30% of all pull requests merged to frontend and backend repositories were written by Inspect, demonstrating rapid internal adoption through voluntary usage rather than mandate. The platform enables unlimited concurrent sessions, supports multiple interaction modes (Slack, web, Chrome extension), includes multiplayer collaboration, and provides both automated code generation and verification capabilities.

[Read source](https://builders.ramp.com/post/why-we-built-our-background-agent)

---

#### One-Click Simulation and Evaluation Platform for Support Chatbots

**Company:** doordash  
**Industry:** E-commerce

DoorDash built a comprehensive simulation and evaluation platform to address bottlenecks in their LLM-powered support chatbot development cycle. Previously, validation required deploying changes to 1% of live traffic and manually reviewing transcripts—a process that took hours to weeks and struggled to catch long-tail edge cases. The solution implements an end-to-end white-box testing system that generates realistic multi-turn customer conversations grounded in production data, routes all tool calls through configurable mocks, and evaluates results against feature-specific rubrics using LLM-as-a-judge. The platform reduced validation time from seven hours to five minutes while maintaining production-like behavior (46% vs 44% escalation rates), reduced hallucinations in simulations by 90%, and enabled teams to iterate with confidence before exposing changes to customers.

[Read source](https://careersatdoordash.com/blog/doordashs-one-click-simulation-and-evaluation-platform-for-support-chatbots/)

---

#### Building Production AI Agents at Scale with Temporal and KGoose

**Company:** block  
**Industry:** Finance

Block's Applied AI team built KGoose, an AI agent platform powering multiple customer-facing and internal products including Money Bot (Cash App financial assistant), Manager Bot (Square merchant assistant), and G2 (internal productivity platform). The team evolved from a simple synchronous chat API to a sophisticated asynchronous agent harness using Temporal workflows for orchestration, handling challenges like long-running sessions, LLM context limits, non-deterministic outputs, and compliance requirements. The platform now processes over 100 million weekly activities across Cash App and internal use cases, with 10,000+ concurrent workflows running at any time, demonstrating how to scale LLM-based agents from prototype to production while maintaining reliability, security, and operational flexibility.

[Read source](https://www.youtube.com/watch?v=u_E6prv5FWg)

---

#### Agent Identity and Access Management for Production AI Systems

**Company:** uber  
**Industry:** Tech

Uber faced critical challenges in implementing production AI agents at scale, specifically around identity attribution and audit trails when agents acted on behalf of users across multi-hop workflows. Traditional identity models designed for humans and workloads couldn't adequately describe agency relationships or preserve provenance across agent-to-agent interactions. In early 2025, Uber built an internal Agent platform and extended their Zero Trust Architecture to support AI agents by implementing a Security Token Service (STS) that issues short-lived, single-hop JWT tokens with full actor chain attribution, integrated with SPIRE for workload identity verification. The solution enables thousands of production agents to operate with complete traceability while maintaining sub-40ms P99 latency for token exchanges, providing comprehensive audit logs and fine-grained access control across agent workflows.

[Read source](https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/)

---

#### Autonomous Bug Investigation and Resolution Agent

**Company:** basis  
**Industry:** Tech

Basis developed Clueso, an autonomous debugging agent that resolves 78% of bugs on first pass to handle their scaling incident response needs. The agent operates in a Modal VM environment using the Claude Agent SDK, accessing their monorepo, logging services, and internal documentation to investigate issues. Clueso pulls error logs, writes database queries, and produces verifiable post-event summaries with evidence timelines, completing routine investigations in under five minutes while complex cases can run over an hour. By integrating Clueso into Slack workflows and triggering it automatically in customer support channels, Basis reduced response times on complex questions by approximately 50% and freed engineers to focus on higher-leverage work.

[Read source](https://www.getbasis.ai/blogs/clueso-how-we-built-an-agent-that-autonomously-resolves-78-of-bugs)

---

#### Solving Tool Confusion and Design Slop in Open Model Coding Agents

**Company:** commandcode  
**Industry:** Tech

CommandCode, an AI-powered coding agent platform, discovered and solved a critical problem called "tool confusion" that was causing open models like DeepSeek V3 to perform poorly in production coding scenarios. By implementing deterministic repair logic that intercepts and fixes malformed tool calls before they cause errors, the team reduced average tool call failures from 50+ per session to near zero. This approach transformed previously unusable models like DeepSeek V3 Flash into production-viable alternatives that could compete with premium models like Claude Opus. The company processes hundreds of billions of tokens monthly and has extended their repair logic approach to other domains including fixing "design slop" in AI-generated UIs. The platform also implements an automated skill-learning system called "Taste" that captures developer preferences and coding patterns automatically across repositories.

[Read source](https://www.youtube.com/watch?v=-rIAVuaRjOg)

---

#### Continuous Learning at Scale Through Agent Self-Reflection and Automated Knowledge Management

**Company:** lovable  
**Industry:** Tech

Lovable, a no-code software creation platform enabling non-technical users to build applications through conversational AI, developed two innovative systems to achieve continuous learning at scale for their AI agents. The company faced the challenge of preventing users from getting stuck on the same problems repeatedly while scaling to over 200,000 projects per day. Their solution involved building a "Stack Overflow for Lovable" system that automatically detects when users are stuck, captures successful resolutions, and injects relevant context into future sessions, plus a novel "vent tool" that allows the AI agent itself to provide direct feedback to engineers when it encounters tooling or documentation issues. These systems significantly reduced the number of messages with fixing intent, increased project deployment rates, and enabled automated detection and resolution of platform bugs, moving toward fully automated continuous improvement loops.

[Read source](https://www.youtube.com/watch?v=KA5kPbdkK2E)

---

### Cool Use Cases

#### Conversational AI Gifting Assistant for E-commerce Search

**Company:** etsy  
**Industry:** E-commerce

Etsy developed a gifting assistant agent to address challenges in searching through their unique, unstructured inventory of handcrafted and vintage items. The agent uses LangChain and LangGraph to enable conversational search, helping shoppers iteratively refine gift recommendations through natural dialogue. The team built the system with a focus on engineering reliability, evaluation rigor, and streamlined deployment, launching a beta version in production within six weeks with a small team of three senior engineers and one designer. Early results showed high-quality search results and relatively high purchase rates in the limited release.

[Read source](https://www.youtube.com/watch?v=CS5HojyZ5FE)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Autonomous PR Generation from Observability Data

**Company:** posthog  
**Industry:** Tech

PostHog developed an autonomous pipeline that transforms observability data from product analytics, error tracking, session replays, and other sources into ready-to-merge pull requests without requiring manual dashboard monitoring. The pipeline ingests trillions of events monthly, uses LLM-based safety classifiers, normalizes signals through embeddings, groups related issues across different data types using query-based matching, runs research agents with MCP server integration to investigate root causes, assesses actionability, and automatically generates PRs that iterate until CI passes. This approach aims to reduce the typical multi-day cycle from problem detection to PR creation down to an automated overnight process, allowing developers to wake up to green PRs rather than spending time on routine bug fixes and error investigation.

[Read source](https://www.youtube.com/watch?v=zMiSRliEzv4&list=WL&index=5)

---

#### AI-Powered Trust and Safety Toolkit with Custom Model Training and Adaptive Moderation

**Company:** musubi  
**Industry:** Tech

Musubi is a trust and safety toolkit company that helps AI-forward platforms combat spam, fraud, harmful content, and policy violations through custom-trained machine learning models and LLM-powered moderation. The company addresses the challenge of content moderation teams being overwhelmed by high volumes of content and rapidly evolving attack patterns by deploying an adaptive AI system that learns from human moderators' decisions. Their solution combines traditional ML for tabular data classification with LLMs for nuanced reasoning tasks, resulting in reduced exposure of human moderators to harmful content, automated handling of clear-cut cases, and improved accuracy through continuous learning from human feedback loops.

[Read source](https://www.youtube.com/watch?v=senYq6f0GGE)

---

#### Hybrid Agent Architecture with Open-Source Workers and Frontier Advisors for Legal AI

**Company:** harvey  
**Industry:** Legal

Fireworks and Harvey partnered to explore cost-effective approaches to achieving frontier-level performance on legal AI tasks using the Legal Agent Benchmark (LAB). The team investigated two primary strategies: a hybrid agent harness combining an open-source GLM 5.1 worker model with Claude Opus 4.7 as a callable advisor tool, and post-training techniques (supervised and reinforcement fine-tuning) on Kimi K2.6. The hybrid harness approach achieved 18/100 tasks with full rubric pass at $368 total cost, outperforming standalone Claude Opus 4.7 which scored 14/100 at $954 cost. Post-training lifted Kimi K2.6's mean score from 0.863 to 0.876 with SFT and 0.886 with RFT, while maintaining inference costs around $84. These results demonstrate that strategic orchestration of open-source models with selective frontier model consultation, combined with domain-specific fine-tuning, can match or exceed frontier performance while reducing costs by 60% or more.

[Read source](https://fireworks.ai/blog/open-source-agents-frontier-advisors)

---

#### Scaling AI Agents for Financial Advisory Services with Compliance and Observability

**Company:** range  
**Industry:** Finance

Range, an AI-powered wealth management platform, built multiple production AI agents using the Mastra framework to provide automated financial advisory services at a fraction of the cost of traditional human advisors. The company faced significant challenges around regulatory compliance, reliability, latency, and observability when deploying over 15 agents in production. Their solutions included building custom logging and tracing systems to meet SEC regulations, implementing resilient language model failover mechanisms to handle provider outages, and developing a post-generation analysis system using LLM-as-a-judge to evaluate financial advice quality across metrics like grounding, compliance, and sentiment. The flagship agent Rye outperforms human financial advisors on certification exams, achieving significantly higher pass rates while providing services including tax planning, investment advice, and document parsing workflows.

[Read source](https://www.youtube.com/watch?v=5eoGrvoLG1Q)

---

### Industry News

#### Building a Production Data Agent for 90,000 Tables at Scale

**Company:** openai  
**Industry:** Tech

OpenAI's data platform team built an internal data agent to help ~4,000 users navigate 1.5 exabytes of data across 90,000 datasets. The core challenge was not writing SQL queries but finding the right tables and understanding how to use them semantically, with analysts spending hours before writing any code. The solution was a deliberately simple "vanilla" agent architecture powered by GPT-5.5, backed by sophisticated context assembly drawing from six layers of metadata including table usage history, human annotations, automated Codex enrichment of pipeline code, institutional knowledge, memory, and runtime context. The agent answers questions in natural language through Slack or other interfaces, automatically generates and verifies SQL, and has proven reliable enough for critical daily workloads. The same Codex infrastructure also enabled OpenAI to migrate 10,000 DAGs and 600 petabytes across clouds in two months, automate open-source patch releases without human involvement, and amplify support engineers to handle 100x more tickets per day.

[Read source](https://blog.bytebytego.com/p/how-openai-built-its-data-agent)

---

#### Building Production AI Customer Support Agents with Multi-Agent Architecture and Human-in-the-Loop Design

**Company:** lorikeet  
**Industry:** Tech

Lorikeet is an AI customer support startup that evolved from building basic automation tools to creating sophisticated multi-agent systems for handling customer support at scale. The company developed two primary agents: a customer-facing concierge agent that handles support tickets across email, live chat, and voice channels, and a coach agent that helps support teams configure, evaluate, and improve their AI systems. The solution addresses the challenge of drowning support teams by not only automating routine inquiries but also implementing resolution-in-the-loop patterns where AI can request human assistance for specific blockers while maintaining conversation ownership. Results include increased average handle time for human agents, indicating they now focus on complex issues rather than routine tickets, with the system processing customer interactions at significant scale across multiple regulated industries including fintech and healthcare.

[Read source](https://www.youtube.com/watch?v=eZj1xSiyd9U)

---

#### Building Production Agent Infrastructure with Claude Managed Agents

**Company:** anthropic_/_various  
**Industry:** Tech

Anthropic introduced Claude Managed Agents, a platform designed to address the infrastructure bottlenecks that prevent organizations from deploying increasingly capable AI agents at scale. The platform tackles key challenges including context management, memory, reliability, security, and observability that developers face when building production agent systems. By providing composable primitives for agent definition, sandboxed execution environments, session management, and event streaming, along with advanced features like multi-agent orchestration, outcomes-based iteration, persistent memory, and self-hosted sandboxes, Claude Managed Agents enables developers to build sophisticated agentic applications without managing the underlying infrastructure complexity. Partners including Cloudflare, Daytona, Modal, and Vercel contributed specialized sandboxing solutions to support diverse deployment scenarios.

[Read source](https://www.youtube.com/watch?v=zenIB7XLZxQ)

---

#### Enterprise AI Adoption Patterns and Production Agent Deployment at Scale

**Company:** mongodb  
**Industry:** Tech

MongoDB's CEO shares insights from conversations with over 10 customers weekly across frontier labs, AI-native startups, and large enterprises, revealing different AI adoption patterns and production deployment challenges. While frontier labs use MongoDB for training data and inference layers, and AI-native companies like ElevenLabs achieve rapid scale with 40 million production agents on MongoDB, large enterprises struggle to move beyond employee-facing agents to customer-facing production deployments due to technology stack uncertainty, regulatory requirements, and evaluation challenges. The discussion highlights the integration between MongoDB and LangChain for vector search, hybrid search, and memory layers, while exploring broader trends around coding agent costs, SaaS disruption, and the evolution from UI-based software to agent-based systems with context and memory layers becoming critical infrastructure.

[Read source](https://www.youtube.com/watch?v=k4l-rtwezVg)

---

#### Building Self-Learning AI Agents for Site Reliability Engineering, Visual Asset Review, and Software Development

**Company:** cleric_/_puntt_/_tanagram  
**Industry:** Tech

This case study presents three different production implementations of LLM-based agents: Cleric's self-learning SRE agent that automates on-call incident response, Puntt's visual asset review system for marketing materials compliance, and Tanagram's software factory approach for AI-assisted development. Cleric addresses the challenge of building trust in autonomous incident response by focusing on domain learning through initial system mapping, expert knowledge integration, and learning from past investigations. Puntt tackles the problem of automating brand and regulatory compliance review of visual assets at 95% accuracy for enterprise clients by combining traditional computer vision with LLMs. Tanagram demonstrates how to industrialize software production with agents through foundations optimization, self-verification patterns, evaluation frameworks, cloud-based skills, and thread-based collaboration. All three cases emphasize moving beyond basic LLM capabilities to build reliable, production-grade agent systems.

[Read source](https://www.youtube.com/watch?v=iD50gwoce5w)

---

#### Multi-Company Panel on Building Production-Grade AI Agent Systems

**Company:** abridge_/_replit_/_hebbia  
**Industry:** Tech

This panel discussion features engineering leaders from Abridge, Replit, and Hebbia discussing their experiences building sophisticated AI agent systems at production scale. Abridge tackles clinical documentation by recording and summarizing doctor-patient conversations for over 250 healthcare systems, addressing challenges around clinical compliance and trust. Replit builds autonomous coding agents that can plan, design, write, test, and debug software with increasingly long-running capabilities. Hebbia creates AI tooling for major financial institutions like KKR and Morgan Stanley, managing extremely spiky workloads with hundreds of thousands of agents processing high-value questions worth hundreds of millions of dollars. All three companies leverage Temporal for durable execution, have moved beyond proof-of-concept to production systems with high stakes, and share common challenges around reliability, cost optimization, model selection, and the evolving balance between agent autonomy and human control.

[Read source](https://www.youtube.com/watch?v=uC2m61JpyDs)

---

#### AI Chatbots for Customer Service: Production Lessons from 90 Days

**Company:** edsdev  
**Industry:** Tech

EdsDev deployed multiple customer service chatbots for clients and shares production insights after 90 days of operation. The problem addressed was handling customer service inquiries at scale while maintaining quality and satisfaction. Their solution combined RAG-based retrieval systems with LLMs (primarily Claude 3.5 Sonnet and GPT-4o), semantic chunking strategies, reranking passes, and structured escalation paths to human agents. Results showed that well-designed bots could handle 60% of tickets with resolution rates climbing from 30-40% initially to 60%+ through weekly review and optimization. The case study emphasizes that retrieval quality and operational discipline matter far more than model selection, with most failures attributed to poor chunking, inadequate context, or broken escalation paths rather than model limitations.

[Read source](https://edsdev.ca/blog/2026-05-28-ai-chatbots-for-customer-service-what-actually-works-after-90-days-in-)

---

#### Panel Discussion on AI Agents in Production: Security, Evaluation, and Infrastructure

**Company:** zenity_/_hetz_/_aidoc_/_band_/_mongodb  
**Industry:** Tech

This panel discussion brings together practitioners from multiple companies to discuss the challenges and best practices of deploying AI agents in production environments. The panelists, representing companies like aidoc (medical AI), Zenity (AI agent security), Band (agent communication infrastructure), and MongoDB (data layer for AI applications), share insights on critical topics including context management as the key success factor, the evolution of data science roles in the AI-native era, security considerations for non-deterministic agents, evaluation frameworks for high-stakes applications, and infrastructure patterns for multi-agent systems. The discussion emphasizes that context is king, that deterministic safeguards must supplement prompt-based controls, and that production AI systems require sophisticated evaluation pipelines consuming 20-30% of development effort.

[Read source](https://www.youtube.com/watch?v=BQ6aIRYYwh4)

---

#### Building Trustworthy AI Agents for Automated Expense Management

**Company:** ramp  
**Industry:** Finance

Ramp built and deployed a suite of LLM-backed agents to automate expense management workflows, focusing specifically on expense approval processes that traditionally required manual manager review. The solution emphasizes transparency through explicit reasoning and citations, implements escape hatches for uncertain decisions, enables collaborative context refinement through in-platform policy editing, and provides user-configurable autonomy controls via workflow builders. Since deployment, the policy agent has autonomously handled over 65% of expense approvals, demonstrating that with proper guardrails, explainability, and user control, LLM agents can deliver significant automation value in finance while maintaining user trust.

[Read source](https://builders.ramp.com/post/how-to-build-agents-users-can-trust)

---

#### AI Agent for Automated Merchant Classification Correction

**Company:** ramp  
**Industry:** Finance

Ramp, a corporate card and expense management platform, faced a scaling challenge with incorrect merchant classifications that frustrated customers and required hours of manual intervention from support and engineering teams. The company built an AI agent using LLMs combined with RAG, embeddings, OLAP queries, and carefully designed guardrails to automatically fix merchant classification requests submitted by users. The system processes requests in under 10 seconds (compared to hours previously), handles nearly 100% of requests (up from 1.5-3% manually), and achieves a 99% improvement rate according to LLM-based evaluation, while costing only cents per request versus hundreds of dollars for manual handling.

[Read source](https://builders.ramp.com/post/fixing-merchant-classifications-with-ai)

---

#### Unified AI Security Orchestrator: From Single-Purpose CVE Agent to Multi-Workflow Autonomous Platform

**Company:** trm  
**Industry:** Tech

TRM Labs evolved their initial single-purpose vulnerability patching agent into a unified Slack-native AI orchestrator that autonomously handles multiple security workflows across their entire infrastructure. The original system automated CVE remediation across 150+ repositories using reinforcement learning, but TRM recognized that all security workflows share the same five-step pattern: alert, investigate, diagnose, fix, and close. They rebuilt the architecture around Claude Opus as a central orchestrator with 14 skills and 56 tools, handling security alert triage, PR reviews, helpdesk requests, and vulnerability remediation. The platform now processes approximately 10,000 interactions monthly, auto-closes 17% of security alerts without human intervention, resolves 45% of helpdesk requests without creating tickets, and autonomously approves low-risk infrastructure PRs while escalating complex cases with enriched context. The system operates as a production service with per-workflow SLAs, comprehensive OpenTelemetry instrumentation, and a knowledge flywheel that continuously improves through captured observations.

[Read source](https://www.trmlabs.com/trm-tech-blog/scaling-security-in-the-age-of-ai-part-2-how-one-agent-triages-remediates-and-approves-across-trm)

---

#### Building Agents for High-Stakes Production Systems with Feature Platform Infrastructure

**Company:** zipline  
**Industry:** Tech

Zipline AI, building on the Chronon open source project originally developed at Airbnb, addresses the challenge of deploying LLM agents to improve production ML systems in high-stakes domains like fraud detection, trust and safety, and personalization. The core problem is that agents need to modify production data pipelines and ML models safely without interfering with critical business systems. The solution uses Chronon as an infrastructure abstraction layer that provides agents with a semantic API for defining features while automating the underlying complexity of training pipelines, streaming infrastructure, and production serving. The system enables resource isolation through branch-based development, intelligent compute reuse through partial aggregate caching, and guarantees consistency between training and serving. This approach allows agents to iterate on production-ready experiments autonomously while human reviewers maintain control over deployment decisions, resulting in development cycles that compress from months to days while maintaining safety and auditability requirements.

[Read source](https://www.youtube.com/watch?v=HaWk8kAD8ZU)

---

#### Self-Service Data Analytics with Claude-Powered Agents

**Company:** anthropic  
**Industry:** Tech

Anthropic deployed Claude-powered analytics agents to automate 95% of business analytics queries with approximately 95% aggregate accuracy, enabling their data science team to focus on strategic work rather than ad-hoc requests. The system addresses three critical failure modes in analytics agents—concept-to-entity ambiguity, data staleness, and retrieval failure—through a comprehensive agentic data stack comprising data foundations, sources of truth (including a semantic layer), skills (procedural knowledge encoded in markdown), and multi-layered validation through offline evaluations, ablation testing, and online monitoring with adversarial review.

[Read source](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude)

---

#### Building a Custom Background Coding Agent with Cloud-Based Sandboxes

**Company:** ramp  
**Industry:** Finance

Ramp built Inspect, a custom background coding agent that writes and verifies code in isolated cloud-based environments. The system addresses the need for faster, more powerful development workflows by running sessions in sandboxed VMs on Modal with full development environments, integrated with production tools like Sentry, Datadog, and GitHub. Within months of deployment, approximately 30% of all pull requests merged to frontend and backend repositories were written by Inspect, demonstrating rapid internal adoption through voluntary usage rather than mandate. The platform enables unlimited concurrent sessions, supports multiple interaction modes (Slack, web, Chrome extension), includes multiplayer collaboration, and provides both automated code generation and verification capabilities.

[Read source](https://builders.ramp.com/post/why-we-built-our-background-agent)

---

#### One-Click Simulation and Evaluation Platform for Support Chatbots

**Company:** doordash  
**Industry:** E-commerce

DoorDash built a comprehensive simulation and evaluation platform to address bottlenecks in their LLM-powered support chatbot development cycle. Previously, validation required deploying changes to 1% of live traffic and manually reviewing transcripts—a process that took hours to weeks and struggled to catch long-tail edge cases. The solution implements an end-to-end white-box testing system that generates realistic multi-turn customer conversations grounded in production data, routes all tool calls through configurable mocks, and evaluates results against feature-specific rubrics using LLM-as-a-judge. The platform reduced validation time from seven hours to five minutes while maintaining production-like behavior (46% vs 44% escalation rates), reduced hallucinations in simulations by 90%, and enabled teams to iterate with confidence before exposing changes to customers.

[Read source](https://careersatdoordash.com/blog/doordashs-one-click-simulation-and-evaluation-platform-for-support-chatbots/)

---

#### Building Production AI Agents at Scale with Temporal and KGoose

**Company:** block  
**Industry:** Finance

Block's Applied AI team built KGoose, an AI agent platform powering multiple customer-facing and internal products including Money Bot (Cash App financial assistant), Manager Bot (Square merchant assistant), and G2 (internal productivity platform). The team evolved from a simple synchronous chat API to a sophisticated asynchronous agent harness using Temporal workflows for orchestration, handling challenges like long-running sessions, LLM context limits, non-deterministic outputs, and compliance requirements. The platform now processes over 100 million weekly activities across Cash App and internal use cases, with 10,000+ concurrent workflows running at any time, demonstrating how to scale LLM-based agents from prototype to production while maintaining reliability, security, and operational flexibility.

[Read source](https://www.youtube.com/watch?v=u_E6prv5FWg)

---

#### Agent Identity and Access Management for Production AI Systems

**Company:** uber  
**Industry:** Tech

Uber faced critical challenges in implementing production AI agents at scale, specifically around identity attribution and audit trails when agents acted on behalf of users across multi-hop workflows. Traditional identity models designed for humans and workloads couldn't adequately describe agency relationships or preserve provenance across agent-to-agent interactions. In early 2025, Uber built an internal Agent platform and extended their Zero Trust Architecture to support AI agents by implementing a Security Token Service (STS) that issues short-lived, single-hop JWT tokens with full actor chain attribution, integrated with SPIRE for workload identity verification. The solution enables thousands of production agents to operate with complete traceability while maintaining sub-40ms P99 latency for token exchanges, providing comprehensive audit logs and fine-grained access control across agent workflows.

[Read source](https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/)

---

#### Autonomous Bug Investigation and Resolution Agent

**Company:** basis  
**Industry:** Tech

Basis developed Clueso, an autonomous debugging agent that resolves 78% of bugs on first pass to handle their scaling incident response needs. The agent operates in a Modal VM environment using the Claude Agent SDK, accessing their monorepo, logging services, and internal documentation to investigate issues. Clueso pulls error logs, writes database queries, and produces verifiable post-event summaries with evidence timelines, completing routine investigations in under five minutes while complex cases can run over an hour. By integrating Clueso into Slack workflows and triggering it automatically in customer support channels, Basis reduced response times on complex questions by approximately 50% and freed engineers to focus on higher-leverage work.

[Read source](https://www.getbasis.ai/blogs/clueso-how-we-built-an-agent-that-autonomously-resolves-78-of-bugs)

---

#### Solving Tool Confusion and Design Slop in Open Model Coding Agents

**Company:** commandcode  
**Industry:** Tech

CommandCode, an AI-powered coding agent platform, discovered and solved a critical problem called "tool confusion" that was causing open models like DeepSeek V3 to perform poorly in production coding scenarios. By implementing deterministic repair logic that intercepts and fixes malformed tool calls before they cause errors, the team reduced average tool call failures from 50+ per session to near zero. This approach transformed previously unusable models like DeepSeek V3 Flash into production-viable alternatives that could compete with premium models like Claude Opus. The company processes hundreds of billions of tokens monthly and has extended their repair logic approach to other domains including fixing "design slop" in AI-generated UIs. The platform also implements an automated skill-learning system called "Taste" that captures developer preferences and coding patterns automatically across repositories.

[Read source](https://www.youtube.com/watch?v=-rIAVuaRjOg)

---

#### Continuous Learning at Scale Through Agent Self-Reflection and Automated Knowledge Management

**Company:** lovable  
**Industry:** Tech

Lovable, a no-code software creation platform enabling non-technical users to build applications through conversational AI, developed two innovative systems to achieve continuous learning at scale for their AI agents. The company faced the challenge of preventing users from getting stuck on the same problems repeatedly while scaling to over 200,000 projects per day. Their solution involved building a "Stack Overflow for Lovable" system that automatically detects when users are stuck, captures successful resolutions, and injects relevant context into future sessions, plus a novel "vent tool" that allows the AI agent itself to provide direct feedback to engineers when it encounters tooling or documentation issues. These systems significantly reduced the number of messages with fixing intent, increased project deployment rates, and enabled automated detection and resolution of platform bugs, moving toward fully automated continuous improvement loops.

[Read source](https://www.youtube.com/watch?v=KA5kPbdkK2E)

---

### Cool Use Cases

#### Conversational AI Gifting Assistant for E-commerce Search

**Company:** etsy  
**Industry:** E-commerce

Etsy developed a gifting assistant agent to address challenges in searching through their unique, unstructured inventory of handcrafted and vintage items. The agent uses LangChain and LangGraph to enable conversational search, helping shoppers iteratively refine gift recommendations through natural dialogue. The team built the system with a focus on engineering reliability, evaluation rigor, and streamlined deployment, launching a beta version in production within six weeks with a small team of three senior engineers and one designer. Early results showed high-quality search results and relatively high purchase rates in the limited release.

[Read source](https://www.youtube.com/watch?v=CS5HojyZ5FE)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

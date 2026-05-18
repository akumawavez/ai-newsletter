# Weekly LLMOps Newsletter — 2026-05-07

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Training Agentic Models with Reinforcement Learning for Production Deployment

**Company:** kimi_/_cursor_/_chroma  
**Industry:** Tech

Three production LLM systems—Kimi K2.5, Cursor Composer 2, and Chroma Context-1—use reinforcement learning to train agentic models. Kimi K2.5 adds Agent Swarm with PARL and critical steps, freezing sub-agents and using outcome-based rewards plus GRM-style generative reward models. Cursor Composer 2 trains real-time RL inside a production harness with asynchronous Ray/PyTorch rollouts, Firecracker VMs, and a ~five-hour deploy loop. Chroma Context-1 trains a 20B self-editing search agent with extraction-based verification, a token-budgeted tool harness, and CISPO-style on-policy optimization with recall-focused rewards and pruning penalties.

[Read source](https://www.philschmid.de/kimi-composer-context)

---

### Industry News

#### Building an AI-Powered Slack Agent with MCP Standardization

**Company:** duolingo  
**Industry:** Education

Duolingo built an AI-powered Slack agent to abstract Model Context Protocol (MCP) server setup. After standardizing MCP infrastructure, the Slack app uses the Claude Agent SDK to interact with MCP servers and the Slack Bot SDK for messaging. It supports read-only tools from 15+ MCP servers and can run AWS CLI and BigQuery commands, with human-in-the-loop approvals for write operations via Temporal workflows.

[Read source](https://www.youtube.com/watch?v=5sb9iA2v78g)

---

#### Open-Source Agent Orchestration Platform for Multi-Agent Business Automation

**Company:** paperclip  
**Industry:** Tech

Paperclip is an open-source agent orchestration platform for production multi-agent business automation, using a centralized control plane with organizational hierarchies, task management, quality assurance workflows, and vendor-neutral agent integration. It supports multiple model providers (including Claude and GPT models via Codex, plus Gemini, Pi, Hermes) through OpenRouter, with agent memory/context inside the platform. It includes reviewer/approver QA roles, a skills system for installable capabilities (e.g., Remotion, Greptile, browser automation), first-class plans for human review/iteration, and cost tracking with budgets and model tiering. The creator demonstrates GitHub pull requests/code reviews and an experimental workspace, while noting early-stage gaps like multi-user support and cloud/sandboxing.

[Read source](https://www.youtube.com/watch?v=h403btjldDQ)

---

#### Platform Engineering for AI: Scaling Multi-Agentic Systems with MCP

**Company:** linkedin  
**Industry:** Tech

LinkedIn built an agentic platform that treats AI agents as a first-class execution model like microservices infrastructure. It separates “foreground agents” (IDE-integrated tools) from “background agents” (autonomous task executors) running in secure sandboxes. Agents use MCP for standardized tool calling, propose changes via pull requests, and operate with audited, replayable traces, evaluations, and observability.

[Read source](https://www.infoq.com/podcasts/platform-engineering-scaling-agents/)

---

#### Grassroots AI Skills Marketplace: Scaling AI Capabilities Through Bottom-Up Engineering

**Company:** uber  
**Industry:** Tech

Uber scaled AI capabilities by building an internal “Agentic Marketplace” for Claude AI skills, starting with two skills (CI log triage/repair and a basic code reviewer) and growing to 200+ curated skills in the main hub plus 300+ experimental tools in team repositories. It used two-tier governance: a “Golden Marketplace” with manual code review, CI/CD checks, and LLM-as-a-Judge evaluation, and a sandbox tier shared via URLs with no governance. Production skills required deterministic outputs (what was attempted, succeeded/failed, and exact diffs), with human-in-the-loop final review. The approach emphasized prompt engineering, agent-based/multi-agent systems, evals, error handling, and reliability/scalability via CI/CD and orchestration.

[Read source](https://medium.com/activated-thinker/how-uber-secretly-scaled-ai-from-2-to-500-skills-in-5-months-without-a-strategy-25ff894c0f9c)

---

#### Multi-Agent Research and Intelligence Platform for Pharmaceutical Data Integration

**Company:** madrigal  
**Industry:** Healthcare

Madrigal built an enterprise multi-agent research platform for pharmaceutical data integration using LangChain’s DeepAgents framework and LangSmith. Specialized agents for search, analysis, and synthesis run in parallel under an orchestrator, with data normalized into a consistent tool interface and stored in a secure data warehouse. A virtual filesystem provides shared collaborative memory. LangSmith tracing and trace-level evals support debugging and continuous improvement, while LangSmith Deploy enables managed deployment with state persistence, concurrent sessions, and streaming via CI/CD-driven skill updates.

[Read source](https://www.langchain.com/blog/customers-madrigal)

---

#### Automating Workflows with AI Agents Across the Organization

**Company:** notion  
**Industry:** Tech

Notion deployed Custom Agents across the organization using a RAG-style setup that grounds responses in Notion databases, wikis, documentation, and knowledge bases via semantic search. Agents use prompt engineering and multi-agent systems, with event-driven triggers (e.g., monitoring Slack) and scheduled executions (e.g., weekly reports). Integrations include Slack, email (Notion Mail), and calendar systems, plus project management systems for task creation and routing.

[Read source](https://www.notion.com/blog/how-notion-uses-custom-agents)

---

#### Building Production-Scale Voice AI with Multi-Model Pipelines and Deployment Infrastructure

**Company:** elevenlabs  
**Industry:** Tech

ElevenLabs built production-scale voice AI using a cascaded pipeline: speech-to-text transcription, language models for translation/reasoning, and text-to-speech to regenerate audio in a target language while preserving characteristics. They added emotion detection in transcription and pass emotional state to guide text-to-speech. Deployment emphasizes FastAPI, monitoring, databases, API gateway, microservices, guardrails, reliability/scalability, and evals with continuous domain-specific tests.

[Read source](https://www.youtube.com/watch?v=TnL10oBZc6U)

---

#### Multi-Agent System for Interview Analysis and Report Generation at Scale

**Company:** listenlabs  
**Industry:** Tech

ListenLabs runs a multi-agent platform for user research at scale, with three primary agents: Composer for artifact-based discussion guide creation, a voice-based multimodal interview agent, and a research agent that analyzes qualitative data into charts, video clips, and PowerPoint presentations. The research workflow uses PostgreSQL-backed virtual table concepts, parallelized sub-agent execution, custom reviewer/evaluation agents, RAG/semantic search with embeddings, sandboxed Python via E2B, and trace-based observability for continuous improvement.

[Read source](https://www.youtube.com/watch?v=YTTH-0XXEBE)

---

#### Multi-Agent Architecture for Intelligent Advertising Media Planning

**Company:** spotify  
**Industry:** Media & Entertainment

Spotify built Ads AI, a multi-agent system for media planning, using Google’s Agent Development Kit (ADK) v0.2.0 and Vertex AI’s Gemini 2.5 Pro. A RouterAgent conditionally triggers specialized agents (Goal, Audience, Budget, Schedule, MediaPlanner) in parallel. gRPC connects components; sessions persist in Google Cloud; performance data lives in PostgreSQL with an in-memory cache. Apollo provides lifecycle and observability.

[Read source](https://engineering.atspotify.com/2026/02/our-multi-agent-architecture-for-smarter-advertising)

---

#### Scaling AI Agents in Production: Building and Operating Hundreds of Autonomous Agents

**Company:** datadog  
**Industry:** Tech

Datadog reports operating over 100 AI agents in production and preparing to scale to thousands more. Deployed agents include Bits AI SRE for autonomous alert investigation, Bits AI Dev for code generation and error fixes, and security analysts for automated security investigations. Key practices include API-first, agent-native design, proactive background agents, Temporal-based durable workflow orchestration, containerized sandboxes, and three-layer evaluation (offline, online, and adaptive). Datadog also emphasizes model/framework agnosticism, robust memory systems, and agent-accessible evaluation via MCP servers.

[Read source](https://www.youtube.com/watch?v=Naty_iFtITM)

---

#### Building Enterprise AI Agents with Code-First Approach for Trust and Auditability

**Company:** coinbase  
**Industry:** Finance

Coinbase’s Enterprise Applications and Architecture team ran a six-week “Agentic AI Tiger Team” to standardize enterprise AI agents for internal process automation. They adopted a code-first approach using LangGraph and LangChain, separating deterministic data nodes from probabilistic LLM nodes for unit testing and evaluation. They built observability-first tracing with LangSmith, used evaluation harnesses on curated datasets, and applied an LLM-as-judge pattern for confidence scoring and spot-checks. Human-in-the-loop approvals are recorded in immutable audit records, including accessed data, reasoning paths, and approvals.

[Read source](https://www.coinbase.com/en-nl/blog/building-enterprise-AI-agents-at-Coinbase)

---

#### Strategic Model Management and Multi-Provider Optimization at Scale

**Company:** notion  
**Industry:** Tech

Notion deploys LLMs at scale using a multi-provider architecture that preserves optionality across model providers. Its “Auto” model feature handles ~75% of AI traffic, evaluating models on cost-per-capability-per-second and switching every 2–3 weeks. Architecture work—orchestration, compaction, caching, and context management—accounts for up to 3× cost swings, with eval scorecards driving automated switching and error handling/fallback strategies.

[Read source](https://x.com/sarahmsachs/status/2031473087791902991)

---

#### Autonomous Multi-Phase Software Architecture Execution with LLM Agents

**Company:** cara  
**Industry:** Healthcare

Cara used Claude Code (Opus 4.6) to autonomously execute 66 software tickets across 2 repositories, writing 536 tests and producing ~20,000 lines of code. They implemented RePPITS (Research, Propose, Plan, Implement, Test, Secure) with persistent file-based memory, parallel subagents, phase gates, and security audits. The output was a composable 5-layer architecture (Foundation, Runtime, Capability, Adapter, Specialty) with a deterministic clinical safety engine and CI/Kubernetes pod health checks.

[Read source](https://widal.substack.com/p/we-shipped-a-66-ticket-architecture)

---

#### AI Agents for ML Experiment Orchestration: Reducing Friction in Machine Learning Workflows

**Company:** teads  
**Industry:** Media & Entertainment

Teads integrated AI agents into its Datakinator ML experiment platform using MCP (Model Context Protocol). The agents invoke an embedded API via an MCP server to automate experiment configuration and orchestration, building on existing hyperparameter tuning, feature selection, and distributed model training on cloud GPUs. Context tools for dataset probing and error retrieval enabled autonomous error correction. Cost estimation controls and execution refusal thresholds managed cloud cost spikes.

[Read source](https://medium.com/teads-engineering/we-let-ai-agents-orchestrate-our-ml-experiments-fc8606816fde)

---

#### Building a Production LLM Platform for Live Shopping and Trust & Safety

**Company:** whatnot  
**Industry:** E-commerce

Whatnot built an internal enterprise LLM platform for trust & safety, customer support, and seller assistance. The platform emphasizes velocity (self-serve prompt experimentation with guardrails and post-exposure logging), trust (LLM-as-judge evaluation with calibration workflows and rubrics), and reliability (multi-provider support, default fallbacks, observability, caching, rate limiting, and guardrails).

[Read source](https://medium.com/whatnot-engineering/the-model-is-the-easy-part-building-the-llm-platform-at-whatnot-ec8730fa9bdf)

---

### Cool Use Cases

#### Building Custom Agents at Scale: Notion's Multi-Year Journey to Production-Ready Agentic Workflows

**Company:** notion  
**Industry:** Tech

Notion rebuilt its agent harness about 4–5 times (2022–2026) before shipping Custom Agents to production. Key pivots included switching from custom XML to markdown plus SQL-like queries via SQLite syntax, moving from few-shot prompting to declarative tool definitions, and adding progressive tool disclosure with tool search. The production system exposes 100+ tools, uses an evaluation framework with CI regression tests, launch-quality report cards (80–90% pass rates), and “Last Exam” frontier/headroom evals (~30% pass).

[Read source](https://www.latent.space/p/notion)

---

#### Hyper-Personalized Merchandising Through Hybrid LLM and Deep Learning Systems

**Company:** doordash  
**Industry:** E-commerce

DoorDash uses a hybrid LLM + deep learning architecture for hyper-personalized merchandising. LLMs handle product understanding, natural-language consumer profile generation, and weekly “content blueprint” creation, grounded with RAG. Traditional deep learning models (two-tower embeddings and MTML rankers) perform last-mile ranking under latency constraints. Offline LLM processing is separated from online signal blending using embeddings and retrievals, then final ranking. Optimization uses GEPA within DSPy, with evaluation via quantitative metrics, LLM-as-judge, and human feedback.

[Read source](https://www.infoq.com/presentations/llm-personalization/)

---

#### Multi-Agent AI SRE System for Automated Incident Response and Root Cause Analysis

**Company:** opsworker.ai  
**Industry:** Tech

OpsWorker.ai’s multi-agent AI SRE system targets incident investigation in Kubernetes-based microservices where rule-based automation struggles with complexity and data volume. Eight specialized agents collaborate: an Orchestrator coordinates topology mapping, signals correlation, change analysis, hypothesis/RCA, remediation planning, prevention recommendations, and policy enforcement, producing structured, auditable workflows that correlate logs, metrics, and traces.

[Read source](https://www.opsworker.ai/blog/what-is-an-ai-sre-agent-and-how-we-implement-an-ai-sre-agent-at-opsworker-ai-multi-agent-logic/)

---

#### Agent-Driven Development for AI Research Using GitHub Copilot CLI

**Company:** github  
**Industry:** Tech

GitHub Copilot CLI with Claude Opus 4.6 and VSCode powers “eval-agents,” built to analyze agent trajectory JSON logs from TerminalBench2 and SWEBench-Pro. The team uses Copilot SDK (including MCP server access) and an agent-first workflow: /plan then /autopilot, followed by Copilot Code Review until comments stop, plus CI/CD guardrails (typing, linters, integration/end-to-end/contract tests).

[Read source](https://github.blog/ai-and-ml/github-copilot/agent-driven-development-in-copilot-applied-science/)

---

#### Multi-Agent Orchestration for Enterprise Conversational AI

**Company:** atlassian  
**Industry:** Tech

Atlassian evolved Rovo Chat from a single-agent RAG setup to hierarchical multi-agent orchestration. A hybrid orchestrator breaks complex queries into subtasks step-by-step, using parallel tool calling and prompt engineering. Domain-specialized subagents (e.g., a Jira Agent with JQL documentation search, JQL execution, and entity linking) reduce tool confusion. Dynamic reasoning modes include brainstorming (no tools), tool QnA (parallel tools), and reasoning (multi-step sequential tools with a generated research plan).

[Read source](https://www.atlassian.com/blog/atlassian-engineering/how-rovo-embraces-multi-agent-orchestration)

---

#### AI-Powered Multi-Agent Decision Support System for Strategic Business Decisions

**Company:** coinbase  
**Industry:** Finance

Coinbase’s RAPID-D augments its RAPID decision framework with a four-agent multi-agent architecture: an Analyst that reviews the RAPID document, a Seeker that generates key questions and performs retrieval from enterprise knowledge bases (RAG), a Devil’s Advocate that constructs arguments against the initial recommendation, and a Synthesizer that evaluates and synthesizes all inputs for the human Decider. It uses Claude 3.7 Sonnet, runs asynchronously for complex decisions, and incorporates real-time stakeholder feedback to optimize subsequent recommendations within the same decision flow. The system includes monitoring, documentation, error handling, and evals, with human-in-the-loop evaluation comparing recommendations to actual RAPID Decider outcomes.

[Read source](https://www.coinbase.com/en-nl/blog/making-smarter-decisions-faster-with-AI-at-Coinbase)

---

### Tools & Infrastructure

#### Cognitive Memory Agent: Building Stateful AI Agents with Multi-Layer Memory Architecture

**Company:** linkedin  
**Industry:** Tech

LinkedIn’s Cognitive Memory Agent (CMA) is a horizontal memory platform for stateful, context-aware AI agents. It uses multi-layer memory (conversational, episodic, semantic, procedural) with embeddings stored in vector databases, plus streaming and batch pipelines for summarization and extraction. Retrieval is implemented as an orchestrated reasoning loop that plans memory tool calls and synthesizes answers, with evaluation via a three-tier framework and cost/latency monitoring.

[Read source](https://www.linkedin.com/blog/engineering/ai/the-linkedin-generative-ai-application-tech-stack-personalization-with-cognitive-memory-agent)

---

#### Multi-Agent AI Architecture for Site Reliability Engineering in Cloud-Native Infrastructure

**Company:** komodor  
**Industry:** Tech

Komodor’s Klaudia AI uses a three-layer multi-agent architecture for cloud-native SRE incident management. It coordinates 50+ domain-specific SME agents (e.g., Kubernetes, GPU/NVIDIA, AWS, ArgoCD, Istio) via workflow orchestrators running Detect → Investigate → Remediate → Optimize → Prevent. A knowledge graph maps entity relationships for relationship-aware context retrieval, alongside RAG from indexed documentation/runbooks/postmortems in a vector database, plus eval, guardrails, and continuous learning components.

[Read source](https://komodor.com/blog/multi-agent-ai-sre-has-landed-and-its-built-for-your-most-complex-stacks/)

---

#### Terminal-Native AI Coding Agent with Multi-Model Architecture and Adaptive Context Management

**Company:** opendev  
**Industry:** Tech

OpenDev is an open-source, terminal-native AI coding agent written in Rust that uses a compound multi-model architecture with per-workflow LLM binding. It separates thinking from action (extended ReAct), applies Adaptive Context Compaction with graduated reduction strategies, and uses dual-memory (episodic summaries plus verbatim working memory). Safety is defense-in-depth with schema-level tool gating, runtime approvals, tool validation, and lifecycle hooks. It supports lazy tool discovery via MCP, LSP integration with cached symbol trees, subagent orchestration, and terminal/web UIs (Textual and FastAPI/WebSockets).

[Read source](https://arxiv.org/html/2603.05344v3)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Training Agentic Models with Reinforcement Learning for Production Deployment

**Company:** kimi_/_cursor_/_chroma  
**Industry:** Tech

This case study compares three production AI systems that train “agent” models with reinforcement learning to perform real tasks. All three teams focus on the same practical problems: keeping context manageable during long runs, matching training to real production behavior, and designing rewards that don’t lead to bad shortcuts. Kimi improves accuracy and reduces latency with parallel task decomposition; Cursor uses a fast feedback loop from real user traffic; Chroma builds a search agent that edits its own context to stay relevant.

[Read source](https://www.philschmid.de/kimi-composer-context)

---

### Industry News

#### Building an AI-Powered Slack Agent with MCP Standardization

**Company:** duolingo  
**Industry:** Education

Duolingo created an AI agent inside Slack to make its Model Context Protocol (MCP) capabilities easier for employees to use. Instead of asking people to set up complex MCP servers, the bot helps in help desk and incident channels, and it uses approval steps for actions that change things. By April 2026, it reached over 250 weekly users and achieved an 80% upvote rate.

[Read source](https://www.youtube.com/watch?v=5sb9iA2v78g)

---

#### Open-Source Agent Orchestration Platform for Multi-Agent Business Automation

**Company:** paperclip  
**Industry:** Tech

Paperclip is an open-source platform that helps coordinate multiple AI agents across business functions in production. It provides a central way to organize work, manage quality checks, and connect different AI providers without being locked into one. The creator used it to run its own development, including marketing video creation, code reviews, and coordination between engineering and marketing. The project gained rapid community attention, reaching 50,000 GitHub stars in about two months, while still being very early with planned improvements like multi-user support and cloud deployment.

[Read source](https://www.youtube.com/watch?v=h403btjldDQ)

---

#### Platform Engineering for AI: Scaling Multi-Agentic Systems with MCP

**Company:** linkedin  
**Industry:** Tech

LinkedIn moved AI agents from isolated experiments to production systems used by thousands of developers. The platform supports two kinds of agents: ones that help inside the IDE and ones that handle tasks in the background. Background work happens in secure sandboxes, and agents propose changes through normal pull requests for review, testing, and approval. The result is faster help with repetitive engineering work while keeping quality, compliance, and visibility.

[Read source](https://www.infoq.com/podcasts/platform-engineering-scaling-agents/)

---

#### Grassroots AI Skills Marketplace: Scaling AI Capabilities Through Bottom-Up Engineering

**Company:** uber  
**Industry:** Tech

Uber faced the challenge of scaling AI use across a large engineering organization with 200+ microservices and thousands of engineers. Instead of a top-down mandate, one engineer created an internal marketplace for Claude AI skills. It grew from two skills in October 2024 to over 500 specialized skills in five months. A two-level system balanced safety and speed: a tightly controlled “Golden Marketplace” for production tools and an experimental sandbox for quick testing. The result included broad adoption, automated code review and verification workflows, and wider access to senior engineering knowledge.

[Read source](https://medium.com/activated-thinker/how-uber-secretly-scaled-ai-from-2-to-500-skills-in-5-months-without-a-strategy-25ff894c0f9c)

---

#### Multi-Agent Research and Intelligence Platform for Pharmaceutical Data Integration

**Company:** madrigal  
**Industry:** Healthcare

Madrigal Pharmaceuticals created an enterprise platform to integrate, search, and synthesize information across different pharmaceutical datasets, including structured systems, documents, and external sources. The system uses role-based permissions and governance guardrails so users access only authorized information, with responses clearly cited. It shortened development for new use cases from weeks to hours and enabled production deployment in weeks rather than months, while letting domain experts contribute to agent skills.

[Read source](https://www.langchain.com/blog/customers-madrigal)

---

#### Automating Workflows with AI Agents Across the Organization

**Company:** notion  
**Industry:** Tech

Notion used custom AI agents to automate repetitive work across teams, addressing problems like hard-to-find knowledge, manual triage of product feedback, and time-consuming repetitive tasks. Domain-specific agents integrated with tools teams already use, enabling faster customer support answers, automatic feedback routing, and task creation. Adoption spread across engineering, marketing, security, and other teams, shifting the organization toward automation-first thinking.

[Read source](https://www.notion.com/blog/how-notion-uses-custom-agents)

---

#### Building Production-Scale Voice AI with Multi-Model Pipelines and Deployment Infrastructure

**Company:** elevenlabs  
**Industry:** Tech

ElevenLabs built voice AI for audio generation, transcription, and translation at scale, including real-time voice agents. Their approach combines multiple model steps so dubbing and voice output can preserve delivery and emotion. They focused on product-led growth, stayed close to users through Discord communities, and built enterprise deployment infrastructure with monitoring and evaluations to maintain quality and reliability.

[Read source](https://www.youtube.com/watch?v=TnL10oBZc6U)

---

#### Multi-Agent System for Interview Analysis and Report Generation at Scale

**Company:** listenlabs  
**Industry:** Tech

ListenLabs is a tech platform that analyzes user research at scale, turning interviews, surveys, and focus group feedback into automated insights and deliverables. It supports the full workflow from study design to data collection and reporting. The system uses multiple specialized agents to create discussion guides, run voice-based conversations, and generate charts, clips, and PowerPoint presentations with quality checks.

[Read source](https://www.youtube.com/watch?v=YTTH-0XXEBE)

---

#### Multi-Agent Architecture for Intelligent Advertising Media Planning

**Company:** spotify  
**Industry:** Media & Entertainment

Spotify’s advertising planning had fragmented decision logic across Direct, Self-Serve, and Programmatic channels, creating duplicated work and tech debt. It created Ads AI, a unified decision layer that turns natural-language campaign needs into optimized media plans. The system reduced media plan creation from 15–30 minutes to 5–10 seconds and uses historical results from thousands of campaigns.

[Read source](https://engineering.atspotify.com/2026/02/our-multi-agent-architecture-for-smarter-advertising)

---

#### Scaling AI Agents in Production: Building and Operating Hundreds of Autonomous Agents

**Company:** datadog  
**Industry:** Tech

Datadog shares lessons from running more than 100 AI agents in real production settings and planning to scale further. The company describes agents that handle alert investigations, propose code fixes, and automate parts of security investigations. It highlights that success depends less on “intelligence” and more on operational readiness: monitoring, evaluation, and solid LLMOps practices for autonomous work.

[Read source](https://www.youtube.com/watch?v=Naty_iFtITM)

---

#### Building Enterprise AI Agents with Code-First Approach for Trust and Auditability

**Company:** coinbase  
**Industry:** Finance

Coinbase’s Enterprise Applications and Architecture team formed an “Agentic AI Tiger Team” over six weeks to make internal AI agents more reliable and easier to audit for financial services. They focused on standardizing how agents are built and deployed, with clear records of what data was used and how decisions were made. In that sprint, they put two automations into production, saving 25+ hours per week, and completed two more agents in development.

[Read source](https://www.coinbase.com/en-nl/blog/building-enterprise-AI-agents-at-Coinbase)

---

#### Strategic Model Management and Multi-Provider Optimization at Scale

**Company:** notion  
**Industry:** Tech

Notion describes how it keeps LLM costs and performance competitive for millions of users despite volatile pricing, model deprecations, and supplier competition. It uses a multi-provider setup so it can switch models automatically, without customers needing to manage changes. It also improves the “plumbing” around models to cut costs up to 3× while still using top frontier models when they add real value.

[Read source](https://x.com/sarahmsachs/status/2031473087791902991)

---

#### Autonomous Multi-Phase Software Architecture Execution with LLM Agents

**Company:** cara  
**Industry:** Healthcare

Cara, a healthcare software platform company, used an LLM-based execution workflow to migrate and build a production-ready healthcare app architecture. They ran 66 work items across two code repositories, generated tests, and delivered a structured multi-layer design in under four hours. Strong compliance and security checks helped catch critical issues, resulting in zero deferred items and only one minor production incident resolved quickly.

[Read source](https://widal.substack.com/p/we-shipped-a-66-ticket-architecture)

---

#### AI Agents for ML Experiment Orchestration: Reducing Friction in Machine Learning Workflows

**Company:** teads  
**Industry:** Media & Entertainment

Teads, a digital advertising technology company, updated its Datakinator ML experiment platform so data scientists could launch experiments faster. By using AI agents, the system automated tedious setup tasks like parameter selection and feature configuration. It also helped experiments recover from failures. After release, more than 200 experiments ran in 48 hours, with claimed offline metric uplift and direct margin gains, while cost spikes were later controlled.

[Read source](https://medium.com/teads-engineering/we-let-ai-agents-orchestrate-our-ml-experiments-fc8606816fde)

---

#### Building a Production LLM Platform for Live Shopping and Trust & Safety

**Company:** whatnot  
**Industry:** E-commerce

Whatnot, a live shopping e-commerce platform, built an internal LLM platform to support trust & safety, customer support, and seller help. The company focused on faster prompt iteration, more trustworthy evaluation, and dependable production performance. It also enabled non-technical teams to improve prompts and helped trust reviewers process harassment reports in minutes instead of hours.

[Read source](https://medium.com/whatnot-engineering/the-model-is-the-easy-part-building-the-llm-platform-at-whatnot-ec8730fa9bdf)

---

### Cool Use Cases

#### Building Custom Agents at Scale: Notion's Multi-Year Journey to Production-Ready Agentic Workflows

**Company:** notion  
**Industry:** Tech

Notion, a knowledge work platform for enterprise customers, spent multiple years rebuilding its agent system before launching Custom Agents in production. The goal was to let users automate complex workflows across their workspaces while meeting enterprise expectations for reliability, security, and cost control. The final system supports many tools and powers workflows like bug triaging, email processing, and meeting notes capture.

[Read source](https://www.latent.space/p/notion)

---

#### Hyper-Personalized Merchandising Through Hybrid LLM and Deep Learning Systems

**Company:** doordash  
**Industry:** E-commerce

DoorDash built a personalization system to help users find relevant items across a large, changing catalog. It combines LLM-based understanding and planning with traditional ranking models so recommendations can adapt to real-time intent while staying fast and cost-aware. The system is tuned using measurable results, LLM evaluations, and human feedback, and it supports multiple shopping moments and use cases.

[Read source](https://www.infoq.com/presentations/llm-personalization/)

---

#### Multi-Agent AI SRE System for Automated Incident Response and Root Cause Analysis

**Company:** opsworker.ai  
**Industry:** Tech

OpsWorker.ai built a multi-agent AI system to help teams handle complex cloud incidents faster. Instead of only sending alerts, it organizes the investigation like an on-call workflow: it maps system dependencies, connects signals to a timeline, checks what changed, identifies likely root causes, and suggests or performs fixes with safety controls. It also captures lessons to improve future responses.

[Read source](https://www.opsworker.ai/blog/what-is-an-ai-sre-agent-and-how-we-implement-an-ai-sre-agent-at-opsworker-ai-multi-agent-logic/)

---

#### Agent-Driven Development for AI Research Using GitHub Copilot CLI

**Company:** github  
**Industry:** Tech

On GitHub’s Copilot Applied Science team, a researcher built “eval-agents” to automate analysis of large evaluation logs from benchmarks like TerminalBench2 and SWEBench-Pro. Using an agent-first approach, improved prompting, and CI/CD quality checks, a five-person team created 11 new agents and four new skills in under three days, with 28,858 lines of code added across 345 files.

[Read source](https://github.blog/ai-and-ml/github-copilot/agent-driven-development-in-copilot-applied-science/)

---

#### Multi-Agent Orchestration for Enterprise Conversational AI

**Company:** atlassian  
**Industry:** Tech

Atlassian improved its enterprise conversational AI, Rovo Chat, for knowledge retrieval and workflow automation. Instead of relying on one agent to handle many tools and domains, it uses specialized subagents and a hybrid orchestrator that adapts as information is retrieved. The result reported is a 3.49% quality improvement over the baseline, plus faster time-to-first-token responses, especially for simpler queries.

[Read source](https://www.atlassian.com/blog/atlassian-engineering/how-rovo-embraces-multi-agent-orchestration)

---

#### AI-Powered Multi-Agent Decision Support System for Strategic Business Decisions

**Company:** coinbase  
**Industry:** Finance

Coinbase built RAPID-D, an internal AI decision support tool for critical strategic decisions in finance. It’s designed to help people make better choices by surfacing unseen risks and reducing cognitive bias. The system uses multiple specialized AI perspectives, pulls relevant internal knowledge, challenges assumptions, and then presents a synthesized recommendation for human review, improving over the course of the same decision using stakeholder feedback.

[Read source](https://www.coinbase.com/en-nl/blog/making-smarter-decisions-faster-with-AI-at-Coinbase)

---

### Tools & Infrastructure

#### Cognitive Memory Agent: Building Stateful AI Agents with Multi-Layer Memory Architecture

**Company:** linkedin  
**Industry:** Tech

LinkedIn built CMA to help AI agents stay useful over time, not just within a single chat. It stores and retrieves relevant information across multiple memory types so agents can maintain continuity and become more personalized. CMA was integrated into Hiring Assistant, where it helps recruiters by suggesting roles, auto-filling hiring requirements, and surfacing insights from past activity to reduce friction and improve productivity.

[Read source](https://www.linkedin.com/blog/engineering/ai/the-linkedin-generative-ai-application-tech-stack-personalization-with-cognitive-memory-agent)

---

#### Multi-Agent AI Architecture for Site Reliability Engineering in Cloud-Native Infrastructure

**Company:** komodor  
**Industry:** Tech

Komodor introduced Klaudia AI to help teams manage incidents in complex cloud environments where symptoms and root causes can be far apart. It uses many specialized AI agents and a shared knowledge system to guide investigations, pull relevant documentation, and learn from past incidents. Komodor reports improvements like reduced time to resolve Kubernetes issues and faster pipeline failure diagnosis.

[Read source](https://komodor.com/blog/multi-agent-ai-sre-has-landed-and-its-built-for-your-most-complex-stacks/)

---

#### Terminal-Native AI Coding Agent with Multi-Model Architecture and Adaptive Context Management

**Company:** opendev  
**Industry:** Tech

OpenDev is an open-source command-line AI coding assistant designed for real developer workflows in the terminal. It focuses on three practical problems: keeping long sessions from running out of context, reducing the risk of destructive actions, and extending capabilities without overwhelming token limits. It uses multiple models, smarter context trimming, and layered safety to help developers manage source control, run builds, and deploy environments.

[Read source](https://arxiv.org/html/2603.05344v3)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

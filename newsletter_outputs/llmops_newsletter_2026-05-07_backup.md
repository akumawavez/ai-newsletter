# Weekly LLMOps Newsletter — 2026-05-07

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Building Production-Ready AI Agents Through Harness Engineering and Continual Learning

**Company:** langchain  
**Industry:** Tech

Langchain frames production AI agents as “model plus harness,” where the harness includes context engineering, prompting (system prompts, tool descriptions, skill front matter, sub-agent specs), verification hooks, and orchestration logic. It emphasizes continual learning via trace mining, context injection, and fine-tuning open models, plus evaluation flywheels using Langsmith and custom suites.

[Read source](https://www.youtube.com/watch?v=NovNcsKX8AU)

---

#### Large-Scale OCR Processing of Academic Papers Using AI Coding Agents and Serverless GPU Infrastructure

**Company:** huggingface  
**Industry:** Tech

Hugging Face used OpenAI’s Codex coding agent to orchestrate an OCR-to-Markdown pipeline for “chat with paper.” They selected Chandra-OCR 2 via Hugging Face leaderboards (OlmOCRBench) and deployed it on Hugging Face Jobs serverless GPUs using vLLM. Processing ran across 16 parallel L40S instances, writing outputs to Hugging Face Buckets via hf-mount, then merging results for Paper Pages integration.

[Read source](https://huggingface.co/blog/nielsr/ocr-papers-jobs)

---

#### Using AI Agents for Codebase Refactoring and Monolith Decomposition

**Company:** 1password  
**Industry:** Tech

1Password used AI agents to refactor and decompose a multi-million-line Go monolith (B5) for its Unified Access system. The toolchain combined Go SSA analysis, SQL parsing, and DataDog runtime coupling data via an MCP integration to produce domain ownership maps, coupling graphs, and prioritized extraction order. Agents automated a 3,000+ call site migration in hours using deterministic manifests, templates, and a playbook with failure modes and human escalation. They used git worktrees for parallel multi-agent execution.

[Read source](https://1password.com/blog/what-we-learned-using-ai-agents-to-refactor-a-monolith)

---

### Industry News

#### AI-Generated Trip Reports for Outdoor Recreation Guides

**Company:** guidesly  
**Industry:** Other

Guidesly’s Jack AI is an AWS serverless, event-driven pipeline that turns uploaded trip media (photos, videos, metadata) into marketing-ready assets. It uses API Gateway to trigger AWS Step Functions, Lambda for stages (EXIF extraction, computer vision inference, media optimization, content generation, publishing), S3 for artifacts, RDS (PostgreSQL) for structured data, and Amazon Bedrock foundation models for generation with contextual prompting and constraints.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-guidesly-built-ai-generated-trip-reports-for-outdoor-guides-on-aws/)

---

#### Building and Operating Production AI Agents at Scale with Vercel's Agent Orchestration Platform

**Company:** vercel  
**Industry:** Tech

Vercel built and operates production AI agents using its agent orchestration platform. The d0 internal analytics agent is a text-to-SQL engine that uses Vercel Sandboxes for isolated execution, Fluid Compute for dynamic scaling, AI Gateway for multi-model routing, and Workflows for durable orchestration with retries and state recovery. Built-in observability traces prompts, model responses, and decision paths. Vercel’s AI SDK provides streaming responses, tool use, and structured outputs, including a Chatbot primitive for Slack delivery.

[Read source](https://vercel.com/blog/anyone-can-build-agents-but-it-takes-a-platform-to-run-them)

---

#### AI-Powered Incident Investigation for Payment Infrastructure

**Company:** razorpay  
**Industry:** Finance

Razorpay built the Razorpay Oncall Agent, a multi-agent LLM system using LangGraph and RAG-based context retrieval. A Supervisor Agent creates an investigation strategy by querying two RAG systems (architecture/dependencies and alert-specific runbooks), then dispatches parallel specialist agents for Kubernetes pod health, Coralogix logs, PromQL performance metrics, and AWS infrastructure checks. Findings are stored as structured evidence with confidence scores, then correlated into an Incident Evidence Timeline to score hypotheses and select a root cause. It integrates with Slack and runs in shadow mode.

[Read source](https://engineering.razorpay.com/project-viveka-from-30-minute-investigations-to-90-second-ai-analysis-e49ec9db2638)

---

#### Building an Autonomous AI SRE Agent for Production Incident Investigation

**Company:** datadog  
**Industry:** Tech

Datadog built Bits AI SRE, an autonomous agent for production incident investigation in distributed systems. It runs an iterative hypothesis-testing loop: form hypotheses, validate via targeted queries against live telemetry, and repeat until a root cause. The approach shifts from summarizing many tool-call outputs to causal reasoning, using recursive decomposition into sub-hypotheses and pivoting when evidence fails.

[Read source](https://www.datadoghq.com/blog/building-bits-ai-sre/)

---

#### 2x Engineering Throughput Through AI-First Development Platform

**Company:** intercom  
**Industry:** Tech

Intercom doubled R&D throughput (merge PRs per head) over nine months by building an AI-first development platform centered on Claude Code. They avoided native plugin mechanisms by syncing plugins to disk via IT, used a base plugin with safety hooks/telemetry, layered developer tools and hundreds of specialized skills, enforced quality with automated hooks and LLM judges, and instrumented usage via Honeycomb plus anonymized Claude session JSON uploaded to S3.

[Read source](https://www.youtube.com/watch?v=BRDKft0-dUU)

---

#### Extreme Harness Engineering: Building Production Systems with Zero Human-Written Code

**Company:** openai  
**Industry:** Tech

OpenAI’s Frontier Product Exploration team ran a five-month experiment building an internal Electron app with zero human-written code, generating over one million lines across 1,500+ pull requests. They developed “harness engineering” principles and Symphony, an Elixir-based multi-agent orchestration system with six layers (policy, configuration, coordination, execution, integration, observability) and CLI-first control. Agents handled the full PR lifecycle, including autonomous review, merge conflict resolution, and CI/CD merging to main, with observability via Vector, VictoriaMetrics, Grafana, and distributed tracing.

[Read source](https://www.latent.space/p/harness-eng)

---

#### LLM-Powered Content Embeddings for Multi-Vertical Search and Recommendations

**Company:** doordash  
**Industry:** E-commerce

DoorDash used LLM-generated merchant and item profiles to standardize declarative content (ingredients, preparation, cuisine, dietary attributes, contextual info), then encoded those profiles with off-the-shelf embedding models. They orchestrated incremental embedding updates with Metaflow, refreshed embeddings only when underlying content changed, and evaluated models using an LLM-as-a-judge harness. Production retrieval used embedding-based retrieval with cosine similarity and temperature-controlled softmax, plus an item-level EBR pipeline with a fine-tuned Qwen 3 reranker consuming the query, top-k item profiles, and store profile.

[Read source](https://careersatdoordash.com/blog/doordash-llms-to-build-content-embeddings-for-search-and-recommendations/)

---

#### Building Durable and Reliable AI Agents at Scale with Dapr Workflows

**Company:** humanlayer  
**Industry:** Tech

HumanLayer’s case study applies Dapr (CNCF graduated) to production AI agents via the Dapr Agents framework. It targets state loss during failures in long-running workflows, adding workflow orchestration with automatic failure detection/recovery, exactly-once execution guarantees, and support for 30+ state stores. It also covers pub/sub multi-agent collaboration, OpenTelemetry observability, and resiliency features like retry policies and circuit breakers.

[Read source](https://www.youtube.com/watch?v=9gejXxl5JzE)

---

#### AI Agent System for Automated Design System Documentation

**Company:** uber  
**Industry:** Tech

Uber’s design systems team built uSpec, an agentic system that connects AI agents in Cursor to Figma via the open-source Figma Console MCP (Model Context Protocol). Agents use modular skills to generate component specs (anatomy, API docs, properties, color annotations, structure, and multi-platform accessibility) by reading Figma data and rendering templates back into Figma locally.

[Read source](https://www.uber.com/us/en/blog/automate-design-specs/)

---

#### Agentic Code Reviewers as System Protectors

**Company:** block  
**Industry:** Finance

Block built “Builderbot,” an agentic code review system positioned as a continuous “protector” rather than a passive assistant. It shifts protection left by running local checks before push using a standardized Just CLI contract. Reviews use progressive context disclosure via AGENTS.md, Amp’s Code Review Checks in .agents/checks/*.md, and Agent Skills for dynamic context loading.

[Read source](https://engineering.block.xyz/blog/protecting-our-systems-with-intelligence)

---

#### Building Internal AI Agent Infrastructure for Software Development at Scale

**Company:** uber  
**Industry:** Tech

Uber built an internal AI agent infrastructure for software development at scale, using a layered stack on top of Michelangelo. It includes a model gateway, an internal context layer (source code, docs, Slack, JIRA), an MCP Gateway for unified agent/data integration, and tools like Minion, Uber Agent Builder, and AIFX CLI. Specialized agents include uReview, Autocover, and Shepherd. Adoption metrics include 84% agentic coding users, 65–72% AI-generated IDE code, and 11% PRs opened by agents, alongside a 6x AI cost increase since 2024 and token cost optimization efforts.

[Read source](https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development)

---

#### AI-Driven Development at Scale: Building a Firecracker MicroVM Platform with Autonomous Agents

**Company:** atlassian  
**Industry:** Tech

Atlassian built Fireworks, a Firecracker microVM orchestration platform on Kubernetes, in four weeks using Rovo Dev AI agents with minimal human-written code. The platform includes a scheduler, autoscaler, node agents, envoy ingress layers, raft persistence, and features like 100ms warm starts, live migration, eBPF network policy enforcement, shared volumes, snapshot restore, and sidecar sandboxes.

[Read source](https://www.atlassian.com/blog/rovo/rovo-dev-platform-driven-development)

---

### Cool Use Cases

#### Building an Autonomous Software Factory for Notion-like Application Development

**Company:** software_factory  
**Industry:** Tech

Software Factory builds a Notion-like collaborative editor (“Memo”) via a fully automated SDLC run by AI agents on the Owner orchestration platform. About 14 scheduled automations maintain the codebase, using GitHub Issues/CLI as the state engine and Sentry for monitoring-driven incident response and bug fixing. Metrics report 88% of PRs completed autonomously, with CI pass ratios around 98%.

[Read source](https://www.youtube.com/watch?v=00Ndri8q8LU)

---

### Tools & Infrastructure

#### Building Production Data Agents with Long-Running Workflows and Context Management

**Company:** hex  
**Industry:** Tech

Hex evolved from single-shot text-to-SQL in notebook cells (GPT-3.5 Turbo) to multi-agent systems spanning entire projects. Agents include Notebook, Threads, Semantic Modeling, and Chat with App, unified via shared modular capability bundles. Hex built custom orchestration with long-running workflows on Temporal, plus context harvesting pipelines, tool search/retrieval, ephemeral SQL execution, and evaluation frameworks for long-horizon tasks.

[Read source](https://www.youtube.com/watch?v=Xyh1EqcjGME)

---

#### Red-Teaming an AI Agent: Security Testing of goose Through Operation Pale Fire

**Company:** block  
**Industry:** Finance

Block’s internal red team engagement “Operation Pale Fire” tested goose, an open-source AI coding agent that can take real-world actions via MCP extensions. The team demonstrated prompt injection through Google Calendar MCP invites using invisible zero-width Unicode characters, then pivoted to poisoning goose “shareable recipes” that append to the system prompt. Successful compromise combined social engineering with AI-specific vulnerabilities, leading to mitigations: calendar policy changes, zero-width stripping, recipe transparency, and prompt-injection detection merged into goose, plus monitoring/runbook updates.

[Read source](https://engineering.block.xyz/blog/how-we-red-teamed-our-own-ai-agent-)

---

#### AI-Driven Contract Analysis and Extraction at Scale

**Company:** pricewaterhousecooper_/_pwc  
**Industry:** Legal

PwC’s AIDA (AI-driven annotation) is a production AWS system for extracting structured insights from unstructured contracts. It combines rule-based extraction with LLM-powered natural-language query using Amazon Bedrock. A RAG pipeline uses Bedrock Embeddings Models, semantic indexing in OpenSearch Serverless, hybrid retrieval, and citation linking to source page text. Asynchronous processing runs OCR and extraction on ECS (AWS Fargate) coordinated via SQS, with results stored in Amazon RDS. Guardrails, human-in-the-loop review, CloudTrail auditability, and CloudWatch/X-Ray monitoring support regulated use.

[Read source](https://aws.amazon.com/blogs/machine-learning/extracting-contract-insights-with-pwcs-ai-driven-annotation-on-aws/)

---

#### Self-Improving Agent Through LLM-Based Session Analysis

**Company:** factory  
**Industry:** Tech

Factory’s Signals analyzes AI agent sessions at scale using a multi-stage pipeline built around OpenAI’s batch API and GPT-5.2. Sessions are fetched from BigQuery, filtered to those with at least 30 agentic steps, then processed to extract structured “facets” and detect friction patterns. Findings are correlated with system logs and releases, stored in BigQuery and reported to Slack. When friction crosses predefined thresholds, Signals files Linear tickets that Droid picks up, implements fixes, and submits pull requests; human approval is required before merge.

[Read source](https://factory.ai/news/factory-signals)

---

#### AI Agents for Accelerating Model Development and Framework Migration

**Company:** linkedin  
**Industry:** Tech

LinkedIn built an agent-based framework to accelerate model experimentation and infrastructure development by using LLMs to optimize the AI development process itself. The system combines code-authoring agents for distributed training, comprehensive evaluation for correctness and quality, and GPU microscheduling for efficient compute utilization. “Autopilot for Torch” runs iterative generate–verify–refine loops with structured verifier feedback, then validates on development GPU pods and promotes via Flyte workflows. Early results report strong performance across 100+ OpenML benchmarks, offline metric parity for internal workloads, and 10%+ training throughput improvements on optimized LLM workloads.

[Read source](https://www.linkedin.com/blog/engineering/ai/ai-helping-build-better-ai-how-agents-accelerate-model-experimentation)

---

#### Autonomous Security Agents for Continuous Vulnerability Detection and Remediation

**Company:** cursor  
**Industry:** Tech

Cursor reports using Cursor Automations to run a fleet of autonomous security agents for continuous vulnerability detection and remediation. Four templates are described: Agentic Security Review, Vuln Hunter, Anybump, and Invariant Sentinel. Agents use a custom security MCP tool deployed as a serverless Lambda function for persistent storage, deduplication, and consistent Slack-formatted reporting.

[Read source](https://cursor.com/blog/security-agents)

---

#### Building a Software Factory with AI Agents and Automation Loops

**Company:** software_factory  
**Industry:** Tech

Memo is built on the Ona platform using AI agents and automation loops to run a largely autonomous software factory. The pipeline includes hourly feature planning and feature builder PR generation, PR reviewer conversation threads for iterative fixes, and an hourly PR shepherd fail-safe that rebases, resolves merge conflicts, and addresses build failures. Post-merge verification deploys and smoke tests, creating high-priority bug reports on failures. It also integrates Sentry with an incident responder automation every 15 minutes, plus daily metrics updates for lines of code, PRs merged, and test coverage.

[Read source](https://www.youtube.com/watch?v=ELS-DvDT3Yg)

---

#### AI-Orchestrated Code Review System at Scale

**Company:** cloudflare  
**Industry:** Tech

Cloudflare built a CI-native, multi-agent AI code review orchestration around OpenCode. A coordinator spawns OpenCode via Bun.spawn, streams JSONL events, and launches up to seven specialized reviewers (security, performance, code quality, documentation, release, compliance) through a runtime plugin. Findings are produced as structured XML, deduplicated and filtered by a judge pass, with risk-tiered model selection, prompt/token optimization, and circuit-breaker failback.

[Read source](https://blog.cloudflare.com/ai-code-review/)

---

#### AI Agents Accelerating GPU Kernel Engineering for LLM Infrastructure

**Company:** linkedin  
**Industry:** Tech

LinkedIn built three agentic workflows for Liger Kernel GPU kernel engineering: liger-kernel-dev (PyTorch→Triton kernel creation), liger-autopatch (HuggingFace Transformers model integration), and liger-kernel-perf (performance optimization). Each uses a three-stage pipeline—understanding, acting, verification—with structured profiles and human review checkpoints. The perf loop profiles kernels, optionally uses NVIDIA NCU, generates versioned variants, and blocks regressions beyond a 5% guardrail.

[Read source](https://www.linkedin.com/blog/engineering/ai/ai-helping-build-better-ai-how-agents-accelerate-liger-kernel-engineering)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Building Production-Ready AI Agents Through Harness Engineering and Continual Learning

**Company:** langchain  
**Industry:** Tech

Langchain’s approach to building production AI agents focuses on wrapping the model with the right “harness” around it—clear instructions, built-in checks, and orchestration logic—so agents can reliably complete specific tasks. They stress custom evaluations tied to real customer needs and continual improvement from production traces, rather than relying only on frontier model power.

[Read source](https://www.youtube.com/watch?v=NovNcsKX8AU)

---

#### Large-Scale OCR Processing of Academic Papers Using AI Coding Agents and Serverless GPU Infrastructure

**Company:** huggingface  
**Industry:** Tech

Hugging Face needed to convert about 27,000 academic papers into Markdown so users could “chat with paper” in HuggingChat. The papers lacked HTML versions on arXiv, so the team used OCR to fill the gap. They processed the full corpus in about 29–30 hours at an estimated cost of $850, enabling chat for all papers on the platform.

[Read source](https://huggingface.co/blog/nielsr/ocr-papers-jobs)

---

#### Using AI Agents for Codebase Refactoring and Monolith Decomposition

**Company:** 1password  
**Industry:** Tech

1Password applied AI agents to refactor and break apart a large Go system that supports its Unified Access product. The team built tools that analyze code, database dependencies, and production behavior to plan safe service extraction. Agents handled a large migration of 3,000+ call sites quickly, improving productivity by about 20–30% on complex tasks, but they needed human oversight for sequencing and system boundaries.

[Read source](https://1password.com/blog/what-we-learned-using-ai-agents-to-refactor-a-monolith)

---

### Industry News

#### AI-Generated Trip Reports for Outdoor Recreation Guides

**Company:** guidesly  
**Industry:** Other

Guidesly built Jack AI to help outdoor guides spend less time on marketing. After a trip, guides upload photos and videos, and the system automatically creates marketing content for websites, social media, and email. Guides saw content generation time drop from 13 minutes to 2 minutes and reported major revenue growth for active users.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-guidesly-built-ai-generated-trip-reports-for-outdoor-guides-on-aws/)

---

#### Building and Operating Production AI Agents at Scale with Vercel's Agent Orchestration Platform

**Company:** vercel  
**Industry:** Tech

Vercel says building AI agents is easier now, but running them reliably at scale is still hard. It describes d0, an internal analytics agent that answers hundreds of data questions daily. Vercel attributes fast development to its platform primitives, and says the same infrastructure supports multiple internal agents and customer-facing products like v0 and Vercel Agent for PR reviews.

[Read source](https://vercel.com/blog/anyone-can-build-agents-but-it-takes-a-platform-to-run-them)

---

#### AI-Powered Incident Investigation for Payment Infrastructure

**Company:** razorpay  
**Industry:** Finance

Razorpay, a finance infrastructure company, reduced the time on-call engineers spent investigating production incidents. Engineers previously spent 20–40 minutes manually connecting information across multiple monitoring systems. Razorpay created an AI “Oncall Agent” that runs parallel specialist checks and delivers a complete investigation for the engineer to review. After three months in shadow mode, it cut investigation time by 80% (to 90 seconds), improved resolution time by 50–60%, and saved 6–8 hours of engineering work weekly, with more consistent results across experience levels.

[Read source](https://engineering.razorpay.com/project-viveka-from-30-minute-investigations-to-90-second-ai-analysis-e49ec9db2638)

---

#### Building an Autonomous AI SRE Agent for Production Incident Investigation

**Company:** datadog  
**Industry:** Tech

Datadog created Bits AI SRE to help teams investigate and resolve production incidents in complex distributed systems. It follows an SRE-style process: it forms hypotheses, checks them against live telemetry, and digs deeper until it finds the root cause. Datadog reports up to a 95% reduction in time to resolution and emphasizes evaluation on real production incidents.

[Read source](https://www.datadoghq.com/blog/building-bits-ai-sre/)

---

#### 2x Engineering Throughput Through AI-First Development Platform

**Company:** intercom  
**Industry:** Tech

Intercom, a customer support SaaS company, boosted engineering output by treating internal AI adoption like a product. They built a large library of specialized AI “skills,” added strong quality checks, and tracked how people used the system. Over nine months, they doubled PR throughput, improved code quality, sped up time-to-market, and shifted culture toward agent-first work.

[Read source](https://www.youtube.com/watch?v=BRDKft0-dUU)

---

#### Extreme Harness Engineering: Building Production Systems with Zero Human-Written Code

**Company:** openai  
**Industry:** Tech

OpenAI’s Frontier Product Exploration team tested whether software can be built and maintained by AI agents without humans writing the code. Over five months, they produced a large internal app through thousands of pull requests, using infrastructure and guardrails so agents could review, resolve conflicts, and deploy. The outcome was high throughput and a shift in human work toward building the systems that let agents operate autonomously.

[Read source](https://www.latent.space/p/harness-eng)

---

#### LLM-Powered Content Embeddings for Multi-Vertical Search and Recommendations

**Company:** doordash  
**Industry:** E-commerce

DoorDash improved search and recommendations across food, grocery, retail, and gifting by creating richer, standardized descriptions of merchants and items using large language models, then turning those descriptions into embeddings for retrieval. They reduced null searches and improved conversion, and their generative personalized homepage carousels increased homepage order rate and offline precision. The approach also helped with cold-start and tail queries, including fairness for small merchants.

[Read source](https://careersatdoordash.com/blog/doordash-llms-to-build-content-embeddings-for-search-and-recommendations/)

---

#### Building Durable and Reliable AI Agents at Scale with Dapr Workflows

**Company:** humanlayer  
**Industry:** Tech

The case study explains why many AI agent systems struggle in real production use at scale—especially when failures happen mid-task and progress is lost, forcing expensive rework. It presents Dapr Agents as a way to make agent workflows more durable, automatically recover from failures, coordinate multiple agents, and provide full visibility for auditing and debugging.

[Read source](https://www.youtube.com/watch?v=9gejXxl5JzE)

---

#### AI Agent System for Automated Design System Documentation

**Company:** uber  
**Industry:** Tech

Uber’s design systems team needed accurate, complete documentation for hundreds of components across multiple technology stacks. They built uSpec to automatically generate full component specifications from Figma, including accessibility details. The system runs locally for enterprise security, produces specs in minutes instead of weeks, and improves consistency and accuracy across the design system.

[Read source](https://www.uber.com/us/en/blog/automate-design-specs/)

---

#### Agentic Code Reviewers as System Protectors

**Company:** block  
**Industry:** Finance

Block, a finance company, faced resilience problems as teams shipped changes that looked fine locally but harmed the overall architecture. It created “Builderbot,” an agentic code review system that acts as a vigilant guardian. The approach catches issues pre-push, reduces the burden on human reviewers, and helps keep changes aligned with the organization’s architectural model.

[Read source](https://engineering.block.xyz/blog/protecting-our-systems-with-intelligence)

---

#### Building Internal AI Agent Infrastructure for Software Development at Scale

**Company:** uber  
**Industry:** Tech

Uber created internal infrastructure so software engineers could use AI agents for development tasks, aiming to reduce “boring” work like upgrades, migrations, and trivial bug fixes and free engineers for more creative work. The company built tools for agent deployment, cost control, and workflow changes, including background agents, a no-code agent builder, and specialized agents for code review, test generation, and migrations. Results showed broad adoption (84% agentic coding users; 92% monthly agent use) but also higher AI costs (6x since 2024) and slower-than-expected uptake that required cultural change and peer-driven sharing.

[Read source](https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development)

---

#### AI-Driven Development at Scale: Building a Firecracker MicroVM Platform with Autonomous Agents

**Company:** atlassian  
**Industry:** Tech

Atlassian used its Rovo Dev AI agent system to build a production-ready platform for running Firecracker microVMs on Kubernetes in four weeks. The goal was to create a secure execution engine with advanced capabilities like fast startup, live migration, and network controls. They did this by letting AI agents handle development, testing, and CI/CD workflows with strong automated validation.

[Read source](https://www.atlassian.com/blog/rovo/rovo-dev-platform-driven-development)

---

### Cool Use Cases

#### Building an Autonomous Software Factory for Notion-like Application Development

**Company:** software_factory  
**Industry:** Tech

Software Factory ran a two-week public experiment to see whether AI agents can handle the full software development lifecycle for a Notion-like collaborative app called Memo. Agents planned, built, reviewed, and deployed the product, with 88% of pull requests finished without human intervention. The project also used monitoring to detect problems and feed fixes back into development.

[Read source](https://www.youtube.com/watch?v=00Ndri8q8LU)

---

### Tools & Infrastructure

#### Building Production Data Agents with Long-Running Workflows and Context Management

**Company:** hex  
**Industry:** Tech

Hex, a collaborative data analytics platform, moved from simple one-off question answering to multi-agent help for complex, iterative analysis. It built long-running workflows and project-level context so agents can produce comprehensive reports over time. The company also invested in evaluation and privacy-preserving monitoring to improve reliability, while still working on verification and handling conflicting context.

[Read source](https://www.youtube.com/watch?v=Xyh1EqcjGME)

---

#### Red-Teaming an AI Agent: Security Testing of goose Through Operation Pale Fire

**Company:** block  
**Industry:** Finance

Block ran an internal security exercise, “Operation Pale Fire,” to find weaknesses in goose, its open-source AI coding agent used in production. The team showed how hidden messages in calendar invites and poisoned shared recipes could lead to a real compromise of an employee laptop, helped by social engineering. Block then improved calendar handling, recipe visibility, and prompt-injection detection, and updated monitoring and response steps.

[Read source](https://engineering.block.xyz/blog/how-we-red-teamed-our-own-ai-agent-)

---

#### AI-Driven Contract Analysis and Extraction at Scale

**Company:** pricewaterhousecooper_/_pwc  
**Industry:** Legal

PwC built AIDA to help legal, compliance, and procurement teams pull structured information from long, unstructured contracts that usually require heavy manual review. The system uses rules plus AI question answering to process contracts at scale on AWS. Customer deployments report up to a 90% reduction in manual contract review time, including a 90% reduction in rights research time for a major film and TV studio, supporting faster retrieval and shorter review cycles.

[Read source](https://aws.amazon.com/blogs/machine-learning/extracting-contract-insights-with-pwcs-ai-driven-annotation-on-aws/)

---

#### Self-Improving Agent Through LLM-Based Session Analysis

**Company:** factory  
**Industry:** Tech

Factory built Signals to understand how users experience its AI coding agent at scale, without exposing conversation content to human reviewers. It analyzes thousands of sessions to spot user friction and delight, then connects those patterns to system logs and releases. When friction crosses set thresholds, it automatically creates tickets and drives fixes through code changes, with human approval required before merging. Early results report 73% of issues auto-resolved, with average fix time under 4 hours.

[Read source](https://factory.ai/news/factory-signals)

---

#### AI Agents for Accelerating Model Development and Framework Migration

**Company:** linkedin  
**Industry:** Tech

LinkedIn created an internal AI system that helps teams build better AI faster by improving the development process itself. It uses agents to generate code, check it against clear quality requirements, and refine it repeatedly. The approach supports large-scale work like migrating TensorFlow models to PyTorch, with validation and deployment through existing production workflows. Early results include strong benchmark performance, matching internal offline results, and higher training throughput, alongside reduced manual effort.

[Read source](https://www.linkedin.com/blog/engineering/ai/ai-helping-build-better-ai-how-agents-accelerate-model-experimentation)

---

#### Autonomous Security Agents for Continuous Vulnerability Detection and Remediation

**Company:** cursor  
**Industry:** Tech

Cursor says its PR volume grew 5x over nine months, making traditional security approaches insufficient at scale. To address this, it built Cursor Automations that continuously find and repair vulnerabilities. The company describes four templates for reviewing new PRs, scanning existing code, updating dependencies, and monitoring compliance daily, with results shared through Slack.

[Read source](https://cursor.com/blog/security-agents)

---

#### Building a Software Factory with AI Agents and Automation Loops

**Company:** software_factory  
**Industry:** Tech

The case study describes how a team built Memo, a note-taking application, using AI agents and automation loops on the Ona platform. The system manages the full development lifecycle—from planning features to deploying and checking results—so human involvement is minimal. It processes pull requests, fixes bugs, and improves its own workflows, aiming to increase development speed while catching production issues through automated verification and reporting.

[Read source](https://www.youtube.com/watch?v=ELS-DvDT3Yg)

---

#### AI-Orchestrated Code Review System at Scale

**Company:** cloudflare  
**Industry:** Tech

Cloudflare created a production AI code review system to reduce delays from manual reviews, where first-review wait times were measured in hours. Instead of generic tools, it uses multiple focused AI reviewers working in parallel, coordinated to produce review comments quickly. In the first month it processed many merge requests across thousands of repositories, with a median review time of minutes and a low manual override rate.

[Read source](https://blog.cloudflare.com/ai-code-review/)

---

#### AI Agents Accelerating GPU Kernel Engineering for LLM Infrastructure

**Company:** linkedin  
**Industry:** Tech

LinkedIn used AI agents to speed up and scale GPU kernel work for its open-source Liger Kernel project. Instead of experts manually writing and optimizing custom Triton kernels, the agents automate kernel creation, model integration, and performance tuning through a step-by-step process with human checks. The result included faster kernels, model updates that needed only review, and major internal training efficiency gains.

[Read source](https://www.linkedin.com/blog/engineering/ai/ai-helping-build-better-ai-how-agents-accelerate-liger-kernel-engineering)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

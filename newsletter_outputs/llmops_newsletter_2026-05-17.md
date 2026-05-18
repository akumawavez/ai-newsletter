# Weekly LLMOps Newsletter — 2026-05-17

*Week of 2026-05-11 (Mon) – 2026-05-17 (Sun)*

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Evaluating AI Agent Performance: Skills vs Documentation for Developer Platforms

**Company:** wix  
**Industry:** Tech

Wix Engineering ran 250 controlled evaluations comparing AI agent performance on developer tasks using standard docs, agent-optimized documentation, and purpose-built “skills” (curated guides). Two task families were tested: CLI extension development and REST API scripting. Each condition was executed three times per task. Metrics included token count, turn count, wall-clock time, and self-evaluation of completion and failure causes via agent assessment.

[Read source](https://www.wix.engineering/post/we-ran-250-ai-agent-evals-to-find-out-if-skills-beat-docs-the-answer-is-more-complicated-than-we-ex)

---

### Industry News

#### AI-Powered Search and Agent Automation for Digital Asset Management

**Company:** bynder  
**Industry:** Media & Entertainment

Bynder built AI search and four configurable agent types on a microservices, event-driven AWS architecture. Assets upload to Amazon S3; metadata persists in Amazon Aurora MySQL (and Aurora PostgreSQL for face recognition). Embeddings via AWS Bedrock feed OpenSearch KNN similarity search. Speech-to-text uses Amazon Transcribe with EventBridge/SQS, indexing transcripts in OpenSearch. Agents run through an orchestrator using SQS triggers and Kafka execution commands, with Bedrock Guardrails and human-in-the-loop approvals.

[Read source](https://www.youtube.com/watch?v=Kyym50EgUOQ)

---

#### Multi-Agent AI Platform for Life Insurance Sales Acceleration

**Company:** prudential  
**Industry:** Insurance

Prudential’s “Just Ask” is a multi-agent AI advisor assistant on AWS. It uses an orchestrator for non-deterministic intent-based routing to specialized agents (product recommendations, medical underwriting, quick quoting, forms selection, and book-of-business management). Chat history and memory are stored in Amazon DynamoDB; Redis supports retrieval and caching. RAG uses embeddings and semantic search with ranking (including cohere ranking). Guardrails are applied via AWS Bedrock at the orchestrator and agent levels, with monitoring/observability centralized in an “agent core.” Evaluation combines human-in-the-loop, rule-based checks, and LLM-as-a-judge; medical underwriting uses human-in-the-loop for complex cases.

[Read source](https://www.youtube.com/watch?v=g-YBqWv2kQ4)

---

#### Building and Scaling AI Agents in Production for DevSecOps Automation

**Company:** datadog  
**Industry:** Tech

Datadog reports deploying over a hundred AI agents in production to automate DevSecOps tasks, planning to scale to thousands more. Deployed agents include an SRE agent for autonomous alert investigation, a Dev agent for code generation and error fixes, and a Security Analyst agent for checklist-driven security investigations. Lessons emphasize agent-first API design, proactive background execution, durable orchestration with Temporal, containerized/sandboxed autonomy, comprehensive evaluation (offline, online, and evolving), framework/model agnosticism, and treating agents as first-class users via MCP servers and documentation access.

[Read source](https://www.youtube.com/watch?v=C3y3M_03Vco)

---

#### AI-Driven Enzyme Design for Advanced Plastic Recycling

**Company:** rhea’s_factory  
**Industry:** Energy

Rhea’s Factory is building a multi-stage enzyme design pipeline that uses protein language models plus embeddings, structural prediction tools (AlphaFold-like), and custom predictive models. It screens millions of sequences computationally, applies layered guard rails for context management, and uses an AI orchestrator coordinating specialized agents with backtracking loops. Wet-lab results feed proprietary training data for performance prediction under industrial conditions.

[Read source](https://www.youtube.com/watch?v=huFaei-6Z4g)

---

#### AI-Powered Bug Routing System Using RAG and Multimodal Processing

**Company:** miro  
**Industry:** Tech

Miro’s BugManager is a Python microservice deployed on Amazon EKS that performs automated bug triaging and routing. It uses Amazon Bedrock Knowledge Bases for RAG across Confluence, help center articles, resolved Jira tickets, GitHub READMEs, and Backstage docs, with Amazon OpenSearch Serverless as the vector store. Amazon Nova Pro parses screenshots and videos into text descriptions, using RAG context to improve interpretation. Anthropic Claude Sonnet 4 classifies bugs across ~100 teams via prompt engineering with XML-tagged structured output (<team>, <confidence>, <rationale>), returning up to five ranked options. Human-in-the-loop review is supported through Slack, and Jira tickets are created with enriched context and optional root-cause analysis using retrieved GitHub code sections. Reported results include 75% top-1 accuracy, 95% top-3 accuracy, six times fewer reassignments, and five times shorter median time-to-resolution; average classification latency is 53 seconds.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-miro-uses-amazon-bedrock-to-boost-software-bug-routing-accuracy-and-improve-time-to-resolution-from-days-to-hours/)

---

#### Building Production Coding Agents with Pi Framework for Sales Process Automation

**Company:** tavon  
**Industry:** Tech

Tavon built a production-grade sales automation system using the Pi agent framework and OpenClaw. The architecture monitors an email inbox, routes RFP messages via a gateway to customer-specific agents, and generates draft responses. Each customer has a dedicated agent configured by agent and customer configuration files. Agents use CLI tools to access CRM/ERP, run tasks in secure sandboxed environments, and maintain case continuity with session management and full action traces for observability and debugging.

[Read source](https://www.youtube.com/watch?v=vAIDdLKB6-w)

---

#### Building a Production AI Code Review Agent with High Engineer Acceptance

**Company:** doordash  
**Industry:** Tech

DoorDash built a production AI code review agent that evolved to a three-agent architecture: a “lead scout” flags suspicious areas, then two deep reviewers verify specific concerns. It uses domain-specific review profiles mined from AGENTS.md, historical PR reviews, Slack decisions, and incident history, routed by touched code. Precision-over-recall includes a “disprove-it” verification pass before posting. Reviews run on remote VMs with full repository clones and support a “fixer” that applies changes back to the PR for CI and human review. DoorDash reports ~60.2% acceptance on high/critical findings across 10,000+ weekly PRs over 56 repositories, at about $3 per review and ~7 minutes completion time.

[Read source](https://careersatdoordash.com/blog/doordash-built-an-ai-code-reviewer-engineers-actually-listen-to/)

---

#### Building Custom Tracing Tools and Development Infrastructure for AI-Powered Meeting Notes

**Company:** granola  
**Industry:** Tech

Granola built custom internal tracing tools for LLM-powered meeting notes to capture tool calls, reasoning, search tool usage, and cost across the full interaction lifecycle. The tracing data is structured for internal teams via a user-friendly interface, avoiding reliance on CloudWatch or complex queries. They note the implementation wraps an AI SDK and saves to a database, with OpenTelemetry as an alternative foundation.

[Read source](https://www.youtube.com/watch?v=ON5LIT0M4do)

---

#### Context Management and Memory Strategies for Production AI Agents

**Company:** arize  
**Industry:** Tech

Arize built Alex on top of its observability platform, analyzing traces and span data. To break a feedback loop where spans grew until context limits caused failures, they used smart truncation with memory stores (first 100 characters + last 100, storing the middle for retrieval), separated context from memory, and delegated heavy data operations to sub-agents. They also ran long session evaluations by loading 10 turns and testing the 11th.

[Read source](https://www.youtube.com/watch?v=esY99nYXxR4)

---

#### Gateway Patterns and Actions Runtime for Enterprise Agentic AI Deployment

**Company:** arcade.dev  
**Industry:** Tech

Arcade.dev’s actions runtime separates reasoning from action execution using an MCP gateway as a front door to a control plane. It enforces identity separation and an AND-gate authorization model (agent permission AND user permission) via OAuth 2.1-based trinary tokens. The runtime curates blessed MCP tools through evaluations, supports multi-user access, and provides comprehensive audit trails for every action and transaction.

[Read source](https://www.youtube.com/watch?v=gQhDwOGdE4E)

---

#### Scaling LLM Production with Reinforcement Learning for Enterprise Agents

**Company:** adaptive_ml  
**Industry:** Tech

Adaptive ML argues that reinforcement learning (RL) is the post-training mechanism needed to move LLM pilots into production, enabling continuous feedback integration from production environments. Its RLOps platform (“Adaptive Engine”) evaluates, tunes, and serves business-specific LLMs on open-source model families including Gemma 4, Mistral, and Qwen. The platform abstracts RL training complexity, including PPO that orchestrates four LLMs simultaneously, and supports agentic use cases via simulated environments, reward functions, and rejection sampling for synthetic trajectories. Human-in-the-loop focuses on defining reward signals (objective checks, business metrics, and LLM-as-judge rubrics) and transitions from improving judge systems to training dedicated reward models as feedback scales.

[Read source](https://www.youtube.com/watch?v=X6NShR2ccOg)

---

#### Scaling AI Agents in Production for B2B Growth and Outreach

**Company:** clay  
**Industry:** Tech

Clay scaled from “chat completions wrapper” use cases to operating ~300M agent runs per month, deploying specialized agents for finding, closing, and growing customers. Runs average 10–30 steps with web research, crawling, synthesis, and content generation. They built an agent harness on Vercel AI SDK, integrated LangSmith for tracing, offline evals, and cost reconciliation, enabling rapid debugging across engineering and customer support.

[Read source](https://www.youtube.com/watch?v=cx6_tb6HCeY)

---

#### AI Employee Agent Operating in Slack with Multi-Tool Integration

**Company:** viktor  
**Industry:** Tech

Viktor is an AI employee agent that runs inside Slack and integrates with 3,000+ integrations via a shared integration model. It uses Claude Opus 4.6 as its primary model, selected after A/B testing against GPT-5.4 for user-preferred tone. The system targets multi-user, multi-channel deployments with memory management, permission scoping, and context isolation across channels and DMs.

[Read source](https://www.youtube.com/watch?v=ohKt066uFhg)

---

#### Autonomous Self-Healing System for Bug Resolution

**Company:** wix  
**Industry:** Tech

Wix’s Gandalf is an autonomous self-healing system that processes support tickets from detection through pull request creation for bug fixes. It uses a four-agent architecture: Detector (ticket ingestion/classification), Bilbo the Enricher (context aggregation), Coder (plan execution in a Docker sandbox via pipeline, agent CLI, and GitLab CLI), and Reviewer (independent validation for security, risk, and side effects). It enriches context from GitLab code, databases via Trino, logs via Grafana, and documentation. Schema validation plus retry logic handles non-deterministic agent outputs, and idempotency checks prevent duplicate fixes. Workflow triggers include cron checks every 30 minutes or manual initiation, with a UI showing ticket states and blocked outcomes for human intervention.

[Read source](https://www.youtube.com/watch?v=3BNoppi6qcs)

---

#### Automating Trading Card Copywriting with Multi-Agent Generative AI

**Company:** fanatics_collectibles  
**Industry:** Media & Entertainment

Fanatics Collectibles built a multi-agent LLM system on Amazon Bedrock, orchestrated with Claude Opus as the supervisor. It uses a structured player stats knowledge base with an automated stats ranking algorithm, plus a web search agent that calls a Lambda function and the Tavily AI API. A QA agent loads MLB style guides and licensing requirements via Bedrock knowledge base, then performs sectional compliance checks (player name, stats presentation, narrative structure). Traditional NLP progressive word tracking flags overuse, and prompts include randomly selected historical card examples for few-shot brand voice. AWS CDK supports repeatable, scalable deployments; Streamlit provides a Python UI with asynchronous job processing.

[Read source](https://www.youtube.com/watch?v=plJylA9v_uc)

---

#### Multi-Agent Software Development System with Extended Autonomous Execution

**Company:** factory  
**Industry:** Tech

Factory’s Missions is a multi-agent software development system built around a three-role architecture: orchestrators (planning, validation contracts), workers (serial feature implementation with Git commits), and validators (scrutiny validators running test suites/type checking/linting plus code review agents, and user testing validators that run the app and interact end-to-end). It uses delegation, creator-verifier, broadcast, and negotiation, with structured handoffs and milestone checkpoints for self-healing.

[Read source](https://www.youtube.com/watch?v=ow1we5PzK-o)

---

#### Evolution from Static Benchmarks to Adaptive Agent Evaluation Systems

**Company:** comet  
**Industry:** Tech

Comet’s Vincent argues that static benchmarks and handcrafted offline eval datasets don’t fit agentic, intent/personalized systems, creating “eval calcification.” The proposed approach treats evaluations as adaptive systems using telemetry and trace data, intent-based outcomes, self-curating test suites, and always-on online evaluation. Harnesses can use telemetry-in-the-loop for self-correction, with Open Claw as an example.

[Read source](https://www.youtube.com/watch?v=4VhbYlfC7Gs)

---

### Cool Use Cases

#### Production Skills Framework for Agentic LLM Workflows

**Company:** workos  
**Industry:** Tech

WorkOS’s “skills” framework productionizes agentic LLM workflows using reusable, composable units defined primarily by markdown files with YAML front matter. Skills include semantic routing metadata (name/description), context and constraints, optional scripts with interpolation to inject deterministic outputs, and progressive disclosure via conditional loading of referenced markdown. Evaluation compares baseline vs skill performance and uses rubric-based confidence thresholds with iterative transcript-driven refinement.

[Read source](https://www.youtube.com/watch?v=pFsfax19yOM)

---

#### Production Agent Observability and Monitoring Platform

**Company:** raindrop  
**Industry:** Tech

Raindrop is a production observability and monitoring platform for AI agents. It combines explicit signals (tool error rates, overall error rates, latency, user regeneration frequency, cost) with implicit signals from trained classifiers and regex patterns to detect issues like refusals, task failures, user frustration, and jailbreaking. It supports alerts, day-by-day visualization, drill-down with full context, and experimentation with control groups.

[Read source](https://www.youtube.com/watch?v=-aM2EDTiaMs)

---

#### AI-Powered Engineering Management and Autonomous Development Workflows

**Company:** notion  
**Industry:** Tech

Notion’s case study describes three AI agent workflows. A custom Notion AI agent (“Hot Potato”) runs daily at 9:00 AM, using a map-reduce fan-out across Slack, a Notion task database, GitHub merged PRs, Honeycomb metrics via MCP, and the prior meeting transcript, then posts a templated pre-read to Slack. Background coding uses “Boxy/Software Factory” VMs provisioned with Aider and Claude Code, triggered by at-mentions in Notion comments to clone repos and generate pull requests from task descriptions. Spec-driven development keeps comprehensive markdown feature specs in a codebase subfolder as source of truth; Notion AI CLI tools enable agents to run, query, enable/disable Ask Mode, and verify behavior, while Aider one-shots implementations from specs and verification sections.

[Read source](https://www.youtube.com/watch?v=pUHA_jNwuYE)

---

### Tools & Infrastructure

#### Building Agentic Spreadsheet Automation from Process Mining to Production

**Company:** ramp  
**Industry:** Finance

Ramp built Ramp Sheets, an agentic spreadsheet editor that automates finance workflows by manipulating spreadsheets via an agent SDK. The agent runs outside Modal sandboxes, with SpreadJS inside. It uses ~10 Excel-specific tools (e.g., read_range, set_range, format_range) and can fall back to Python for edge cases. Typical execution is 7–10 minutes per task. Ramp also uses Inspect to analyze code and automatically create DataDog monitors, initially in shadow mode, then promotes high-signal monitors and opens GitHub PRs with fixes.

[Read source](https://www.youtube.com/watch?v=trEM9OKr5Sc)

---

#### AI-Powered Workflow Assistant for Seismic Data Processing

**Company:** halliburton  
**Industry:** Energy

Halliburton built a cloud-native seismic workflow assistant using FastAPI on AWS App Runner with streaming responses. It uses Amazon Bedrock for intent routing (Amazon Nova Lite) and multi-model Q&A/workflow generation (Amazon Nova and Claude models). RAG uses Amazon Bedrock Knowledge Bases with retrieve_and_generate, embeddings, and inline citations. Workflow generation uses LangChain agent-based orchestration with 82 tools, producing executable YAML and storing conversation history in Amazon DynamoDB.

[Read source](https://aws.amazon.com/blogs/machine-learning/halliburton-enhances-seismic-workflow-creation-with-amazon-bedrock-and-generative-ai/)

---

#### Enterprise Code Search and Bug Investigation with Multi-Agent AI Systems

**Company:** wix  
**Industry:** Tech

Wix built two interconnected systems for enterprise code search and bug investigation. OctoCode is an MCP-based tool that uses structured tool schemas, forced reasoning, parallel tool calls, caching, context-aware hints, and pagination for repository/dependency search. Bilbo orchestrates multiple AI agents via a Planner/Research flow, unified tool protocol, sub-agent parallelism, dynamic sub-agent creation, and vector-database memory (Vectara).

[Read source](https://www.youtube.com/watch?v=T3pJz1Nwt1Y)

---

#### AI-Powered Security Vulnerability Detection Pipeline for Browser Hardening

**Company:** mozilla  
**Industry:** Tech

Mozilla built a production AI security auditing pipeline for Firefox using an agentic harness atop existing fuzzing infrastructure. The harness can statically analyze code and dynamically create and run reproducible test cases to validate hypotheses. It uses a multi-model strategy (e.g., Claude Opus 4.6, Claude Mythos Preview), prompt engineering, orchestration, evals, and human-in-the-loop review.

[Read source](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Evaluating AI Agent Performance: Skills vs Documentation for Developer Platforms

**Company:** wix  
**Industry:** Tech

Wix Engineering tested how well AI agents can do developer work using three kinds of help: regular documentation, improved documentation tailored for agents, and curated “skills” (short guides). Across CLI and REST API tasks, agent-optimized documentation completed more tasks and did so faster and with fewer resources. Skills helped only when they stayed accurate, so Wix treats skills as a caching layer maintained by ongoing checks.

[Read source](https://www.wix.engineering/post/we-ran-250-ai-agent-evals-to-find-out-if-skills-beat-docs-the-answer-is-more-complicated-than-we-ex)

---

### Industry News

#### AI-Powered Search and Agent Automation for Digital Asset Management

**Company:** bynder  
**Industry:** Media & Entertainment

Bynder, a digital asset management platform for retail and CPG, addressed a bottleneck where customers had to manually tag and categorize uploads to make them searchable. It added natural-language and similarity search plus automated enrichment, brand compliance checking, and governance automation. Reported outcomes include a pet food retailer saving almost 4,000 hours and a tea brand cutting migration time from months to weeks while improving metadata quality.

[Read source](https://www.youtube.com/watch?v=Kyym50EgUOQ)

---

#### Multi-Agent AI Platform for Life Insurance Sales Acceleration

**Company:** prudential  
**Industry:** Insurance

Prudential built “Just Ask,” an AI advisor assistant to reduce friction in life insurance sales, a process that can take 8–10 weeks and involves many products, regulatory requirements, and forms across states. The conversational tool helps financial planners with product guidance, quoting, forms, and underwriting support, while using guardrails for compliance. In 12 weeks, it processed 1,800 messages, delivered 100+ successful quotes, and saved about 4,500 human hours, with organic adoption growing for some agents and accuracy reported as 90%+ for most specialized areas.

[Read source](https://www.youtube.com/watch?v=g-YBqWv2kQ4)

---

#### Building and Scaling AI Agents in Production for DevSecOps Automation

**Company:** datadog  
**Industry:** Tech

Datadog, an observability company, says it has already put more than a hundred AI agents into production to automate DevSecOps work, with plans to expand to thousands more. The agents help with incident alert investigation, code generation and error fixes, and security investigations. Datadog highlights that successful agents run on their own in the background, are supported by strong evaluation, and are built to fit how teams and customers actually use the platform.

[Read source](https://www.youtube.com/watch?v=C3y3M_03Vco)

---

#### AI-Driven Enzyme Design for Advanced Plastic Recycling

**Company:** rhea’s_factory  
**Industry:** Energy

Rhea’s Factory is developing AI-designed enzymes to recycle plastics back into their original monomer building blocks. Traditional recycling degrades quality after only two to three cycles, limiting global recycling to about 10%. Their AI platform speeds enzyme discovery, reduces the number of wet-lab experiments needed, and aims for enzymes that work under industrial conditions while targeting different plastic types.

[Read source](https://www.youtube.com/watch?v=huFaei-6Z4g)

---

#### AI-Powered Bug Routing System Using RAG and Multimodal Processing

**Company:** miro  
**Industry:** Tech

Miro built BugManager to route software bug reports to the right engineering team faster. The system was designed for a large organization with nearly 100 teams, where misrouting and repeated reassignments caused major delays. BugManager uses AI to understand bug details, including screenshots and videos, and then suggests the best team(s) with explanations. People can review and change the suggested routing, and the system creates the Jira ticket with the needed information. Miro reports higher routing accuracy, fewer reassignments, and faster resolution—moving from days to hours.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-miro-uses-amazon-bedrock-to-boost-software-bug-routing-accuracy-and-improve-time-to-resolution-from-days-to-hours/)

---

#### Building Production Coding Agents with Pi Framework for Sales Process Automation

**Company:** tavon  
**Industry:** Tech

Tavon, a small European tech company, created an automated sales workflow to handle requests for proposals (RFPs). It watches an email inbox, routes messages to the right customer-focused agent, and produces draft replies. Each customer gets its own tailored agent settings. Human users review and approve drafts in their email client, reducing manual work while keeping people in control.

[Read source](https://www.youtube.com/watch?v=vAIDdLKB6-w)

---

#### Building a Production AI Code Review Agent with High Engineer Acceptance

**Company:** doordash  
**Industry:** Tech

DoorDash created an AI code review agent to help catch serious problems that human reviewers often miss in pull requests. It focuses on high and critical issues like dangerous deletions, cross-boundary inconsistencies, and silent behavior changes. The system evolved into a three-step approach that first spots suspicious areas, then double-checks them before posting. DoorDash says it achieved a 60.2% acceptance rate on high and critical findings across 10,000+ weekly PRs in 56 repositories, with reviews costing about $3 and finishing in about 7 minutes.

[Read source](https://careersatdoordash.com/blog/doordash-built-an-ai-code-reviewer-engineers-actually-listen-to/)

---

#### Building Custom Tracing Tools and Development Infrastructure for AI-Powered Meeting Notes

**Company:** granola  
**Industry:** Tech

Granola’s meeting-notes app uses real-time transcription and LLMs to produce summaries and a chat experience. In production, they struggled with unpredictable LLM behavior, controlling costs, and testing features. They built internal tracing so teams can see what happened and why, and they moved their desktop front-end into an online web shell for easier pull-request previews and faster testing.

[Read source](https://www.youtube.com/watch?v=ON5LIT0M4do)

---

#### Context Management and Memory Strategies for Production AI Agents

**Company:** arize  
**Industry:** Tech

Arize built an AI agent, Alex, to help teams build AI applications by analyzing observability traces and span data. As conversations and data volumes grew, the agent struggled with context and began failing in a repeating cycle. Arize fixed this by keeping only key parts of the conversation, using a separate memory for the rest, and offloading heavy work to other agents, then testing long sessions to keep performance stable.

[Read source](https://www.youtube.com/watch?v=esY99nYXxR4)

---

#### Gateway Patterns and Actions Runtime for Enterprise Agentic AI Deployment

**Company:** arcade.dev  
**Industry:** Tech

Arcade.dev focuses on deploying AI agents safely in enterprise environments with high-stakes, regulated use cases. It addresses security and governance gaps in common agent setups, especially authorization, tool quality, and visibility. The approach uses a gateway to enforce permission boundaries for multi-user agents, helping prevent authorization bypass and enabling controlled access to business systems like CRMs, ERPs, and email.

[Read source](https://www.youtube.com/watch?v=gQhDwOGdE4E)

---

#### Scaling LLM Production with Reinforcement Learning for Enterprise Agents

**Company:** adaptive_ml  
**Industry:** Tech

Adaptive ML says most GenAI pilots fail to reach production because teams lack a systematic way to improve models after launch. It promotes reinforcement learning to continuously incorporate feedback from real use, using an RLOps platform to train smaller, faster, more cost-effective specialized LLMs. The approach targets agent-style customer support and other enterprise workflows, aiming to cut inference costs and reduce latency. The company cites deployments serving enterprises including AT&T, Manulife, and CCS Medical Supply.

[Read source](https://www.youtube.com/watch?v=X6NShR2ccOg)

---

#### Scaling AI Agents in Production for B2B Growth and Outreach

**Company:** clay  
**Industry:** Tech

Clay, a B2B growth and customer acquisition tool, scaled its AI agents to handle very high monthly volume while keeping quality and costs under control. It uses specialized agents to support customer finding, outreach, and growth. With LangSmith observability and evaluation, teams can track spending across providers and debug issues when customers report problems.

[Read source](https://www.youtube.com/watch?v=cx6_tb6HCeY)

---

#### AI Employee Agent Operating in Slack with Multi-Tool Integration

**Company:** viktor  
**Industry:** Tech

Viktor is an AI “employee” that works directly in Slack for customer support, chatbot use, and code generation. It connects teams to 3,000+ integrations and company-wide context. The product evolved from earlier web and email agent experiments, and launched in February 2026 with immediate product-market fit. It also focuses on keeping conversations and access separated across channels.

[Read source](https://www.youtube.com/watch?v=ohKt066uFhg)

---

#### Autonomous Self-Healing System for Bug Resolution

**Company:** wix  
**Industry:** Tech

Wix built Gandalf to reduce the time it takes to resolve support issues by automatically turning support tickets into code changes. The system reads tickets, gathers relevant information from the company’s systems, generates a proposed fix, and creates a pull request for human review. Wix aimed to cut resolution time from an average of 14 days to under 24 hours, while still requiring engineers to make final deployment decisions. The team also found that some tickets are hard to classify and that important know-how often lives only in people’s experience rather than accessible documentation, so some work still needs human help.

[Read source](https://www.youtube.com/watch?v=3BNoppi6qcs)

---

#### Automating Trading Card Copywriting with Multi-Agent Generative AI

**Company:** fanatics_collectibles  
**Industry:** Media & Entertainment

Fanatics Collectibles needed to create trading card back copy at scale while meeting strict licensing and compliance rules. Their editorial teams previously spent weeks researching player stats, writing narratives, and checking complex rulebooks. They implemented a multi-agent system that automates research, writing, and quality checks. The result was faster production (weeks to hours), fewer QA edits, and large cost savings, while maintaining collector-acceptable quality.

[Read source](https://www.youtube.com/watch?v=plJylA9v_uc)

---

#### Multi-Agent Software Development System with Extended Autonomous Execution

**Company:** factory  
**Industry:** Tech

Factory built Missions to reduce the bottleneck of human attention in software engineering, letting engineers supervise only a few tasks while the system continues autonomously for days. Missions runs long projects with planning, verification, and end-to-end user testing, and it can produce cleaner codebases than the starting point while maintaining 90% test coverage in production use.

[Read source](https://www.youtube.com/watch?v=ow1we5PzK-o)

---

#### Evolution from Static Benchmarks to Adaptive Agent Evaluation Systems

**Company:** comet  
**Industry:** Tech

Comet’s Vincent says traditional LLM testing that relies on fixed benchmark sets can fall out of sync with how agent systems behave in real use, especially as user behavior changes. The proposed shift is to evaluate continuously in production using real interaction traces, so systems can catch and adapt to the unpredictable portion of user requests that static tests miss.

[Read source](https://www.youtube.com/watch?v=4VhbYlfC7Gs)

---

### Cool Use Cases

#### Production Skills Framework for Agentic LLM Workflows

**Company:** workos  
**Industry:** Tech

WorkOS created a “skills” framework to make AI workflows more consistent and easier to share. Instead of reloading the same context every time, teams codify tasks, rules, and knowledge once, then reuse them across people and projects. WorkOS applied the approach to developer onboarding and authentication setup, plus content and media generation, aiming for more deterministic results.

[Read source](https://www.youtube.com/watch?v=pFsfax19yOM)

---

#### Production Agent Observability and Monitoring Platform

**Company:** raindrop  
**Industry:** Tech

Raindrop helps teams monitor and debug AI agents in production when traditional testing doesn’t cover real-world behavior. It tracks both measurable problems (like errors and latency) and less obvious issues (like user frustration and refusals) using trained classifiers and pattern checks. Teams can set alerts, compare agent versions with real users, and use an automated triage agent to investigate spikes faster.

[Read source](https://www.youtube.com/watch?v=-aM2EDTiaMs)

---

#### AI-Powered Engineering Management and Autonomous Development Workflows

**Company:** notion  
**Industry:** Tech

Notion’s engineering manager Ryan Nestrom shows how AI agents can reduce routine overhead and speed up software delivery. The team automates standup prep by compiling the last 24 hours of activity into a ready-to-read summary. It also runs background coding from short task requests, and uses detailed written specs so agents can implement and verify features. The result is less time spent on status work, faster iteration, and more focus on architecture and checking correctness.

[Read source](https://www.youtube.com/watch?v=pUHA_jNwuYE)

---

### Tools & Infrastructure

#### Building Agentic Spreadsheet Automation from Process Mining to Production

**Company:** ramp  
**Industry:** Finance

Ramp (Finance) created Ramp Sheets to automate complex finance work in spreadsheets. It started from internal process mining that turned Loom videos of finance tasks into automation pipelines, then shifted to spreadsheet-native actions so users can audit what the system does. The agent runs in isolated sandboxes and typically completes tasks in about 7–10 minutes. Ramp also added self-monitoring that creates monitoring alerts and helps fix issues through PRs.

[Read source](https://www.youtube.com/watch?v=trEM9OKr5Sc)

---

#### AI-Powered Workflow Assistant for Seismic Data Processing

**Company:** halliburton  
**Industry:** Energy

Halliburton partnered with the AWS Generative AI Innovation Center to simplify seismic data processing workflow creation. Instead of manually configuring about 100 specialized tools, users can describe what they need in natural language. A proof-of-concept generated complete workflows with 84–97% success, cutting workflow creation time by over 95% and delivering results in seconds.

[Read source](https://aws.amazon.com/blogs/machine-learning/halliburton-enhances-seismic-workflow-creation-with-amazon-bedrock-and-generative-ai/)

---

#### Enterprise Code Search and Bug Investigation with Multi-Agent AI Systems

**Company:** wix  
**Industry:** Tech

Wix created two AI systems to help teams find answers in a very large codebase and investigate bugs. OctoCode helps developers search repositories, understand dependencies, and navigate complex code. Bilbo coordinates multiple AI agents to research issues across internal tools like code, logs, databases, and documentation, while learning from past investigations to improve future results.

[Read source](https://www.youtube.com/watch?v=T3pJz1Nwt1Y)

---

#### AI-Powered Security Vulnerability Detection Pipeline for Browser Hardening

**Company:** mozilla  
**Industry:** Tech

Mozilla used AI to audit Firefox security and help fix vulnerabilities that traditional fuzzing and manual code review struggled to find, including complex sandbox escapes and race conditions. The pipeline generated reproducible tests to confirm findings, then fed them into a full bug lifecycle process to ship fixes. Results included hundreds of security bugs fixed in April 2026 releases.

[Read source](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

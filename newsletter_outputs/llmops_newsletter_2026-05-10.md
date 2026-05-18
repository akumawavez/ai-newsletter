# Weekly LLMOps Newsletter — 2026-05-10

*Week of 2026-05-04 (Mon) – 2026-05-10 (Sun)*

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Industry News

#### Scaling Model Context Protocol (MCP) Infrastructure for Enterprise Agentic AI

**Company:** uber  
**Industry:** Tech

Uber built an enterprise MCP Gateway and Registry as a centralized control plane for MCP interactions. A gateway orchestrator crawls proto/thrift IDL files to generate MCP tool descriptions via an LLM, stores definitions in object storage, and serves MCP servers via a config provider. Updates flow through version-controlled diffs with unified security scanning, plus observability, guardrails, and PII redaction.

[Read source](https://www.youtube.com/watch?v=yVqMxBahjfA)

---

#### Demand-Driven Context Management for Enterprise AI Agents

**Company:** ikea  
**Industry:** E-commerce

IKEA’s demand-driven context management assigns real work items (incidents, Jira tickets) to agents with minimal initial context. Using Claude Code with skills, rules, and MCP-style hooks, agents retrieve existing knowledge, score confidence on a 1–5 scale, identify specific knowledge gaps, and categorize missing business logic/terminology. Domain experts fill gaps, and agents curate structured context blocks. Confidence improved from ~1.4–1.5 to 4.4 across 14 incident cycles; an automated context gap scanner batches historical items and generates probe-based reports.

[Read source](https://www.youtube.com/watch?v=_QAVExf_1uw)

---

#### Context Engine for Continual Learning in AI Coding Agents

**Company:** applied_commute  
**Industry:** Tech

Applied Compute built a Context Engine for continual learning in AI coding agents using a three-stage Remember/Refine/Retrieve pipeline. Production traces from Cursor, Claude Code, and Codex are logged into ACL-Wiki, refined daily into hierarchical memories with deduplication and pruning, and served at runtime via an MCP server. Human-in-the-loop flags feed back into Refine. They monitor Critical Memory Rate with GPT-4.5-mini judged via majority vote and evaluate with ACLBench using a minimal coding agent harness (Claude Opus 4.6).

[Read source](https://x.com/appliedcompute/status/2052826576723841292)

---

#### Building Production AI Agent Infrastructure at Scale with Claude Managed Agents

**Company:** anthropic  
**Industry:** Tech

Anthropic describes the shift from simple completion endpoints to Claude Managed Agents, a fully managed environment with persistent memory, file systems, execution sandboxes, and orchestration. The platform targets productionization gaps—secure sandboxing, state persistence, credential management, connection reliability, and async scaling—by offering opinionated primitives (file systems, skills, memory) with modular endpoints and APIs.

[Read source](https://www.youtube.com/watch?v=lLypHkIVLqc&pp=ugUEEgJlbg%3D%3D)

---

#### Building a Production AI Slack Bot with Pydantic AI and Logfire

**Company:** tiger_data  
**Industry:** Tech

Tiger Data built Tiger Agent for Work, a production AI Slack bot handling thousands of concurrent conversations with memory and context. They used Pydantic AI for LLM orchestration and MCP server integration, connecting eight MCP servers (including Slack search, documentation, Salesforce, GitHub, Linear, meeting transcripts, user memory, and progress reports). Pydantic AI provided automatic retry for tool calls and environment-variable model switching. Logfire supplied distributed tracing and “Agent Run” visualizations, with SQL-based trace querying and automatic instrumentation via logfire.instrument_pydantic_ai().

[Read source](https://pydantic.dev/articles/tiger-data-ai-slack-bot-pydantic-logfire)

---

#### Scaling Multimodal Visual AI with Self-Supervised Learning for Real-Time Generation

**Company:** black_forest_labs  
**Industry:** Research & Academia

Black Forest Labs describes Selfflow, a self-supervised multimodal training approach that removes external encoders. It uses a dual-noise setup with student-teacher models: the student denoises heavily noised inputs while the teacher (an EMA of the student) processes lightly noised inputs. The student minimizes generation and representation losses, enabling unified training across images, video, audio, and robotic actions.

[Read source](https://www.youtube.com/watch?v=x8Yb4RidLgM)

---

### Cool Use Cases

#### Agentic Search and Context Engineering for Production LLM Systems

**Company:** elastic  
**Industry:** Tech

Elastic’s case study outlines production patterns for agentic search and context engineering for LLM apps. It moves from fixed RAG pipelines to agentic retrieval where an agent decides whether to retrieve, assess relevance, and retrieve multiple times. Implementations use Elasticsearch with LangChain, tool description design, error handling, progressive disclosure skills, and logging agent behavior.

[Read source](https://www.youtube.com/watch?v=ynJyIKwjonM)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Industry News

#### Scaling Model Context Protocol (MCP) Infrastructure for Enterprise Agentic AI

**Company:** uber  
**Industry:** Tech

Uber scaled agentic AI beyond pilots by standardizing how AI agents access the company’s services. Without shared rules, teams created custom integrations that raised security, governance, and quality concerns. Uber’s centralized MCP Gateway and Registry translate service endpoints into tools, enforce permissions and privacy redaction, and support multiple agent experiences, including a no-code builder, an SDK, and coding agents.

[Read source](https://www.youtube.com/watch?v=yVqMxBahjfA)

---

#### Demand-Driven Context Management for Enterprise AI Agents

**Company:** ikea  
**Industry:** E-commerce

IKEA’s delivery and services teams built a new way to help enterprise AI agents deliver value when key know-how isn’t written down. Instead of expecting agents to find everything in documents, the system gives them real incidents to work on, spots what’s missing when they fail, and then turns expert-provided answers into reusable knowledge. In tests across 14 incidents, confidence rose from about 1.5 to 4.4, and a scanner can assess documentation quality at scale. The approach was validated in a preprint published in March 2026.

[Read source](https://www.youtube.com/watch?v=_QAVExf_1uw)

---

#### Context Engine for Continual Learning in AI Coding Agents

**Company:** applied_commute  
**Industry:** Tech

Applied Compute created a production memory system so AI coding agents can remember and reuse enterprise context over time. They tested it internally by logging coding-agent interactions across Cursor, Claude Code, and Codex into ACL-Wiki. Over two weeks, the share of retrievals deemed essential roughly doubled from under 10% to around 20%. On a curated benchmark, agents with the Contextbase beat no-memory baselines across categories like reducing time-to-value and exposing user preferences, without significant regression on distractor tasks.

[Read source](https://x.com/appliedcompute/status/2052826576723841292)

---

#### Building Production AI Agent Infrastructure at Scale with Claude Managed Agents

**Company:** anthropic  
**Industry:** Tech

Anthropic says teams often succeed in prototypes but hit an “infrastructure wall” when moving AI agents into real production. Claude Managed Agents is positioned as a managed platform that helps teams run long-running agents reliably by handling key operational needs like secure sandboxing, keeping state, and managing credentials—without teams managing servers or orchestration complexity.

[Read source](https://www.youtube.com/watch?v=lLypHkIVLqc&pp=ugUEEgJlbg%3D%3D)

---

#### Building a Production AI Slack Bot with Pydantic AI and Logfire

**Company:** tiger_data  
**Industry:** Tech

Tiger Data, a fully remote tech company, struggled with information overload because all communication and decisions happened in Slack. They built a production AI Slack bot, Tiger Agent for Work, to help employees quickly get context on ongoing discussions. The bot reached daily use by more than half the company within 6 weeks, while reducing debugging time through clearer visibility into what the agent did.

[Read source](https://pydantic.dev/articles/tiger-data-ai-slack-bot-pydantic-logfire)

---

#### Scaling Multimodal Visual AI with Self-Supervised Learning for Real-Time Generation

**Company:** black_forest_labs  
**Industry:** Research & Academia

Black Forest Labs, known for Stable Diffusion and the Flux model series, is working on faster, more scalable multimodal AI. They say Selfflow avoids external encoders and supports training across images, video, audio, and robotic actions. They also highlight their Client model series for near real-time generation and editing, aiming at interactive visual intelligence and physical AI applications.

[Read source](https://www.youtube.com/watch?v=x8Yb4RidLgM)

---

### Cool Use Cases

#### Agentic Search and Context Engineering for Production LLM Systems

**Company:** elastic  
**Industry:** Tech

Elastic describes how to build production LLM systems that can find the right information when answering questions or generating code. The approach shifts from fixed retrieval to an agent that can decide when and how to search across multiple sources. It emphasizes clear tool instructions, safe tool use, error recovery, and tracking agent behavior to improve reliability.

[Read source](https://www.youtube.com/watch?v=ynJyIKwjonM)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

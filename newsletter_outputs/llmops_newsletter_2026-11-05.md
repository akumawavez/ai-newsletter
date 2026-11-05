# Weekly LLMOps Newsletter — 2026-11-05

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Trace-Driven Cost, Quality, and Security Optimization for Coding Agents

**Company:** databricks  
**Industry:** Tech

Databricks deployed Unity Gateway as a centralized AI gateway for its engineering coding agents, using it to enforce budgets and security policies, collect agent traces, and provide flexibility across proprietary and open models and agent harnesses. Databricks then analyzed those traces with Genie and built task benchmarks to identify integration errors, excessive tool outputs, inappropriate model selection, and harness inefficiencies. Reported results included finding seven MCP bugs, identifying a Jira integration issue associated with approximately $90,000 in annual token cost and 5,000 agent-hours, reducing Slack-search payloads by an estimated 60%, and lowering model spend through task-aware routing. The approach is promising but the presentation provides limited independent validation, detailed quality measurements, or security results, so the savings should be treated as organization-specific findings rather than generally guaranteed outcomes.

[Read source](https://www.youtube.com/watch?v=8mylEGP37bw)

---

#### Training a Coding Agent Through an External Harness

**Company:** hugging_face  
**Industry:** Tech

Hugging Face demonstrated an open training pipeline for improving a small language model on coding-agent tasks without modifying the coding-agent harness itself. The system combines TRL's asynchronous GRPO trainer, the OpenEnv framework, OpenCode as a containerized agent harness, a capture proxy that records model interactions and log probabilities, isolated Hugging Face Sandboxes for each rollout, and hidden-test-based rewards. In a 10-step demonstration using two H100 GPUs and eight rollouts per step, the reported reward increased and reached 1, showing that the integration can run end to end; however, the result is explicitly preliminary because task difficulty was not controlled and the evaluation did not establish generalization or parity with a frontier model.

[Read source](https://www.youtube.com/watch?v=tjcQCnSk620)

---

#### Ontology-Driven Observability for Agentic Root-Cause Analysis

**Company:** netflix  
**Industry:** Media & Entertainment

Netflix built an ontology-backed knowledge graph to unify observability data and operational knowledge across applications, incidents, deployments, telemetry, and incident discussions. The system uses RDF, OWL, SHACL, SPARQL, sequential enrichment pipelines, correlation analysis, and internal agentic AI to turn noisy and inconsistently named data into typed, queryable triples. Its AutoRCA system presents engineers with ranked, evidence-backed hypotheses, reducing the manual effort required to reconstruct context during incidents. The approach improves consistency and context availability, but the source describes the system as early, with sometimes incorrect hypotheses and no formal quantitative results for investigation-time reduction or diagnostic accuracy.

[Read source](https://netflixtechblog.com/ontology-driven-observability-building-an-end-to-end-knowledge-graph-at-netflix-scale-421392cf5adf)

---

#### Agentic Cloud Security Remediation with Governed LLM Workflows

**Company:** tamnoon  
**Industry:** Tech

Tamnoon built Tami, an agentic cloud-security remediation platform, to reduce the backlog of findings produced by CNAPPs, CSPM systems, and cloud-native security tools. The system uses specialized agents on Amazon Bedrock to investigate findings, score remediation safety, generate backup-remediate-verify plans, and produce executable code, while applying guardrails, human approval, least-privilege access, rollback procedures, and independent review before changes reach customer environments. Tamnoon reports that Tami has analyzed more than 14 million alerts, enabled up to a 90% reduction in critical cloud exposure within 90 days, delivered up to 100x efficiency through root-cause clustering, saved more than 13,000 engineer hours per week across its customer base, and produced zero reported production issues; these results are company-reported claims rather than independently validated benchmarks.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-tamnoon-built-ai-powered-cloud-security-remediation-with-amazon-bedrock/)

---

#### Operating Always-On Persistent Agents in the Cloud

**Company:** stanford_(cs146s)  
**Industry:** Tech

Stanford CS146S presents an architecture for turning a short-lived tool-calling LLM harness into an always-on agent that can operate for hours, days, or potentially weeks. The design separates a durable server-side agent loop from a suspendable Linux sandbox, persists conversations and memories, accepts event-driven triggers, delegates work to sub-agents, and uses workflow orchestration, dynamic tool discovery, prompt caching, compaction, and automated review. The approach improves continuity, scalability, and autonomy, but the material identifies substantial unresolved risks around prompt injection, irreversible actions, memory quality, long-running evaluation, security, notification fatigue, and the reliability of claims that model-based command review is safer than human approval.

[Read source](https://youtu.be/L1OBRtfPS34)

---

#### Generative User-Journey Inference at Notification Scale

**Company:** pinterest  
**Industry:** Tech

Pinterest replaced a multi-stage keyword-clustering pipeline for identifying users’ longer-term goals with a fine-tuned 4-billion-parameter Qwen model that converts chronological activity logs into ranked, localized journey names. The system uses carefully specified prompts, synthetic data distilled from frontier models, structured-output validation, safety filtering, fallback behavior, and GPU-optimized serving through NVIDIA Dynamo and vLLM. Compared with the legacy system, Pinterest reports better consolidation, specificity, multilingual support, and noise removal; an initial US and Canada experiment showed 1.1% higher email click-through and 1.3% higher push opens, although the company notes that latent user intent has no definitive ground-truth label and that several proposed extensions remain experimental.

[Read source](https://medium.com/pinterest-engineering/from-activity-to-intent-generating-user-journeys-with-llms-9652b9417626)

---

#### Multimodal Semantic Video Discovery at Scale

**Company:** conde_nast  
**Industry:** Media & Entertainment

Condé Nast partnered with the AWS Generative AI Innovation Center to replace metadata-only video search with multimodal semantic discovery across a library of more than 140,000 videos. The production system uses TwelveLabs Marengo embeddings through Amazon Bedrock to represent visual, audio, and transcript content, Amazon OpenSearch Service for vector search, and decoupled asynchronous ingestion and query-serving planes running on AWS. In a May 2026 benchmarking workshop, Condé Nast reported that discovery time fell from an average of 250 minutes to approximately 2 minutes per task, with more than 90% less manual review effort and estimated annual operational savings of approximately $800,000; these outcomes are customer-reported estimates rather than independently validated results.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-conde-nast-built-multimodal-video-discovery-with-amazon-bedrock/)

---

#### Runtime Policy Enforcement for Secure Legal AI Agents

**Company:** harvey  
**Industry:** Legal

Harvey built an MCP Policy Engine to reduce the security risks created when production legal AI agents connect to external research, document, and communication systems. The design combines partner and connector security reviews with tool pinning, least-privilege controls, complete mediation of every tool call, context-aware information-flow policies, sanitization of hidden characters, human approval gates, and adversarial evaluation. The system is intended to limit the impact of tool poisoning, rug-pull changes, prompt injection, data exfiltration, and multi-agent workflow abuse, although Harvey presents it as an evolving defense-in-depth architecture rather than a complete solution to prompt injection.

[Read source](https://www.harvey.ai/blog/building-harveys-mcp-policy-engine)

---

#### Productionizing an Autonomous AI Research and Iteration Agent

**Company:** weights_&_biases  
**Industry:** Tech

Weights & Biases developed Arya, an AI research and iteration agent intended to help researchers analyze experiments, generate reports and workspaces, and autonomously launch further model-training jobs. Arya combines a conversational agent harness with shell and Python execution, Weights & Biases project data, Kubernetes-backed GPU workloads through Launch and CoreWeave, and Weave-based tracing, monitoring, LLM-judge signals, and nightly evaluations. In the demonstrated workflow, the agent ran batches of experiments on the Karpathy Auto Research project, identified patterns in metrics and hyperparameters, and produced a candidate model scoring 73% on an internal evaluation suite versus 72% for the production model; a live training batch produced only a marginal improvement in the showcased metric, so the evidence supports an iterative research workflow rather than fully autonomous breakthrough discovery.

[Read source](https://www.youtube.com/watch?v=hd7TOvmyAxU)

---

#### Distilling LLM Understanding into Marketplace Discovery

**Company:** doordash  
**Industry:** E-commerce

DoorDash uses LLMs to improve marketplace search, retrieval, ranking, personalization, and merchandising across restaurants, grocery, retail, pets, and other categories. Rather than placing an LLM directly in the latency-sensitive serving path, DoorDash uses stronger models offline to generate graded relevance labels, semantic catalog identifiers, user memory representations, and steerable collection content, then distills these outputs into retrieval, ranking, and recommendation systems. Reported results include a 2.3% improvement in relevance NDCG, a 4–5% improvement in ranker MRR, and early pet-category gains of nearly 1% in order rate and 6% in active users, although the presentation does not provide experimental details sufficient to independently assess attribution, statistical significance, or performance across all surfaces.

[Read source](https://www.youtube.com/watch?v=ACPEpji5NV4)

---

### Industry News

#### Grounded, Multi-Agent Enterprise AI at Global Scale

**Company:** qlik  
**Industry:** Tech

Qlik built Qlik Answers to let employees ask natural-language questions across structured analytics, documents, knowledge bases, glossaries, and automations while receiving sourced answers suitable for enterprise and regulated environments. The production architecture separates conversational entry, lightweight routing, answer planning, specialist agents, conversational analytics, retrieval, and model access, with Amazon Bedrock providing multi-model inference, embeddings, reranking, cross-Region inference, and Guardrails-based safety and grounding validation; Amazon OpenSearch Service supports document retrieval and Amazon SageMaker AI provides a regional fallback when a required model is unavailable in Bedrock. Qlik reports that, since general availability in February 2026, its Discovery Agent has surfaced more than 100,000 discoveries, while customer examples report up to 75% faster response times, as much as seven hours saved per week for managers, and a chatbot deployed in 15 minutes. These outcomes are vendor-reported and are not accompanied in the source by independent benchmarks, detailed quality metrics, or cost data.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-qlik-built-grounded-enterprise-scale-ai-with-amazon-bedrock/)

---

#### Industrializing Ontology-Grounded Agentic AI Across a Telecommunications Enterprise

**Company:** various  
**Industry:** Telecommunications

EchoStar is moving from isolated AI proofs of concept toward persistent, secure, and scalable AI operations across telecommunications, technology, and corporate functions. Its approach combines cleaned and governed enterprise data, semantic models, metrics, ontologies, and knowledge graphs to ground agents in business context, while federated governance and embedded AI business partners connect central architecture and security teams with individual business units. Reported production use includes more than 80 AI use cases across 16 business units, with approximately $200 million in annual incremental savings and benefits claimed by the company; additional vendor testing reports up to 85% hallucination reduction and 90% improvement in policy-grounded responses, although these figures are presented as internal or lab results rather than independently validated benchmarks.

[Read source](https://www.youtube.com/watch?v=S0876Xk3b4Y)

---

#### Slack-Based AI IT Help Desk with Retrieval and Ticket Automation

**Company:** shipstation  
**Industry:** E-commerce

ShipStation built Deckhand, an AI IT help desk that operates in Slack and uses Amazon Bedrock AgentCore, Claude, retrieval-augmented generation, and Jira Service Management integrations to answer routine questions, interpret error screenshots, and create contextualized tickets when self-service is insufficient. The system indexes curated internal documentation and validated historical Slack resolutions, applies rules to avoid interrupting human conversations, and collects employee feedback for iterative improvement. According to the AWS-published case study, Deckhand handled 1,935 messages during its first three months, replied to 97.5% of messages, received 96% positive feedback by June 2026, and deflected 812 of 1,221 agent conversations from becoming Jira tickets; the reported time savings are directional because they assume each avoided ticket would otherwise require approximately 30 minutes of work.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-shipstation-global-built-an-ai-it-help-desk-on-amazon-bedrock-agentcore/)

---

#### Building Production-Grade Company Memory and Portable AI Infrastructure

**Company:** various  
**Industry:** Tech

Several AI companies are addressing different production challenges that emerge when LLM systems move beyond small prototypes: retrieval over rapidly changing enterprise data, strict customer-cloud deployment requirements, and the loss of organizational knowledge across disconnected tools. The proposed solutions combine event-based memory, entity graphs, raw-document links, database-aware retrieval, sandboxed code execution, and provider-agnostic interfaces. Reported results include processing approximately 100 terabytes of knowledge, state-of-the-art performance on selected memory benchmarks, substantially lower retrieval costs when using less expensive models, support for deployment across multiple cloud environments, and a shared workspace in which company context is continuously captured. These claims are promising but are presented primarily as vendor demonstrations and should be validated against an organization’s own data, security model, workloads, and evaluation criteria.

[Read source](https://www.youtube.com/watch?v=dS_VDa620VM)

---

#### Building and Operating a Cloud-Native Coding Agent with Autonomous Verification

**Company:** amp  
**Industry:** Tech

Amp operates a TypeScript-based coding-agent product with a small team and a highly automated delivery model. The company uses its own agent across product development, testing, deployment, observability, feature-flag management, bug diagnosis, customer support, and controlled rollout workflows. Amp reports shipping about 90 times per day with changes reaching production in roughly seven minutes, while replacing conventional pull-request review with agent-thread collaboration, automated verification, risk-based rollout, monitoring, and selective human approval. The approach increases speed and enables a 21-person team to manage a broad operational surface, but it also introduces material tradeoffs around governance, model reliability, access control, auditability, incident risk, and the sustainability of relying on a single agent platform.

[Read source](https://www.youtube.com/watch?v=kQguG4YS0d0)

---

#### Building an AI-Native Growth Operations Platform

**Company:** rippling  
**Industry:** Tech

Rippling developed an internal AI platform to help revenue operations, marketing, sales, finance, and other go-to-market teams turn warehouse data into operational decisions. The system evolved from deterministic retrieval tools that supplied curated data to agents, to text-to-SQL capabilities that let agents investigate questions across the company’s warehouse and generate campaign, account, and strategy recommendations. A web application and horizontally scalable backend run agent loops that may issue multiple SQL queries, validate generated SQL, retrieve bespoke aggregate datasets, and synthesize results. Rippling evaluates changes through engineering benchmarks, rubric-based evaluations, CI checks, and user feedback, while selectively using smaller decision models for classification workloads. The approach improves access to analytics and reduces the distance between insight and action, but requires continuing data engineering, warehouse optimization, guardrails, evaluation maintenance, and human validation.

[Read source](https://www.youtube.com/watch?v=bGMiRmXbRUs)

---

#### A Shared Evaluation and Tracing Framework for Production AI Agents

**Company:** elastic  
**Industry:** Tech

Elastic consolidated fragmented evaluation practices for production AI agents used in cybersecurity, observability, enterprise chat, retrieval, and query generation. Its shared framework combines trace-based analysis, deterministic and domain-specific checks, RAG metrics, and LLM-as-a-judge evaluations, while keeping bespoke datasets and calibration with product and domain experts. The approach improves reuse, regression detection, and troubleshooting across teams, but the case study reports no aggregate quality, latency, cost, or release-frequency metrics, and emphasizes that the framework cannot replace expert-created test data, human review, or careful evaluator calibration.

[Read source](https://www.infoq.com/presentations/elastic-ai-agent-evaluations)

---

#### Building a Provider-Agnostic Agent Platform for Fintech Products

**Company:** ramp  
**Industry:** Finance

Ramp built Laminar, an in-house managed agent harness, to provide a common production platform for its growing portfolio of fintech agents, including support chat, invoice processing, coding, and long-horizon knowledge-work agents. The platform abstracts durable execution, model-provider interoperability, tool use, sandboxes, asynchronous interaction, human approvals, subagents, streaming, and agent-first observability while using Postgres, Temporal, and S3 as core infrastructure. Ramp reports that Laminar’s first version was built in six weeks and that, five months later, all of its agentic products ran on the platform, although the account provides no independent performance, reliability, cost, or quality metrics and emphasizes that ongoing engineering and on-call ownership remain necessary.

[Read source](https://builders.ramp.com/post/building-laminar)

---

#### Automated Agent Engineering with Trace Analysis and Validated Fixes

**Company:** langchain  
**Industry:** Tech

LangChain developed Engine, an agent-engineering system within LangSmith, to automate the production lifecycle of debugging and improving LLM-based agents. Engine analyzes production traces, identifies and clusters issues, performs root-cause analysis, proposes deployable fixes, generates evaluation cases, and checks for regressions. Its newer validated-fixes workflow reproduces failures in production, tests proposed changes in preview deployments, and evaluates them against broader datasets before human approval. LangChain reports that Engine has scanned more than 70 million traces and created more than 21,000 issues, while also reporting a twofold improvement in error identification on its IssueBench benchmark; these results are vendor-reported and the validated-fixes and red-teaming capabilities remain limited to private beta or specified deployment configurations.

[Read source](https://www.youtube.com/watch?v=S3l7U7gOsyY)

---

#### Securing and Scaling Agent Connectors Across Legal Tools

**Company:** harvey  
**Industry:** Legal

Harvey built a production Connector Library that lets legal agents use services such as email, document-management systems, and transaction data rooms while preserving user permissions and controlling the risks of third-party tools. The platform combines a code-based connector registry, native and MCP adapters, pre-launch security review, an in-process Rego/Open Policy Agent policy engine, tool-schema fingerprinting, customer-level controls, credential-management safeguards, and vendor-specific authorization normalization. Harvey reports more than 110,000 user connections, tens of thousands of connector tool calls per week, and approximately 13 million credential reads per day, although the source does not provide independent validation, error rates, quality measurements, or detailed security outcomes.

[Read source](https://www.harvey.ai/blog/how-we-built-harvey-connector-library)

---

### Cool Use Cases

#### Scaling a Company-Wide GenAI Platform with Gateways, Open Models, and Agent Infrastructure

**Company:** doordash  
**Industry:** E-commerce

DoorDash built an internal GenAI platform to help thousands of employees and product teams deploy LLM-powered automation, recommendations, personalization, and agents while balancing accuracy, latency, cost, velocity, and accountability. The platform evolved from an API-first LLM Gateway with provider abstraction, fallbacks, cost attribution, logging, and observability into an open-model serving capability and an Agent Gateway supporting MCP and other agent protocols, identity, authorization, rate limits, tool discovery, and streaming. DoorDash reports more than 5,000 internal users, approximately 45 new users onboarding daily, more than 50 MCP servers, roughly 300,000 daily tool calls, and annualized savings in the single-digit millions of dollars; however, agent runtime state, evaluation maturity, and safety enforcement remain partly decentralized or unresolved.

[Read source](https://www.infoq.com/presentations/doordash-genai-platform-architecture/)

---

#### Multi-Agent Database Operations and Proactive Incident Diagnosis

**Company:** cornerstone_on_demand  
**Industry:** HR

CornerStone On Demand built Orion AI to reduce the manual effort involved in diagnosing database incidents, managing database lifecycles, and coordinating DataOps and SRE workflows. The production system uses Amazon Bedrock, Strands Agents, specialized domain agents, hybrid keyword and semantic routing, MCP and API-based tool integrations, retrieval-augmented generation, memory controls, guardrails, and AWS observability services. According to the AWS-published case study, diagnosis time fell from approximately 45 minutes to 10 minutes, manual lifecycle work was reduced from more than 10 steps to one interaction, SRE-to-data-team reporting became real time, and redundant alerts decreased by a median of 65%; these results are vendor-reported and the text does not provide independent validation, workload volume, error rates, or cost data.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-cornerstone-ondemand-cut-database-diagnosis-by-78-with-amazon-bedrock/)

---

### Tools & Infrastructure

#### Enterprise Context and Grounded Agentic Workflows for Genie1

**Company:** databricks  
**Industry:** Tech

Databricks built Genie1 as a general-purpose enterprise AI co-worker that can answer business questions, explore governed data, execute analyses, and interact with workplace systems. The central challenge is that capable language models lack organization-specific definitions, data relationships, permissions, and operational context. Genie1 addresses this by dynamically reconstructing context from Unity Catalog and activity across the Databricks platform, using semantic and agentic asset search, authority signals, deferred tool loading, parallel execution, optional sub-agents, personalization, and strict grounding in executable SQL or Python with citations. The design aims to improve enterprise relevance, auditability, and responsiveness, although the presentation describes an evolving product and provides no independent accuracy, latency, adoption, or cost metrics.

[Read source](https://www.youtube.com/watch?v=eTZc0JBj2AY)

---

#### Production Multi-Agent Advertising Platform

**Company:** spotify  
**Industry:** Media & Entertainment

Spotify Ads built Ads AI, a production multi-agent platform that helps advertisers generate ad scripts and resolve audience targeting from natural-language campaign briefs. The platform uses Vertex AI through an internal LLM gateway, Google ADK Java, shared session state, domain-specific tools, deterministic validation, moderation gates, and trace-based evaluation. Spotify reports that more than 70% of ads use AI tools and that approximately 20,000 creatives have been generated for more than 7,000 advertisers, although audience recommendation remains in pilot and the presentation does not provide independent quality, revenue, latency, or cost comparisons.

[Read source](https://www.infoq.com/presentations/spotify-multi-agent-ai-architecture)

---

#### Building a Governed Trusted Data Layer for Agentic AI

**Company:** precisely  
**Industry:** Telecommunications

Precisely and Databricks present an architecture for deploying agentic AI on trusted enterprise data, using data classification, address verification, iterative address fixing, enrichment, spatial analytics, and governed orchestration. In the telecommunications example, customer, network-coverage, property, and location data are combined into a source-of-truth table so AI agents can answer operational questions and diagnose customer-service issues, such as why a subscriber receives lower broadband speeds than expected. The design emphasizes data quality, metadata, confidence scores, governance, audit logs, retry and recovery logic, and observability, although the presentation demonstrates a proposed solution rather than reporting independently validated production metrics or measured business outcomes.

[Read source](https://www.youtube.com/watch?v=RyaRUbk8r4w)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Trace-Driven Cost, Quality, and Security Optimization for Coding Agents

**Company:** databricks  
**Industry:** Tech

Databricks deployed Unity Gateway as a centralized AI gateway for its engineering coding agents, using it to enforce budgets and security policies, collect agent traces, and provide flexibility across proprietary and open models and agent harnesses. Databricks then analyzed those traces with Genie and built task benchmarks to identify integration errors, excessive tool outputs, inappropriate model selection, and harness inefficiencies. Reported results included finding seven MCP bugs, identifying a Jira integration issue associated with approximately $90,000 in annual token cost and 5,000 agent-hours, reducing Slack-search payloads by an estimated 60%, and lowering model spend through task-aware routing. The approach is promising but the presentation provides limited independent validation, detailed quality measurements, or security results, so the savings should be treated as organization-specific findings rather than generally guaranteed outcomes.

[Read source](https://www.youtube.com/watch?v=8mylEGP37bw)

---

#### Training a Coding Agent Through an External Harness

**Company:** hugging_face  
**Industry:** Tech

Hugging Face demonstrated an open training pipeline for improving a small language model on coding-agent tasks without modifying the coding-agent harness itself. The system combines TRL's asynchronous GRPO trainer, the OpenEnv framework, OpenCode as a containerized agent harness, a capture proxy that records model interactions and log probabilities, isolated Hugging Face Sandboxes for each rollout, and hidden-test-based rewards. In a 10-step demonstration using two H100 GPUs and eight rollouts per step, the reported reward increased and reached 1, showing that the integration can run end to end; however, the result is explicitly preliminary because task difficulty was not controlled and the evaluation did not establish generalization or parity with a frontier model.

[Read source](https://www.youtube.com/watch?v=tjcQCnSk620)

---

#### Ontology-Driven Observability for Agentic Root-Cause Analysis

**Company:** netflix  
**Industry:** Media & Entertainment

Netflix built an ontology-backed knowledge graph to unify observability data and operational knowledge across applications, incidents, deployments, telemetry, and incident discussions. The system uses RDF, OWL, SHACL, SPARQL, sequential enrichment pipelines, correlation analysis, and internal agentic AI to turn noisy and inconsistently named data into typed, queryable triples. Its AutoRCA system presents engineers with ranked, evidence-backed hypotheses, reducing the manual effort required to reconstruct context during incidents. The approach improves consistency and context availability, but the source describes the system as early, with sometimes incorrect hypotheses and no formal quantitative results for investigation-time reduction or diagnostic accuracy.

[Read source](https://netflixtechblog.com/ontology-driven-observability-building-an-end-to-end-knowledge-graph-at-netflix-scale-421392cf5adf)

---

#### Agentic Cloud Security Remediation with Governed LLM Workflows

**Company:** tamnoon  
**Industry:** Tech

Tamnoon built Tami, an agentic cloud-security remediation platform, to reduce the backlog of findings produced by CNAPPs, CSPM systems, and cloud-native security tools. The system uses specialized agents on Amazon Bedrock to investigate findings, score remediation safety, generate backup-remediate-verify plans, and produce executable code, while applying guardrails, human approval, least-privilege access, rollback procedures, and independent review before changes reach customer environments. Tamnoon reports that Tami has analyzed more than 14 million alerts, enabled up to a 90% reduction in critical cloud exposure within 90 days, delivered up to 100x efficiency through root-cause clustering, saved more than 13,000 engineer hours per week across its customer base, and produced zero reported production issues; these results are company-reported claims rather than independently validated benchmarks.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-tamnoon-built-ai-powered-cloud-security-remediation-with-amazon-bedrock/)

---

#### Operating Always-On Persistent Agents in the Cloud

**Company:** stanford_(cs146s)  
**Industry:** Tech

Stanford CS146S presents an architecture for turning a short-lived tool-calling LLM harness into an always-on agent that can operate for hours, days, or potentially weeks. The design separates a durable server-side agent loop from a suspendable Linux sandbox, persists conversations and memories, accepts event-driven triggers, delegates work to sub-agents, and uses workflow orchestration, dynamic tool discovery, prompt caching, compaction, and automated review. The approach improves continuity, scalability, and autonomy, but the material identifies substantial unresolved risks around prompt injection, irreversible actions, memory quality, long-running evaluation, security, notification fatigue, and the reliability of claims that model-based command review is safer than human approval.

[Read source](https://youtu.be/L1OBRtfPS34)

---

#### Generative User-Journey Inference at Notification Scale

**Company:** pinterest  
**Industry:** Tech

Pinterest replaced a multi-stage keyword-clustering pipeline for identifying users’ longer-term goals with a fine-tuned 4-billion-parameter Qwen model that converts chronological activity logs into ranked, localized journey names. The system uses carefully specified prompts, synthetic data distilled from frontier models, structured-output validation, safety filtering, fallback behavior, and GPU-optimized serving through NVIDIA Dynamo and vLLM. Compared with the legacy system, Pinterest reports better consolidation, specificity, multilingual support, and noise removal; an initial US and Canada experiment showed 1.1% higher email click-through and 1.3% higher push opens, although the company notes that latent user intent has no definitive ground-truth label and that several proposed extensions remain experimental.

[Read source](https://medium.com/pinterest-engineering/from-activity-to-intent-generating-user-journeys-with-llms-9652b9417626)

---

#### Multimodal Semantic Video Discovery at Scale

**Company:** conde_nast  
**Industry:** Media & Entertainment

Condé Nast partnered with the AWS Generative AI Innovation Center to replace metadata-only video search with multimodal semantic discovery across a library of more than 140,000 videos. The production system uses TwelveLabs Marengo embeddings through Amazon Bedrock to represent visual, audio, and transcript content, Amazon OpenSearch Service for vector search, and decoupled asynchronous ingestion and query-serving planes running on AWS. In a May 2026 benchmarking workshop, Condé Nast reported that discovery time fell from an average of 250 minutes to approximately 2 minutes per task, with more than 90% less manual review effort and estimated annual operational savings of approximately $800,000; these outcomes are customer-reported estimates rather than independently validated results.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-conde-nast-built-multimodal-video-discovery-with-amazon-bedrock/)

---

#### Runtime Policy Enforcement for Secure Legal AI Agents

**Company:** harvey  
**Industry:** Legal

Harvey built an MCP Policy Engine to reduce the security risks created when production legal AI agents connect to external research, document, and communication systems. The design combines partner and connector security reviews with tool pinning, least-privilege controls, complete mediation of every tool call, context-aware information-flow policies, sanitization of hidden characters, human approval gates, and adversarial evaluation. The system is intended to limit the impact of tool poisoning, rug-pull changes, prompt injection, data exfiltration, and multi-agent workflow abuse, although Harvey presents it as an evolving defense-in-depth architecture rather than a complete solution to prompt injection.

[Read source](https://www.harvey.ai/blog/building-harveys-mcp-policy-engine)

---

#### Productionizing an Autonomous AI Research and Iteration Agent

**Company:** weights_&_biases  
**Industry:** Tech

Weights & Biases developed Arya, an AI research and iteration agent intended to help researchers analyze experiments, generate reports and workspaces, and autonomously launch further model-training jobs. Arya combines a conversational agent harness with shell and Python execution, Weights & Biases project data, Kubernetes-backed GPU workloads through Launch and CoreWeave, and Weave-based tracing, monitoring, LLM-judge signals, and nightly evaluations. In the demonstrated workflow, the agent ran batches of experiments on the Karpathy Auto Research project, identified patterns in metrics and hyperparameters, and produced a candidate model scoring 73% on an internal evaluation suite versus 72% for the production model; a live training batch produced only a marginal improvement in the showcased metric, so the evidence supports an iterative research workflow rather than fully autonomous breakthrough discovery.

[Read source](https://www.youtube.com/watch?v=hd7TOvmyAxU)

---

#### Distilling LLM Understanding into Marketplace Discovery

**Company:** doordash  
**Industry:** E-commerce

DoorDash uses LLMs to improve marketplace search, retrieval, ranking, personalization, and merchandising across restaurants, grocery, retail, pets, and other categories. Rather than placing an LLM directly in the latency-sensitive serving path, DoorDash uses stronger models offline to generate graded relevance labels, semantic catalog identifiers, user memory representations, and steerable collection content, then distills these outputs into retrieval, ranking, and recommendation systems. Reported results include a 2.3% improvement in relevance NDCG, a 4–5% improvement in ranker MRR, and early pet-category gains of nearly 1% in order rate and 6% in active users, although the presentation does not provide experimental details sufficient to independently assess attribution, statistical significance, or performance across all surfaces.

[Read source](https://www.youtube.com/watch?v=ACPEpji5NV4)

---

### Industry News

#### Grounded, Multi-Agent Enterprise AI at Global Scale

**Company:** qlik  
**Industry:** Tech

Qlik built Qlik Answers to let employees ask natural-language questions across structured analytics, documents, knowledge bases, glossaries, and automations while receiving sourced answers suitable for enterprise and regulated environments. The production architecture separates conversational entry, lightweight routing, answer planning, specialist agents, conversational analytics, retrieval, and model access, with Amazon Bedrock providing multi-model inference, embeddings, reranking, cross-Region inference, and Guardrails-based safety and grounding validation; Amazon OpenSearch Service supports document retrieval and Amazon SageMaker AI provides a regional fallback when a required model is unavailable in Bedrock. Qlik reports that, since general availability in February 2026, its Discovery Agent has surfaced more than 100,000 discoveries, while customer examples report up to 75% faster response times, as much as seven hours saved per week for managers, and a chatbot deployed in 15 minutes. These outcomes are vendor-reported and are not accompanied in the source by independent benchmarks, detailed quality metrics, or cost data.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-qlik-built-grounded-enterprise-scale-ai-with-amazon-bedrock/)

---

#### Industrializing Ontology-Grounded Agentic AI Across a Telecommunications Enterprise

**Company:** various  
**Industry:** Telecommunications

EchoStar is moving from isolated AI proofs of concept toward persistent, secure, and scalable AI operations across telecommunications, technology, and corporate functions. Its approach combines cleaned and governed enterprise data, semantic models, metrics, ontologies, and knowledge graphs to ground agents in business context, while federated governance and embedded AI business partners connect central architecture and security teams with individual business units. Reported production use includes more than 80 AI use cases across 16 business units, with approximately $200 million in annual incremental savings and benefits claimed by the company; additional vendor testing reports up to 85% hallucination reduction and 90% improvement in policy-grounded responses, although these figures are presented as internal or lab results rather than independently validated benchmarks.

[Read source](https://www.youtube.com/watch?v=S0876Xk3b4Y)

---

#### Slack-Based AI IT Help Desk with Retrieval and Ticket Automation

**Company:** shipstation  
**Industry:** E-commerce

ShipStation built Deckhand, an AI IT help desk that operates in Slack and uses Amazon Bedrock AgentCore, Claude, retrieval-augmented generation, and Jira Service Management integrations to answer routine questions, interpret error screenshots, and create contextualized tickets when self-service is insufficient. The system indexes curated internal documentation and validated historical Slack resolutions, applies rules to avoid interrupting human conversations, and collects employee feedback for iterative improvement. According to the AWS-published case study, Deckhand handled 1,935 messages during its first three months, replied to 97.5% of messages, received 96% positive feedback by June 2026, and deflected 812 of 1,221 agent conversations from becoming Jira tickets; the reported time savings are directional because they assume each avoided ticket would otherwise require approximately 30 minutes of work.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-shipstation-global-built-an-ai-it-help-desk-on-amazon-bedrock-agentcore/)

---

#### Building Production-Grade Company Memory and Portable AI Infrastructure

**Company:** various  
**Industry:** Tech

Several AI companies are addressing different production challenges that emerge when LLM systems move beyond small prototypes: retrieval over rapidly changing enterprise data, strict customer-cloud deployment requirements, and the loss of organizational knowledge across disconnected tools. The proposed solutions combine event-based memory, entity graphs, raw-document links, database-aware retrieval, sandboxed code execution, and provider-agnostic interfaces. Reported results include processing approximately 100 terabytes of knowledge, state-of-the-art performance on selected memory benchmarks, substantially lower retrieval costs when using less expensive models, support for deployment across multiple cloud environments, and a shared workspace in which company context is continuously captured. These claims are promising but are presented primarily as vendor demonstrations and should be validated against an organization’s own data, security model, workloads, and evaluation criteria.

[Read source](https://www.youtube.com/watch?v=dS_VDa620VM)

---

#### Building and Operating a Cloud-Native Coding Agent with Autonomous Verification

**Company:** amp  
**Industry:** Tech

Amp operates a TypeScript-based coding-agent product with a small team and a highly automated delivery model. The company uses its own agent across product development, testing, deployment, observability, feature-flag management, bug diagnosis, customer support, and controlled rollout workflows. Amp reports shipping about 90 times per day with changes reaching production in roughly seven minutes, while replacing conventional pull-request review with agent-thread collaboration, automated verification, risk-based rollout, monitoring, and selective human approval. The approach increases speed and enables a 21-person team to manage a broad operational surface, but it also introduces material tradeoffs around governance, model reliability, access control, auditability, incident risk, and the sustainability of relying on a single agent platform.

[Read source](https://www.youtube.com/watch?v=kQguG4YS0d0)

---

#### Building an AI-Native Growth Operations Platform

**Company:** rippling  
**Industry:** Tech

Rippling developed an internal AI platform to help revenue operations, marketing, sales, finance, and other go-to-market teams turn warehouse data into operational decisions. The system evolved from deterministic retrieval tools that supplied curated data to agents, to text-to-SQL capabilities that let agents investigate questions across the company’s warehouse and generate campaign, account, and strategy recommendations. A web application and horizontally scalable backend run agent loops that may issue multiple SQL queries, validate generated SQL, retrieve bespoke aggregate datasets, and synthesize results. Rippling evaluates changes through engineering benchmarks, rubric-based evaluations, CI checks, and user feedback, while selectively using smaller decision models for classification workloads. The approach improves access to analytics and reduces the distance between insight and action, but requires continuing data engineering, warehouse optimization, guardrails, evaluation maintenance, and human validation.

[Read source](https://www.youtube.com/watch?v=bGMiRmXbRUs)

---

#### A Shared Evaluation and Tracing Framework for Production AI Agents

**Company:** elastic  
**Industry:** Tech

Elastic consolidated fragmented evaluation practices for production AI agents used in cybersecurity, observability, enterprise chat, retrieval, and query generation. Its shared framework combines trace-based analysis, deterministic and domain-specific checks, RAG metrics, and LLM-as-a-judge evaluations, while keeping bespoke datasets and calibration with product and domain experts. The approach improves reuse, regression detection, and troubleshooting across teams, but the case study reports no aggregate quality, latency, cost, or release-frequency metrics, and emphasizes that the framework cannot replace expert-created test data, human review, or careful evaluator calibration.

[Read source](https://www.infoq.com/presentations/elastic-ai-agent-evaluations)

---

#### Building a Provider-Agnostic Agent Platform for Fintech Products

**Company:** ramp  
**Industry:** Finance

Ramp built Laminar, an in-house managed agent harness, to provide a common production platform for its growing portfolio of fintech agents, including support chat, invoice processing, coding, and long-horizon knowledge-work agents. The platform abstracts durable execution, model-provider interoperability, tool use, sandboxes, asynchronous interaction, human approvals, subagents, streaming, and agent-first observability while using Postgres, Temporal, and S3 as core infrastructure. Ramp reports that Laminar’s first version was built in six weeks and that, five months later, all of its agentic products ran on the platform, although the account provides no independent performance, reliability, cost, or quality metrics and emphasizes that ongoing engineering and on-call ownership remain necessary.

[Read source](https://builders.ramp.com/post/building-laminar)

---

#### Automated Agent Engineering with Trace Analysis and Validated Fixes

**Company:** langchain  
**Industry:** Tech

LangChain developed Engine, an agent-engineering system within LangSmith, to automate the production lifecycle of debugging and improving LLM-based agents. Engine analyzes production traces, identifies and clusters issues, performs root-cause analysis, proposes deployable fixes, generates evaluation cases, and checks for regressions. Its newer validated-fixes workflow reproduces failures in production, tests proposed changes in preview deployments, and evaluates them against broader datasets before human approval. LangChain reports that Engine has scanned more than 70 million traces and created more than 21,000 issues, while also reporting a twofold improvement in error identification on its IssueBench benchmark; these results are vendor-reported and the validated-fixes and red-teaming capabilities remain limited to private beta or specified deployment configurations.

[Read source](https://www.youtube.com/watch?v=S3l7U7gOsyY)

---

#### Securing and Scaling Agent Connectors Across Legal Tools

**Company:** harvey  
**Industry:** Legal

Harvey built a production Connector Library that lets legal agents use services such as email, document-management systems, and transaction data rooms while preserving user permissions and controlling the risks of third-party tools. The platform combines a code-based connector registry, native and MCP adapters, pre-launch security review, an in-process Rego/Open Policy Agent policy engine, tool-schema fingerprinting, customer-level controls, credential-management safeguards, and vendor-specific authorization normalization. Harvey reports more than 110,000 user connections, tens of thousands of connector tool calls per week, and approximately 13 million credential reads per day, although the source does not provide independent validation, error rates, quality measurements, or detailed security outcomes.

[Read source](https://www.harvey.ai/blog/how-we-built-harvey-connector-library)

---

### Cool Use Cases

#### Scaling a Company-Wide GenAI Platform with Gateways, Open Models, and Agent Infrastructure

**Company:** doordash  
**Industry:** E-commerce

DoorDash built an internal GenAI platform to help thousands of employees and product teams deploy LLM-powered automation, recommendations, personalization, and agents while balancing accuracy, latency, cost, velocity, and accountability. The platform evolved from an API-first LLM Gateway with provider abstraction, fallbacks, cost attribution, logging, and observability into an open-model serving capability and an Agent Gateway supporting MCP and other agent protocols, identity, authorization, rate limits, tool discovery, and streaming. DoorDash reports more than 5,000 internal users, approximately 45 new users onboarding daily, more than 50 MCP servers, roughly 300,000 daily tool calls, and annualized savings in the single-digit millions of dollars; however, agent runtime state, evaluation maturity, and safety enforcement remain partly decentralized or unresolved.

[Read source](https://www.infoq.com/presentations/doordash-genai-platform-architecture/)

---

#### Multi-Agent Database Operations and Proactive Incident Diagnosis

**Company:** cornerstone_on_demand  
**Industry:** HR

CornerStone On Demand built Orion AI to reduce the manual effort involved in diagnosing database incidents, managing database lifecycles, and coordinating DataOps and SRE workflows. The production system uses Amazon Bedrock, Strands Agents, specialized domain agents, hybrid keyword and semantic routing, MCP and API-based tool integrations, retrieval-augmented generation, memory controls, guardrails, and AWS observability services. According to the AWS-published case study, diagnosis time fell from approximately 45 minutes to 10 minutes, manual lifecycle work was reduced from more than 10 steps to one interaction, SRE-to-data-team reporting became real time, and redundant alerts decreased by a median of 65%; these results are vendor-reported and the text does not provide independent validation, workload volume, error rates, or cost data.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-cornerstone-ondemand-cut-database-diagnosis-by-78-with-amazon-bedrock/)

---

### Tools & Infrastructure

#### Enterprise Context and Grounded Agentic Workflows for Genie1

**Company:** databricks  
**Industry:** Tech

Databricks built Genie1 as a general-purpose enterprise AI co-worker that can answer business questions, explore governed data, execute analyses, and interact with workplace systems. The central challenge is that capable language models lack organization-specific definitions, data relationships, permissions, and operational context. Genie1 addresses this by dynamically reconstructing context from Unity Catalog and activity across the Databricks platform, using semantic and agentic asset search, authority signals, deferred tool loading, parallel execution, optional sub-agents, personalization, and strict grounding in executable SQL or Python with citations. The design aims to improve enterprise relevance, auditability, and responsiveness, although the presentation describes an evolving product and provides no independent accuracy, latency, adoption, or cost metrics.

[Read source](https://www.youtube.com/watch?v=eTZc0JBj2AY)

---

#### Production Multi-Agent Advertising Platform

**Company:** spotify  
**Industry:** Media & Entertainment

Spotify Ads built Ads AI, a production multi-agent platform that helps advertisers generate ad scripts and resolve audience targeting from natural-language campaign briefs. The platform uses Vertex AI through an internal LLM gateway, Google ADK Java, shared session state, domain-specific tools, deterministic validation, moderation gates, and trace-based evaluation. Spotify reports that more than 70% of ads use AI tools and that approximately 20,000 creatives have been generated for more than 7,000 advertisers, although audience recommendation remains in pilot and the presentation does not provide independent quality, revenue, latency, or cost comparisons.

[Read source](https://www.infoq.com/presentations/spotify-multi-agent-ai-architecture)

---

#### Building a Governed Trusted Data Layer for Agentic AI

**Company:** precisely  
**Industry:** Telecommunications

Precisely and Databricks present an architecture for deploying agentic AI on trusted enterprise data, using data classification, address verification, iterative address fixing, enrichment, spatial analytics, and governed orchestration. In the telecommunications example, customer, network-coverage, property, and location data are combined into a source-of-truth table so AI agents can answer operational questions and diagnose customer-service issues, such as why a subscriber receives lower broadband speeds than expected. The design emphasizes data quality, metadata, confidence scores, governance, audit logs, retry and recovery logic, and observability, although the presentation demonstrates a proposed solution rather than reporting independently validated production metrics or measured business outcomes.

[Read source](https://www.youtube.com/watch?v=RyaRUbk8r4w)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

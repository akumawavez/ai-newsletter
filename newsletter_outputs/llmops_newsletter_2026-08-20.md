# Weekly LLMOps Newsletter — 2026-08-20

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Training and Deploying Create 2: A Stylistically Diverse Image Foundation Model

**Company:** krea  
**Industry:** Media & Entertainment

Krea developed and open-sourced Create 2, an image foundation model designed to prioritize stylistic diversity and faster generation over the mode-collapsed outputs of competitors. The team addressed the challenge of creative professionals needing diverse visual exploration tools rather than consistently safe but homogeneous results. Their solution involved a comprehensive LLMOps pipeline including custom data curation with 30-40 in-house classifiers, multi-stage training from low to high resolution, vision-language model captioning, sparse autoencoder-based filtering, preference optimization, and reinforcement learning. The medium variant was successfully open-sourced and demonstrates strong world knowledge and stylistic range while maintaining fast iteration speeds for creative workflows.

[Read source](https://www.youtube.com/watch?v=-tviRdpmHvs)

---

#### Scaling Agentic AI Infrastructure for Production ML Workflows

**Company:** linkedin  
**Industry:** Tech

LinkedIn's AI platforms team developed an agentic platform to automate complex machine learning tasks including migrating 400+ TensorFlow models to PyTorch, optimizing cluster performance, and conducting autonomous research experiments. The platform uses code-based agents that run iterative experiments over hours or days, launching hundreds of jobs autonomously. To support this scale, LinkedIn built specialized infrastructure including a warm GPU pool with low-latency job launching, restricted execution environments for untrusted agent-generated code, and robust checkpointing systems. The implementation resulted in 100% growth in cluster experiments over six months, demonstrating the potential for agents to dramatically increase experimentation velocity and model improvement opportunities.

[Read source](https://www.youtube.com/watch?v=FJUrsZn1BSI)

---

#### Scaling Reinforcement Learning for AI Coding Agents

**Company:** cognition  
**Industry:** Tech

Cognition, the company behind Devin (the AI software engineer) and Windsurf, undertook an ambitious research program to build production-ready coding agents through increasingly complex reinforcement learning training runs. Starting with a modest 32 H200 GPUs and a small team, they progressed through four major projects: Kevin 32B for CUDA kernel optimization, Swee Grab for file search, and Sweep v1.6 and v1.7 for end-to-end software engineering tasks. The company tackled significant technical challenges including multi-turn agentic training, parallel tool calling, asynchronous RL for throughput optimization, and entropy collapse. Their latest model, Sweep 1.7, achieves frontier-level performance on benchmarks like SWE-bench Pro while being considerably smaller and cheaper than competing models, demonstrating that careful execution of RL techniques can squeeze exceptional performance from smaller models.

[Read source](https://www.youtube.com/watch?v=z--bPNOvoi0)

---

#### Memory Harnesses for Long-Running Research Agents on Local Models

**Company:** sakana  
**Industry:** Research & Academia

Sakana AI developed a memory harness system to address context degradation in long-horizon agentic tasks running on local models. The problem tackled was context rot, where models contradict themselves, forget completed tasks, or drift from original questions during extended operations. The solution involved designing a write-manage-read memory loop with different recall policies, tested on local models including Qwen 27B and DeepSeek V4 Flash running on Apple M3 Ultra hardware. Results showed that ranked recall policies outperformed baseline approaches on benchmarks like XBench, achieving better accuracy while reducing token costs, demonstrating that structured memory management is essential for cost-effective long-horizon agent performance on local infrastructure.

[Read source](https://www.youtube.com/watch?v=R3-anFK1YM8)

---

### Industry News

#### Building Scalable AI Agents for Go-to-Market Automation at Production Scale

**Company:** unify  
**Industry:** Tech

UniFi developed an AI agent platform that automates go-to-market research and outreach for sales teams, powering $900 million in pipeline. The company evolved from running millions of asynchronous web research agents to launching a chat-based interface where sales reps interact with agents that can write TypeScript code, manipulate tabular data, and orchestrate API calls. Through aggressive cost optimization including prompt caching strategies, reducing sub-agent usage, implementing efficient tool calling patterns, and moving from expensive sub-agent architectures to smarter main agents that write code, UniFi achieved a 90-95% cost reduction. The platform now enables individual sales reps to perform research and outreach tasks that previously required entire teams, while maintaining strong data tenancy, durability, and observability across cloud-based execution environments.

[Read source](https://www.youtube.com/watch?v=6898VdRtKDE)

---

#### Multi-Agent AI Platform for Streaming Media Analytics and Content Production

**Company:** mbc_shahid  
**Industry:** Media & Entertainment

MBC Shahid, the leading Arabic streaming platform in the MENA region with 35 million monthly active users, evolved from traditional BI dashboards to AI-powered data products through a three-season journey. The company built multiple production LLM applications using Databricks, including Enigma (a conversational analytics platform merging quantitative viewing data with qualitative sentiment from customer comments), interactive AI-generated dashboards via Genie, and Spectra Studio (an automated video processing system for generating short-form content, subtitles, and compliance checks). These applications process massive scale data including 2.5 billion viewing hours annually, handle multi-language Arabic dialects, and significantly reduce manual work like generating 50 daily shorts during Ramadan peak periods while maintaining human oversight for quality control.

[Read source](https://www.youtube.com/watch?v=cA_HTWEhTtM)

---

#### UK-Sovereign AI Platform with Self-Hosted LLMs and 50+ Specialized Agents

**Company:** oneadvanced  
**Industry:** Tech

OneAdvanced, a UK-based enterprise software provider serving over 10,000 customers in regulated industries including healthcare, legal, and public sector, needed to deploy AI capabilities while ensuring strict UK data sovereignty requirements. The company built a production AI solution by self-hosting Llama 4 Maverick and Llama Guard 4 models on Amazon SageMaker AI infrastructure in the London region, orchestrating over 50 specialized agents using Strands Agents SDK on Amazon ECS, and implementing a RAG pipeline backed by Amazon Aurora PostgreSQL with pgvector. The solution went from prototype to production through an AWS advisory engagement, deployed over 50 agents in three weeks, and has been serving customers in production since July 2025, achieving its performance targets while maintaining complete UK data residency and earning ISO 42001 certification for AI governance.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-oneadvanced-deployed-over-50-ai-agents-on-uk-sovereign-aws/)

---

#### Enterprise-Scale Agentic Engineering: Building LLM Infrastructure and Tooling for 250+ Engineering Teams

**Company:** zalando  
**Industry:** E-commerce

Zalando, a major e-commerce company, shares their 2.5-year journey implementing agentic engineering and LLMOps practices across 250+ engineering teams. The company built a comprehensive LLM infrastructure starting with a LiteLLM-based API proxy deployed in January 2024, complemented by chat UIs, CLI tools, and coding agents. They addressed challenges around vendor independence, model access, authentication, and governance while implementing risk-based PR approval systems and training programs. The initiative resulted in measurable impacts on PR throughput, code complexity patterns, and developer productivity, with 33% of PRs achieving low-risk auto-approval and significant reductions in PR lead time (20-40% for auto-approved changes).

[Read source](https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html)

---

#### Enterprise Sales Intelligence Agent: From Prototype to Production

**Company:** postman  
**Industry:** Tech

Postman developed an enterprise sales intelligence agent to address context loss and information handoff challenges across their sales organization, which relied on multiple disconnected systems throughout the sales lifecycle. Starting with a hackathon that produced numerous prototypes, they identified a win-loss analysis agent as most promising and evolved it through four architectural stages: a monolith agent with broad knowledge, domain-specific agents with hallucination controls, strategic content integration from sales teams, and finally role-based access controls. This iterative approach reduced agent development time from 30 hours to just hours, expanded usage organization-wide, and created compounding value by improving both the quality of sales discovery activities and the underlying agent performance through increased user engagement.

[Read source](https://www.youtube.com/watch?v=gjGAnb0if28)

---

#### Building Autonomous Software Factories with AI Agents

**Company:** factory  
**Industry:** Tech

Factory presents a vision for transforming software development through "software factories" - autonomous systems where signals like customer feedback, bugs, and business requirements flow directly to deployed code with minimal human intervention. The problem addressed is that while AI-powered coding tools have evolved from autocomplete to chatbots to agents, organizations haven't seen promised productivity gains because these tools only automate narrow slices of the development process while planning, triage, validation, and deployment remain human-driven bottlenecks. Factory's solution involves building model-independent, organization-owned agent platforms with shared agent cores that operate across all product and engineering workflows - from code review to incident response - with extensive governance controls, deterministic feedback loops, and continuous evaluation systems. The approach emphasizes preparing the engineering environment for agent readiness, implementing governance before scaling, and measuring outcomes like cycle time and bug rates rather than token usage.

[Read source](https://www.youtube.com/watch?v=Pa3MAnWeNB4)

---

#### Verifiable and Auditable AI Agent Payment Processing with Hardware Attestation

**Company:** solv_labs  
**Industry:** Tech

Solv Labs built an AI agent payment workflow on Amazon Bedrock AgentCore payments to address the enterprise challenge of proving that autonomous agent payments are authorized, risk-priced, and auditable. The solution combines AgentCore payments for payment processing, ORACLE (Solv's policy engine) for pre-authorization, ICME PreFlight for privacy-preserving compliance verification, and AWS Nitro Enclaves for hardware attestation. Each transaction completes in under four seconds and produces a complete audit trail with cryptographic proofs, hardware attestations, per-transaction risk pricing, and on-chain anchoring via Coinbase and Base blockchain. The system enables enterprises to deploy agent payments in regulated environments with verifiable governance at machine speed, scaling review effort with exceptions rather than transaction volume.

[Read source](https://aws.amazon.com/blogs/machine-learning/pay-with-confidence-how-solv-labs-built-verifiable-auditable-agent-payments-on-amazon-bedrock-agentcore-payments/)

---

#### Multi-Tenant AI Agent Deployment with Secure Isolation Using Amazon Bedrock AgentCore

**Company:** axonious  
**Industry:** Tech

Axonius, a cybersecurity asset intelligence platform serving hundreds of isolated customer environments, needed to add AI agents to their SaaS offering while maintaining strict tenant isolation and security requirements. They deployed a silo-model architecture using Amazon Bedrock AgentCore runtime, where each customer receives a dedicated agent with microVM-level session isolation. This approach integrated with their existing VPC-based tenant deployment model, using JWT-based authentication, IAM role tagging for cost allocation, Amazon Bedrock Knowledge Bases for RAG, and VPC Lattice for private networking. The solution reduced development time from an estimated eight weeks to 10 days—a 75% reduction in time-to-market—while maintaining the security-first architecture required for handling sensitive cybersecurity data across multiple enterprise customers.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-axonius-built-secure-multi-tenant-ai-agents-on-bedrock-agentcore/)

---

#### Practical Approaches to AI Agent Evaluation and Floor Raising in Production

**Company:** raindrop  
**Industry:** Tech

Raindrop's CTO presents practical lessons from observing real-world AI agent deployments across finance, healthcare, and defense sectors. The talk challenges conventional evaluation approaches inherited from the chatbot era, arguing that static benchmark-style evaluations don't scale for modern agentic systems. Instead, the company advocates for "raising the floor" by focusing on preventing critical failures rather than maximizing ceiling capabilities. Their solution involves production monitoring similar to Sentry, treating evaluations as code-based tests rather than cloud-managed prompts, and using deterministic signals to trigger agent-based investigation rather than asking agents to detect anomalies directly. The approach emphasizes understanding when issues started and how many users they affect, with different strategies for high-volume versus low-volume deployments.

[Read source](https://www.youtube.com/watch?v=jHMiYtjoJfA)

---

#### Building Context-Aware Consumer AI at Scale with Agentic Recommendations

**Company:** doordash  
**Industry:** E-commerce

DoorDash transformed their recommendation systems from legacy one-shot predictions to a sophisticated agentic platform to support multi-state shopping experiences like grocery planning. The company developed language-native consumer memory blocks to replace traditional embeddings, implemented semantic IDs (RQ-VAE) for granular catalog representation, built grounded search systems for intent understanding, and modernized ranking with LLM-generated relevance labels. These innovations enabled dramatic improvements across key metrics: 10% lift in mean reciprocal rank (MRR) from graph-based memory, 13% accuracy improvement on long-tail query intent, and 2.2% conversion rate increase from improved relevance. The system culminates in multi-turn agentic shopping assistants that leverage all these primitives, evaluated through comprehensive trajectory-based rubrics and agentic harness engineering.

[Read source](https://www.infoq.com/presentations/ai-agentic-recommendations-semantic-ids/)

---

#### Runtime Security and Governance Framework for AI Agents

**Company:** thales_group  
**Industry:** Tech

Thales Group developed a comprehensive security and governance framework to address the operational risks of autonomous AI agents in production environments. The problem centered on agents potentially exceeding their intended boundaries and performing unauthorized actions, particularly concerning given the complex interactions between users, agents, sub-agents, and downstream systems. Thales built a runtime trust plane that monitors and enforces controls across identity, delegation, policy, risk, and evidence layers. The solution creates a continuous record of trust, compares declared versus observed agent behavior to identify variance, and implements risk-based execution controls including quarantine, rollback, and kill switches. This approach enables real-time governance over dynamic control paths while maintaining observability and enforcing authorization boundaries across multi-agent workflows.

[Read source](https://www.youtube.com/watch?v=czfKC-p79tA)

---

#### Building Agent-First Data Infrastructure with Comprehensive Evaluation Frameworks

**Company:** bauplan  
**Industry:** Tech

Bauplan, a data infrastructure company built for agents as first-class users, developed a comprehensive evaluation framework for LLM coding agents working on data engineering tasks. The company created 700 evaluation tasks derived from real-world customer usage patterns, significantly more than competing frameworks from Supabase (20+ tasks) and Snowflake (100 tasks). By leveraging their Git-for-data architecture that enables deterministic verification of agent actions through API-first design and branch immutability, Bauplan optimized agent performance through automated skill improvement using the DSPy optimizer. Results showed that optimized skills improved performance across all models, and surprisingly, open-source models like DeepSeek could achieve results comparable to frontier models like Claude Opus at one-third the cost when working with properly designed agent-first infrastructure.

[Read source](https://www.youtube.com/watch?v=3JvR0Wb3XWg)

---

#### Securing AI Agents with Network-Level Proxy Controls for Production Infrastructure

**Company:** deno  
**Industry:** Tech

Deno faced the challenge of using AI agents powered by models like Claude Opus to automatically handle production incidents in their Deno Deploy hosting service, requiring agents to access critical systems like PostgreSQL, Kubernetes, ClickHouse, AWS, GitHub, and Slack with write permissions. While the agents proved capable of resolving many incidents that previously required human intervention, the company recognized that agents could not be trusted to police themselves due to risks like prompt injection attacks and unpredictable behavior. To address this, Deno developed Claw Patrol, an open-source network proxy that sits between agents and infrastructure, parsing every byte of network communication across multiple protocols including non-HTTP ones, enforcing granular permission rules defined in version-controlled configuration files, injecting credentials so agents never see secrets directly, and providing approval workflows and dashboards for monitoring agent actions in real-time.

[Read source](https://www.youtube.com/watch?v=MkRYPFIMCSA)

---

#### Autonomous Integration Factory Using LLM Agents

**Company:** ramp  
**Industry:** Finance

Ramp faced the classic engineering scaling problem where customer demand for integrations with third-party tools far exceeded their team's capacity to build and maintain them manually. To solve this, they built two complementary LLM-powered systems: a customer-facing agentic system that autonomously builds custom integrations on-demand within minutes based on natural language descriptions, and an internal "integration factory" that converts these custom integrations into production-grade first-party connectors. The solution has already shipped 75 integrations, reducing time-to-integration from weeks or months down to hours (for first-party) or minutes (for custom), while dramatically reducing cost and expanding coverage to nearly any integration customers need.

[Read source](https://builders.ramp.com/post/integrations-that-write-themselves)

---

#### Building an Evaluation-First Culture for Enterprise Agent Platform

**Company:** uber  
**Industry:** Tech

Uber's agent platform team faced a common challenge where development teams would ship LLM-powered agents to production and defer evaluation development until later, creating a cycle of retrofitting and debugging. To solve this, they built platform capabilities that made evaluations the default from day one, including automatic tracing across all environments, AI-generated starter evaluation kits delivered via Slack, and CLI-based tools that democratized eval ownership beyond engineering to product and customer teams. This shift from treating evals as a checkbox to an engine for continuous improvement enabled them to catch critical issues early, such as discovering that their voice booking agent had a 95% offline eval score but was misinterpreting background conversations in production, leading to fundamental changes in how the agent understood intent.

[Read source](https://www.youtube.com/watch?v=UTcKagbKp4A)

---

#### Scaling Demand Forecasting at Global Scale with Agentic AI

**Company:** pepsico  
**Industry:** Other

PepsiCo transformed their demand forecasting system to handle 125 million weekly forecast combinations across 1.5 million demand forecasting units (DFUs) in the United States snacks business. The company partnered with Databricks to build an agentic AI-powered platform called PEP Planner that shifts from delivering forecasts to delivering actionable decisions. The system uses multiple AI agents for anomaly detection, causal reasoning, and incident triage, enabling demand planners and data scientists to identify forecast anomalies proactively and retrain models with contextual recommendations. The solution achieved over 80% accuracy (compared to a legacy system used for 10+ years), reduced costs by 50%, decreased compute costs by 60%, and doubled time-to-value by enabling market rollouts six months earlier than planned.

[Read source](https://www.youtube.com/watch?v=AFFgWW-oAI0)

---

#### Intelligent Model Routing for Cost Optimization and Operational Resilience

**Company:** digital_ocean  
**Industry:** Tech

Digital Ocean developed an inference routing system to address the escalating costs of LLM deployments where frontier models were being used unnecessarily for every task. The solution involves a purpose-built 30-billion parameter routing model that sits as a server-side proxy, intelligently directing requests to appropriate models based on task complexity, real-time latency, cost constraints, and availability metrics. Early customer results demonstrate 40-50% cost reductions with one legal AI startup, with potential savings of up to 80% for some workloads, while maintaining quality and actually reducing latency by approximately 67% compared to using frontier models exclusively.

[Read source](https://www.youtube.com/watch?v=LBQhRjc8qrI)

---

#### Agentic Video Editing with AI Agents and Code-Based Video Generation

**Company:** reelful  
**Industry:** Media & Entertainment

Reelful addresses the problem that video editing is tedious, time-consuming, and largely manual, preventing people from sharing the content they record. Their solution involves building an agentic video editing system where users upload their raw footage and photos along with simple context or directions, and AI agents automatically understand the media, select the best moments, assemble compositions, generate captions, music, voiceovers, and B-rolls to produce ready-to-share clips. The platform uses Remotion, an open-source framework for creating videos as React code, leveraging the fact that LLM agents excel at code generation. The system features a multi-stage pipeline including media understanding, creative planning, sandbox execution environments, skill-based agents, and verification layers. Results demonstrate fully automated video creation deployed in a mobile-first application with directional templates and a built-in editor for manual tweaks, recently funded by A16Z's Speed Run program.

[Read source](https://www.youtube.com/watch?v=pPj_tjlvYjA)

---

#### Multi-Agent Orchestration and Delegation Decisions in In-Car Voice Assistants

**Company:** bmw  
**Industry:** Automotive

BMW Research is developing a multi-agent in-car voice assistant system that faces the critical challenge of reliable agent orchestration and delegation decisions at runtime. The problem centers on determining which specialized agent should handle specific tasks in constantly changing contexts, where multiple agents may be capable of solving the same problem but with different tradeoffs in cost, latency, and user experience. The proposed solution emphasizes treating agent delegation as fundamentally different from simple tool selection, recognizing that agents can initiate autonomous loops and that multiple valid execution paths may exist for the same user request. Rather than forcing canonical ground truth labels, the approach advocates for context-aware delegation decisions and evaluation frameworks that assess not just task success but also the quality of the chosen path, including metrics around latency, cost, and human-machine collaboration.

[Read source](https://www.youtube.com/watch?v=H6E46K0WPWg)

---

### Cool Use Cases

#### Building Shared Memory for AI Agents with Notion-Backed Persistence

**Company:** notion  
**Industry:** Tech

Notion developed Lore, an open-source system for shared, persistent memory for AI agents, to address the problem of tribal knowledge and experiential learning being lost across agent sessions. The solution uses Notion as a backing store with five interconnected databases (Projects, Topics, Memories, Entities, Facts) that agents access through the Model Context Protocol (MCP), enabling both humans and agents to read and write organizational knowledge. Evaluation results showed 84% success in retrieval tasks using the SkillRet dataset, and a statistically significant performance lift in model-hard evaluations, with memory-enabled agents recovering approximately 46% of failures that no-memory agents couldn't solve, though the team emphasizes that memory quality and maintenance are critical to realizing these benefits.

[Read source](https://www.notion.com/blog/building-shared-memory-for-ai-agents-in-notion)

---

#### Building LLM-Powered Knowledge Management Systems for Personal Note-Taking

**Company:** warp  
**Industry:** Tech

This presentation addresses the challenge of managing disorganized personal notes and research materials by building an LLM-powered knowledge management system. The solution involves using voice transcription tools for rapid note capture, LLM agents to enrich and interconnect notes through automated tagging and backlinking, automated wiki generation to organize concepts and entities, and visualization tools to create graph views of knowledge connections. The system runs on scheduled automation in cloud environments, transforming raw markdown notes into an interconnected knowledge base that surfaces forgotten insights and makes personal research navigable through Wikipedia-style browsing of one's own thoughts.

[Read source](https://www.youtube.com/watch?v=I3bpdgFJCUY)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Training and Deploying Create 2: A Stylistically Diverse Image Foundation Model

**Company:** krea  
**Industry:** Media & Entertainment

Krea developed and open-sourced Create 2, an image foundation model designed to prioritize stylistic diversity and faster generation over the mode-collapsed outputs of competitors. The team addressed the challenge of creative professionals needing diverse visual exploration tools rather than consistently safe but homogeneous results. Their solution involved a comprehensive LLMOps pipeline including custom data curation with 30-40 in-house classifiers, multi-stage training from low to high resolution, vision-language model captioning, sparse autoencoder-based filtering, preference optimization, and reinforcement learning. The medium variant was successfully open-sourced and demonstrates strong world knowledge and stylistic range while maintaining fast iteration speeds for creative workflows.

[Read source](https://www.youtube.com/watch?v=-tviRdpmHvs)

---

#### Scaling Agentic AI Infrastructure for Production ML Workflows

**Company:** linkedin  
**Industry:** Tech

LinkedIn's AI platforms team developed an agentic platform to automate complex machine learning tasks including migrating 400+ TensorFlow models to PyTorch, optimizing cluster performance, and conducting autonomous research experiments. The platform uses code-based agents that run iterative experiments over hours or days, launching hundreds of jobs autonomously. To support this scale, LinkedIn built specialized infrastructure including a warm GPU pool with low-latency job launching, restricted execution environments for untrusted agent-generated code, and robust checkpointing systems. The implementation resulted in 100% growth in cluster experiments over six months, demonstrating the potential for agents to dramatically increase experimentation velocity and model improvement opportunities.

[Read source](https://www.youtube.com/watch?v=FJUrsZn1BSI)

---

#### Scaling Reinforcement Learning for AI Coding Agents

**Company:** cognition  
**Industry:** Tech

Cognition, the company behind Devin (the AI software engineer) and Windsurf, undertook an ambitious research program to build production-ready coding agents through increasingly complex reinforcement learning training runs. Starting with a modest 32 H200 GPUs and a small team, they progressed through four major projects: Kevin 32B for CUDA kernel optimization, Swee Grab for file search, and Sweep v1.6 and v1.7 for end-to-end software engineering tasks. The company tackled significant technical challenges including multi-turn agentic training, parallel tool calling, asynchronous RL for throughput optimization, and entropy collapse. Their latest model, Sweep 1.7, achieves frontier-level performance on benchmarks like SWE-bench Pro while being considerably smaller and cheaper than competing models, demonstrating that careful execution of RL techniques can squeeze exceptional performance from smaller models.

[Read source](https://www.youtube.com/watch?v=z--bPNOvoi0)

---

#### Memory Harnesses for Long-Running Research Agents on Local Models

**Company:** sakana  
**Industry:** Research & Academia

Sakana AI developed a memory harness system to address context degradation in long-horizon agentic tasks running on local models. The problem tackled was context rot, where models contradict themselves, forget completed tasks, or drift from original questions during extended operations. The solution involved designing a write-manage-read memory loop with different recall policies, tested on local models including Qwen 27B and DeepSeek V4 Flash running on Apple M3 Ultra hardware. Results showed that ranked recall policies outperformed baseline approaches on benchmarks like XBench, achieving better accuracy while reducing token costs, demonstrating that structured memory management is essential for cost-effective long-horizon agent performance on local infrastructure.

[Read source](https://www.youtube.com/watch?v=R3-anFK1YM8)

---

### Industry News

#### Building Scalable AI Agents for Go-to-Market Automation at Production Scale

**Company:** unify  
**Industry:** Tech

UniFi developed an AI agent platform that automates go-to-market research and outreach for sales teams, powering $900 million in pipeline. The company evolved from running millions of asynchronous web research agents to launching a chat-based interface where sales reps interact with agents that can write TypeScript code, manipulate tabular data, and orchestrate API calls. Through aggressive cost optimization including prompt caching strategies, reducing sub-agent usage, implementing efficient tool calling patterns, and moving from expensive sub-agent architectures to smarter main agents that write code, UniFi achieved a 90-95% cost reduction. The platform now enables individual sales reps to perform research and outreach tasks that previously required entire teams, while maintaining strong data tenancy, durability, and observability across cloud-based execution environments.

[Read source](https://www.youtube.com/watch?v=6898VdRtKDE)

---

#### Multi-Agent AI Platform for Streaming Media Analytics and Content Production

**Company:** mbc_shahid  
**Industry:** Media & Entertainment

MBC Shahid, the leading Arabic streaming platform in the MENA region with 35 million monthly active users, evolved from traditional BI dashboards to AI-powered data products through a three-season journey. The company built multiple production LLM applications using Databricks, including Enigma (a conversational analytics platform merging quantitative viewing data with qualitative sentiment from customer comments), interactive AI-generated dashboards via Genie, and Spectra Studio (an automated video processing system for generating short-form content, subtitles, and compliance checks). These applications process massive scale data including 2.5 billion viewing hours annually, handle multi-language Arabic dialects, and significantly reduce manual work like generating 50 daily shorts during Ramadan peak periods while maintaining human oversight for quality control.

[Read source](https://www.youtube.com/watch?v=cA_HTWEhTtM)

---

#### UK-Sovereign AI Platform with Self-Hosted LLMs and 50+ Specialized Agents

**Company:** oneadvanced  
**Industry:** Tech

OneAdvanced, a UK-based enterprise software provider serving over 10,000 customers in regulated industries including healthcare, legal, and public sector, needed to deploy AI capabilities while ensuring strict UK data sovereignty requirements. The company built a production AI solution by self-hosting Llama 4 Maverick and Llama Guard 4 models on Amazon SageMaker AI infrastructure in the London region, orchestrating over 50 specialized agents using Strands Agents SDK on Amazon ECS, and implementing a RAG pipeline backed by Amazon Aurora PostgreSQL with pgvector. The solution went from prototype to production through an AWS advisory engagement, deployed over 50 agents in three weeks, and has been serving customers in production since July 2025, achieving its performance targets while maintaining complete UK data residency and earning ISO 42001 certification for AI governance.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-oneadvanced-deployed-over-50-ai-agents-on-uk-sovereign-aws/)

---

#### Enterprise-Scale Agentic Engineering: Building LLM Infrastructure and Tooling for 250+ Engineering Teams

**Company:** zalando  
**Industry:** E-commerce

Zalando, a major e-commerce company, shares their 2.5-year journey implementing agentic engineering and LLMOps practices across 250+ engineering teams. The company built a comprehensive LLM infrastructure starting with a LiteLLM-based API proxy deployed in January 2024, complemented by chat UIs, CLI tools, and coding agents. They addressed challenges around vendor independence, model access, authentication, and governance while implementing risk-based PR approval systems and training programs. The initiative resulted in measurable impacts on PR throughput, code complexity patterns, and developer productivity, with 33% of PRs achieving low-risk auto-approval and significant reductions in PR lead time (20-40% for auto-approved changes).

[Read source](https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html)

---

#### Enterprise Sales Intelligence Agent: From Prototype to Production

**Company:** postman  
**Industry:** Tech

Postman developed an enterprise sales intelligence agent to address context loss and information handoff challenges across their sales organization, which relied on multiple disconnected systems throughout the sales lifecycle. Starting with a hackathon that produced numerous prototypes, they identified a win-loss analysis agent as most promising and evolved it through four architectural stages: a monolith agent with broad knowledge, domain-specific agents with hallucination controls, strategic content integration from sales teams, and finally role-based access controls. This iterative approach reduced agent development time from 30 hours to just hours, expanded usage organization-wide, and created compounding value by improving both the quality of sales discovery activities and the underlying agent performance through increased user engagement.

[Read source](https://www.youtube.com/watch?v=gjGAnb0if28)

---

#### Building Autonomous Software Factories with AI Agents

**Company:** factory  
**Industry:** Tech

Factory presents a vision for transforming software development through "software factories" - autonomous systems where signals like customer feedback, bugs, and business requirements flow directly to deployed code with minimal human intervention. The problem addressed is that while AI-powered coding tools have evolved from autocomplete to chatbots to agents, organizations haven't seen promised productivity gains because these tools only automate narrow slices of the development process while planning, triage, validation, and deployment remain human-driven bottlenecks. Factory's solution involves building model-independent, organization-owned agent platforms with shared agent cores that operate across all product and engineering workflows - from code review to incident response - with extensive governance controls, deterministic feedback loops, and continuous evaluation systems. The approach emphasizes preparing the engineering environment for agent readiness, implementing governance before scaling, and measuring outcomes like cycle time and bug rates rather than token usage.

[Read source](https://www.youtube.com/watch?v=Pa3MAnWeNB4)

---

#### Verifiable and Auditable AI Agent Payment Processing with Hardware Attestation

**Company:** solv_labs  
**Industry:** Tech

Solv Labs built an AI agent payment workflow on Amazon Bedrock AgentCore payments to address the enterprise challenge of proving that autonomous agent payments are authorized, risk-priced, and auditable. The solution combines AgentCore payments for payment processing, ORACLE (Solv's policy engine) for pre-authorization, ICME PreFlight for privacy-preserving compliance verification, and AWS Nitro Enclaves for hardware attestation. Each transaction completes in under four seconds and produces a complete audit trail with cryptographic proofs, hardware attestations, per-transaction risk pricing, and on-chain anchoring via Coinbase and Base blockchain. The system enables enterprises to deploy agent payments in regulated environments with verifiable governance at machine speed, scaling review effort with exceptions rather than transaction volume.

[Read source](https://aws.amazon.com/blogs/machine-learning/pay-with-confidence-how-solv-labs-built-verifiable-auditable-agent-payments-on-amazon-bedrock-agentcore-payments/)

---

#### Multi-Tenant AI Agent Deployment with Secure Isolation Using Amazon Bedrock AgentCore

**Company:** axonious  
**Industry:** Tech

Axonius, a cybersecurity asset intelligence platform serving hundreds of isolated customer environments, needed to add AI agents to their SaaS offering while maintaining strict tenant isolation and security requirements. They deployed a silo-model architecture using Amazon Bedrock AgentCore runtime, where each customer receives a dedicated agent with microVM-level session isolation. This approach integrated with their existing VPC-based tenant deployment model, using JWT-based authentication, IAM role tagging for cost allocation, Amazon Bedrock Knowledge Bases for RAG, and VPC Lattice for private networking. The solution reduced development time from an estimated eight weeks to 10 days—a 75% reduction in time-to-market—while maintaining the security-first architecture required for handling sensitive cybersecurity data across multiple enterprise customers.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-axonius-built-secure-multi-tenant-ai-agents-on-bedrock-agentcore/)

---

#### Practical Approaches to AI Agent Evaluation and Floor Raising in Production

**Company:** raindrop  
**Industry:** Tech

Raindrop's CTO presents practical lessons from observing real-world AI agent deployments across finance, healthcare, and defense sectors. The talk challenges conventional evaluation approaches inherited from the chatbot era, arguing that static benchmark-style evaluations don't scale for modern agentic systems. Instead, the company advocates for "raising the floor" by focusing on preventing critical failures rather than maximizing ceiling capabilities. Their solution involves production monitoring similar to Sentry, treating evaluations as code-based tests rather than cloud-managed prompts, and using deterministic signals to trigger agent-based investigation rather than asking agents to detect anomalies directly. The approach emphasizes understanding when issues started and how many users they affect, with different strategies for high-volume versus low-volume deployments.

[Read source](https://www.youtube.com/watch?v=jHMiYtjoJfA)

---

#### Building Context-Aware Consumer AI at Scale with Agentic Recommendations

**Company:** doordash  
**Industry:** E-commerce

DoorDash transformed their recommendation systems from legacy one-shot predictions to a sophisticated agentic platform to support multi-state shopping experiences like grocery planning. The company developed language-native consumer memory blocks to replace traditional embeddings, implemented semantic IDs (RQ-VAE) for granular catalog representation, built grounded search systems for intent understanding, and modernized ranking with LLM-generated relevance labels. These innovations enabled dramatic improvements across key metrics: 10% lift in mean reciprocal rank (MRR) from graph-based memory, 13% accuracy improvement on long-tail query intent, and 2.2% conversion rate increase from improved relevance. The system culminates in multi-turn agentic shopping assistants that leverage all these primitives, evaluated through comprehensive trajectory-based rubrics and agentic harness engineering.

[Read source](https://www.infoq.com/presentations/ai-agentic-recommendations-semantic-ids/)

---

#### Runtime Security and Governance Framework for AI Agents

**Company:** thales_group  
**Industry:** Tech

Thales Group developed a comprehensive security and governance framework to address the operational risks of autonomous AI agents in production environments. The problem centered on agents potentially exceeding their intended boundaries and performing unauthorized actions, particularly concerning given the complex interactions between users, agents, sub-agents, and downstream systems. Thales built a runtime trust plane that monitors and enforces controls across identity, delegation, policy, risk, and evidence layers. The solution creates a continuous record of trust, compares declared versus observed agent behavior to identify variance, and implements risk-based execution controls including quarantine, rollback, and kill switches. This approach enables real-time governance over dynamic control paths while maintaining observability and enforcing authorization boundaries across multi-agent workflows.

[Read source](https://www.youtube.com/watch?v=czfKC-p79tA)

---

#### Building Agent-First Data Infrastructure with Comprehensive Evaluation Frameworks

**Company:** bauplan  
**Industry:** Tech

Bauplan, a data infrastructure company built for agents as first-class users, developed a comprehensive evaluation framework for LLM coding agents working on data engineering tasks. The company created 700 evaluation tasks derived from real-world customer usage patterns, significantly more than competing frameworks from Supabase (20+ tasks) and Snowflake (100 tasks). By leveraging their Git-for-data architecture that enables deterministic verification of agent actions through API-first design and branch immutability, Bauplan optimized agent performance through automated skill improvement using the DSPy optimizer. Results showed that optimized skills improved performance across all models, and surprisingly, open-source models like DeepSeek could achieve results comparable to frontier models like Claude Opus at one-third the cost when working with properly designed agent-first infrastructure.

[Read source](https://www.youtube.com/watch?v=3JvR0Wb3XWg)

---

#### Securing AI Agents with Network-Level Proxy Controls for Production Infrastructure

**Company:** deno  
**Industry:** Tech

Deno faced the challenge of using AI agents powered by models like Claude Opus to automatically handle production incidents in their Deno Deploy hosting service, requiring agents to access critical systems like PostgreSQL, Kubernetes, ClickHouse, AWS, GitHub, and Slack with write permissions. While the agents proved capable of resolving many incidents that previously required human intervention, the company recognized that agents could not be trusted to police themselves due to risks like prompt injection attacks and unpredictable behavior. To address this, Deno developed Claw Patrol, an open-source network proxy that sits between agents and infrastructure, parsing every byte of network communication across multiple protocols including non-HTTP ones, enforcing granular permission rules defined in version-controlled configuration files, injecting credentials so agents never see secrets directly, and providing approval workflows and dashboards for monitoring agent actions in real-time.

[Read source](https://www.youtube.com/watch?v=MkRYPFIMCSA)

---

#### Autonomous Integration Factory Using LLM Agents

**Company:** ramp  
**Industry:** Finance

Ramp faced the classic engineering scaling problem where customer demand for integrations with third-party tools far exceeded their team's capacity to build and maintain them manually. To solve this, they built two complementary LLM-powered systems: a customer-facing agentic system that autonomously builds custom integrations on-demand within minutes based on natural language descriptions, and an internal "integration factory" that converts these custom integrations into production-grade first-party connectors. The solution has already shipped 75 integrations, reducing time-to-integration from weeks or months down to hours (for first-party) or minutes (for custom), while dramatically reducing cost and expanding coverage to nearly any integration customers need.

[Read source](https://builders.ramp.com/post/integrations-that-write-themselves)

---

#### Building an Evaluation-First Culture for Enterprise Agent Platform

**Company:** uber  
**Industry:** Tech

Uber's agent platform team faced a common challenge where development teams would ship LLM-powered agents to production and defer evaluation development until later, creating a cycle of retrofitting and debugging. To solve this, they built platform capabilities that made evaluations the default from day one, including automatic tracing across all environments, AI-generated starter evaluation kits delivered via Slack, and CLI-based tools that democratized eval ownership beyond engineering to product and customer teams. This shift from treating evals as a checkbox to an engine for continuous improvement enabled them to catch critical issues early, such as discovering that their voice booking agent had a 95% offline eval score but was misinterpreting background conversations in production, leading to fundamental changes in how the agent understood intent.

[Read source](https://www.youtube.com/watch?v=UTcKagbKp4A)

---

#### Scaling Demand Forecasting at Global Scale with Agentic AI

**Company:** pepsico  
**Industry:** Other

PepsiCo transformed their demand forecasting system to handle 125 million weekly forecast combinations across 1.5 million demand forecasting units (DFUs) in the United States snacks business. The company partnered with Databricks to build an agentic AI-powered platform called PEP Planner that shifts from delivering forecasts to delivering actionable decisions. The system uses multiple AI agents for anomaly detection, causal reasoning, and incident triage, enabling demand planners and data scientists to identify forecast anomalies proactively and retrain models with contextual recommendations. The solution achieved over 80% accuracy (compared to a legacy system used for 10+ years), reduced costs by 50%, decreased compute costs by 60%, and doubled time-to-value by enabling market rollouts six months earlier than planned.

[Read source](https://www.youtube.com/watch?v=AFFgWW-oAI0)

---

#### Intelligent Model Routing for Cost Optimization and Operational Resilience

**Company:** digital_ocean  
**Industry:** Tech

Digital Ocean developed an inference routing system to address the escalating costs of LLM deployments where frontier models were being used unnecessarily for every task. The solution involves a purpose-built 30-billion parameter routing model that sits as a server-side proxy, intelligently directing requests to appropriate models based on task complexity, real-time latency, cost constraints, and availability metrics. Early customer results demonstrate 40-50% cost reductions with one legal AI startup, with potential savings of up to 80% for some workloads, while maintaining quality and actually reducing latency by approximately 67% compared to using frontier models exclusively.

[Read source](https://www.youtube.com/watch?v=LBQhRjc8qrI)

---

#### Agentic Video Editing with AI Agents and Code-Based Video Generation

**Company:** reelful  
**Industry:** Media & Entertainment

Reelful addresses the problem that video editing is tedious, time-consuming, and largely manual, preventing people from sharing the content they record. Their solution involves building an agentic video editing system where users upload their raw footage and photos along with simple context or directions, and AI agents automatically understand the media, select the best moments, assemble compositions, generate captions, music, voiceovers, and B-rolls to produce ready-to-share clips. The platform uses Remotion, an open-source framework for creating videos as React code, leveraging the fact that LLM agents excel at code generation. The system features a multi-stage pipeline including media understanding, creative planning, sandbox execution environments, skill-based agents, and verification layers. Results demonstrate fully automated video creation deployed in a mobile-first application with directional templates and a built-in editor for manual tweaks, recently funded by A16Z's Speed Run program.

[Read source](https://www.youtube.com/watch?v=pPj_tjlvYjA)

---

#### Multi-Agent Orchestration and Delegation Decisions in In-Car Voice Assistants

**Company:** bmw  
**Industry:** Automotive

BMW Research is developing a multi-agent in-car voice assistant system that faces the critical challenge of reliable agent orchestration and delegation decisions at runtime. The problem centers on determining which specialized agent should handle specific tasks in constantly changing contexts, where multiple agents may be capable of solving the same problem but with different tradeoffs in cost, latency, and user experience. The proposed solution emphasizes treating agent delegation as fundamentally different from simple tool selection, recognizing that agents can initiate autonomous loops and that multiple valid execution paths may exist for the same user request. Rather than forcing canonical ground truth labels, the approach advocates for context-aware delegation decisions and evaluation frameworks that assess not just task success but also the quality of the chosen path, including metrics around latency, cost, and human-machine collaboration.

[Read source](https://www.youtube.com/watch?v=H6E46K0WPWg)

---

### Cool Use Cases

#### Building Shared Memory for AI Agents with Notion-Backed Persistence

**Company:** notion  
**Industry:** Tech

Notion developed Lore, an open-source system for shared, persistent memory for AI agents, to address the problem of tribal knowledge and experiential learning being lost across agent sessions. The solution uses Notion as a backing store with five interconnected databases (Projects, Topics, Memories, Entities, Facts) that agents access through the Model Context Protocol (MCP), enabling both humans and agents to read and write organizational knowledge. Evaluation results showed 84% success in retrieval tasks using the SkillRet dataset, and a statistically significant performance lift in model-hard evaluations, with memory-enabled agents recovering approximately 46% of failures that no-memory agents couldn't solve, though the team emphasizes that memory quality and maintenance are critical to realizing these benefits.

[Read source](https://www.notion.com/blog/building-shared-memory-for-ai-agents-in-notion)

---

#### Building LLM-Powered Knowledge Management Systems for Personal Note-Taking

**Company:** warp  
**Industry:** Tech

This presentation addresses the challenge of managing disorganized personal notes and research materials by building an LLM-powered knowledge management system. The solution involves using voice transcription tools for rapid note capture, LLM agents to enrich and interconnect notes through automated tagging and backlinking, automated wiki generation to organize concepts and entities, and visualization tools to create graph views of knowledge connections. The system runs on scheduled automation in cloud environments, transforming raw markdown notes into an interconnected knowledge base that surfaces forgotten insights and makes personal research navigable through Wikipedia-style browsing of one's own thoughts.

[Read source](https://www.youtube.com/watch?v=I3bpdgFJCUY)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

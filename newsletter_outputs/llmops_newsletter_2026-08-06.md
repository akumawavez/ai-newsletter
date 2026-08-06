# Weekly LLMOps Newsletter — 2026-08-06

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Training Specialized Legal AI Models with Synthetic Data and KV Cache Compaction

**Company:** harvey_/_baseten  
**Industry:** Legal

Harvey, a legal AI company, partnered with Baseten's training team to develop specialized models for legal tasks like due diligence data room analysis. The core challenge was that frontier models failed at exhaustive document review and struggled with context windows far smaller than typical legal data rooms (50-100 million tokens vs 250K-1M token limits). The solution involved training open-source models using synthetic legal data to ensure proper associate-level work patterns, exploring KV cache compaction strategies to handle massive context requirements, and developing specialized legal reasoning capabilities. This approach allows Harvey to offer both general-purpose frontier models for unstructured tasks and specialized models for high-value, structured legal workflows while maintaining cost efficiency and client data security.

[Read source](https://www.youtube.com/watch?v=TU8kwE7z1qY)

---

#### Building a Model Factory for Rapid Foundation Model Development

**Company:** poolside  
**Industry:** Tech

Poolside AI, a foundation model company focused on code generation, developed a comprehensive "Model Factory" system that enables them to train and deploy models from scratch to production in 5-8 weeks with a team of fewer than 70 researchers. Their approach treats model building as 90% engineering, emphasizing automation, reproducibility, and rapid experimentation (10,000-20,000 experiments per month). The result is the Laguna S model (118B parameters, 8B active), which demonstrates that smaller models with better behaviors—persistence, verification, and backtracking—can compete with models 10x their size, suggesting a path toward commoditized, open-weight foundation models.

[Read source](https://www.latent.space/p/poolside?utm_source=post-email-title&publication_id=1084089&post_id=208082176)

---

#### Scaling Model Training Through Recursive Self-Improvement and Agent-Driven Research Automation

**Company:** cursor_/_spacexai  
**Industry:** Tech

Cursor has developed a comprehensive approach to training large language models at scale, focusing on both outer and inner training loops to accelerate model improvement. The company moved from fine-tuning open-source models to conducting full pre-training from scratch, leveraging massive compute infrastructure from SpaceX's Colossus supercomputer. Their approach incorporates reinforcement learning at scale, private evaluation sets based on real-world software engineering tasks, novel learning methods like textual feedback coaching, and critically, a recursive self-improvement system where newer, smarter models train derivative models that improve subsequent training runs. This has enabled them to release models like Composer 2.5 that balance speed, intelligence, and cost-effectiveness while automating the research process through agent systems that allow researchers to launch and monitor training runs directly from Slack.

[Read source](https://www.youtube.com/watch?v=q4Tr-DknG2M)

---

#### Benchmarking Real-Time Voice Agents on Real-World Customer Service Tasks

**Company:** sierra  
**Industry:** Tech

Sierra developed τ-voice, the first benchmark to evaluate voice agents on both task completion accuracy and conversational dynamics under realistic audio conditions. The problem addressed is that existing benchmarks either measure conversational quality without verifying task success, or evaluate task completion in clean text environments without realistic audio challenges. Sierra's solution combines 278 customer service tasks from their text benchmark (τ-bench) with live simultaneous speech, realistic audio degradation (noise, compression, accents), and a sophisticated voice user simulator. Results show that voice agents have rapidly improved from 30% task completion (August 2025) to 67% (April 2026), with the best models now retaining 79% of text agent capability, though all providers still suffer degradation under realistic conditions including background noise, diverse accents, and interruptions.

[Read source](https://sierra.ai/blog/tau-voice-benchmarking-real-time-voice-agents-on-real-world-tasks)

---

#### Engineering the Software Factory: Why Model Training Limits Matter for Production Code Generation

**Company:** humanlayer  
**Industry:** Tech

This case study examines the challenges encountered by HumanLayer when attempting to deploy a "lights-off" software factory where AI coding agents generate production code without human review. The company discovered through their July 2025 experiment that while AI coding agents excel at creating new code, they systematically degrade codebase quality and maintainability over time due to fundamental model training limitations. The solution involved reverting to human-in-the-loop workflows with extensive upfront planning including product review, system architecture design, program design with call graphs, and vertical slicing to coordinate multi-repo implementations. This approach enabled faster development while maintaining code quality, leading to the development of HumanLayer's AI IDE and collaboration platform that implements these workflows.

[Read source](https://www.youtube.com/watch?v=Ib5GBkD555M)

---

#### Asynchronous Agents and Long-Horizon Task Execution at Scale

**Company:** anthropic  
**Industry:** Tech

Anthropic presents their approach to deploying long-horizon asynchronous AI agents capable of autonomous work spanning 12+ hours, a significant increase from the 10-20 minute task horizons of earlier models from 2024. The solution involves architectural innovations including decoupling the agent harness from execution environments, implementing verifier loops for self-correction, building sophisticated memory systems with both in-band and out-of-band consolidation, and creating organization-level harnesses that enable multiplayer agent experiences. These advances enable production deployment of agents through their Managed Agents API and products like Claude Tag, with demonstrated results on benchmarks like SWE-bench Meter showing frontier models achieving 12+ hour autonomous task completion and practical applications in code generation and ML research tasks.

[Read source](https://www.youtube.com/watch?v=9QebvrrY3KY)

---

#### Local Agentic AI for Accessible Mobile Gaming

**Company:** new_york_times  
**Industry:** Media & Entertainment

The New York Times explored experimental on-device agentic AI systems for mobile puzzle games to improve accessibility and gameplay while maintaining privacy and offline functionality. The team developed local language model agents that run entirely on mobile devices to solve games like Space Invaders and Mini Crosswords, and to provide real-time accessibility adaptations for players with diverse needs. By leveraging on-device models rather than cloud-based AI, they achieved lower latency, better privacy, offline capability, and personalized experiences, while addressing critical constraints around device memory, processing time (16ms frame budgets), and battery consumption. The work demonstrates how local agentic systems can dynamically adjust game interfaces and difficulty in real-time based on player behavior patterns like gaze tracking, tap accuracy, and navigation challenges.

[Read source](https://www.youtube.com/watch?v=418t26CVz-w)

---

### Industry News

#### Building Sustainable AI Products Through Model Agnosticism and Cost Optimization

**Company:** notion  
**Industry:** Tech

Notion faced the challenge of building AI-native products at scale while managing escalating token costs and avoiding vendor lock-in with frontier model providers. The company developed a comprehensive strategy centered on model agnosticism, implementing an "auto model" that handles 75% of traffic by intelligently routing requests between different models based on task complexity, cost, and latency requirements. By building multimodal model interoperability, leveraging open-weight models for appropriate tasks, using CPU-based workers for deterministic operations, and maintaining detailed evaluation frameworks for entire task trajectories rather than single API calls, Notion achieved sustainable AI economics while delivering state-of-the-art capabilities. This approach enabled them to launch collaborative multi-agent workflows where different AI providers work together in a shared document environment, resulting in significant productivity gains including over three minutes saved per task at scale.

[Read source](https://www.youtube.com/watch?v=-I5W5QVAT8E)

---

#### Benchmarking AI Agents on Real-World Knowledge Retrieval and Tool Use

**Company:** sierra  
**Industry:** Tech

Sierra introduced 𝜏-knowledge, a benchmark designed to evaluate AI agents on realistic customer service scenarios that require navigating large, messy knowledge bases while executing multi-step tool calls in live conversations. The benchmark extends Sierra's existing 𝜏-bench with a fintech-inspired domain featuring 698 documents across 21 product categories, where tasks require searching knowledge bases, reasoning over findings, and executing tool calls (averaging 18.6 documents and 9.5 tool calls per task). Initial results showed frontier models like GPT-5.2 achieving only 25.5% Pass^1 success rates in March 2026, improving to 37.4% with GPT-5.5 by May 2026, revealing significant gaps in production-ready agent capabilities and highlighting behavioral patterns that distinguish stronger agents, including continuous retrieval strategies, smarter search approaches, and better calibration on when to act.

[Read source](https://sierra.ai/blog/tau-knowledge)

---

#### Production AI Agents at Scale: Engineering Agentic AI for Software Development

**Company:** monday  
**Industry:** Tech

Monday.com built and deployed production AI agents ("AI Teammates") that function as autonomous software engineers within their existing engineering organization. Facing the challenge of scaling software development in a decade-old codebase serving millions of users, they created an agent system called Sphera that treats AI agents as teammates with identities, managers, and performance metrics. Built on Amazon Bedrock and AWS infrastructure, the system evolved from basic AI assistants to fully autonomous agents that can take tickets from backlogs, write code, and ship features to production. The results are significant: nine in ten engineers use AI coding tools monthly (up from roughly half a year earlier), per-engineer PR throughput increased by over 50%, and their most advanced agent (Morphex) achieves a 95% autonomous merge rate with revert rates in the low single digits.

[Read source](https://aws.amazon.com/blogs/machine-learning/ai-teammates-how-monday-com-runs-production-ai-agents-on-amazon-bedrock/)

---

#### Building a Memory Layer for Video Intelligence Systems

**Company:** twelve_labs  
**Industry:** Media & Entertainment

Twelve Labs, a Series B startup, addresses the fundamental limitation that most video AI systems lack true memory capabilities, treating videos as bags of frames rather than spatial-temporal volumes. The company built a production video intelligence infrastructure consisting of foundation models that preserve temporal, multimodal, and relational context across massive video corpora. Their solution includes semantic chunking, multimodal embeddings (Marengo encoder), a spatial-temporal context store, and a video-aware language model (Pegasus) exposed via API. The system enables applications across sports analysis, security surveillance, and advertising by shifting from simple clip retrieval to corpus-level memory and reasoning, supporting workflows that require understanding across years of footage and multiple camera perspectives.

[Read source](https://www.youtube.com/watch?v=mOf-PP4mVjA)

---

#### Agentic AI for SAP Digital Transformation on Amazon Bedrock AgentCore

**Company:** ktern_ai  
**Industry:** Consulting

KTern AI, an SAP digital transformation platform, faced challenges in building autonomous agents that could operate across long-running SAP transformation projects requiring persistent context, secure tool integration, multi-tenancy, dynamic scalability, and production-grade observability. The company migrated from a self-managed container stack to Amazon Bedrock AgentCore using the Strands Agents SDK, building over 20 specialized agents through configuration rather than custom orchestration code. This approach reduced agent development time by 85%, cut infrastructure costs by 70%, and reclaimed 480 engineering hours per month. In production, the agentic platform delivered 45% faster SAP project timelines, 60-70% reduction in discovery and assessment time, 90% autonomous identification of operational exceptions, and 82% first-pass success rate on automated test case generation.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-ktern-ai-built-agentic-ai-for-sap-on-amazon-bedrock-agentcore/)

---

#### Agentic Hiring System Reduces Time-to-Interview by 60% for Small Businesses

**Company:** linkedin  
**Industry:** HR

LinkedIn's hiring team built an AI-powered hiring agent using LangChain and LangGraph to address the challenge small businesses face with time-intensive candidate review processes, where hiring managers spend an average of 9.5 hours per week on recruitment tasks. The team evolved from static workflows to a sophisticated agentic system with a centralized LLM-powered planner operating on a plan-execute-replan pattern, supporting the full hiring lifecycle from job description generation to candidate sourcing, applicant evaluation, and AI-powered screening interviews. The solution achieved a 60% reduction in time to interview for small businesses while maintaining consistency and compliance through careful architecture decisions including context-driven human-in-the-loop mechanisms, deterministic output formatting, and integration with LinkedIn's existing infrastructure and LangSmith for observability.

[Read source](https://www.youtube.com/watch?v=LUemJGG2k4c)

---

#### Building Production-Ready Local AI Infrastructure at Scale

**Company:** nvidia_/_osmantic_/_roboflow,_exo_labs  
**Industry:** Tech

This panel discussion from the Local AI Summit explores the growing movement toward deploying large language models and AI systems locally rather than relying solely on cloud services. Industry leaders from NVIDIA, EXO Labs, Roboflow, and Osmantic discuss the challenges and opportunities of running frontier-level AI models on local hardware, from consumer devices to enterprise on-premises infrastructure. The discussion covers critical LLMOps topics including multi-model routing, model optimization, quantization techniques, specialized model deployment, and the importance of data sovereignty. Key achievements highlighted include 10x performance improvements on NVIDIA DGX Spark hardware, successful deployment of 500+ billion parameter models running at 30 tokens per second on local hardware, and the emergence of infrastructure that makes local AI accessible to mainstream users while maintaining control over data, compute, and model weights.

[Read source](https://www.youtube.com/watch?v=KB41dTlX1Uc)

---

#### Enterprise Knowledge Graph Platform for Agentic AI Retrieval

**Company:** gates_foundation  
**Industry:** Other

The Gates Foundation developed the Strategic Intelligence Platform (SIP), an enterprise-wide knowledge graph system designed to enable agentic AI retrieval across 25+ years of organizational data spanning over $7 billion in annual grant disbursements. The platform addresses the challenge of extracting data-driven insights from complex, siloed systems of record by creating a unified semantic graph layer that connects structured and unstructured data from across 2,000+ annual grants, 4,000 employees, and 100+ countries. The solution combines Neo4j graph database technology with Model Context Protocol (MCP) integration to enable AI agents to dynamically discover and reason across organizational structures at query time, serving users through existing interfaces like Claude and ChatGPT while maintaining the foundation's competitive advantage through deep modeling of internal processes and tacit knowledge.

[Read source](https://www.youtube.com/watch?v=jt1Pbr_n6oU)

---

#### Building an Internal Cloud Agent Platform to Scale Organizational Knowledge

**Company:** sierra  
**Industry:** Tech

Sierra built Pinecone, an internal cloud-based agent platform, to capture and scale the accumulated wisdom of its workforce across all departments. The problem was that productivity improvements and better workflows typically remained siloed with individual employees or teams, with no practical way to capture and distribute them company-wide. Pinecone enables every employee to create, organize, and automate agents that live in the cloud, with features like durable sessions, multiplayer collaboration, automated PR management, reusable skills, and intent-based routing. The results have been transformative: in the last month, 600 employees created over 75,000 sessions, 96% of engineering now uses Pinecone, 70% of PRs were opened through Pinecone, usage tripled monthly since April while costs fell, and the platform fundamentally changed how the company works.

[Read source](https://sierra.ai/blog/pinecone-harnessing-the-wisdom-of-the-workforce)

---

#### Building an MCP Gateway for Enterprise-Wide AI Agent Integration

**Company:** sierra  
**Industry:** Tech

Sierra built an internal MCP (Model Context Protocol) Gateway to connect AI agents across the company to dozens of enterprise systems and data sources. The challenge was creating a unified, secure integration layer that would provide agents with necessary context from Slack, GitHub, Salesforce, data warehouses, and other SaaS tools while preventing data misuse and ensuring proper permissioning. The solution involved building a centralized gateway with sophisticated access controls, audit logging, cross-customer protection mechanisms, and support for both human and service account identities. The result is a system now used by 89% of Sierra employees connecting to 45 different services, with two-thirds of ongoing commits coming from teams across the company rather than the original builders.

[Read source](https://sierra.ai/blog/building-sierras-mcp-gateway-an-engineering-iceberg)

---

#### Building an MCP Gateway for Internal Agent Access to SaaS and Data Systems

**Company:** sierra  
**Industry:** Tech

Sierra built an internal "MCP Gateway" service to provide their internal agents with safe and comprehensive access to the company's SaaS products and internal systems. The problem was that even the best AI models struggle without proper context about company data, teams, and projects. The solution was a gateway built on the Model Context Protocol (MCP) that grew from 1 service to 45 services over 13 weeks, incorporating sophisticated cross-customer data protection, tagging systems for sensitive information, multi-region support, and extensive tooling integrations. The results were impressive: 89% weekly company adoption, with 33 contributors and nearly two-thirds of commits coming from users outside the core team, creating a self-service system where employees could prompt agents to add the tools they needed.

[Read source](https://blog.persistent.info/2026/07/sierra-mcp-gateway-dev-diary.html?m=1)

---

#### Self-Optimizing Classification Loops with Domain Expertise and High-Signal Evaluation

**Company:** langfuse  
**Industry:** Tech

Langfuse, an open-source observability and evaluation platform for AI systems, conducted an experiment to understand how to build effective self-optimizing loops for AI applications by testing a minimal loop on a clear-cut classification task. The team used a single-label classification task on academic papers with GPT-4o mini as the agent and Claude Opus 4.8 as the optimizer, starting from a basic prompt and allowing the system to iteratively improve through error analysis. The experiment achieved a 15% accuracy improvement (from 68% to 83%) with most gains occurring in the first iteration, demonstrating that high-signal feedback (clear right/wrong evaluations) combined with sufficient training data enables effective auto-optimization, though the team emphasizes that most real-world applications require carefully designed domain-specific evaluators rather than generic metrics like correctness or helpfulness.

[Read source](https://www.youtube.com/watch?v=eAXxdtNlK04)

---

#### Building a Context Layer for Production AI Agents

**Company:** atlan  
**Industry:** Tech

Atlan, a company that helps organizations make AI understand their business, evolved from bootstrapping individual specialized agents to building a unified context layer architecture over an 18-month period. The initial approach of creating isolated agents for specific tasks faced challenges including context engineering overhead, agent silos, lack of shared learning, and context sprawl across different agent frameworks. The solution involved developing a centralized company brain or context layer that manages knowledge, skills, and business norms as version-controlled assets similar to code, enabling 300 skills and 40 agents to work cohesively. This approach addressed dependency management, quality ownership, security governance, and context portability while creating compounding learning loops from AI interactions.

[Read source](https://www.youtube.com/watch?v=8G_1-3IO4ZQ)

---

#### Execution Graph-Based Anomaly Detection and Automated Remediation in Payment Processing

**Company:** jp_morgan_chase  
**Industry:** Finance

JP Morgan Chase's payments team implemented an execution graph-based system to detect anomalies and drifts in their real-time payment processing infrastructure. The system represents request processing as directed acyclic graphs (DAGs), establishing baselines for normal behavior and using statistical methods to identify structural changes, scale deviations, and performance degradations. By leveraging OpenTelemetry for telemetry data collection and stream processing for analysis, the solution identifies where issues occur in multi-node service architectures and automates remediation actions based on drift categorization. The approach significantly reduced mean time to discovery by enabling real-time detection within single time windows rather than waiting for multiple monitoring periods, while minimizing false alarms through fine-tuned thresholds and client-specific baselines.

[Read source](https://www.youtube.com/watch?v=u1yaOeEX4e8)

---

### Cool Use Cases

#### Building a World Model for Contextual AI Understanding in Workplace Software

**Company:** monday  
**Industry:** Tech

Monday developed an AI assistant called Sidekick that shifts their platform from a system of record to a system of context, addressing the fundamental challenge that while agents have access to massive amounts of workplace data (tasks, emails, messages, meetings), they lack true understanding of how these elements connect and what users should prioritize. Their solution, called the Monday World Model, uses a dual-engine architecture inspired by neuroscience and data processing systems: a slow engine that learns user patterns, personas, and work rhythms over weeks to build a durable profile, and a fast engine that processes recent activity to generate live signals about current priorities and urgencies. This architecture enables the AI to understand user context offline and ahead of time rather than attempting to construct meaning at query time, resulting in an assistant that can proactively determine what users should focus on based on deep understanding of their work patterns and current state.

[Read source](https://www.youtube.com/watch?v=Btk8wDUVs74)

---

#### Scaling an AI Health Assistant from Launch to Production at Scale

**Company:** maven_clinic  
**Industry:** Healthcare

Maven Clinic deployed an AI agent called Maven Assistant to help users navigate women's and family health services, including finding providers, scheduling appointments, and answering health questions. Initially launched to 20% of active users in March 2026, the assistant has since scaled to 100% of users with 10x conversation volume growth over four months. The team addressed critical challenges including overly strict guardrails, model selection and upgrades from Gemini to GPT models, building robust evaluation systems with LLM-as-judge calibrated against human reviewers, and managing the complex interplay between administrative tools and health question answering. Key success metrics include less than 10% escalation rates and 90%+ agreement between automated judges and human evaluators, demonstrating that rapid iteration informed by production data is essential for building reliable customer-facing AI agents.

[Read source](https://www.youtube.com/watch?v=XnyzhRsig9I)

---

### Tools & Infrastructure

#### In-House LLM Serving Infrastructure at Scale

**Company:** netflix  
**Industry:** Media & Entertainment

Netflix built a comprehensive in-house LLM serving platform to run the full inference stack internally rather than relying on hosted APIs, addressing needs for low latency, deep customization, and integration with existing production infrastructure. The platform unified LLM serving with their existing Model Scoring Service (MSS), selecting vLLM as the inference engine and integrating it with NVIDIA Triton Inference Server, while exposing both gRPC and OpenAI-compatible HTTP APIs. Key challenges included engine version compatibility, constrained decoding at scale, and deployment strategies for GPU-based models. The solution enabled seamless experimentation-to-production workflows, handled diverse workloads including embeddings, prefill-only inference, autoregressive decoding, and custom constraint logic, with particular success in migrating from vLLM V0 to V1 to achieve batch-level constrained decoding that kept latency flat as batch sizes grew.

[Read source](https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Training Specialized Legal AI Models with Synthetic Data and KV Cache Compaction

**Company:** harvey_/_baseten  
**Industry:** Legal

Harvey, a legal AI company, partnered with Baseten's training team to develop specialized models for legal tasks like due diligence data room analysis. The core challenge was that frontier models failed at exhaustive document review and struggled with context windows far smaller than typical legal data rooms (50-100 million tokens vs 250K-1M token limits). The solution involved training open-source models using synthetic legal data to ensure proper associate-level work patterns, exploring KV cache compaction strategies to handle massive context requirements, and developing specialized legal reasoning capabilities. This approach allows Harvey to offer both general-purpose frontier models for unstructured tasks and specialized models for high-value, structured legal workflows while maintaining cost efficiency and client data security.

[Read source](https://www.youtube.com/watch?v=TU8kwE7z1qY)

---

#### Building a Model Factory for Rapid Foundation Model Development

**Company:** poolside  
**Industry:** Tech

Poolside AI, a foundation model company focused on code generation, developed a comprehensive "Model Factory" system that enables them to train and deploy models from scratch to production in 5-8 weeks with a team of fewer than 70 researchers. Their approach treats model building as 90% engineering, emphasizing automation, reproducibility, and rapid experimentation (10,000-20,000 experiments per month). The result is the Laguna S model (118B parameters, 8B active), which demonstrates that smaller models with better behaviors—persistence, verification, and backtracking—can compete with models 10x their size, suggesting a path toward commoditized, open-weight foundation models.

[Read source](https://www.latent.space/p/poolside?utm_source=post-email-title&publication_id=1084089&post_id=208082176)

---

#### Scaling Model Training Through Recursive Self-Improvement and Agent-Driven Research Automation

**Company:** cursor_/_spacexai  
**Industry:** Tech

Cursor has developed a comprehensive approach to training large language models at scale, focusing on both outer and inner training loops to accelerate model improvement. The company moved from fine-tuning open-source models to conducting full pre-training from scratch, leveraging massive compute infrastructure from SpaceX's Colossus supercomputer. Their approach incorporates reinforcement learning at scale, private evaluation sets based on real-world software engineering tasks, novel learning methods like textual feedback coaching, and critically, a recursive self-improvement system where newer, smarter models train derivative models that improve subsequent training runs. This has enabled them to release models like Composer 2.5 that balance speed, intelligence, and cost-effectiveness while automating the research process through agent systems that allow researchers to launch and monitor training runs directly from Slack.

[Read source](https://www.youtube.com/watch?v=q4Tr-DknG2M)

---

#### Benchmarking Real-Time Voice Agents on Real-World Customer Service Tasks

**Company:** sierra  
**Industry:** Tech

Sierra developed τ-voice, the first benchmark to evaluate voice agents on both task completion accuracy and conversational dynamics under realistic audio conditions. The problem addressed is that existing benchmarks either measure conversational quality without verifying task success, or evaluate task completion in clean text environments without realistic audio challenges. Sierra's solution combines 278 customer service tasks from their text benchmark (τ-bench) with live simultaneous speech, realistic audio degradation (noise, compression, accents), and a sophisticated voice user simulator. Results show that voice agents have rapidly improved from 30% task completion (August 2025) to 67% (April 2026), with the best models now retaining 79% of text agent capability, though all providers still suffer degradation under realistic conditions including background noise, diverse accents, and interruptions.

[Read source](https://sierra.ai/blog/tau-voice-benchmarking-real-time-voice-agents-on-real-world-tasks)

---

#### Engineering the Software Factory: Why Model Training Limits Matter for Production Code Generation

**Company:** humanlayer  
**Industry:** Tech

This case study examines the challenges encountered by HumanLayer when attempting to deploy a "lights-off" software factory where AI coding agents generate production code without human review. The company discovered through their July 2025 experiment that while AI coding agents excel at creating new code, they systematically degrade codebase quality and maintainability over time due to fundamental model training limitations. The solution involved reverting to human-in-the-loop workflows with extensive upfront planning including product review, system architecture design, program design with call graphs, and vertical slicing to coordinate multi-repo implementations. This approach enabled faster development while maintaining code quality, leading to the development of HumanLayer's AI IDE and collaboration platform that implements these workflows.

[Read source](https://www.youtube.com/watch?v=Ib5GBkD555M)

---

#### Asynchronous Agents and Long-Horizon Task Execution at Scale

**Company:** anthropic  
**Industry:** Tech

Anthropic presents their approach to deploying long-horizon asynchronous AI agents capable of autonomous work spanning 12+ hours, a significant increase from the 10-20 minute task horizons of earlier models from 2024. The solution involves architectural innovations including decoupling the agent harness from execution environments, implementing verifier loops for self-correction, building sophisticated memory systems with both in-band and out-of-band consolidation, and creating organization-level harnesses that enable multiplayer agent experiences. These advances enable production deployment of agents through their Managed Agents API and products like Claude Tag, with demonstrated results on benchmarks like SWE-bench Meter showing frontier models achieving 12+ hour autonomous task completion and practical applications in code generation and ML research tasks.

[Read source](https://www.youtube.com/watch?v=9QebvrrY3KY)

---

#### Local Agentic AI for Accessible Mobile Gaming

**Company:** new_york_times  
**Industry:** Media & Entertainment

The New York Times explored experimental on-device agentic AI systems for mobile puzzle games to improve accessibility and gameplay while maintaining privacy and offline functionality. The team developed local language model agents that run entirely on mobile devices to solve games like Space Invaders and Mini Crosswords, and to provide real-time accessibility adaptations for players with diverse needs. By leveraging on-device models rather than cloud-based AI, they achieved lower latency, better privacy, offline capability, and personalized experiences, while addressing critical constraints around device memory, processing time (16ms frame budgets), and battery consumption. The work demonstrates how local agentic systems can dynamically adjust game interfaces and difficulty in real-time based on player behavior patterns like gaze tracking, tap accuracy, and navigation challenges.

[Read source](https://www.youtube.com/watch?v=418t26CVz-w)

---

### Industry News

#### Building Sustainable AI Products Through Model Agnosticism and Cost Optimization

**Company:** notion  
**Industry:** Tech

Notion faced the challenge of building AI-native products at scale while managing escalating token costs and avoiding vendor lock-in with frontier model providers. The company developed a comprehensive strategy centered on model agnosticism, implementing an "auto model" that handles 75% of traffic by intelligently routing requests between different models based on task complexity, cost, and latency requirements. By building multimodal model interoperability, leveraging open-weight models for appropriate tasks, using CPU-based workers for deterministic operations, and maintaining detailed evaluation frameworks for entire task trajectories rather than single API calls, Notion achieved sustainable AI economics while delivering state-of-the-art capabilities. This approach enabled them to launch collaborative multi-agent workflows where different AI providers work together in a shared document environment, resulting in significant productivity gains including over three minutes saved per task at scale.

[Read source](https://www.youtube.com/watch?v=-I5W5QVAT8E)

---

#### Benchmarking AI Agents on Real-World Knowledge Retrieval and Tool Use

**Company:** sierra  
**Industry:** Tech

Sierra introduced 𝜏-knowledge, a benchmark designed to evaluate AI agents on realistic customer service scenarios that require navigating large, messy knowledge bases while executing multi-step tool calls in live conversations. The benchmark extends Sierra's existing 𝜏-bench with a fintech-inspired domain featuring 698 documents across 21 product categories, where tasks require searching knowledge bases, reasoning over findings, and executing tool calls (averaging 18.6 documents and 9.5 tool calls per task). Initial results showed frontier models like GPT-5.2 achieving only 25.5% Pass^1 success rates in March 2026, improving to 37.4% with GPT-5.5 by May 2026, revealing significant gaps in production-ready agent capabilities and highlighting behavioral patterns that distinguish stronger agents, including continuous retrieval strategies, smarter search approaches, and better calibration on when to act.

[Read source](https://sierra.ai/blog/tau-knowledge)

---

#### Production AI Agents at Scale: Engineering Agentic AI for Software Development

**Company:** monday  
**Industry:** Tech

Monday.com built and deployed production AI agents ("AI Teammates") that function as autonomous software engineers within their existing engineering organization. Facing the challenge of scaling software development in a decade-old codebase serving millions of users, they created an agent system called Sphera that treats AI agents as teammates with identities, managers, and performance metrics. Built on Amazon Bedrock and AWS infrastructure, the system evolved from basic AI assistants to fully autonomous agents that can take tickets from backlogs, write code, and ship features to production. The results are significant: nine in ten engineers use AI coding tools monthly (up from roughly half a year earlier), per-engineer PR throughput increased by over 50%, and their most advanced agent (Morphex) achieves a 95% autonomous merge rate with revert rates in the low single digits.

[Read source](https://aws.amazon.com/blogs/machine-learning/ai-teammates-how-monday-com-runs-production-ai-agents-on-amazon-bedrock/)

---

#### Building a Memory Layer for Video Intelligence Systems

**Company:** twelve_labs  
**Industry:** Media & Entertainment

Twelve Labs, a Series B startup, addresses the fundamental limitation that most video AI systems lack true memory capabilities, treating videos as bags of frames rather than spatial-temporal volumes. The company built a production video intelligence infrastructure consisting of foundation models that preserve temporal, multimodal, and relational context across massive video corpora. Their solution includes semantic chunking, multimodal embeddings (Marengo encoder), a spatial-temporal context store, and a video-aware language model (Pegasus) exposed via API. The system enables applications across sports analysis, security surveillance, and advertising by shifting from simple clip retrieval to corpus-level memory and reasoning, supporting workflows that require understanding across years of footage and multiple camera perspectives.

[Read source](https://www.youtube.com/watch?v=mOf-PP4mVjA)

---

#### Agentic AI for SAP Digital Transformation on Amazon Bedrock AgentCore

**Company:** ktern_ai  
**Industry:** Consulting

KTern AI, an SAP digital transformation platform, faced challenges in building autonomous agents that could operate across long-running SAP transformation projects requiring persistent context, secure tool integration, multi-tenancy, dynamic scalability, and production-grade observability. The company migrated from a self-managed container stack to Amazon Bedrock AgentCore using the Strands Agents SDK, building over 20 specialized agents through configuration rather than custom orchestration code. This approach reduced agent development time by 85%, cut infrastructure costs by 70%, and reclaimed 480 engineering hours per month. In production, the agentic platform delivered 45% faster SAP project timelines, 60-70% reduction in discovery and assessment time, 90% autonomous identification of operational exceptions, and 82% first-pass success rate on automated test case generation.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-ktern-ai-built-agentic-ai-for-sap-on-amazon-bedrock-agentcore/)

---

#### Agentic Hiring System Reduces Time-to-Interview by 60% for Small Businesses

**Company:** linkedin  
**Industry:** HR

LinkedIn's hiring team built an AI-powered hiring agent using LangChain and LangGraph to address the challenge small businesses face with time-intensive candidate review processes, where hiring managers spend an average of 9.5 hours per week on recruitment tasks. The team evolved from static workflows to a sophisticated agentic system with a centralized LLM-powered planner operating on a plan-execute-replan pattern, supporting the full hiring lifecycle from job description generation to candidate sourcing, applicant evaluation, and AI-powered screening interviews. The solution achieved a 60% reduction in time to interview for small businesses while maintaining consistency and compliance through careful architecture decisions including context-driven human-in-the-loop mechanisms, deterministic output formatting, and integration with LinkedIn's existing infrastructure and LangSmith for observability.

[Read source](https://www.youtube.com/watch?v=LUemJGG2k4c)

---

#### Building Production-Ready Local AI Infrastructure at Scale

**Company:** nvidia_/_osmantic_/_roboflow,_exo_labs  
**Industry:** Tech

This panel discussion from the Local AI Summit explores the growing movement toward deploying large language models and AI systems locally rather than relying solely on cloud services. Industry leaders from NVIDIA, EXO Labs, Roboflow, and Osmantic discuss the challenges and opportunities of running frontier-level AI models on local hardware, from consumer devices to enterprise on-premises infrastructure. The discussion covers critical LLMOps topics including multi-model routing, model optimization, quantization techniques, specialized model deployment, and the importance of data sovereignty. Key achievements highlighted include 10x performance improvements on NVIDIA DGX Spark hardware, successful deployment of 500+ billion parameter models running at 30 tokens per second on local hardware, and the emergence of infrastructure that makes local AI accessible to mainstream users while maintaining control over data, compute, and model weights.

[Read source](https://www.youtube.com/watch?v=KB41dTlX1Uc)

---

#### Enterprise Knowledge Graph Platform for Agentic AI Retrieval

**Company:** gates_foundation  
**Industry:** Other

The Gates Foundation developed the Strategic Intelligence Platform (SIP), an enterprise-wide knowledge graph system designed to enable agentic AI retrieval across 25+ years of organizational data spanning over $7 billion in annual grant disbursements. The platform addresses the challenge of extracting data-driven insights from complex, siloed systems of record by creating a unified semantic graph layer that connects structured and unstructured data from across 2,000+ annual grants, 4,000 employees, and 100+ countries. The solution combines Neo4j graph database technology with Model Context Protocol (MCP) integration to enable AI agents to dynamically discover and reason across organizational structures at query time, serving users through existing interfaces like Claude and ChatGPT while maintaining the foundation's competitive advantage through deep modeling of internal processes and tacit knowledge.

[Read source](https://www.youtube.com/watch?v=jt1Pbr_n6oU)

---

#### Building an Internal Cloud Agent Platform to Scale Organizational Knowledge

**Company:** sierra  
**Industry:** Tech

Sierra built Pinecone, an internal cloud-based agent platform, to capture and scale the accumulated wisdom of its workforce across all departments. The problem was that productivity improvements and better workflows typically remained siloed with individual employees or teams, with no practical way to capture and distribute them company-wide. Pinecone enables every employee to create, organize, and automate agents that live in the cloud, with features like durable sessions, multiplayer collaboration, automated PR management, reusable skills, and intent-based routing. The results have been transformative: in the last month, 600 employees created over 75,000 sessions, 96% of engineering now uses Pinecone, 70% of PRs were opened through Pinecone, usage tripled monthly since April while costs fell, and the platform fundamentally changed how the company works.

[Read source](https://sierra.ai/blog/pinecone-harnessing-the-wisdom-of-the-workforce)

---

#### Building an MCP Gateway for Enterprise-Wide AI Agent Integration

**Company:** sierra  
**Industry:** Tech

Sierra built an internal MCP (Model Context Protocol) Gateway to connect AI agents across the company to dozens of enterprise systems and data sources. The challenge was creating a unified, secure integration layer that would provide agents with necessary context from Slack, GitHub, Salesforce, data warehouses, and other SaaS tools while preventing data misuse and ensuring proper permissioning. The solution involved building a centralized gateway with sophisticated access controls, audit logging, cross-customer protection mechanisms, and support for both human and service account identities. The result is a system now used by 89% of Sierra employees connecting to 45 different services, with two-thirds of ongoing commits coming from teams across the company rather than the original builders.

[Read source](https://sierra.ai/blog/building-sierras-mcp-gateway-an-engineering-iceberg)

---

#### Building an MCP Gateway for Internal Agent Access to SaaS and Data Systems

**Company:** sierra  
**Industry:** Tech

Sierra built an internal "MCP Gateway" service to provide their internal agents with safe and comprehensive access to the company's SaaS products and internal systems. The problem was that even the best AI models struggle without proper context about company data, teams, and projects. The solution was a gateway built on the Model Context Protocol (MCP) that grew from 1 service to 45 services over 13 weeks, incorporating sophisticated cross-customer data protection, tagging systems for sensitive information, multi-region support, and extensive tooling integrations. The results were impressive: 89% weekly company adoption, with 33 contributors and nearly two-thirds of commits coming from users outside the core team, creating a self-service system where employees could prompt agents to add the tools they needed.

[Read source](https://blog.persistent.info/2026/07/sierra-mcp-gateway-dev-diary.html?m=1)

---

#### Self-Optimizing Classification Loops with Domain Expertise and High-Signal Evaluation

**Company:** langfuse  
**Industry:** Tech

Langfuse, an open-source observability and evaluation platform for AI systems, conducted an experiment to understand how to build effective self-optimizing loops for AI applications by testing a minimal loop on a clear-cut classification task. The team used a single-label classification task on academic papers with GPT-4o mini as the agent and Claude Opus 4.8 as the optimizer, starting from a basic prompt and allowing the system to iteratively improve through error analysis. The experiment achieved a 15% accuracy improvement (from 68% to 83%) with most gains occurring in the first iteration, demonstrating that high-signal feedback (clear right/wrong evaluations) combined with sufficient training data enables effective auto-optimization, though the team emphasizes that most real-world applications require carefully designed domain-specific evaluators rather than generic metrics like correctness or helpfulness.

[Read source](https://www.youtube.com/watch?v=eAXxdtNlK04)

---

#### Building a Context Layer for Production AI Agents

**Company:** atlan  
**Industry:** Tech

Atlan, a company that helps organizations make AI understand their business, evolved from bootstrapping individual specialized agents to building a unified context layer architecture over an 18-month period. The initial approach of creating isolated agents for specific tasks faced challenges including context engineering overhead, agent silos, lack of shared learning, and context sprawl across different agent frameworks. The solution involved developing a centralized company brain or context layer that manages knowledge, skills, and business norms as version-controlled assets similar to code, enabling 300 skills and 40 agents to work cohesively. This approach addressed dependency management, quality ownership, security governance, and context portability while creating compounding learning loops from AI interactions.

[Read source](https://www.youtube.com/watch?v=8G_1-3IO4ZQ)

---

#### Execution Graph-Based Anomaly Detection and Automated Remediation in Payment Processing

**Company:** jp_morgan_chase  
**Industry:** Finance

JP Morgan Chase's payments team implemented an execution graph-based system to detect anomalies and drifts in their real-time payment processing infrastructure. The system represents request processing as directed acyclic graphs (DAGs), establishing baselines for normal behavior and using statistical methods to identify structural changes, scale deviations, and performance degradations. By leveraging OpenTelemetry for telemetry data collection and stream processing for analysis, the solution identifies where issues occur in multi-node service architectures and automates remediation actions based on drift categorization. The approach significantly reduced mean time to discovery by enabling real-time detection within single time windows rather than waiting for multiple monitoring periods, while minimizing false alarms through fine-tuned thresholds and client-specific baselines.

[Read source](https://www.youtube.com/watch?v=u1yaOeEX4e8)

---

### Cool Use Cases

#### Building a World Model for Contextual AI Understanding in Workplace Software

**Company:** monday  
**Industry:** Tech

Monday developed an AI assistant called Sidekick that shifts their platform from a system of record to a system of context, addressing the fundamental challenge that while agents have access to massive amounts of workplace data (tasks, emails, messages, meetings), they lack true understanding of how these elements connect and what users should prioritize. Their solution, called the Monday World Model, uses a dual-engine architecture inspired by neuroscience and data processing systems: a slow engine that learns user patterns, personas, and work rhythms over weeks to build a durable profile, and a fast engine that processes recent activity to generate live signals about current priorities and urgencies. This architecture enables the AI to understand user context offline and ahead of time rather than attempting to construct meaning at query time, resulting in an assistant that can proactively determine what users should focus on based on deep understanding of their work patterns and current state.

[Read source](https://www.youtube.com/watch?v=Btk8wDUVs74)

---

#### Scaling an AI Health Assistant from Launch to Production at Scale

**Company:** maven_clinic  
**Industry:** Healthcare

Maven Clinic deployed an AI agent called Maven Assistant to help users navigate women's and family health services, including finding providers, scheduling appointments, and answering health questions. Initially launched to 20% of active users in March 2026, the assistant has since scaled to 100% of users with 10x conversation volume growth over four months. The team addressed critical challenges including overly strict guardrails, model selection and upgrades from Gemini to GPT models, building robust evaluation systems with LLM-as-judge calibrated against human reviewers, and managing the complex interplay between administrative tools and health question answering. Key success metrics include less than 10% escalation rates and 90%+ agreement between automated judges and human evaluators, demonstrating that rapid iteration informed by production data is essential for building reliable customer-facing AI agents.

[Read source](https://www.youtube.com/watch?v=XnyzhRsig9I)

---

### Tools & Infrastructure

#### In-House LLM Serving Infrastructure at Scale

**Company:** netflix  
**Industry:** Media & Entertainment

Netflix built a comprehensive in-house LLM serving platform to run the full inference stack internally rather than relying on hosted APIs, addressing needs for low latency, deep customization, and integration with existing production infrastructure. The platform unified LLM serving with their existing Model Scoring Service (MSS), selecting vLLM as the inference engine and integrating it with NVIDIA Triton Inference Server, while exposing both gRPC and OpenAI-compatible HTTP APIs. Key challenges included engine version compatibility, constrained decoding at scale, and deployment strategies for GPU-based models. The solution enabled seamless experimentation-to-production workflows, handled diverse workloads including embeddings, prefill-only inference, autoregressive decoding, and custom constraint logic, with particular success in migrating from vLLM V0 to V1 to achieve batch-level constrained decoding that kept latency flat as batch sizes grew.

[Read source](https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

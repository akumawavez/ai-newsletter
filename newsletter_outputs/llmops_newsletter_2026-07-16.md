# Weekly LLMOps Newsletter — 2026-07-16

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Forward-Deployed AI Engineering in UK Government Justice System

**Company:** uk_ministry_of_justice  
**Industry:** Government

The UK Ministry of Justice established the Justice AI Unit to address critical inefficiencies in the prison, probation, and court systems that were causing operational failures including erroneous prisoner releases. The unit adopted a forward-deployed engineering model where a lean team of approximately 40 engineers work directly on-site with prison officers, probation officers, and court staff to rapidly build and deploy AI-powered tools. By spending 2-3 days per week embedded with frontline staff, the team ships production-ready AI products in days to weeks rather than the typical years-long government procurement cycles. Key solutions include transcription services, CCTV analytics, automated assistance agents, and offline-capable tools designed to work within the constraints of legacy infrastructure, poor connectivity, and fragmented systems across England and Wales.

[Read source](https://www.youtube.com/watch?v=qlHaO6laBlM)

---

#### Building AI-Native Cloud Infrastructure for Elastic Inference and Agent Workloads

**Company:** modal  
**Industry:** Tech

Modal evolved from a serverless container platform into a comprehensive AI cloud infrastructure provider designed specifically for the bursty, compute-intensive workloads that characterize modern AI applications. Starting with custom model inference for companies like Suno, Runway, and robotics firms, Modal addressed the challenge of elastic GPU autoscaling across multiple regions and providers. The company has since expanded to support the full AI lifecycle including training, batch processing, sandboxes for agent workloads, and LLM inference with frontier-level performance optimizations. With their $355M Series C funding, Modal serves production AI applications that require specialized compute, rapid scaling, and the ability to handle everything from RL rollouts requiring 100,000 sandboxes to real-time audio-video streaming with regional routing.

[Read source](https://www.latent.space/p/modal2026)

---

### Industry News

#### Multi-Agent Orchestration for Enterprise Sales with Amazon Bedrock AgentCore

**Company:** aws  
**Industry:** Tech

AWS Sales faced an agent proliferation challenge with over 20 domain-specific AI agents deployed globally, forcing sales representatives to manually navigate between systems and manage context across fragmented conversations. To address this, AWS built Field Advisor on Amazon Bedrock AgentCore, creating a unified conversational interface that orchestrates specialized agents, maintains context, and handles human-in-the-loop workflows. The solution delivered measurable results including over 120K prompts processed, up to 2 hours saved per week per sales rep, 41% reduction in latency, and consolidation from seven AWS accounts to a single AgentCore Runtime.

[Read source](https://aws.amazon.com/blogs/machine-learning/powering-agentic-ai-sales-strategy-with-amazon-bedrock-agentcore/)

---

#### Conversational AI Shopping Assistant with Multi-Agent Architecture and Real-Time Grounding

**Company:** doordash  
**Industry:** E-commerce

DoorDash built a conversational AI shopping assistant called "Ask DoorDash" to help consumers discover restaurants and shop for groceries through natural language interactions. The system addresses the challenge of maintaining accurate grounding against rapidly changing local commerce data (menus, prices, inventory, ETAs) while providing personalized recommendations across multi-turn conversations. Using a multi-agent architecture built on Google's Agent Development Kit, the solution incorporates a three-layer memory system, real-time catalog integration through Model Context Protocol tools, and a comprehensive LLM-as-judge evaluation framework. Early production results show that approximately 70% of traffic is discovery-related, most sessions are multi-turn interactions, and the largest failure category is grounding errors, which the team addresses by routing all claims through tool calls to authoritative data sources.

[Read source](https://careersatdoordash.com/blog/building-doordash-assistant-an-engineering-overview/)

---

#### Healthcare Agentic AI Transformation: From Pilot to Production Scale

**Company:** davita_/_elevance_health_/_hca_healthcare_/_independence_blue_cross  
**Industry:** Healthcare

This panel discussion at Google Cloud Next features leaders from HCA Healthcare, Independence Blue Cross, Davita, and Elevance Health discussing their journeys from pilot projects to production-scale deployment of AI agents across healthcare operations. The organizations address common challenges including pilot purgatory, fragmented use cases, and change management while implementing AI solutions across clinical workflows, revenue cycle management, patient engagement, and administrative tasks. Key success factors identified include domain-based architectures, tight workflow integration, comprehensive governance frameworks, employee upskilling, and moving beyond pure financial ROI to measure patient outcomes and clinician productivity improvements.

[Read source](https://youtu.be/lm5mHq95Hbg)

---

#### Multi-Agent Skills Matching Platform for Construction Workforce

**Company:** burns_&_mcdonnel  
**Industry:** Consulting

Burns & McDonnell, a global architectural engineering and construction company, deployed a multi-agent system called "Experience IQ" to solve the challenge of matching employees with complex skill requirements across diverse projects and locations. Built using Google Cloud's Agent Development Kit (ADK) and deployed through Gemini Enterprise App, the system leverages historical data stored in Spanner, generates SQL queries from natural language, and uses multiple specialized agents with callbacks and routing logic to find qualified personnel. The solution successfully replaced tribal knowledge and disconnected systems with an automated, production-ready agent platform that pairs the right people with the right projects, improving project outcomes and client satisfaction.

[Read source](https://youtu.be/Req2PndZ7HM)

---

#### Production-Grade AI Agents for Financial Compliance Review Automation

**Company:** stripe  
**Industry:** Finance

Stripe, processing $1.4 trillion annually across 50 countries, faced a critical compliance scaling challenge where skilled analysts spent up to 80% of their time navigating fragmented systems rather than performing risk assessments. To address this, Stripe built a production-grade AI agent system on AWS using Amazon Bedrock, implementing a ReAct agent framework with human-in-the-loop oversight, task decomposition via directed acyclic graphs (DAG), and a dedicated agent service infrastructure distinct from traditional ML inference systems. The solution achieved a 26 percent reduction in median review handling time while maintaining over 96 percent helpfulness ratings from reviewers, with human experts retaining final decision authority and full audit trails for regulatory compliance.

[Read source](https://aws.amazon.com/blogs/machine-learning/production-grade-ai-agents-for-financial-compliance-lessons-from-stripe/)

---

#### Rethinking Insurance with AI: Operational Deployment Strategies for Brokers, Carriers, and Advisors

**Company:** deloitte  
**Industry:** Insurance

This panel discussion features insurance technology leaders from Baldwin Group, Ameriprise Financial (RiverSource), and Hudson Insurance discussing how they are deploying AI and LLM-based solutions into production workflows. The discussion covers the challenges of moving from AI experimentation to production adoption, including the need to embed AI directly into business workflows, the importance of business-led rather than technology-led initiatives, and the critical role of data foundations and architecture. Key results mentioned include reducing product rollout times from 3-6 months to 3 days at Baldwin Group, and plans to roll out enterprise-wide AI capabilities through partnerships with hyperscalers like Anthropic while maintaining appropriate governance and guardrails.

[Read source](https://www.youtube.com/watch?v=8THW-2PpwnY)

---

#### AI-Powered Conversational Business Intelligence Assistant for Enterprise Leadership

**Company:** aws  
**Industry:** Tech

AWS SMGS faced significant business intelligence challenges including time-intensive manual data preparation, fragmented data across multiple systems, and limited dashboard accessibility that delayed critical leadership decisions. To address these issues, they built NarrateAI, an AI-powered conversational assistant using Amazon Bedrock AgentCore that delivers on-demand business insights through natural language. The solution employs a two-layer architecture combining batch narrative generation with real-time multi-agent orchestration, powered by Anthropic's Claude Sonnet 4. Since deployment, NarrateAI has served over 4,000 active users across AWS leadership, reducing business review preparation time from hours to minutes while maintaining comprehensive data accuracy and row-level security through persona-based narrative isolation.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-aws-smgs-uses-an-ai-powered-conversational-assistant-to-transform-business-management-with-amazon-bedrock-agentcore/)

---

#### Purpose-Built AI Agent Hierarchies for GPU Infrastructure Reliability

**Company:** nvidia  
**Industry:** Tech

NVIDIA's Applied AI Lab for DGX Cloud developed LLo11yPop, a hierarchical agent system for managing large-scale GPU infrastructure. The problem involved monitoring and optimizing hundreds of GPU clusters with complex failure modes, resource allocation constraints, and the need for proactive incident detection. The solution employed a multi-tier agent architecture with specialized worker agents for data retrieval, analyst agents for reasoning, orchestrator agents for coordination, and tool agents for actions. By constraining individual agents to specific tasks and using deterministic fallbacks where needed, the system achieved production-grade reliability for GPU fleet management. The architecture demonstrated that balancing agentic discovery with deterministic tools, coupled with comprehensive evaluation strategies and rare context integration, enables scalable AI operations in high-stakes environments.

[Read source](https://www.infoq.com/presentations/reliable-ai-platforms)

---

#### Infrastructure Challenges in Production AI: Multi-Company Panel on Scaling, Cost, and Governance

**Company:** forge_/_cockroach_labs_/_doubleword_/_mesa  
**Industry:** Tech

This panel discussion from InfoQ Live brings together infrastructure experts from Forge, Cockroach Labs, Doubleword, and MESA to address the operational challenges of running AI systems at scale. The problem identified is that while building AI models has become relatively straightforward, maintaining production databases and infrastructure under constant AI-driven pressure has emerged as the critical bottleneck. The experts discuss solutions including distributed SQL databases, inference optimization, governance frameworks, and architectural evolution strategies. Key insights reveal that token costs are scaling 100x year-over-year rather than the predicted 10x, database layers have become the control plane for agentic AI, and traditional capacity planning approaches are obsolete in favor of bounded elasticity with guardrails.

[Read source](https://www.infoq.com/presentations/ai-infrastructure-scaling-architecture/)

---

#### Building Production-Grade Customer Experience Agents at Enterprise Scale

**Company:** sierra  
**Industry:** Tech

Sierra has built a comprehensive platform for deploying customer experience agents across sales, service, and loyalty touchpoints for Fortune 20 companies. The platform addresses the challenge of building reliable, low-latency conversational AI at enterprise scale by developing a modular architecture that orchestrates 10-15 different models per conversation turn, supports voice and multimodal experiences with sub-2-second latency requirements, and implements outcome-based pricing models tied to business results like sales conversions and customer satisfaction. Sierra serves most of the Fortune 20, handling use cases from airline booking and flight disruptions to retail product discovery and payment processing, with agents operating across 60+ languages and processing conversation volumes that would represent billions of annual interactions.

[Read source](https://www.youtube.com/watch?v=uCKhOmth2ms)

---

#### AI-Powered Consumer Feedback Analysis at Scale for Product Safety and Quality

**Company:** mattel  
**Industry:** Other

Mattel, a global toy manufacturer with $5.5 billion in annual revenue and operations across 100+ manufacturing sites, faced a critical scaling challenge in analyzing consumer feedback for product safety and quality decisions. Their teams were manually reviewing millions of consumer signals including reviews, service transcripts, and social media feedback using spreadsheets and handwritten tally sheets, a process that took days to months per analysis. Working with Insight and Google Cloud, Mattel built a production AI system using Gemini and Vertex AI that automatically classifies and analyzes consumer feedback in real-time. The system integrates directly into their Jira workflow, automatically surfaces classified sentiment data when tickets are created, and reduces analysis time from months to minutes. This transformation enabled proactive quality management, informed major product innovations including the Speed Snap track system (the most significant Hot Wheels track improvement in 50 years), and established a governed, enterprise-grade AI foundation that the organization is expanding across 68 identified AI projects.

[Read source](https://www.youtube.com/watch?v=2swzoVYU_iQ&list=PLFZU5nT4APFA&index=147)

---

#### Scaling LLM Inference with Multi-Accelerator Strategy for Recommendations and Safety

**Company:** spotify  
**Industry:** Media & Entertainment

Spotify faced exponentially growing compute demands from deploying LLMs across recommendation systems and content safety at global scale, serving 700 million users. The company implemented a multi-accelerator strategy using both GPUs and TPUs through a shared resource pool, leveraging open-source inference engines (vLLM and SGLang) to enable seamless hardware switching. By adopting Google Cloud's TPUs alongside their existing GPU fleet and fine-tuning open-weight models like Gemma on Spotify-specific data, they achieved 30-40% cost savings on certain workloads while maintaining latency targets, allowing continuous innovation in AI features like AI DJ and multilingual safety moderation without being constrained by accelerator availability.

[Read source](https://youtu.be/WbMlr83CYDA)

---

#### Multimodal AI at Scale: Voice, Video, and Visual Generation for E-commerce and Enterprise Communication

**Company:** heygen_/_elevenlabs_/_photogen  
**Industry:** Tech

This panel discussion features three AI companies operating multimodal production systems at massive scale: PhotoRoom (20 million users processing 10 billion e-commerce images annually), ElevenLabs (voice AI serving major enterprises and creative studios), and HeyGen (40 million users generating 100+ million minutes of video). Each company addresses distinct production challenges: PhotoRoom ensures product fidelity for e-commerce imagery across 180 countries, ElevenLabs balances voice quality with sub-second latency for conversational agents, and HeyGen pioneered code-to-video generation for communication workflows. All three leverage Google's Gemini models alongside proprietary frontier models, employing sophisticated model orchestration, evaluation frameworks, and vertical specialization to maintain quality, cost-efficiency, and trust at global scale.

[Read source](https://www.youtube.com/watch?v=WgMx66iImXI&list=PLFZU5nT4APFA&index=56)

---

#### CPU-Based Infrastructure for AI Inference and Agentic Workflows

**Company:** resemble_ai_/_turpopuffer  
**Industry:** Tech

This case study explores how Turpopuffer and Resemble AI architect their AI infrastructure to optimize for inference and agentic workflows on Google Cloud Platform. Turpopuffer built a search engine enabling models to attend to trillions of tokens by caching data from object storage to NVMe and DRAM, serving customers like Cursor and Notion with billions of documents. Resemble AI developed foundation models for generative voice AI and deepfake detection, strategically distributing workloads between GPUs for low-latency inference and CPUs for data processing, batch operations, and model distillation. Both companies demonstrate significant cost savings and performance improvements by auditing their AI stacks and identifying which workloads benefit from CPU-based infrastructure versus accelerators, achieving up to 30% better price performance with specific VM configurations.

[Read source](https://www.youtube.com/watch?v=x3LntcL1ffs&list=PLFZU5nT4APFA&index=47)

---

#### Autonomous SRE Agent System for Large-Scale Incident Management

**Company:** paypal  
**Industry:** Finance

PayPal faced significant challenges managing reliability across 3,000 microservices processing $5 million per minute, with SRE teams overwhelmed by manual incident response work where 70% of effort went to data collection and correlation. The company developed an autonomous SRE agent system using Google Cloud's Vertex AI and Agent Development Kit (ADK) that orchestrates multiple specialized agents to detect, triage, mitigate, and report incidents in parallel rather than sequentially. The solution integrated with PayPal's diverse data sources through a unified MCP tools layer and was deployed into production in two to three weeks with 40-50% less code than alternative frameworks, reducing development time by 60-70% while providing built-in governance, observability, and the ability to evaluate and swap models without code changes.

[Read source](https://youtu.be/8tB01DYGMAs)

---

#### Scaling Agentic AI for Fleet Management Insights to 100,000 Users

**Company:** verizon_connect  
**Industry:** Telecommunications

Verizon Connect faced the challenge of transforming overwhelming fleet data—over 500 million data points daily from 1.2 million vehicle subscriptions across 80,000 indicators—into actionable insights for fleet managers. Rather than building static dashboards or rule-based systems, they deployed an agentic AI solution on AWS that combines serverless statistical anomaly detection with dynamic LLM-based investigation. The system uses AWS Lambda, Step Functions, Amazon Bedrock (with Claude and Amazon Nova models), and Strands Agents to automatically detect anomalies, investigate root causes through autonomous tool-calling, and generate natural language insights. Deployed in November 2025, the solution now delivers daily insights to 100,000 users, helping fleet managers identify safety patterns, operational inefficiencies, and maintenance needs proactively rather than reactively.

[Read source](https://aws.amazon.com/blogs/machine-learning/from-data-overload-to-actionable-insights-how-verizon-connect-scaled-agentic-ai-to-100000-users/)

---

#### Deterministic Verification Layer for AI Coding Agents

**Company:** checkout  
**Industry:** Tech

A developer at Checkout encountered reliability issues with AI coding agents like Claude, where tasks appeared completed but contained subtle failures requiring manual intervention. To address this, they built Vector, a deterministic verification system that uses hooks to automatically check agent outputs against predefined test cases before accepting completion. The solution evolved from a company-specific tool into a language-agnostic pattern applicable across industries, demonstrating that verification design rather than code generation is becoming the critical value proposition in AI-assisted development. This approach enables the use of smaller, less expensive models while maintaining output quality through comprehensive guardrails.

[Read source](https://www.youtube.com/watch?v=MpZzWMdmQCE)

---

#### Agent Reinforcement Fine-Tuning for Production AI Agents

**Company:** openai  
**Industry:** Tech

OpenAI presented Agent RFT (Agent Reinforcement Fine-Tuning), a platform that enables organizations to fine-tune reasoning models to improve agentic behavior through real-time tool interactions and custom reward signals. The platform addresses the challenge of training AI agents that need to interact with external tools and environments during production workflows, moving beyond traditional supervised fine-tuning approaches. Multiple enterprise customers across coding, healthcare, and finance domains demonstrated significant improvements, including reduced tool call latency (up to 18% faster), elimination of long-tail loops (from 100+ messages to tight clusters), and substantial accuracy gains (5-23% improvements) while maintaining or reducing resource consumption through reinforcement learning-based credit assignment.

[Read source](https://www.infoq.com/presentations/rft-openai-model/)

---

#### AI-Led Restaurant Metadata Platform with LLM Juries and Context Optimization

**Company:** doordash  
**Industry:** E-commerce

DoorDash built an AI-led restaurant metadata platform to address the challenge of generating reliable, structured metadata for millions of diverse menu items at scale. The problem stemmed from food being deeply contextual, culturally rich, and highly non-standardized, making traditional approaches impractical. Their solution employed multimodal LLMs with several key innovations: an LLM jury system for automated evaluation that increased accuracy by 20% over human reviewers, reinforcement learning-inspired context optimization agents that improved precision by over 20% and accelerated prompt development tenfold, distributed computing infrastructure that reduced backfill time from over a month to just days, and AI-led annotation that enabled fine-tuned models achieving frontier LLM quality at 10% of the inference cost. The resulting metadata platform powers customer search, personalization, filtering, and analytics across the DoorDash platform while demonstrating that generative AI can be deployed reliably and cost-effectively at high volume.

[Read source](https://careersatdoordash.com/blog/building-food-metadata-with-llm-juries-context-optimization-multimodal-ai/)

---

### Cool Use Cases

#### Building Production-Scale Voice and Multi-Modal Customer Experience Agents

**Company:** sierra  
**Industry:** Tech

Sierra has built an enterprise agent platform serving most of the Fortune 20 companies, focusing on customer experience across sales, service, and loyalty touchpoints. The platform addresses the challenge of building reliable, low-latency conversational agents that can handle complex customer interactions across voice and chat modalities in dozens of languages. Sierra's approach combines a constellation of 10-15 models per conversation turn, custom infrastructure for sensitive operations like payments (achieving PCI DSS level one certification), and a no-code journey builder that compiles to their Agent SDK. The company has achieved notable success with outcome-based pricing models where agents earn commissions on sales, demonstrating measurable business value through improved resolution rates, conversion rates, and customer satisfaction metrics across retail, airline, and other enterprise verticals.

[Read source](https://www.youtube.com/watch?v=uCKhOmth2ms)

---

#### Agent Memory System for Personalized Food Ordering and Discovery

**Company:** doordash  
**Industry:** E-commerce

DoorDash built an agent memory system to power their Ask DoorDash conversational ordering experience, addressing the challenge of enabling AI agents to maintain persistent, structured understanding of user preferences across sessions. The solution connects their long-term memory platform with live agents through a three-layer architecture: offline memory generation that distills behavioral history into structured blocks, a distributed storage layer with vector search capabilities, and a tooling orchestration layer that handles task-aware retrieval, conversational memory extraction, and context engineering. Early production data showed grocery agent sessions backed by memory converted to checkout at ~24% higher relative rates, restaurant queries converted at ~15% higher rates, and sessions were ~33% less likely to misunderstand user intent compared to baseline sessions without computed memory.

[Read source](https://careersatdoordash.com/blog/building-ask-doordash-part-two-intelligence/)

---

### Tools & Infrastructure

#### Production-Ready AI Agents for Automated User Story Generation in Financial Services

**Company:** ford  
**Industry:** Automotive

Ford Credit, the financial services arm of Ford Motor Company, deployed production-ready AI agents to automate the conversion of product requirements in Confluence into technical user stories. The problem addressed was the "blank page problem" where product managers had to manually translate high-level requirements into detailed technical user stories, leading to high cognitive load, variance in quality, and capacity drain. The solution involved building a user story agent using Google Cloud's Agent Development Kit and platform infrastructure, with extensive architectural controls including prompt injection defense, circuit breakers, rate limiting, human-in-the-loop gates, end-to-end telemetry, and rigorous evaluation frameworks. The results showed 24% improvement in user story fidelity, 40% faster story creation cycles, and significantly improved consistency, enabling better downstream automation and faster product execution.

[Read source](https://www.youtube.com/watch?v=Mq4ZY3eE5dI&list=PLFZU5nT4APFA&index=15)

---

#### AI-Powered Document Fraud Detection with Multi-Model Agentic System

**Company:** inscribe  
**Industry:** Finance

Inscribe, a document fraud detection company serving financial institutions, faced the challenge of detecting sophisticated AI-generated forgeries and tampered documents at scale, where manual review took 30 minutes per application and couldn't keep pace with evolving fraud tactics. They developed an agentic AI system using Amazon Bedrock that coordinates multiple foundation models—Claude Haiku for high-volume parsing, Llama models for transaction analysis, and Claude Sonnet for complex cross-document reasoning—alongside proprietary ML models on Amazon SageMaker for forensic analysis. The solution reduced review time from 30 minutes to under 90 seconds (20x improvement) while maintaining regulatory compliance, with customers reporting millions in fraud losses prevented, up to 99% reduction in manual review time, and the ability to detect coordinated fraud rings that manual processes missed.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-inscribe-uses-amazon-bedrock-to-stop-document-fraud-in-seconds/)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Forward-Deployed AI Engineering in UK Government Justice System

**Company:** uk_ministry_of_justice  
**Industry:** Government

The UK Ministry of Justice established the Justice AI Unit to address critical inefficiencies in the prison, probation, and court systems that were causing operational failures including erroneous prisoner releases. The unit adopted a forward-deployed engineering model where a lean team of approximately 40 engineers work directly on-site with prison officers, probation officers, and court staff to rapidly build and deploy AI-powered tools. By spending 2-3 days per week embedded with frontline staff, the team ships production-ready AI products in days to weeks rather than the typical years-long government procurement cycles. Key solutions include transcription services, CCTV analytics, automated assistance agents, and offline-capable tools designed to work within the constraints of legacy infrastructure, poor connectivity, and fragmented systems across England and Wales.

[Read source](https://www.youtube.com/watch?v=qlHaO6laBlM)

---

#### Building AI-Native Cloud Infrastructure for Elastic Inference and Agent Workloads

**Company:** modal  
**Industry:** Tech

Modal evolved from a serverless container platform into a comprehensive AI cloud infrastructure provider designed specifically for the bursty, compute-intensive workloads that characterize modern AI applications. Starting with custom model inference for companies like Suno, Runway, and robotics firms, Modal addressed the challenge of elastic GPU autoscaling across multiple regions and providers. The company has since expanded to support the full AI lifecycle including training, batch processing, sandboxes for agent workloads, and LLM inference with frontier-level performance optimizations. With their $355M Series C funding, Modal serves production AI applications that require specialized compute, rapid scaling, and the ability to handle everything from RL rollouts requiring 100,000 sandboxes to real-time audio-video streaming with regional routing.

[Read source](https://www.latent.space/p/modal2026)

---

### Industry News

#### Multi-Agent Orchestration for Enterprise Sales with Amazon Bedrock AgentCore

**Company:** aws  
**Industry:** Tech

AWS Sales faced an agent proliferation challenge with over 20 domain-specific AI agents deployed globally, forcing sales representatives to manually navigate between systems and manage context across fragmented conversations. To address this, AWS built Field Advisor on Amazon Bedrock AgentCore, creating a unified conversational interface that orchestrates specialized agents, maintains context, and handles human-in-the-loop workflows. The solution delivered measurable results including over 120K prompts processed, up to 2 hours saved per week per sales rep, 41% reduction in latency, and consolidation from seven AWS accounts to a single AgentCore Runtime.

[Read source](https://aws.amazon.com/blogs/machine-learning/powering-agentic-ai-sales-strategy-with-amazon-bedrock-agentcore/)

---

#### Conversational AI Shopping Assistant with Multi-Agent Architecture and Real-Time Grounding

**Company:** doordash  
**Industry:** E-commerce

DoorDash built a conversational AI shopping assistant called "Ask DoorDash" to help consumers discover restaurants and shop for groceries through natural language interactions. The system addresses the challenge of maintaining accurate grounding against rapidly changing local commerce data (menus, prices, inventory, ETAs) while providing personalized recommendations across multi-turn conversations. Using a multi-agent architecture built on Google's Agent Development Kit, the solution incorporates a three-layer memory system, real-time catalog integration through Model Context Protocol tools, and a comprehensive LLM-as-judge evaluation framework. Early production results show that approximately 70% of traffic is discovery-related, most sessions are multi-turn interactions, and the largest failure category is grounding errors, which the team addresses by routing all claims through tool calls to authoritative data sources.

[Read source](https://careersatdoordash.com/blog/building-doordash-assistant-an-engineering-overview/)

---

#### Healthcare Agentic AI Transformation: From Pilot to Production Scale

**Company:** davita_/_elevance_health_/_hca_healthcare_/_independence_blue_cross  
**Industry:** Healthcare

This panel discussion at Google Cloud Next features leaders from HCA Healthcare, Independence Blue Cross, Davita, and Elevance Health discussing their journeys from pilot projects to production-scale deployment of AI agents across healthcare operations. The organizations address common challenges including pilot purgatory, fragmented use cases, and change management while implementing AI solutions across clinical workflows, revenue cycle management, patient engagement, and administrative tasks. Key success factors identified include domain-based architectures, tight workflow integration, comprehensive governance frameworks, employee upskilling, and moving beyond pure financial ROI to measure patient outcomes and clinician productivity improvements.

[Read source](https://youtu.be/lm5mHq95Hbg)

---

#### Multi-Agent Skills Matching Platform for Construction Workforce

**Company:** burns_&_mcdonnel  
**Industry:** Consulting

Burns & McDonnell, a global architectural engineering and construction company, deployed a multi-agent system called "Experience IQ" to solve the challenge of matching employees with complex skill requirements across diverse projects and locations. Built using Google Cloud's Agent Development Kit (ADK) and deployed through Gemini Enterprise App, the system leverages historical data stored in Spanner, generates SQL queries from natural language, and uses multiple specialized agents with callbacks and routing logic to find qualified personnel. The solution successfully replaced tribal knowledge and disconnected systems with an automated, production-ready agent platform that pairs the right people with the right projects, improving project outcomes and client satisfaction.

[Read source](https://youtu.be/Req2PndZ7HM)

---

#### Production-Grade AI Agents for Financial Compliance Review Automation

**Company:** stripe  
**Industry:** Finance

Stripe, processing $1.4 trillion annually across 50 countries, faced a critical compliance scaling challenge where skilled analysts spent up to 80% of their time navigating fragmented systems rather than performing risk assessments. To address this, Stripe built a production-grade AI agent system on AWS using Amazon Bedrock, implementing a ReAct agent framework with human-in-the-loop oversight, task decomposition via directed acyclic graphs (DAG), and a dedicated agent service infrastructure distinct from traditional ML inference systems. The solution achieved a 26 percent reduction in median review handling time while maintaining over 96 percent helpfulness ratings from reviewers, with human experts retaining final decision authority and full audit trails for regulatory compliance.

[Read source](https://aws.amazon.com/blogs/machine-learning/production-grade-ai-agents-for-financial-compliance-lessons-from-stripe/)

---

#### Rethinking Insurance with AI: Operational Deployment Strategies for Brokers, Carriers, and Advisors

**Company:** deloitte  
**Industry:** Insurance

This panel discussion features insurance technology leaders from Baldwin Group, Ameriprise Financial (RiverSource), and Hudson Insurance discussing how they are deploying AI and LLM-based solutions into production workflows. The discussion covers the challenges of moving from AI experimentation to production adoption, including the need to embed AI directly into business workflows, the importance of business-led rather than technology-led initiatives, and the critical role of data foundations and architecture. Key results mentioned include reducing product rollout times from 3-6 months to 3 days at Baldwin Group, and plans to roll out enterprise-wide AI capabilities through partnerships with hyperscalers like Anthropic while maintaining appropriate governance and guardrails.

[Read source](https://www.youtube.com/watch?v=8THW-2PpwnY)

---

#### AI-Powered Conversational Business Intelligence Assistant for Enterprise Leadership

**Company:** aws  
**Industry:** Tech

AWS SMGS faced significant business intelligence challenges including time-intensive manual data preparation, fragmented data across multiple systems, and limited dashboard accessibility that delayed critical leadership decisions. To address these issues, they built NarrateAI, an AI-powered conversational assistant using Amazon Bedrock AgentCore that delivers on-demand business insights through natural language. The solution employs a two-layer architecture combining batch narrative generation with real-time multi-agent orchestration, powered by Anthropic's Claude Sonnet 4. Since deployment, NarrateAI has served over 4,000 active users across AWS leadership, reducing business review preparation time from hours to minutes while maintaining comprehensive data accuracy and row-level security through persona-based narrative isolation.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-aws-smgs-uses-an-ai-powered-conversational-assistant-to-transform-business-management-with-amazon-bedrock-agentcore/)

---

#### Purpose-Built AI Agent Hierarchies for GPU Infrastructure Reliability

**Company:** nvidia  
**Industry:** Tech

NVIDIA's Applied AI Lab for DGX Cloud developed LLo11yPop, a hierarchical agent system for managing large-scale GPU infrastructure. The problem involved monitoring and optimizing hundreds of GPU clusters with complex failure modes, resource allocation constraints, and the need for proactive incident detection. The solution employed a multi-tier agent architecture with specialized worker agents for data retrieval, analyst agents for reasoning, orchestrator agents for coordination, and tool agents for actions. By constraining individual agents to specific tasks and using deterministic fallbacks where needed, the system achieved production-grade reliability for GPU fleet management. The architecture demonstrated that balancing agentic discovery with deterministic tools, coupled with comprehensive evaluation strategies and rare context integration, enables scalable AI operations in high-stakes environments.

[Read source](https://www.infoq.com/presentations/reliable-ai-platforms)

---

#### Infrastructure Challenges in Production AI: Multi-Company Panel on Scaling, Cost, and Governance

**Company:** forge_/_cockroach_labs_/_doubleword_/_mesa  
**Industry:** Tech

This panel discussion from InfoQ Live brings together infrastructure experts from Forge, Cockroach Labs, Doubleword, and MESA to address the operational challenges of running AI systems at scale. The problem identified is that while building AI models has become relatively straightforward, maintaining production databases and infrastructure under constant AI-driven pressure has emerged as the critical bottleneck. The experts discuss solutions including distributed SQL databases, inference optimization, governance frameworks, and architectural evolution strategies. Key insights reveal that token costs are scaling 100x year-over-year rather than the predicted 10x, database layers have become the control plane for agentic AI, and traditional capacity planning approaches are obsolete in favor of bounded elasticity with guardrails.

[Read source](https://www.infoq.com/presentations/ai-infrastructure-scaling-architecture/)

---

#### Building Production-Grade Customer Experience Agents at Enterprise Scale

**Company:** sierra  
**Industry:** Tech

Sierra has built a comprehensive platform for deploying customer experience agents across sales, service, and loyalty touchpoints for Fortune 20 companies. The platform addresses the challenge of building reliable, low-latency conversational AI at enterprise scale by developing a modular architecture that orchestrates 10-15 different models per conversation turn, supports voice and multimodal experiences with sub-2-second latency requirements, and implements outcome-based pricing models tied to business results like sales conversions and customer satisfaction. Sierra serves most of the Fortune 20, handling use cases from airline booking and flight disruptions to retail product discovery and payment processing, with agents operating across 60+ languages and processing conversation volumes that would represent billions of annual interactions.

[Read source](https://www.youtube.com/watch?v=uCKhOmth2ms)

---

#### AI-Powered Consumer Feedback Analysis at Scale for Product Safety and Quality

**Company:** mattel  
**Industry:** Other

Mattel, a global toy manufacturer with $5.5 billion in annual revenue and operations across 100+ manufacturing sites, faced a critical scaling challenge in analyzing consumer feedback for product safety and quality decisions. Their teams were manually reviewing millions of consumer signals including reviews, service transcripts, and social media feedback using spreadsheets and handwritten tally sheets, a process that took days to months per analysis. Working with Insight and Google Cloud, Mattel built a production AI system using Gemini and Vertex AI that automatically classifies and analyzes consumer feedback in real-time. The system integrates directly into their Jira workflow, automatically surfaces classified sentiment data when tickets are created, and reduces analysis time from months to minutes. This transformation enabled proactive quality management, informed major product innovations including the Speed Snap track system (the most significant Hot Wheels track improvement in 50 years), and established a governed, enterprise-grade AI foundation that the organization is expanding across 68 identified AI projects.

[Read source](https://www.youtube.com/watch?v=2swzoVYU_iQ&list=PLFZU5nT4APFA&index=147)

---

#### Scaling LLM Inference with Multi-Accelerator Strategy for Recommendations and Safety

**Company:** spotify  
**Industry:** Media & Entertainment

Spotify faced exponentially growing compute demands from deploying LLMs across recommendation systems and content safety at global scale, serving 700 million users. The company implemented a multi-accelerator strategy using both GPUs and TPUs through a shared resource pool, leveraging open-source inference engines (vLLM and SGLang) to enable seamless hardware switching. By adopting Google Cloud's TPUs alongside their existing GPU fleet and fine-tuning open-weight models like Gemma on Spotify-specific data, they achieved 30-40% cost savings on certain workloads while maintaining latency targets, allowing continuous innovation in AI features like AI DJ and multilingual safety moderation without being constrained by accelerator availability.

[Read source](https://youtu.be/WbMlr83CYDA)

---

#### Multimodal AI at Scale: Voice, Video, and Visual Generation for E-commerce and Enterprise Communication

**Company:** heygen_/_elevenlabs_/_photogen  
**Industry:** Tech

This panel discussion features three AI companies operating multimodal production systems at massive scale: PhotoRoom (20 million users processing 10 billion e-commerce images annually), ElevenLabs (voice AI serving major enterprises and creative studios), and HeyGen (40 million users generating 100+ million minutes of video). Each company addresses distinct production challenges: PhotoRoom ensures product fidelity for e-commerce imagery across 180 countries, ElevenLabs balances voice quality with sub-second latency for conversational agents, and HeyGen pioneered code-to-video generation for communication workflows. All three leverage Google's Gemini models alongside proprietary frontier models, employing sophisticated model orchestration, evaluation frameworks, and vertical specialization to maintain quality, cost-efficiency, and trust at global scale.

[Read source](https://www.youtube.com/watch?v=WgMx66iImXI&list=PLFZU5nT4APFA&index=56)

---

#### CPU-Based Infrastructure for AI Inference and Agentic Workflows

**Company:** resemble_ai_/_turpopuffer  
**Industry:** Tech

This case study explores how Turpopuffer and Resemble AI architect their AI infrastructure to optimize for inference and agentic workflows on Google Cloud Platform. Turpopuffer built a search engine enabling models to attend to trillions of tokens by caching data from object storage to NVMe and DRAM, serving customers like Cursor and Notion with billions of documents. Resemble AI developed foundation models for generative voice AI and deepfake detection, strategically distributing workloads between GPUs for low-latency inference and CPUs for data processing, batch operations, and model distillation. Both companies demonstrate significant cost savings and performance improvements by auditing their AI stacks and identifying which workloads benefit from CPU-based infrastructure versus accelerators, achieving up to 30% better price performance with specific VM configurations.

[Read source](https://www.youtube.com/watch?v=x3LntcL1ffs&list=PLFZU5nT4APFA&index=47)

---

#### Autonomous SRE Agent System for Large-Scale Incident Management

**Company:** paypal  
**Industry:** Finance

PayPal faced significant challenges managing reliability across 3,000 microservices processing $5 million per minute, with SRE teams overwhelmed by manual incident response work where 70% of effort went to data collection and correlation. The company developed an autonomous SRE agent system using Google Cloud's Vertex AI and Agent Development Kit (ADK) that orchestrates multiple specialized agents to detect, triage, mitigate, and report incidents in parallel rather than sequentially. The solution integrated with PayPal's diverse data sources through a unified MCP tools layer and was deployed into production in two to three weeks with 40-50% less code than alternative frameworks, reducing development time by 60-70% while providing built-in governance, observability, and the ability to evaluate and swap models without code changes.

[Read source](https://youtu.be/8tB01DYGMAs)

---

#### Scaling Agentic AI for Fleet Management Insights to 100,000 Users

**Company:** verizon_connect  
**Industry:** Telecommunications

Verizon Connect faced the challenge of transforming overwhelming fleet data—over 500 million data points daily from 1.2 million vehicle subscriptions across 80,000 indicators—into actionable insights for fleet managers. Rather than building static dashboards or rule-based systems, they deployed an agentic AI solution on AWS that combines serverless statistical anomaly detection with dynamic LLM-based investigation. The system uses AWS Lambda, Step Functions, Amazon Bedrock (with Claude and Amazon Nova models), and Strands Agents to automatically detect anomalies, investigate root causes through autonomous tool-calling, and generate natural language insights. Deployed in November 2025, the solution now delivers daily insights to 100,000 users, helping fleet managers identify safety patterns, operational inefficiencies, and maintenance needs proactively rather than reactively.

[Read source](https://aws.amazon.com/blogs/machine-learning/from-data-overload-to-actionable-insights-how-verizon-connect-scaled-agentic-ai-to-100000-users/)

---

#### Deterministic Verification Layer for AI Coding Agents

**Company:** checkout  
**Industry:** Tech

A developer at Checkout encountered reliability issues with AI coding agents like Claude, where tasks appeared completed but contained subtle failures requiring manual intervention. To address this, they built Vector, a deterministic verification system that uses hooks to automatically check agent outputs against predefined test cases before accepting completion. The solution evolved from a company-specific tool into a language-agnostic pattern applicable across industries, demonstrating that verification design rather than code generation is becoming the critical value proposition in AI-assisted development. This approach enables the use of smaller, less expensive models while maintaining output quality through comprehensive guardrails.

[Read source](https://www.youtube.com/watch?v=MpZzWMdmQCE)

---

#### Agent Reinforcement Fine-Tuning for Production AI Agents

**Company:** openai  
**Industry:** Tech

OpenAI presented Agent RFT (Agent Reinforcement Fine-Tuning), a platform that enables organizations to fine-tune reasoning models to improve agentic behavior through real-time tool interactions and custom reward signals. The platform addresses the challenge of training AI agents that need to interact with external tools and environments during production workflows, moving beyond traditional supervised fine-tuning approaches. Multiple enterprise customers across coding, healthcare, and finance domains demonstrated significant improvements, including reduced tool call latency (up to 18% faster), elimination of long-tail loops (from 100+ messages to tight clusters), and substantial accuracy gains (5-23% improvements) while maintaining or reducing resource consumption through reinforcement learning-based credit assignment.

[Read source](https://www.infoq.com/presentations/rft-openai-model/)

---

#### AI-Led Restaurant Metadata Platform with LLM Juries and Context Optimization

**Company:** doordash  
**Industry:** E-commerce

DoorDash built an AI-led restaurant metadata platform to address the challenge of generating reliable, structured metadata for millions of diverse menu items at scale. The problem stemmed from food being deeply contextual, culturally rich, and highly non-standardized, making traditional approaches impractical. Their solution employed multimodal LLMs with several key innovations: an LLM jury system for automated evaluation that increased accuracy by 20% over human reviewers, reinforcement learning-inspired context optimization agents that improved precision by over 20% and accelerated prompt development tenfold, distributed computing infrastructure that reduced backfill time from over a month to just days, and AI-led annotation that enabled fine-tuned models achieving frontier LLM quality at 10% of the inference cost. The resulting metadata platform powers customer search, personalization, filtering, and analytics across the DoorDash platform while demonstrating that generative AI can be deployed reliably and cost-effectively at high volume.

[Read source](https://careersatdoordash.com/blog/building-food-metadata-with-llm-juries-context-optimization-multimodal-ai/)

---

### Cool Use Cases

#### Building Production-Scale Voice and Multi-Modal Customer Experience Agents

**Company:** sierra  
**Industry:** Tech

Sierra has built an enterprise agent platform serving most of the Fortune 20 companies, focusing on customer experience across sales, service, and loyalty touchpoints. The platform addresses the challenge of building reliable, low-latency conversational agents that can handle complex customer interactions across voice and chat modalities in dozens of languages. Sierra's approach combines a constellation of 10-15 models per conversation turn, custom infrastructure for sensitive operations like payments (achieving PCI DSS level one certification), and a no-code journey builder that compiles to their Agent SDK. The company has achieved notable success with outcome-based pricing models where agents earn commissions on sales, demonstrating measurable business value through improved resolution rates, conversion rates, and customer satisfaction metrics across retail, airline, and other enterprise verticals.

[Read source](https://www.youtube.com/watch?v=uCKhOmth2ms)

---

#### Agent Memory System for Personalized Food Ordering and Discovery

**Company:** doordash  
**Industry:** E-commerce

DoorDash built an agent memory system to power their Ask DoorDash conversational ordering experience, addressing the challenge of enabling AI agents to maintain persistent, structured understanding of user preferences across sessions. The solution connects their long-term memory platform with live agents through a three-layer architecture: offline memory generation that distills behavioral history into structured blocks, a distributed storage layer with vector search capabilities, and a tooling orchestration layer that handles task-aware retrieval, conversational memory extraction, and context engineering. Early production data showed grocery agent sessions backed by memory converted to checkout at ~24% higher relative rates, restaurant queries converted at ~15% higher rates, and sessions were ~33% less likely to misunderstand user intent compared to baseline sessions without computed memory.

[Read source](https://careersatdoordash.com/blog/building-ask-doordash-part-two-intelligence/)

---

### Tools & Infrastructure

#### Production-Ready AI Agents for Automated User Story Generation in Financial Services

**Company:** ford  
**Industry:** Automotive

Ford Credit, the financial services arm of Ford Motor Company, deployed production-ready AI agents to automate the conversion of product requirements in Confluence into technical user stories. The problem addressed was the "blank page problem" where product managers had to manually translate high-level requirements into detailed technical user stories, leading to high cognitive load, variance in quality, and capacity drain. The solution involved building a user story agent using Google Cloud's Agent Development Kit and platform infrastructure, with extensive architectural controls including prompt injection defense, circuit breakers, rate limiting, human-in-the-loop gates, end-to-end telemetry, and rigorous evaluation frameworks. The results showed 24% improvement in user story fidelity, 40% faster story creation cycles, and significantly improved consistency, enabling better downstream automation and faster product execution.

[Read source](https://www.youtube.com/watch?v=Mq4ZY3eE5dI&list=PLFZU5nT4APFA&index=15)

---

#### AI-Powered Document Fraud Detection with Multi-Model Agentic System

**Company:** inscribe  
**Industry:** Finance

Inscribe, a document fraud detection company serving financial institutions, faced the challenge of detecting sophisticated AI-generated forgeries and tampered documents at scale, where manual review took 30 minutes per application and couldn't keep pace with evolving fraud tactics. They developed an agentic AI system using Amazon Bedrock that coordinates multiple foundation models—Claude Haiku for high-volume parsing, Llama models for transaction analysis, and Claude Sonnet for complex cross-document reasoning—alongside proprietary ML models on Amazon SageMaker for forensic analysis. The solution reduced review time from 30 minutes to under 90 seconds (20x improvement) while maintaining regulatory compliance, with customers reporting millions in fraud losses prevented, up to 99% reduction in manual review time, and the ability to detect coordinated fraud rings that manual processes missed.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-inscribe-uses-amazon-bedrock-to-stop-document-fraud-in-seconds/)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

# Weekly LLMOps Newsletter — 2026-08-13

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### LLM-Powered Product Relevance Labeling for E-commerce Search

**Company:** flipkart  
**Industry:** E-commerce

Flipkart replaced a manual, human-driven product relevance labeling process with an LLM-based system called Product Analyser (PA) to address bottlenecks in their search quality evaluation pipeline. The manual process was slow, expensive, and produced inconsistent judgments across annotators, limiting their ability to generate the high-quality training data needed for semantic retrievers and ranking models. The solution employed a two-stage training approach: first, supervised fine-tuning (SFT) to teach the model what good relevance judgments look like using millions of query-product pairs with reasoning traces, then Grouped Relative Policy Optimization (GRPO) to align the model's reasoning process for consistency and reliability. The system achieved human-level performance with +2.3% improvement on 3-level accuracy and +2.9% on binary accuracy over human annotators, while operating at a fraction of the cost and enabling continuous, scalable evaluation of millions of query-product pairs that was previously rate-limited by human bandwidth.

[Read source](https://blog.flipkart.tech/llms-for-relevance-automating-high-quality-product-relevance-labeling-in-flipkart-search-ddd5ca50b584)

---

#### Adapting Conversational AI Chatbots for Japanese Market Cultural Requirements

**Company:** uber  
**Industry:** Tech

This case study explores the challenges of deploying conversational AI chatbots in the Japanese market, focusing on cultural and linguistic adaptations required for successful implementation. The speaker, drawing from experience at Rakuten implementing chatbots across multiple business verticals and currently leading customer experience at Uber Japan, identifies key problems including the unique Japanese customer service philosophy of omotenashi (anticipating needs, showing empathy, and attention to detail), extremely high customer expectations with low tolerance for mistakes, and complex linguistic requirements. The proposed solution involves five critical adaptation areas: linguistic etiquette (proper formality levels, avoiding over-politeness), appropriate writing conventions (managing three alphabets, character limits), culturally appropriate personas (using mascots), understanding high-context communication (reading implicit messages and ambiguous expressions), and ecosystem integration (deploying on LINE platform). Results are primarily framed as best practices and guidelines rather than quantitative metrics, emphasizing the need for culturally-aware prompt engineering and chatbot design to meet Japanese market expectations.

[Read source](https://www.youtube.com/watch?v=D04QogLI3M8)

---

### Industry News

#### AI-Powered Citizen Inquiry Automation with Ticketing System Integration

**Company:** city_of_munich  
**Industry:** Government

The City of Munich IT department developed an AI-powered system to automate citizen inquiries through their Zammad ticketing platform, initially targeting the driver's licensing authority which handles approximately 16,000 requests annually. The solution uses a RAG-based architecture combining LLM-driven ticket classification, automated response generation from knowledge bases, and human-in-the-loop oversight. A comprehensive pre-study analyzed over 15,000 historical tickets using prompt-engineered LLM categorization to validate feasibility and calculate ROI. The system, still in development at the time of presentation, is designed as a reusable, event-driven platform that can scale across multiple city departments through configuration rather than custom development, following open-source principles and EU AI Act compliance requirements.

[Read source](https://www.youtube.com/watch?v=9Sfxy2nmUU0)

---

#### Scaling Generative AI in Large Industrial Enterprise Through Platform Architecture

**Company:** omv  
**Industry:** Energy

OMV, Austria's largest industrial company operating across chemicals, fuels, and plastics sectors, faced the challenge of scaling generative AI across highly heterogeneous business divisions with 140+ use case demands from business units. The company implemented a federated platform approach centered on a central AI platform team that develops reusable building blocks and reference architectures, which multiple product development teams then assemble into AI products. This resulted in 40+ proof-of-concepts and delivery projects, 15 live generative AI use cases, and 11 generative AI products unified through a single web portal called the AI Hub, enabling the organization to scale AI capabilities without requiring hundreds of developers while maintaining consistency and operational efficiency across diverse business models ranging from geological engineering to retail operations.

[Read source](https://www.youtube.com/watch?v=c8KP7I7x6f8)

---

#### Deploying AI Agents in High-Risk Finance and Legal Operations

**Company:** circle_/_wells_fargo_/_mayfield  
**Industry:** Finance

Circle and Wells Fargo discuss their approaches to deploying AI agents in high-stakes finance and legal environments where the cost of failure is substantial. The organizations emphasize the critical importance of verifiability, auditability, and rigorous evaluation frameworks when implementing agents for tasks like SOX compliance, earnings preparation, credit underwriting, and home mortgage processing. Both companies are building agentic infrastructures including agent gateways, harness layers, and enabling self-publishing capabilities for employees, while grappling with challenges around long-running processes, agent-to-agent communication, and organizational transformation where individual contributors become managers of agents.

[Read source](https://www.youtube.com/watch?v=elptCI-FSCA)

---

#### Risk Management and Production Deployment Practices for Generative AI Agents in Banking and Retail

**Company:** carrefour_/_lloyds_banking  
**Industry:** Finance

This panel discussion brings together practitioners from Lloyds Banking, Yaya Finance, and Carrefour to discuss practical approaches to managing risk when deploying generative AI agents in production. The panelists share their experiences building customer-facing conversational AI systems, from low-risk internal documentation assistants to high-stakes financial services agents handling vulnerable customers and fraud detection. Key themes include the importance of starting with low-risk use cases and gradually expanding scope, the fundamental design shift from building up deterministic systems to constraining generative ones, the need for continuous testing pipelines, and formal risk assessment frameworks that evaluate both likelihood and financial impact. The discussion emphasizes that good risk management practices are ultimately good product development practices focused on serving user needs.

[Read source](https://www.youtube.com/watch?v=SmC6-LS7EtY)

---

#### Rapid Deployment of Agentic AI for Customer Experience Through Structured Onboarding

**Company:** accelerate  
**Industry:** Consulting

Accelerate, a Zoom CX and AI specialist deployment partner, and Zoom present their approach to deploying agentic AI systems in production environments within 30 days. They argue that AI initiatives often stall not due to model capability limitations but because of inadequate operational management, messy integrations, and unclear governance. Their solution treats AI agents like human employees, implementing structured onboarding processes with defined roles, bounded autonomy, controlled tool access, and continuous monitoring. Two case studies demonstrate this approach: SharkNinja deployed a virtual agent in 4 weeks achieving over 90% success rate handling complex customer service cases including troubleshooting and warranty checking, while Oxfordshire County Council implemented AI agents for high-volume citizen services like blue badge applications and congestion charging to improve service delivery under budget constraints.

[Read source](https://www.youtube.com/watch?v=O-gQIsQI2Ac)

---

#### Autonomous AI Agent for Development Workflow Automation

**Company:** nordic_corporate_bank  
**Industry:** Finance

Nordic Corporate Bank, a small bank with only 26 employees, implemented an autonomous AI development agent named Nils Korg to handle their entire software development workflow. The agent, built using GitHub Copilot SDK and deployed on Azure, was integrated directly into Azure DevOps where product owners could assign tasks and interact with it naturally. The system handles everything from requirements clarification through code implementation, testing, and pull request creation, resulting in a dramatic increase in development velocity - from 141 completed pull requests per month to 572 per month with the same two-developer team. The agent operates autonomously, with product owners directly assigning work items and receiving completed features in test environments, sometimes within the same day, fundamentally transforming the development bottleneck from coding to requirements gathering and pull request verification.

[Read source](https://www.youtube.com/watch?v=p8M8--12h1Y)

---

#### Agentic Engineering: Building Production Systems with Coding Agents

**Company:** oschlo  
**Industry:** Tech

This case study explores the evolution of software development using AI coding agents over an 18-month period, from late 2024 through 2025 and into 2026. The speaker, a developer at Oschlo, transitioned from traditional software engineering to building production systems primarily using coding agents like Claude Code, Aider, Codex, and Pi. The solution involved developing systematic workflows incorporating skills, deterministic tools, multi-agent orchestration, automated verification, and autonomous systems like a "sentinel" that monitors CI/CD pipelines and automatically creates pull requests. Results demonstrate that complex features can be built in hours instead of weeks, with one example showing an end-to-end feature built using 2 million tokens over 1 hour 45 minutes with minimal human intervention, though at significant token costs that are becoming a limiting factor for enterprise adoption.

[Read source](https://www.youtube.com/watch?v=Tj6Df_K-IRc)

---

#### Building Production AI Chatbot for Compliance Intelligence in Life Sciences

**Company:** qualio  
**Industry:** Healthcare

Qualio, a compliance-as-code platform for life sciences companies, developed an AI-powered chatbot to help customers remediate compliance gaps in their quality management documentation. The team evolved their architecture from an over-engineered multi-agent system with 20+ specialized tools to a simplified single-agent approach using API abstraction, skill-based workflows, and a simple to-do list planner. By leveraging Pydantic AI, progressive disclosure of capabilities, human-in-the-loop approvals for safety-critical operations, and LLM-as-a-judge evaluation frameworks, they achieved a production-ready system that balances autonomy with regulatory requirements while significantly reducing code complexity and improving developer experience.

[Read source](https://www.youtube.com/watch?v=MTyO3W7MYTs)

---

#### AI-Powered Analytics Platform with Contextual Governance and Agent-Driven Workflows

**Company:** hex  
**Industry:** Tech

Hex addresses the challenge of data teams struggling to meet infinite demand for insights while managing fragmented tooling across BI tools, notebooks, SQL editors, and spreadsheets. Their solution provides a unified analytics platform that combines deep technical workflows (SQL, Python notebooks) with AI agent capabilities for both technical users and business stakeholders. The platform integrates tightly with ClickHouse for high-performance data processing and features sophisticated context management through their Context Studio, enabling governed self-service analytics. Key results include the ability to scaffold complex analyses in minutes rather than days using notebook agents, compound knowledge through endorsed projects that become reusable context, and enterprise-grade observability for monitoring agent performance and identifying context gaps across over 2,000 customers globally, with 300+ shared customers between Hex and ClickHouse.

[Read source](https://www.youtube.com/watch?v=zlwqx05qNSk)

---

#### Converged Database Architecture for RAG and AI Agent Workloads

**Company:** oracle  
**Industry:** Tech

Oracle presents a converged database architecture designed to address the challenges of deploying RAG (Retrieval-Augmented Generation) systems and AI agents in production environments. The problem centers on the limitations of multi-store architectures where vector indexes, operational databases, and search systems exist as separate services connected by synchronization pipelines, creating staleness, governance gaps, and consistency issues. Oracle's solution—the Oracle AI Database 26ai—provides native support for relational, document/JSON, graph, vector, spatial, and text data models under a single optimizer, transaction boundary, consistency model, and security domain. The approach eliminates synchronization lag between embeddings and source data, enables cross-model queries with unified access control, and allows atomic transactions spanning multiple data models, thereby reducing the risk of agents acting on stale information and simplifying the operational complexity of production AI systems.

[Read source](https://blogs.oracle.com/developers/what-is-a-converged-database-definition-five-tests-and-ai-use-cases?utm_source=substack&utm_medium=email)

---

#### Building a Production AI Agent for Project Management Software

**Company:** linear  
**Industry:** Tech

Linear, a project management software company, built Linear Agent, an AI assistant designed to help users manage their workflows through natural language interactions. The challenge was to create an agent flexible enough to handle unanticipated user requests while maintaining predictability and safety in a production environment. Linear's solution involved a custom-built agent architecture with carefully designed system prompts, tool abstractions, a skill-based system for progressive context disclosure, and a proprietary harness for fine-grained orchestration control. The approach emphasizes balancing flexibility with boundaries, trading some potential breadth of capabilities for greater predictability and reduced error surface area, while positioning the system to benefit from future model improvements.

[Read source](https://linear.app/now/how-we-built-linear-agent)

---

#### Building and Scaling an AI-Powered Virtual Banking Assistant

**Company:** virgin_money  
**Industry:** Finance

Virgin Money developed Ready, an AI-powered virtual assistant for conversational banking, starting with a credit card service problem in 2023. The team began with basic FAQ bot functionality and gradually evolved through 2024 and 2025, adding API connectivity, proactive messaging, and contextual capabilities. Despite two failed attempts to deploy generative AI customer-facing in 2024 due to risk concerns and hallucination issues, they successfully pivoted to deploying generative AI internally for colleague support. By maintaining disciplined iteration, customer-focused design principles, and a cross-functional team structure, Virgin Money achieved the highest customer satisfaction scores in the bank, reduced live agent escalations by 25-33% across different banking services, and delivered enhancements every four working days on average throughout 2025.

[Read source](https://www.youtube.com/watch?v=WuhytMprzcc)

---

#### Deep Research News Analysis Platform with Synthetic Data and Vector Search

**Company:** asknews  
**Industry:** Media & Entertainment

AskNews built a production deep research system for news analysis that addresses the limitations of raw web scraping approaches used by competitors. The company processes 500,000 documents per day, converting raw news articles into grounded synthetic data that preserves context while removing journalistic narrative voice. Using Qdrant vector database with hybrid search, datetime indexing, and distributed deployment, they serve thousands of queries per minute across 200 million documents. The system demonstrates measurable superiority in external validation through Metaculus forecasting tournaments, where AskNews-powered bots consistently outperform those using Perplexity, Exa, and Gemini for real-world predictions.

[Read source](https://www.youtube.com/watch?v=mhsXLO5ZN8I)

---

#### Scaling Vector Search Infrastructure with Kubernetes Operators

**Company:** hubspot  
**Industry:** Tech

HubSpot built a centralized vector storage and search platform called VAST (Vector as a Service) on top of Qdrant to serve 38+ teams across the organization, managing 20 billion+ vectors across 150 clusters. The platform initially used Helm for deployments but faced significant operational challenges as it scaled, including manual cluster provisioning taking hours and complex stateful operations. To address these limitations, HubSpot migrated to a custom Kubernetes operator pattern that automated cluster lifecycle management, shard balancing, and resource provisioning. This migration reduced cluster spin-up time from hours to minutes, eliminated the need for idle standby clusters, and enabled automatic shard rebalancing that reduced resource usage skew by 65% in production workloads.

[Read source](https://www.youtube.com/watch?v=46aQff4pxRE)

---

#### Scaling Synopsis Quality Evaluation with LLM-as-a-Judge

**Company:** netflix  
**Industry:** Media & Entertainment

Netflix faced the challenge of evaluating hundreds of thousands of show synopses at scale to ensure members consistently receive high-quality content descriptions that help them choose what to watch. Manual evaluation by creative experts wasn't scalable given the volume and multiple variants per show. The solution involved developing an LLM-as-a-Judge system that evaluates synopses across four quality dimensions (tone, clarity, precision, and factuality) using techniques including prompt optimization, tiered rationales, consensus scoring, and Agents-as-a-Judge for factuality checking. The system achieves over 85% agreement with expert creative writers on binary quality assessments and demonstrates statistically significant correlations with key streaming metrics like take fraction and abandonment rate, enabling Netflix to proactively identify and fix quality issues before shows debut.

[Read source](https://netflixtechblog.com/evaluating-netflix-show-synopses-with-llm-as-a-judge-6269251e6f28)

---

#### Containment Architectures for AI Agents Across Product Lines

**Company:** anthropic  
**Industry:** Tech

Anthropic describes their engineering approach to containing AI agents across three products (claude.ai, Claude Code, and Claude Cowork) as agent capabilities and access expand. The problem centers on managing the blast radius of increasingly capable autonomous agents that can now access sensitive systems and data. Their solution implements layered containment strategies combining environmental isolation (sandboxes, VMs, egress controls), model-level defenses (system prompts, classifiers), and external content controls, tailored to each product's user base and use case. The results include production deployment of agents with significant access privileges while maintaining security through deterministic boundaries, though they encountered several notable security incidents that informed their evolving architecture, including prompt injection attacks, pre-trust-boundary execution vulnerabilities, and exfiltration through approved domains.

[Read source](https://www.anthropic.com/engineering/how-we-contain-claude)

---

#### Voice Assistant Design for Industrial Workers: Architecture Over Prompts

**Company:** spix_industry  
**Industry:** Other

This case study addresses the challenge of designing voice AI systems for industrial workers in physically demanding environments where hands and eyes are occupied. The speaker, a conversational system designer, argues that most organizations build voice assistants incorrectly by focusing on LLM prompts first rather than robust system architecture. The solution involves prioritizing state management, permission logic, escalation paths, and error handling before any prompt engineering, treating LLMs as just one component within a larger decision engine rather than the entire system. The approach emphasizes that voice succeeds when it makes users feel capable rather than when it sounds smart, requiring concise responses, multimodal context awareness, and user-centric design that accounts for real-world conditions like noise, interruptions, and cognitive load.

[Read source](https://www.youtube.com/watch?v=QJBfY5JaTRY)

---

#### Enterprise AI Assistant Spanning Knowledge Management, Data Analytics, and Process Orchestration

**Company:** heineken  
**Industry:** Other

Heineken developed Hoppy, an enterprise-wide AI assistant designed to address scattered data platforms, language barriers, remote assistance needs, self-service analytics, and event-driven alerts across their global operations. The solution consists of three main pillars: knowledge management indexing documents from SharePoint, Collibra, and other sources; chat-with-data functionality connecting to Power BI, Azure, and SAP systems with over 95% accuracy; and process orchestration for accelerated workflows including Service Now integration. The platform serves all Heineken employees globally through Microsoft Teams and web/mobile apps, with personalized responses based on user location and role, and has achieved recognition where 50% of users report learning new things through the assistant.

[Read source](https://www.youtube.com/watch?v=PN8eFF2jYx4)

---

#### Building Foundation Models for General Purpose Robotics with Multi-Database Architecture

**Company:** physical_intelligence  
**Industry:** Research & Academia

Physical Intelligence, a robotics research company, developed a foundation model for general-purpose robotics that can operate across different environments, robot embodiments, and tasks. The company faced significant data infrastructure challenges managing petabyte-scale training data, transactional operational data, and billions of rows of metadata and annotations. They implemented a hybrid database architecture using Postgres for transactional workloads and ClickHouse for analytical queries, connected via ClickPipes for automatic replication. This infrastructure enabled them to build sophisticated tools like an AI-powered data exploration dashboard that allows researchers to query their massive datasets efficiently, which was critical for validating training data composition and supporting their model development workflow. The solution eliminated previous scaling bottlenecks and reduced query times from days to near real-time.

[Read source](https://www.youtube.com/watch?v=4CaEBYbthFc)

---

### Cool Use Cases

#### Evolution of AI-Powered Digital Assistant for Telecommunications Customer Service

**Company:** bt  
**Industry:** Telecommunications

BT Group's consumer division developed Amy, an AI-powered digital assistant designed to handle customer service across broadband, mobile, and TV products. Starting from a basic routing chatbot in 2021, the team evolved the system through multiple generations, partnering with Sprinklr in 2024 after ChatGPT's launch reshaped their vendor assessment. The implementation combines traditional NLU-based intent recognition with generative AI capabilities including semantic routing and grounded knowledge retrieval, while maintaining strict controls around authentication, guardrails, and preventing hallucination. The team is now building toward "agentic AI" with an agent-based architecture that provides tools and skills rather than rigid conversational flows, aiming to shift customer interactions from the current 1 million weekly voice calls toward digital channels while also providing AI-powered assistance to human customer service agents.

[Read source](https://www.youtube.com/watch?v=4orLY_8QLAg)

---

#### Building an Agentic Financial Guidance Chatbot from Deterministic Foundations

**Company:** lloyds_banking  
**Industry:** Finance

Lloyds Banking Group's Conversational Banking Lab developed a fully agentic financial guidance chatbot to help beginner investors understand investment concepts, representing a major shift from their mature deterministic Watson Assistant chatbot that had been in production since 2015. The team encountered significant challenges transitioning from deterministic to generative AI approaches, including underestimating the complexity of safety requirements, the need for manual knowledge curation despite using foundation models, and the dramatic differences in conversation design patterns. The solution involved building comprehensive safety layers throughout the entire stack, creating manually curated knowledge bases to prevent hallucinations, and establishing rigorous testing frameworks beyond simple "vibe testing" to ensure the agentic system performed reliably within acceptable boundaries while maintaining some of the magic and unpredictability that makes generative AI valuable.

[Read source](https://www.youtube.com/watch?v=mO-4TDElwwg)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### LLM-Powered Product Relevance Labeling for E-commerce Search

**Company:** flipkart  
**Industry:** E-commerce

Flipkart replaced a manual, human-driven product relevance labeling process with an LLM-based system called Product Analyser (PA) to address bottlenecks in their search quality evaluation pipeline. The manual process was slow, expensive, and produced inconsistent judgments across annotators, limiting their ability to generate the high-quality training data needed for semantic retrievers and ranking models. The solution employed a two-stage training approach: first, supervised fine-tuning (SFT) to teach the model what good relevance judgments look like using millions of query-product pairs with reasoning traces, then Grouped Relative Policy Optimization (GRPO) to align the model's reasoning process for consistency and reliability. The system achieved human-level performance with +2.3% improvement on 3-level accuracy and +2.9% on binary accuracy over human annotators, while operating at a fraction of the cost and enabling continuous, scalable evaluation of millions of query-product pairs that was previously rate-limited by human bandwidth.

[Read source](https://blog.flipkart.tech/llms-for-relevance-automating-high-quality-product-relevance-labeling-in-flipkart-search-ddd5ca50b584)

---

#### Adapting Conversational AI Chatbots for Japanese Market Cultural Requirements

**Company:** uber  
**Industry:** Tech

This case study explores the challenges of deploying conversational AI chatbots in the Japanese market, focusing on cultural and linguistic adaptations required for successful implementation. The speaker, drawing from experience at Rakuten implementing chatbots across multiple business verticals and currently leading customer experience at Uber Japan, identifies key problems including the unique Japanese customer service philosophy of omotenashi (anticipating needs, showing empathy, and attention to detail), extremely high customer expectations with low tolerance for mistakes, and complex linguistic requirements. The proposed solution involves five critical adaptation areas: linguistic etiquette (proper formality levels, avoiding over-politeness), appropriate writing conventions (managing three alphabets, character limits), culturally appropriate personas (using mascots), understanding high-context communication (reading implicit messages and ambiguous expressions), and ecosystem integration (deploying on LINE platform). Results are primarily framed as best practices and guidelines rather than quantitative metrics, emphasizing the need for culturally-aware prompt engineering and chatbot design to meet Japanese market expectations.

[Read source](https://www.youtube.com/watch?v=D04QogLI3M8)

---

### Industry News

#### AI-Powered Citizen Inquiry Automation with Ticketing System Integration

**Company:** city_of_munich  
**Industry:** Government

The City of Munich IT department developed an AI-powered system to automate citizen inquiries through their Zammad ticketing platform, initially targeting the driver's licensing authority which handles approximately 16,000 requests annually. The solution uses a RAG-based architecture combining LLM-driven ticket classification, automated response generation from knowledge bases, and human-in-the-loop oversight. A comprehensive pre-study analyzed over 15,000 historical tickets using prompt-engineered LLM categorization to validate feasibility and calculate ROI. The system, still in development at the time of presentation, is designed as a reusable, event-driven platform that can scale across multiple city departments through configuration rather than custom development, following open-source principles and EU AI Act compliance requirements.

[Read source](https://www.youtube.com/watch?v=9Sfxy2nmUU0)

---

#### Scaling Generative AI in Large Industrial Enterprise Through Platform Architecture

**Company:** omv  
**Industry:** Energy

OMV, Austria's largest industrial company operating across chemicals, fuels, and plastics sectors, faced the challenge of scaling generative AI across highly heterogeneous business divisions with 140+ use case demands from business units. The company implemented a federated platform approach centered on a central AI platform team that develops reusable building blocks and reference architectures, which multiple product development teams then assemble into AI products. This resulted in 40+ proof-of-concepts and delivery projects, 15 live generative AI use cases, and 11 generative AI products unified through a single web portal called the AI Hub, enabling the organization to scale AI capabilities without requiring hundreds of developers while maintaining consistency and operational efficiency across diverse business models ranging from geological engineering to retail operations.

[Read source](https://www.youtube.com/watch?v=c8KP7I7x6f8)

---

#### Deploying AI Agents in High-Risk Finance and Legal Operations

**Company:** circle_/_wells_fargo_/_mayfield  
**Industry:** Finance

Circle and Wells Fargo discuss their approaches to deploying AI agents in high-stakes finance and legal environments where the cost of failure is substantial. The organizations emphasize the critical importance of verifiability, auditability, and rigorous evaluation frameworks when implementing agents for tasks like SOX compliance, earnings preparation, credit underwriting, and home mortgage processing. Both companies are building agentic infrastructures including agent gateways, harness layers, and enabling self-publishing capabilities for employees, while grappling with challenges around long-running processes, agent-to-agent communication, and organizational transformation where individual contributors become managers of agents.

[Read source](https://www.youtube.com/watch?v=elptCI-FSCA)

---

#### Risk Management and Production Deployment Practices for Generative AI Agents in Banking and Retail

**Company:** carrefour_/_lloyds_banking  
**Industry:** Finance

This panel discussion brings together practitioners from Lloyds Banking, Yaya Finance, and Carrefour to discuss practical approaches to managing risk when deploying generative AI agents in production. The panelists share their experiences building customer-facing conversational AI systems, from low-risk internal documentation assistants to high-stakes financial services agents handling vulnerable customers and fraud detection. Key themes include the importance of starting with low-risk use cases and gradually expanding scope, the fundamental design shift from building up deterministic systems to constraining generative ones, the need for continuous testing pipelines, and formal risk assessment frameworks that evaluate both likelihood and financial impact. The discussion emphasizes that good risk management practices are ultimately good product development practices focused on serving user needs.

[Read source](https://www.youtube.com/watch?v=SmC6-LS7EtY)

---

#### Rapid Deployment of Agentic AI for Customer Experience Through Structured Onboarding

**Company:** accelerate  
**Industry:** Consulting

Accelerate, a Zoom CX and AI specialist deployment partner, and Zoom present their approach to deploying agentic AI systems in production environments within 30 days. They argue that AI initiatives often stall not due to model capability limitations but because of inadequate operational management, messy integrations, and unclear governance. Their solution treats AI agents like human employees, implementing structured onboarding processes with defined roles, bounded autonomy, controlled tool access, and continuous monitoring. Two case studies demonstrate this approach: SharkNinja deployed a virtual agent in 4 weeks achieving over 90% success rate handling complex customer service cases including troubleshooting and warranty checking, while Oxfordshire County Council implemented AI agents for high-volume citizen services like blue badge applications and congestion charging to improve service delivery under budget constraints.

[Read source](https://www.youtube.com/watch?v=O-gQIsQI2Ac)

---

#### Autonomous AI Agent for Development Workflow Automation

**Company:** nordic_corporate_bank  
**Industry:** Finance

Nordic Corporate Bank, a small bank with only 26 employees, implemented an autonomous AI development agent named Nils Korg to handle their entire software development workflow. The agent, built using GitHub Copilot SDK and deployed on Azure, was integrated directly into Azure DevOps where product owners could assign tasks and interact with it naturally. The system handles everything from requirements clarification through code implementation, testing, and pull request creation, resulting in a dramatic increase in development velocity - from 141 completed pull requests per month to 572 per month with the same two-developer team. The agent operates autonomously, with product owners directly assigning work items and receiving completed features in test environments, sometimes within the same day, fundamentally transforming the development bottleneck from coding to requirements gathering and pull request verification.

[Read source](https://www.youtube.com/watch?v=p8M8--12h1Y)

---

#### Agentic Engineering: Building Production Systems with Coding Agents

**Company:** oschlo  
**Industry:** Tech

This case study explores the evolution of software development using AI coding agents over an 18-month period, from late 2024 through 2025 and into 2026. The speaker, a developer at Oschlo, transitioned from traditional software engineering to building production systems primarily using coding agents like Claude Code, Aider, Codex, and Pi. The solution involved developing systematic workflows incorporating skills, deterministic tools, multi-agent orchestration, automated verification, and autonomous systems like a "sentinel" that monitors CI/CD pipelines and automatically creates pull requests. Results demonstrate that complex features can be built in hours instead of weeks, with one example showing an end-to-end feature built using 2 million tokens over 1 hour 45 minutes with minimal human intervention, though at significant token costs that are becoming a limiting factor for enterprise adoption.

[Read source](https://www.youtube.com/watch?v=Tj6Df_K-IRc)

---

#### Building Production AI Chatbot for Compliance Intelligence in Life Sciences

**Company:** qualio  
**Industry:** Healthcare

Qualio, a compliance-as-code platform for life sciences companies, developed an AI-powered chatbot to help customers remediate compliance gaps in their quality management documentation. The team evolved their architecture from an over-engineered multi-agent system with 20+ specialized tools to a simplified single-agent approach using API abstraction, skill-based workflows, and a simple to-do list planner. By leveraging Pydantic AI, progressive disclosure of capabilities, human-in-the-loop approvals for safety-critical operations, and LLM-as-a-judge evaluation frameworks, they achieved a production-ready system that balances autonomy with regulatory requirements while significantly reducing code complexity and improving developer experience.

[Read source](https://www.youtube.com/watch?v=MTyO3W7MYTs)

---

#### AI-Powered Analytics Platform with Contextual Governance and Agent-Driven Workflows

**Company:** hex  
**Industry:** Tech

Hex addresses the challenge of data teams struggling to meet infinite demand for insights while managing fragmented tooling across BI tools, notebooks, SQL editors, and spreadsheets. Their solution provides a unified analytics platform that combines deep technical workflows (SQL, Python notebooks) with AI agent capabilities for both technical users and business stakeholders. The platform integrates tightly with ClickHouse for high-performance data processing and features sophisticated context management through their Context Studio, enabling governed self-service analytics. Key results include the ability to scaffold complex analyses in minutes rather than days using notebook agents, compound knowledge through endorsed projects that become reusable context, and enterprise-grade observability for monitoring agent performance and identifying context gaps across over 2,000 customers globally, with 300+ shared customers between Hex and ClickHouse.

[Read source](https://www.youtube.com/watch?v=zlwqx05qNSk)

---

#### Converged Database Architecture for RAG and AI Agent Workloads

**Company:** oracle  
**Industry:** Tech

Oracle presents a converged database architecture designed to address the challenges of deploying RAG (Retrieval-Augmented Generation) systems and AI agents in production environments. The problem centers on the limitations of multi-store architectures where vector indexes, operational databases, and search systems exist as separate services connected by synchronization pipelines, creating staleness, governance gaps, and consistency issues. Oracle's solution—the Oracle AI Database 26ai—provides native support for relational, document/JSON, graph, vector, spatial, and text data models under a single optimizer, transaction boundary, consistency model, and security domain. The approach eliminates synchronization lag between embeddings and source data, enables cross-model queries with unified access control, and allows atomic transactions spanning multiple data models, thereby reducing the risk of agents acting on stale information and simplifying the operational complexity of production AI systems.

[Read source](https://blogs.oracle.com/developers/what-is-a-converged-database-definition-five-tests-and-ai-use-cases?utm_source=substack&utm_medium=email)

---

#### Building a Production AI Agent for Project Management Software

**Company:** linear  
**Industry:** Tech

Linear, a project management software company, built Linear Agent, an AI assistant designed to help users manage their workflows through natural language interactions. The challenge was to create an agent flexible enough to handle unanticipated user requests while maintaining predictability and safety in a production environment. Linear's solution involved a custom-built agent architecture with carefully designed system prompts, tool abstractions, a skill-based system for progressive context disclosure, and a proprietary harness for fine-grained orchestration control. The approach emphasizes balancing flexibility with boundaries, trading some potential breadth of capabilities for greater predictability and reduced error surface area, while positioning the system to benefit from future model improvements.

[Read source](https://linear.app/now/how-we-built-linear-agent)

---

#### Building and Scaling an AI-Powered Virtual Banking Assistant

**Company:** virgin_money  
**Industry:** Finance

Virgin Money developed Ready, an AI-powered virtual assistant for conversational banking, starting with a credit card service problem in 2023. The team began with basic FAQ bot functionality and gradually evolved through 2024 and 2025, adding API connectivity, proactive messaging, and contextual capabilities. Despite two failed attempts to deploy generative AI customer-facing in 2024 due to risk concerns and hallucination issues, they successfully pivoted to deploying generative AI internally for colleague support. By maintaining disciplined iteration, customer-focused design principles, and a cross-functional team structure, Virgin Money achieved the highest customer satisfaction scores in the bank, reduced live agent escalations by 25-33% across different banking services, and delivered enhancements every four working days on average throughout 2025.

[Read source](https://www.youtube.com/watch?v=WuhytMprzcc)

---

#### Deep Research News Analysis Platform with Synthetic Data and Vector Search

**Company:** asknews  
**Industry:** Media & Entertainment

AskNews built a production deep research system for news analysis that addresses the limitations of raw web scraping approaches used by competitors. The company processes 500,000 documents per day, converting raw news articles into grounded synthetic data that preserves context while removing journalistic narrative voice. Using Qdrant vector database with hybrid search, datetime indexing, and distributed deployment, they serve thousands of queries per minute across 200 million documents. The system demonstrates measurable superiority in external validation through Metaculus forecasting tournaments, where AskNews-powered bots consistently outperform those using Perplexity, Exa, and Gemini for real-world predictions.

[Read source](https://www.youtube.com/watch?v=mhsXLO5ZN8I)

---

#### Scaling Vector Search Infrastructure with Kubernetes Operators

**Company:** hubspot  
**Industry:** Tech

HubSpot built a centralized vector storage and search platform called VAST (Vector as a Service) on top of Qdrant to serve 38+ teams across the organization, managing 20 billion+ vectors across 150 clusters. The platform initially used Helm for deployments but faced significant operational challenges as it scaled, including manual cluster provisioning taking hours and complex stateful operations. To address these limitations, HubSpot migrated to a custom Kubernetes operator pattern that automated cluster lifecycle management, shard balancing, and resource provisioning. This migration reduced cluster spin-up time from hours to minutes, eliminated the need for idle standby clusters, and enabled automatic shard rebalancing that reduced resource usage skew by 65% in production workloads.

[Read source](https://www.youtube.com/watch?v=46aQff4pxRE)

---

#### Scaling Synopsis Quality Evaluation with LLM-as-a-Judge

**Company:** netflix  
**Industry:** Media & Entertainment

Netflix faced the challenge of evaluating hundreds of thousands of show synopses at scale to ensure members consistently receive high-quality content descriptions that help them choose what to watch. Manual evaluation by creative experts wasn't scalable given the volume and multiple variants per show. The solution involved developing an LLM-as-a-Judge system that evaluates synopses across four quality dimensions (tone, clarity, precision, and factuality) using techniques including prompt optimization, tiered rationales, consensus scoring, and Agents-as-a-Judge for factuality checking. The system achieves over 85% agreement with expert creative writers on binary quality assessments and demonstrates statistically significant correlations with key streaming metrics like take fraction and abandonment rate, enabling Netflix to proactively identify and fix quality issues before shows debut.

[Read source](https://netflixtechblog.com/evaluating-netflix-show-synopses-with-llm-as-a-judge-6269251e6f28)

---

#### Containment Architectures for AI Agents Across Product Lines

**Company:** anthropic  
**Industry:** Tech

Anthropic describes their engineering approach to containing AI agents across three products (claude.ai, Claude Code, and Claude Cowork) as agent capabilities and access expand. The problem centers on managing the blast radius of increasingly capable autonomous agents that can now access sensitive systems and data. Their solution implements layered containment strategies combining environmental isolation (sandboxes, VMs, egress controls), model-level defenses (system prompts, classifiers), and external content controls, tailored to each product's user base and use case. The results include production deployment of agents with significant access privileges while maintaining security through deterministic boundaries, though they encountered several notable security incidents that informed their evolving architecture, including prompt injection attacks, pre-trust-boundary execution vulnerabilities, and exfiltration through approved domains.

[Read source](https://www.anthropic.com/engineering/how-we-contain-claude)

---

#### Voice Assistant Design for Industrial Workers: Architecture Over Prompts

**Company:** spix_industry  
**Industry:** Other

This case study addresses the challenge of designing voice AI systems for industrial workers in physically demanding environments where hands and eyes are occupied. The speaker, a conversational system designer, argues that most organizations build voice assistants incorrectly by focusing on LLM prompts first rather than robust system architecture. The solution involves prioritizing state management, permission logic, escalation paths, and error handling before any prompt engineering, treating LLMs as just one component within a larger decision engine rather than the entire system. The approach emphasizes that voice succeeds when it makes users feel capable rather than when it sounds smart, requiring concise responses, multimodal context awareness, and user-centric design that accounts for real-world conditions like noise, interruptions, and cognitive load.

[Read source](https://www.youtube.com/watch?v=QJBfY5JaTRY)

---

#### Enterprise AI Assistant Spanning Knowledge Management, Data Analytics, and Process Orchestration

**Company:** heineken  
**Industry:** Other

Heineken developed Hoppy, an enterprise-wide AI assistant designed to address scattered data platforms, language barriers, remote assistance needs, self-service analytics, and event-driven alerts across their global operations. The solution consists of three main pillars: knowledge management indexing documents from SharePoint, Collibra, and other sources; chat-with-data functionality connecting to Power BI, Azure, and SAP systems with over 95% accuracy; and process orchestration for accelerated workflows including Service Now integration. The platform serves all Heineken employees globally through Microsoft Teams and web/mobile apps, with personalized responses based on user location and role, and has achieved recognition where 50% of users report learning new things through the assistant.

[Read source](https://www.youtube.com/watch?v=PN8eFF2jYx4)

---

#### Building Foundation Models for General Purpose Robotics with Multi-Database Architecture

**Company:** physical_intelligence  
**Industry:** Research & Academia

Physical Intelligence, a robotics research company, developed a foundation model for general-purpose robotics that can operate across different environments, robot embodiments, and tasks. The company faced significant data infrastructure challenges managing petabyte-scale training data, transactional operational data, and billions of rows of metadata and annotations. They implemented a hybrid database architecture using Postgres for transactional workloads and ClickHouse for analytical queries, connected via ClickPipes for automatic replication. This infrastructure enabled them to build sophisticated tools like an AI-powered data exploration dashboard that allows researchers to query their massive datasets efficiently, which was critical for validating training data composition and supporting their model development workflow. The solution eliminated previous scaling bottlenecks and reduced query times from days to near real-time.

[Read source](https://www.youtube.com/watch?v=4CaEBYbthFc)

---

### Cool Use Cases

#### Evolution of AI-Powered Digital Assistant for Telecommunications Customer Service

**Company:** bt  
**Industry:** Telecommunications

BT Group's consumer division developed Amy, an AI-powered digital assistant designed to handle customer service across broadband, mobile, and TV products. Starting from a basic routing chatbot in 2021, the team evolved the system through multiple generations, partnering with Sprinklr in 2024 after ChatGPT's launch reshaped their vendor assessment. The implementation combines traditional NLU-based intent recognition with generative AI capabilities including semantic routing and grounded knowledge retrieval, while maintaining strict controls around authentication, guardrails, and preventing hallucination. The team is now building toward "agentic AI" with an agent-based architecture that provides tools and skills rather than rigid conversational flows, aiming to shift customer interactions from the current 1 million weekly voice calls toward digital channels while also providing AI-powered assistance to human customer service agents.

[Read source](https://www.youtube.com/watch?v=4orLY_8QLAg)

---

#### Building an Agentic Financial Guidance Chatbot from Deterministic Foundations

**Company:** lloyds_banking  
**Industry:** Finance

Lloyds Banking Group's Conversational Banking Lab developed a fully agentic financial guidance chatbot to help beginner investors understand investment concepts, representing a major shift from their mature deterministic Watson Assistant chatbot that had been in production since 2015. The team encountered significant challenges transitioning from deterministic to generative AI approaches, including underestimating the complexity of safety requirements, the need for manual knowledge curation despite using foundation models, and the dramatic differences in conversation design patterns. The solution involved building comprehensive safety layers throughout the entire stack, creating manually curated knowledge bases to prevent hallucinations, and establishing rigorous testing frameworks beyond simple "vibe testing" to ensure the agentic system performed reliably within acceptable boundaries while maintaining some of the magic and unpredictability that makes generative AI valuable.

[Read source](https://www.youtube.com/watch?v=mO-4TDElwwg)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

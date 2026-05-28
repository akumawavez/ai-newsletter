# Weekly LLMOps Newsletter — 2026-05-28

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Industry News

#### AI-Driven Enzyme Design for Advanced Plastic Recycling

**Company:** rhea’s_factory  
**Industry:** Energy

Rhea's Factory is developing enzymatic plastic recycling technology that uses AI and protein language models to design novel enzymes capable of breaking down polymers to their original monomer building blocks. The traditional plastic recycling process only allows materials to be recycled two to three times before quality degradation makes them unusable, limiting recycling rates to approximately 10% globally. Rhea's Factory uses a multi-stage AI platform combining protein language models, structural prediction tools, and custom predictive models to design enzymes that can operate at low temperatures and atmospheric pressure while achieving high selectivity for different plastic types. The AI platform has dramatically accelerated their enzyme discovery timeline compared to traditional trial-and-error laboratory methods, enabling them to explore design spaces beyond what nature has evolved and reducing the number of wet lab experiments needed while increasing hit rates for successful enzyme candidates.

[Read source](https://www.youtube.com/watch?v=huFaei-6Z4g)

---

#### Scaling Model Context Protocol (MCP) Infrastructure for Enterprise Agentic AI

**Company:** uber  
**Industry:** Tech

Uber faced challenges scaling agentic AI workflows across over 5,000 engineers and 10,000+ services, with 1,500 monthly active agents generating 60,000+ executions per week. Without standardization, teams built custom integrations independently, creating security risks, governance concerns, and quality issues. The solution involved building an MCP Gateway and Registry as a centralized control plane, featuring automated translation of service endpoints into MCP tools, config-driven development, integrated security and PII redaction, and differentiated handling of internal versus third-party MCPs. This infrastructure now supports three main surfaces: a no-code agent builder, an agent SDK for production use cases like grocery assistance and customer support, and coding agents that generate approximately 1,800 code changes weekly.

[Read source](https://www.youtube.com/watch?v=yVqMxBahjfA)

---

#### Demand-Driven Context Management for Enterprise AI Agents

**Company:** ikea  
**Industry:** E-commerce

IKEA's delivery and services domain, comprising over 100 engineers across six product teams, developed a novel approach to addressing the institutional knowledge gap that prevents AI agents from delivering business value in enterprise environments. While 88% of companies use AI, only 6% see meaningful value creation, primarily because agents struggle with undocumented institutional knowledge that exists only in people's minds. The demand-driven context approach treats agents as knowledge managers rather than mere consumers, using a pull-based strategy where agents are assigned tasks, identify knowledge gaps through failure, and then curate discovered knowledge into structured context blocks. Initial implementations demonstrated the ability to surface previously undocumented knowledge and improve confidence scores from 1.5 to 4.4 across 14 incident resolution cycles, with the approach validated through a preprint published in March 2026.

[Read source](https://www.youtube.com/watch?v=_QAVExf_1uw)

---

#### Context Engine for Continual Learning in AI Coding Agents

**Company:** applied_commute  
**Industry:** Tech

Applied Compute developed Context Engine, a production system for enabling AI coding agents to remember, refine, and retrieve enterprise context through continual learning. The company deployed this internally on their own codebase by logging all coding agent interactions across Cursor, Claude Code, and Codex, creating what they call ACL-Wiki. Over two weeks of production use, they observed the Critical Memory Rate (percentage of times retrieved memories were essential to task completion) roughly double from under 10% to around 20%. On a curated benchmark of tasks where memory was clearly beneficial, agents using the Contextbase outperformed no-memory baselines across all categories (reducing time-to-value, exposing user preferences, and solving underspecified tasks) while showing no significant regression on distractor tasks.

[Read source](https://x.com/appliedcompute/status/2052826576723841292)

---

#### Building Production AI Agent Infrastructure at Scale with Claude Managed Agents

**Company:** anthropic  
**Industry:** Tech

Anthropic's platform team discusses the evolution from simple API completions to stateful, production-ready AI agent infrastructure. The conversation covers Claude Managed Agents, a platform that abstracts away infrastructure complexity for teams building autonomous agents at scale. The platform addresses the common challenge where teams prototype agents successfully but hit infrastructure walls during productionization, particularly around sandboxing, state management, and async execution. By providing opinionated primitives like file systems, skills, and memory while maintaining modularity, the platform enables both internal teams and external customers to deploy long-running agents without managing servers, credentials, or orchestration complexity.

[Read source](https://www.youtube.com/watch?v=lLypHkIVLqc&pp=ugUEEgJlbg%3D%3D)

---

#### AI-Powered Identity Verification and Fraud Detection for Online Lending

**Company:** sun_finance  
**Industry:** Finance

Sun Finance, a Latvian fintech operating across nine countries, faced challenges with their identity document verification pipeline where 60% of microloan applications required manual review due to OCR extraction errors, with processing times ranging from 10 minutes to 20 hours. Partnering with the AWS Generative AI Innovation Center, they built a serverless AI-powered solution combining Amazon Textract for OCR, Amazon Rekognition for fallback extraction and face detection, and Amazon Bedrock's Claude Sonnet 4 for intelligent structuring and fraud detection. The solution improved extraction accuracy from 79.7% to 90.8%, reduced per-document costs by 91%, cut processing time to under 5 seconds, and achieved 81% accuracy in fraud detection by combining visual pattern analysis with vector-based background similarity search using Amazon Titan Multimodal Embeddings and Amazon S3 Vectors.

[Read source](https://aws.amazon.com/blogs/machine-learning/sun-finance-automates-id-extraction-and-fraud-detection-with-generative-ai-on-aws/)

---

#### Building a Production AI Slack Bot with Pydantic AI and Logfire

**Company:** tiger_data  
**Industry:** Tech

Tiger Data, a fully remote company, faced challenges with information overload as all company communications occurred on Slack, making it difficult for employees to gain context on ongoing discussions. They built Tiger Agent for Work, a production AI Slack bot capable of handling thousands of concurrent conversations with its own memory and context. Using Pydantic AI for LLM orchestration and MCP server integration, and Logfire for distributed tracing and observability, they deployed a solution that achieved daily usage by more than half the company within 6 weeks. The approach reduced debugging time through comprehensive "Agent Run" visualizations and enabled seamless LLM provider switching while maintaining production-grade reliability.

[Read source](https://pydantic.dev/articles/tiger-data-ai-slack-bot-pydantic-logfire)

---

#### Scaling Multimodal Visual AI with Self-Supervised Learning for Real-Time Generation

**Company:** black_forest_labs  
**Industry:** Research & Academia

Black Forest Labs, the team behind Stable Diffusion and the Flux model series, presents their journey from releasing breakthrough text-to-image models to developing self-supervised learning approaches for multimodal generative AI. The company faced fundamental limitations with traditional representation alignment methods that relied on external encoders, creating scaling ceilings and modality-specific constraints. Their solution, Selfflow, eliminates external encoders through a dual-noise training approach with student-teacher models, enabling unified training across images, video, audio, and robotic actions. Results demonstrate faster convergence, improved text rendering and anatomy, sub-second generation times with their Client model series, and scalable multimodal capabilities that position the company toward real-time visual intelligence and physical AI applications.

[Read source](https://www.youtube.com/watch?v=x8Yb4RidLgM)

---

### Cool Use Cases

#### AI-Powered Customer Feedback Analysis System for Container Shipping

**Company:** hapag-lloyd  
**Industry:** Other

Hapag-Lloyd, a global container shipping company, transformed their manual and time-consuming customer feedback analysis process into an automated AI-powered system using Amazon Bedrock. Previously, product managers spent hours or days manually categorizing sentiment and themes from hundreds of feedback comments exported as CSV files. The new solution automatically ingests customer feedback, performs sentiment classification using Claude Sonnet 4.6, generates embeddings, indexes data in OpenSearch, and provides stakeholders with interactive dashboards and an AI chatbot for natural language queries. The system now processes over 15,000 feedback items monthly with 95% accuracy on sentiment classification, enabling teams to move from insight to action within days instead of weeks, and has already driven measurable improvements in product decisions and user satisfaction.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-hapag-lloyd-uses-amazon-bedrock-to-transform-customer-feedback-into-actionable-insights/)

---

#### Engineering and Optimizing an Agent Harness for Production AI Coding Assistants

**Company:** cursor  
**Industry:** Tech

Cursor, an AI-powered code editor company, details their approach to building and continuously improving their "agent harness"—the production infrastructure layer that orchestrates LLM-based coding agents. The challenge was creating a robust, measurable system that could effectively manage context windows, support multiple LLM providers with different characteristics, and maintain high code quality at scale. Their solution involves a sophisticated evaluation framework combining offline benchmarks (including their proprietary CursorBench) with online A/B testing, custom metrics like "Keep Rate" for measuring code retention, LLM-based sentiment analysis of user satisfaction, and model-specific prompt engineering and tool customization. Results include a 10x reduction in unexpected tool call errors, optimized context management that shifted from static to dynamic retrieval, and a production system capable of seamlessly supporting multiple models from different providers while maintaining quality and performance.

[Read source](https://cursor.com/blog/continually-improving-agent-harness)

---

#### Agentic Search and Context Engineering for Production LLM Systems

**Company:** elastic  
**Industry:** Tech

This case study presents Elastic's approach to implementing agentic search systems for production LLM applications, focusing on context engineering challenges. The presentation addresses the limitations of fixed RAG pipelines and demonstrates how agentic search tools can dynamically retrieve and filter information from multiple context sources including databases, local file systems, and web sources. Through practical demonstrations using conference session data, the presenter shows how different search tool architectures—from simple semantic search to general-purpose query execution and shell-based tools—can be combined to create robust production systems. The solution emphasizes the importance of tool description design, error handling, agent skills for complex queries, and logging agent behavior to optimize the balance between specialized and general-purpose search tools.

[Read source](https://www.youtube.com/watch?v=ynJyIKwjonM)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Industry News

#### AI-Driven Enzyme Design for Advanced Plastic Recycling

**Company:** rhea’s_factory  
**Industry:** Energy

Rhea's Factory is developing enzymatic plastic recycling technology that uses AI and protein language models to design novel enzymes capable of breaking down polymers to their original monomer building blocks. The traditional plastic recycling process only allows materials to be recycled two to three times before quality degradation makes them unusable, limiting recycling rates to approximately 10% globally. Rhea's Factory uses a multi-stage AI platform combining protein language models, structural prediction tools, and custom predictive models to design enzymes that can operate at low temperatures and atmospheric pressure while achieving high selectivity for different plastic types. The AI platform has dramatically accelerated their enzyme discovery timeline compared to traditional trial-and-error laboratory methods, enabling them to explore design spaces beyond what nature has evolved and reducing the number of wet lab experiments needed while increasing hit rates for successful enzyme candidates.

[Read source](https://www.youtube.com/watch?v=huFaei-6Z4g)

---

#### Scaling Model Context Protocol (MCP) Infrastructure for Enterprise Agentic AI

**Company:** uber  
**Industry:** Tech

Uber faced challenges scaling agentic AI workflows across over 5,000 engineers and 10,000+ services, with 1,500 monthly active agents generating 60,000+ executions per week. Without standardization, teams built custom integrations independently, creating security risks, governance concerns, and quality issues. The solution involved building an MCP Gateway and Registry as a centralized control plane, featuring automated translation of service endpoints into MCP tools, config-driven development, integrated security and PII redaction, and differentiated handling of internal versus third-party MCPs. This infrastructure now supports three main surfaces: a no-code agent builder, an agent SDK for production use cases like grocery assistance and customer support, and coding agents that generate approximately 1,800 code changes weekly.

[Read source](https://www.youtube.com/watch?v=yVqMxBahjfA)

---

#### Demand-Driven Context Management for Enterprise AI Agents

**Company:** ikea  
**Industry:** E-commerce

IKEA's delivery and services domain, comprising over 100 engineers across six product teams, developed a novel approach to addressing the institutional knowledge gap that prevents AI agents from delivering business value in enterprise environments. While 88% of companies use AI, only 6% see meaningful value creation, primarily because agents struggle with undocumented institutional knowledge that exists only in people's minds. The demand-driven context approach treats agents as knowledge managers rather than mere consumers, using a pull-based strategy where agents are assigned tasks, identify knowledge gaps through failure, and then curate discovered knowledge into structured context blocks. Initial implementations demonstrated the ability to surface previously undocumented knowledge and improve confidence scores from 1.5 to 4.4 across 14 incident resolution cycles, with the approach validated through a preprint published in March 2026.

[Read source](https://www.youtube.com/watch?v=_QAVExf_1uw)

---

#### Context Engine for Continual Learning in AI Coding Agents

**Company:** applied_commute  
**Industry:** Tech

Applied Compute developed Context Engine, a production system for enabling AI coding agents to remember, refine, and retrieve enterprise context through continual learning. The company deployed this internally on their own codebase by logging all coding agent interactions across Cursor, Claude Code, and Codex, creating what they call ACL-Wiki. Over two weeks of production use, they observed the Critical Memory Rate (percentage of times retrieved memories were essential to task completion) roughly double from under 10% to around 20%. On a curated benchmark of tasks where memory was clearly beneficial, agents using the Contextbase outperformed no-memory baselines across all categories (reducing time-to-value, exposing user preferences, and solving underspecified tasks) while showing no significant regression on distractor tasks.

[Read source](https://x.com/appliedcompute/status/2052826576723841292)

---

#### Building Production AI Agent Infrastructure at Scale with Claude Managed Agents

**Company:** anthropic  
**Industry:** Tech

Anthropic's platform team discusses the evolution from simple API completions to stateful, production-ready AI agent infrastructure. The conversation covers Claude Managed Agents, a platform that abstracts away infrastructure complexity for teams building autonomous agents at scale. The platform addresses the common challenge where teams prototype agents successfully but hit infrastructure walls during productionization, particularly around sandboxing, state management, and async execution. By providing opinionated primitives like file systems, skills, and memory while maintaining modularity, the platform enables both internal teams and external customers to deploy long-running agents without managing servers, credentials, or orchestration complexity.

[Read source](https://www.youtube.com/watch?v=lLypHkIVLqc&pp=ugUEEgJlbg%3D%3D)

---

#### AI-Powered Identity Verification and Fraud Detection for Online Lending

**Company:** sun_finance  
**Industry:** Finance

Sun Finance, a Latvian fintech operating across nine countries, faced challenges with their identity document verification pipeline where 60% of microloan applications required manual review due to OCR extraction errors, with processing times ranging from 10 minutes to 20 hours. Partnering with the AWS Generative AI Innovation Center, they built a serverless AI-powered solution combining Amazon Textract for OCR, Amazon Rekognition for fallback extraction and face detection, and Amazon Bedrock's Claude Sonnet 4 for intelligent structuring and fraud detection. The solution improved extraction accuracy from 79.7% to 90.8%, reduced per-document costs by 91%, cut processing time to under 5 seconds, and achieved 81% accuracy in fraud detection by combining visual pattern analysis with vector-based background similarity search using Amazon Titan Multimodal Embeddings and Amazon S3 Vectors.

[Read source](https://aws.amazon.com/blogs/machine-learning/sun-finance-automates-id-extraction-and-fraud-detection-with-generative-ai-on-aws/)

---

#### Building a Production AI Slack Bot with Pydantic AI and Logfire

**Company:** tiger_data  
**Industry:** Tech

Tiger Data, a fully remote company, faced challenges with information overload as all company communications occurred on Slack, making it difficult for employees to gain context on ongoing discussions. They built Tiger Agent for Work, a production AI Slack bot capable of handling thousands of concurrent conversations with its own memory and context. Using Pydantic AI for LLM orchestration and MCP server integration, and Logfire for distributed tracing and observability, they deployed a solution that achieved daily usage by more than half the company within 6 weeks. The approach reduced debugging time through comprehensive "Agent Run" visualizations and enabled seamless LLM provider switching while maintaining production-grade reliability.

[Read source](https://pydantic.dev/articles/tiger-data-ai-slack-bot-pydantic-logfire)

---

#### Scaling Multimodal Visual AI with Self-Supervised Learning for Real-Time Generation

**Company:** black_forest_labs  
**Industry:** Research & Academia

Black Forest Labs, the team behind Stable Diffusion and the Flux model series, presents their journey from releasing breakthrough text-to-image models to developing self-supervised learning approaches for multimodal generative AI. The company faced fundamental limitations with traditional representation alignment methods that relied on external encoders, creating scaling ceilings and modality-specific constraints. Their solution, Selfflow, eliminates external encoders through a dual-noise training approach with student-teacher models, enabling unified training across images, video, audio, and robotic actions. Results demonstrate faster convergence, improved text rendering and anatomy, sub-second generation times with their Client model series, and scalable multimodal capabilities that position the company toward real-time visual intelligence and physical AI applications.

[Read source](https://www.youtube.com/watch?v=x8Yb4RidLgM)

---

### Cool Use Cases

#### AI-Powered Customer Feedback Analysis System for Container Shipping

**Company:** hapag-lloyd  
**Industry:** Other

Hapag-Lloyd, a global container shipping company, transformed their manual and time-consuming customer feedback analysis process into an automated AI-powered system using Amazon Bedrock. Previously, product managers spent hours or days manually categorizing sentiment and themes from hundreds of feedback comments exported as CSV files. The new solution automatically ingests customer feedback, performs sentiment classification using Claude Sonnet 4.6, generates embeddings, indexes data in OpenSearch, and provides stakeholders with interactive dashboards and an AI chatbot for natural language queries. The system now processes over 15,000 feedback items monthly with 95% accuracy on sentiment classification, enabling teams to move from insight to action within days instead of weeks, and has already driven measurable improvements in product decisions and user satisfaction.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-hapag-lloyd-uses-amazon-bedrock-to-transform-customer-feedback-into-actionable-insights/)

---

#### Engineering and Optimizing an Agent Harness for Production AI Coding Assistants

**Company:** cursor  
**Industry:** Tech

Cursor, an AI-powered code editor company, details their approach to building and continuously improving their "agent harness"—the production infrastructure layer that orchestrates LLM-based coding agents. The challenge was creating a robust, measurable system that could effectively manage context windows, support multiple LLM providers with different characteristics, and maintain high code quality at scale. Their solution involves a sophisticated evaluation framework combining offline benchmarks (including their proprietary CursorBench) with online A/B testing, custom metrics like "Keep Rate" for measuring code retention, LLM-based sentiment analysis of user satisfaction, and model-specific prompt engineering and tool customization. Results include a 10x reduction in unexpected tool call errors, optimized context management that shifted from static to dynamic retrieval, and a production system capable of seamlessly supporting multiple models from different providers while maintaining quality and performance.

[Read source](https://cursor.com/blog/continually-improving-agent-harness)

---

#### Agentic Search and Context Engineering for Production LLM Systems

**Company:** elastic  
**Industry:** Tech

This case study presents Elastic's approach to implementing agentic search systems for production LLM applications, focusing on context engineering challenges. The presentation addresses the limitations of fixed RAG pipelines and demonstrates how agentic search tools can dynamically retrieve and filter information from multiple context sources including databases, local file systems, and web sources. Through practical demonstrations using conference session data, the presenter shows how different search tool architectures—from simple semantic search to general-purpose query execution and shell-based tools—can be combined to create robust production systems. The solution emphasizes the importance of tool description design, error handling, agent skills for complex queries, and logging agent behavior to optimize the balance between specialized and general-purpose search tools.

[Read source](https://www.youtube.com/watch?v=ynJyIKwjonM)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

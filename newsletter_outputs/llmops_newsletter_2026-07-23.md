# Weekly LLMOps Newsletter — 2026-07-23

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Building Production-Grade Evaluation Systems for Customer Support AI Agents

**Company:** lyft  
**Industry:** Tech

Lyft's data science team developed a comprehensive evaluation framework for their customer support AI agent system over a two-year period, addressing the challenge of ensuring AI agents perform reliably before deployment to live users. The solution involves a multi-layered approach combining offline evaluations with synthetic conversation simulation, fine-tuned user models that realistically mimic actual customer behavior, actionable LLM-as-judge metrics tied to business outcomes, and rigorous statistical validation methods. The team achieved more reliable production deployments by replacing generic evaluation metrics with task-specific binary outcomes validated against human-labeled ground truth, while also establishing a continuous error analysis loop that feeds insights back into model improvements through context learning, harness tuning, and planned reinforcement learning approaches.

[Read source](https://www.youtube.com/watch?v=3z2uT5aDx_Y)

---

#### Autonomous Agent System for Scientific Machine Learning Model Optimization

**Company:** radicait  
**Industry:** Healthcare

Radicait developed an autonomous agent system to address the challenge of improving scientific machine learning models, specifically for generating synthetic PET scans from CT images for cancer detection. The core problem was that traditional coding agents would saturate after implementing initial optimizations, lacking the ability to generate novel research hypotheses needed for continued improvement. The solution involved creating a hierarchical decomposition framework that breaks down complex scientific problems into components (data, architecture, training, metrics), enabling LLMs to generate more radical and comprehensive hypotheses for model improvement. The system uses multiple specialized models in collaborative and adversarial loops, with reasoning models like GPT-4.5 for hypothesis generation and multimodal models for qualitative review of results, allowing the research loop to continue beyond the typical saturation point.

[Read source](https://www.youtube.com/watch?v=XLEYtv3cMlw)

---

#### Data-Centric AI for Virtual Cell Modeling and Drug Discovery

**Company:** xaira  
**Industry:** Healthcare

Xaira Therapeutics developed X-Cell, a foundation model for predicting cellular responses to gene expression changes, to enable AI-driven drug discovery. The team encountered a fundamental scaling limitation where test loss flatlined at 1.5B parameters despite continued training loss improvements, indicating an information bottleneck in existing datasets like CELLxGENE. To overcome this, they invested tens of millions in generating X-Atlas, a causally-structured dataset using CRISPR-based experiments that systematically perturb individual genes across millions of parallel tests. This 30x increase in information-rich data enabled continued scaling past 3.1B parameters, allowed the model to beat linear baselines that had previously outperformed other virtual cell models, and demonstrated generalization to real lab experiments in human cells.

[Read source](https://www.latent.space/p/xaira)

---

### Industry News

#### Building and Operating Claude Code with AI Agents at Scale

**Company:** anthropic  
**Industry:** Tech

Anthropic's product and engineering teams describe their internal use of Claude Code and Claude Tag AI coding agents to build and ship production software at unprecedented speed. The teams leverage aggressive dogfooding, automated code review through AI classifiers, extensive evaluation suites, and security features like auto mode to safely delegate substantial portions of their software development workflow to AI agents. Claude Tag currently lands 65% of product PRs at Anthropic, representing a fundamental shift in how engineering teams operate. The approach emphasizes reduced system prompt constraints, multi-agent collaboration through Slack integration, sophisticated permission management, and continuous evaluation to maintain quality while dramatically accelerating development velocity.

[Read source](https://www.youtube.com/watch?v=uU5Gv2h8-9g)

---

#### AI-Powered Vulnerability Discovery and Patching at Scale

**Company:** anthropic  
**Industry:** Tech

Anthropic developed an agentic harness system to help security teams discover, verify, and patch code vulnerabilities at scale using Claude. The system addresses the challenge that while frontier AI models have dramatically increased the number of vulnerabilities that can be found (Mozilla Firefox saw findings increase 20x in April alone), the bottleneck has shifted from discovery to verification, triage, and patching. Through a six-step process involving threat modeling, sandboxed testing, discovery, verification, triage, and patching, teams working with Anthropic achieved true positive rates of up to 90% while automating much of the security workflow, with over 1,600 vulnerabilities reported to maintainers and 100 patched upstream from scanning 1,000+ open source repositories.

[Read source](https://www.youtube.com/watch?v=imFedndyXYQ)

---

#### Multi-Model AI Architecture for Database Developer Assistant

**Company:** couchbase  
**Industry:** Tech

Couchbase built Capella iQ, an AI-powered developer assistant that generates database queries, recommends indexes, and supports multi-turn conversational workflows. As enterprise adoption grew, they needed a scalable, multi-model inference architecture that could handle traffic bursts and maintain high availability across regions without pre-provisioned capacity. They adopted Amazon Bedrock with Anthropic's Claude Sonnet 4.5, implementing a provider-agnostic architecture on Amazon EKS with private VPC endpoints and Cross-Region Inference. The production system achieved approximately 76 percent accuracy on internal benchmarks modeled on BIRD methodology across core workflows including SQL++ generation, index recommendations, and multi-turn conversations, while delivering improved operational resilience and flexibility to adopt newer models through configuration changes rather than code modifications.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-couchbase-built-a-multi-model-ai-architecture-for-capella-iq-with-amazon-bedrock/)

---

#### Cost-Efficient LLM Routing with Online Learning and Thompson Sampling

**Company:** ramp  
**Industry:** Finance

Ramp built an internal LLM gateway processing trillions of tokens daily to centralize AI usage across internal development and external products. To optimize costs while maintaining reliability, they developed a dynamic, failure-aware routing system using Thompson Sampling and exponentially-weighted moving averages (EWMA) to learn real-time latency and failure distributions across different models and service tiers. This approach enabled intelligent routing that considers both model preference and performance characteristics, ultimately achieving over 25% cost savings while simultaneously reducing error rates across their LLM workloads.

[Read source](https://builders.ramp.com/post/thompson-sampling-model-routing)

---

### Cool Use Cases

#### Scaling AI-Powered Developer Support Through Agentic Systems

**Company:** coinbase  
**Industry:** Finance

Coinbase's developer support engineering team transformed their support model from manual Discord responses to a comprehensive agentic AI system to scale support for their growing developer platform. The small team built multiple customer-facing and internal AI agents including Discord AI Chat, Slack Triage, and Support Engineer Assistant, leveraging Python services, self-hosted LangSmith for tracing, MCP tools with RAG fallback, and multi-layered guardrails. The transformation enabled the team to maintain high customer satisfaction while increasing automation levels, handling multilingual conversations, and establishing a foundation for human-in-the-loop workflows, though specific quantitative metrics on automation improvements were not yet finalized.

[Read source](https://www.youtube.com/watch?v=py9d6zTl4Dc)

---

#### End-to-End Automation of Oncology Prior Authorization Workflows

**Company:** risa_labs  
**Industry:** Healthcare

Trisca, a healthcare automation company, developed a multi-agent LLM system to automate oncology prior authorization workflows for cancer drugs, eliminating human review for a significant portion of orders. The system uses four specialized agents (EV, Auth, Necessity, and Submission) to handle patient eligibility verification, authorization determination, clinical reasoning, and submission to payers. The solution combines deterministic rules with LLM-based extraction, multi-source evidence reconciliation, a patient medical knowledge graph, and self-healing RPA automations. By integrating multiple data sources including insurance portals, authorization letters, and clinical notes, and applying confidence scoring to LLM outputs, the system achieves "no-touch" processing for orders that can be confidently processed without human intervention while escalating uncertain cases for clinical review.

[Read source](https://www.youtube.com/watch?v=_cVfz88_j7A)

---

### Tools & Infrastructure

#### Agentic Diagnostics Tool for Apache Spark Failure Troubleshooting

**Company:** pinterest  
**Industry:** Tech

Pinterest built Medic for Apache Spark, an agentic diagnostics tool that automatically troubleshoots Spark job failures to address the unsustainable burden of manual support and complex distributed system debugging. The system evolved from a simple prototype using Model Context Protocol and a single ReAct agent to a sophisticated multi-agent architecture built on LangGraph, incorporating specialized agents for triage, research, and remediation, along with exception classification pipelines and metrics analysis sub-agents. The solution achieved substantial improvements in diagnostic accuracy through investments in observability using OpenTelemetry and LangFuse, comprehensive end-to-end testing with fixture-based evaluation harness, and careful prompt engineering per specialized agent role, while maintaining scalability by converting token-inefficient raw data into images and structured summaries.

[Read source](https://www.youtube.com/watch?v=0RNNfxpdbQk)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Building Production-Grade Evaluation Systems for Customer Support AI Agents

**Company:** lyft  
**Industry:** Tech

Lyft's data science team developed a comprehensive evaluation framework for their customer support AI agent system over a two-year period, addressing the challenge of ensuring AI agents perform reliably before deployment to live users. The solution involves a multi-layered approach combining offline evaluations with synthetic conversation simulation, fine-tuned user models that realistically mimic actual customer behavior, actionable LLM-as-judge metrics tied to business outcomes, and rigorous statistical validation methods. The team achieved more reliable production deployments by replacing generic evaluation metrics with task-specific binary outcomes validated against human-labeled ground truth, while also establishing a continuous error analysis loop that feeds insights back into model improvements through context learning, harness tuning, and planned reinforcement learning approaches.

[Read source](https://www.youtube.com/watch?v=3z2uT5aDx_Y)

---

#### Autonomous Agent System for Scientific Machine Learning Model Optimization

**Company:** radicait  
**Industry:** Healthcare

Radicait developed an autonomous agent system to address the challenge of improving scientific machine learning models, specifically for generating synthetic PET scans from CT images for cancer detection. The core problem was that traditional coding agents would saturate after implementing initial optimizations, lacking the ability to generate novel research hypotheses needed for continued improvement. The solution involved creating a hierarchical decomposition framework that breaks down complex scientific problems into components (data, architecture, training, metrics), enabling LLMs to generate more radical and comprehensive hypotheses for model improvement. The system uses multiple specialized models in collaborative and adversarial loops, with reasoning models like GPT-4.5 for hypothesis generation and multimodal models for qualitative review of results, allowing the research loop to continue beyond the typical saturation point.

[Read source](https://www.youtube.com/watch?v=XLEYtv3cMlw)

---

#### Data-Centric AI for Virtual Cell Modeling and Drug Discovery

**Company:** xaira  
**Industry:** Healthcare

Xaira Therapeutics developed X-Cell, a foundation model for predicting cellular responses to gene expression changes, to enable AI-driven drug discovery. The team encountered a fundamental scaling limitation where test loss flatlined at 1.5B parameters despite continued training loss improvements, indicating an information bottleneck in existing datasets like CELLxGENE. To overcome this, they invested tens of millions in generating X-Atlas, a causally-structured dataset using CRISPR-based experiments that systematically perturb individual genes across millions of parallel tests. This 30x increase in information-rich data enabled continued scaling past 3.1B parameters, allowed the model to beat linear baselines that had previously outperformed other virtual cell models, and demonstrated generalization to real lab experiments in human cells.

[Read source](https://www.latent.space/p/xaira)

---

### Industry News

#### Building and Operating Claude Code with AI Agents at Scale

**Company:** anthropic  
**Industry:** Tech

Anthropic's product and engineering teams describe their internal use of Claude Code and Claude Tag AI coding agents to build and ship production software at unprecedented speed. The teams leverage aggressive dogfooding, automated code review through AI classifiers, extensive evaluation suites, and security features like auto mode to safely delegate substantial portions of their software development workflow to AI agents. Claude Tag currently lands 65% of product PRs at Anthropic, representing a fundamental shift in how engineering teams operate. The approach emphasizes reduced system prompt constraints, multi-agent collaboration through Slack integration, sophisticated permission management, and continuous evaluation to maintain quality while dramatically accelerating development velocity.

[Read source](https://www.youtube.com/watch?v=uU5Gv2h8-9g)

---

#### AI-Powered Vulnerability Discovery and Patching at Scale

**Company:** anthropic  
**Industry:** Tech

Anthropic developed an agentic harness system to help security teams discover, verify, and patch code vulnerabilities at scale using Claude. The system addresses the challenge that while frontier AI models have dramatically increased the number of vulnerabilities that can be found (Mozilla Firefox saw findings increase 20x in April alone), the bottleneck has shifted from discovery to verification, triage, and patching. Through a six-step process involving threat modeling, sandboxed testing, discovery, verification, triage, and patching, teams working with Anthropic achieved true positive rates of up to 90% while automating much of the security workflow, with over 1,600 vulnerabilities reported to maintainers and 100 patched upstream from scanning 1,000+ open source repositories.

[Read source](https://www.youtube.com/watch?v=imFedndyXYQ)

---

#### Multi-Model AI Architecture for Database Developer Assistant

**Company:** couchbase  
**Industry:** Tech

Couchbase built Capella iQ, an AI-powered developer assistant that generates database queries, recommends indexes, and supports multi-turn conversational workflows. As enterprise adoption grew, they needed a scalable, multi-model inference architecture that could handle traffic bursts and maintain high availability across regions without pre-provisioned capacity. They adopted Amazon Bedrock with Anthropic's Claude Sonnet 4.5, implementing a provider-agnostic architecture on Amazon EKS with private VPC endpoints and Cross-Region Inference. The production system achieved approximately 76 percent accuracy on internal benchmarks modeled on BIRD methodology across core workflows including SQL++ generation, index recommendations, and multi-turn conversations, while delivering improved operational resilience and flexibility to adopt newer models through configuration changes rather than code modifications.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-couchbase-built-a-multi-model-ai-architecture-for-capella-iq-with-amazon-bedrock/)

---

#### Cost-Efficient LLM Routing with Online Learning and Thompson Sampling

**Company:** ramp  
**Industry:** Finance

Ramp built an internal LLM gateway processing trillions of tokens daily to centralize AI usage across internal development and external products. To optimize costs while maintaining reliability, they developed a dynamic, failure-aware routing system using Thompson Sampling and exponentially-weighted moving averages (EWMA) to learn real-time latency and failure distributions across different models and service tiers. This approach enabled intelligent routing that considers both model preference and performance characteristics, ultimately achieving over 25% cost savings while simultaneously reducing error rates across their LLM workloads.

[Read source](https://builders.ramp.com/post/thompson-sampling-model-routing)

---

### Cool Use Cases

#### Scaling AI-Powered Developer Support Through Agentic Systems

**Company:** coinbase  
**Industry:** Finance

Coinbase's developer support engineering team transformed their support model from manual Discord responses to a comprehensive agentic AI system to scale support for their growing developer platform. The small team built multiple customer-facing and internal AI agents including Discord AI Chat, Slack Triage, and Support Engineer Assistant, leveraging Python services, self-hosted LangSmith for tracing, MCP tools with RAG fallback, and multi-layered guardrails. The transformation enabled the team to maintain high customer satisfaction while increasing automation levels, handling multilingual conversations, and establishing a foundation for human-in-the-loop workflows, though specific quantitative metrics on automation improvements were not yet finalized.

[Read source](https://www.youtube.com/watch?v=py9d6zTl4Dc)

---

#### End-to-End Automation of Oncology Prior Authorization Workflows

**Company:** risa_labs  
**Industry:** Healthcare

Trisca, a healthcare automation company, developed a multi-agent LLM system to automate oncology prior authorization workflows for cancer drugs, eliminating human review for a significant portion of orders. The system uses four specialized agents (EV, Auth, Necessity, and Submission) to handle patient eligibility verification, authorization determination, clinical reasoning, and submission to payers. The solution combines deterministic rules with LLM-based extraction, multi-source evidence reconciliation, a patient medical knowledge graph, and self-healing RPA automations. By integrating multiple data sources including insurance portals, authorization letters, and clinical notes, and applying confidence scoring to LLM outputs, the system achieves "no-touch" processing for orders that can be confidently processed without human intervention while escalating uncertain cases for clinical review.

[Read source](https://www.youtube.com/watch?v=_cVfz88_j7A)

---

### Tools & Infrastructure

#### Agentic Diagnostics Tool for Apache Spark Failure Troubleshooting

**Company:** pinterest  
**Industry:** Tech

Pinterest built Medic for Apache Spark, an agentic diagnostics tool that automatically troubleshoots Spark job failures to address the unsustainable burden of manual support and complex distributed system debugging. The system evolved from a simple prototype using Model Context Protocol and a single ReAct agent to a sophisticated multi-agent architecture built on LangGraph, incorporating specialized agents for triage, research, and remediation, along with exception classification pipelines and metrics analysis sub-agents. The solution achieved substantial improvements in diagnostic accuracy through investments in observability using OpenTelemetry and LangFuse, comprehensive end-to-end testing with fixture-based evaluation harness, and careful prompt engineering per specialized agent role, while maintaining scalability by converting token-inefficient raw data into images and structured summaries.

[Read source](https://www.youtube.com/watch?v=0RNNfxpdbQk)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

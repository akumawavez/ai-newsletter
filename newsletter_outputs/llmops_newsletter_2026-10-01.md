# Weekly LLMOps Newsletter — 2026-10-01

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Simulation-Driven Testing and Continuous Improvement for Multi-Turn AI Agents

**Company:** arklex  
**Industry:** Tech

Arklex applies LLM-based user simulation to the testing and improvement of production-oriented AI agents, addressing the limits of manual testing and static single-turn benchmarks. Synthetic users are generated from personas, goals, agent capabilities, and contextual knowledge, then used to exercise conversational and workflow agents through multi-turn trajectories, tool calls, and optional interface actions. The resulting simulations are integrated into CI/CD, scored with task-specific rules and LLM-as-judge metrics, and compared with production logs to evolve a golden scenario set. The approach is presented as reducing manual testing and exposing edge cases earlier, with reported work involving Pearson, but the source provides no independently validated quantitative results and acknowledges that simulation quality depends on expert input, realistic data, and ongoing calibration.

[Read source](https://www.infoq.com/presentations/ai-agent-testing-evaluation/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations)

---

#### AI-Native Investment Research with Governed Per-Query Data Purchasing

**Company:** heurist_finance  
**Industry:** Finance

Heurist Finance built a production investment-research workbench for retail investors that combines portfolio-aware analysis, premium market data, financial research, scenario analysis, and monitoring in a conversational interface. Its agents are orchestrated with Strands and Anthropic Claude on Amazon Bedrock, while Amazon Bedrock AgentCore provides identity, cross-session memory, isolated code execution, observability, and per-query payments for premium data accessed through the x402 protocol. The architecture links user identity, spending limits, payment credentials, data access, analysis artifacts, and traces into an auditable workflow. AWS and Heurist report that managed infrastructure reduced the estimated agent-system engineering effort by roughly 80% and saved months of platform development, although the source does not provide independent validation of these claims or detailed production quality, cost, latency, or investment-outcome metrics.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-heurist-finance-built-an-ai-native-investment-workbench-on-amazon-bedrock-agentcore/)

---

#### Multi-Agent Contract Playbook Review with Conflict-Aware Redlining

**Company:** harvey  
**Industry:** Legal

Harvey rebuilt its contract playbook review system from a sequential prompt pipeline into an orchestrator-worker multi-agent architecture. The system assigns individual playbook rules to parallel agents that can search and inspect a versioned document, classify risk, propose minimal tracked edits, and produce rationale, while a lead agent reconciles conflicting changes and validates the complete review. On Harvey's internal benchmark, risk-classification performance increased from 59% to 77% and redline-rubric performance from 53% to 87%, while average latency increased from 2.6 to 3.8 minutes. The reported results indicate a substantial quality improvement, but they are based on an in-house evaluation using legal-defined rubrics and LLM judges, so they should not be treated as independently validated production outcomes.

[Read source](https://www.harvey.ai/blog/rebuilding-playbook-review-as-a-multi-agent-system)

---

#### Production Quality Assurance for Real-Time Executive AI Answers

**Company:** narrateai  
**Industry:** Tech

NarrateAI provides a conversational agentic AI assistant that helps more than 4,000 AWS executive leaders answer business-intelligence questions during live business reviews. To address hallucinated metrics, slow validation, API throttling, and inconsistent presentation, the system combines adaptive retrieval and analysis routing, cross-account and multi-model Amazon Bedrock failover, paragraph-level streaming evaluation, parallel specialist evaluators, and a two-stage numerical grounding check. AWS reports approximately 13-second median time to first evaluated content, approximately 99% numerical accuracy, a 86.8% latency reduction versus sequential post-generation evaluation, and sustained availability in its six-month deployment and load tests; these results are deployment-specific and should be independently validated for other workloads.

[Read source](https://aws.amazon.com/blogs/machine-learning/narrateai-production-ready-llm-quality-assurance-on-amazon-bedrock/)

---

### Industry News

#### A Shared Production Platform for Governed Enterprise Agents

**Company:** wood_mackenzie  
**Industry:** Energy

Wood Mackenzie built APEX (Agentic Platform for Energy eXperience), a shared platform on Amazon Bedrock AgentCore, to move multiple agentic AI applications from prototypes into governed production. APEX centralizes runtime hosting, identity and entitlements, tool connectivity, memory, retrieval, guardrails, observability, evaluation, and generative user interfaces, while allowing product teams to choose different agent frameworks and models. The platform supports internal workflows in Woody, external-facing assistance in Lens AI, and trading use cases through common infrastructure. The source reports faster delivery and reduced duplicated engineering, but does not provide independent production-quality, cost, accuracy, or adoption metrics; many benefits remain architectural claims and planned capabilities rather than quantitatively validated outcomes.

[Read source](https://aws.amazon.com/blogs/machine-learning/a-shared-agentic-platform-for-wood-mackenzie-on-amazon-bedrock-agentcore/)

---

#### Multichannel Customer-Service Agents with Model Routing and Production Evaluation

**Company:** ringg  
**Industry:** Tech

Ringg built a multichannel enterprise agent platform for voice, chat, WhatsApp, and web interactions, using OpenAI models, retrieval, tool orchestration, specialized subagents, and human escalation to automate customer-service workflows. The platform reportedly handles more than 7 million connected calls per month, resolves up to 65% of routine inquiries without human involvement, and achieves an average CSAT of 4.8. Ringg uses model routing, historical and simulated evaluations, canary deployments, endpoint monitoring, structured conversation summarization, and regional failover to balance quality, latency, reliability, and cost; it reports approximately 90% lower model costs for selected workloads after migrating them from GPT-4.1 to GPT-5.6. These results are vendor-reported and are not accompanied in the source by independent validation or detailed measurement methodology.

[Read source](https://openai.com/index/ringg/)

---

#### Scaling Context-Aware Coding Agents with MCP Playbooks

**Company:** linkedin  
**Industry:** Tech

LinkedIn found that generic AI coding agents performed poorly against its large, mature codebase because they lacked internal architectural knowledge, procedural guidance, and reliable access to company systems. It built a local Model Context Protocol (MCP) server that exposes code search, documentation, operational systems, and authentication alongside centrally managed and repository-specific playbooks containing procedural memory. A catalog-search layer keeps thousands of tools and playbooks usable without overwhelming the model context window, while code review, InfoSec review, usage metrics, verification steps, and human confirmation provide operational guardrails. LinkedIn reports more than 8,000 daily users, over 600 playbooks, approximately 20% higher productivity, and no observed decrease in reliability or quality, although these outcomes are company-reported and the presentation does not describe a controlled evaluation.

[Read source](https://www.infoq.com/presentations/linkedin-context-engineering/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations)

---

#### Conversational HVAC Diagnostics and Building Intelligence

**Company:** trane  
**Industry:** Other

Trane Technologies built a multi-agent conversational system that gives building operators, field technicians, service managers, and owners natural-language access to live HVAC telemetry, technical documentation, and operational tools. Using the Strands framework with Amazon Bedrock AgentCore, AgentCore Gateway, AgentCore Memory, CloudWatch observability, and Anthropic Claude models on Amazon Bedrock, the system reduced a dashboard-based diagnostic workflow reported to take 20 minutes to approximately 20 seconds in internal benchmarking. The implementation also introduced role-aware responses, session isolation, tool-level integrations, guardrails, and a phased internal-beta rollout, although the published results are vendor-authored and provide limited detail about accuracy, costs, adoption, or comparison with non-agent alternatives.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-trane-gets-building-insights-60x-faster-with-amazon-bedrock-agentcore/)

---

#### Operating Identity-Aware Digital Employees at Enterprise Scale

**Company:** china_merchants_bank  
**Industry:** Finance

China Merchants Bank describes an enterprise platform for operating more than 20,000 digital employee agents, 200 domain experts, and over 10,000 registered skills across employee-facing workflows. The approach treats agents as persistent production services rather than isolated model-and-tool demos: channel adapters normalize events, a harness and runtime manage context and state, Kubernetes and microVM-based sandboxes isolate execution, and an MCP gateway governs access to enterprise capabilities. Identity separation, role-based permissions, approvals, tracing, cost accounting, recovery checkpoints, and audit records are intended to make agent behavior observable and controllable. The presentation reports the scale and design of the platform, but does not provide independent task-quality, reliability, latency, or return-on-investment measurements, so the operational benefits should be understood as an architecture and engineering account rather than a quantified outcome study.

[Read source](https://www.youtube.com/watch?v=KRuU_nhoMH0)

---

#### Multi-Agent Open Finance Onboarding on Amazon Bedrock

**Company:** ninth_wave  
**Industry:** Finance

Ninth Wave built Compass to reduce the specialist effort required to validate bank APIs, map fields to the Financial Data Exchange (FDX) standard, answer integration questions, and assess readiness for production connectivity. The production system uses a Strands Agents orchestrator on Amazon Bedrock AgentCore, seven task-focused specialist agents, tenant-scoped grounding from Amazon OpenSearch Service and Amazon S3, and a narrowly scoped Amazon Bedrock Knowledge Base for readiness analysis. It combines per-task model selection, deterministic readiness scoring, application-layer safety controls, and AWS security and observability services. Ninth Wave reports a 95 percent reduction in API mapping and analysis time, although the source does not provide the baseline, measurement methodology, sample size, or independent validation for that result.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-ninth-wave-built-ai-powered-open-finance-onboarding-on-amazon-bedrock/)

---

#### Governed Self-Service AI Agents for a Regulated Insurance Broker

**Company:** mrh_trowe  
**Industry:** Insurance

MRH Trowe needed to give employees practical access to generative AI without exposing sensitive insurance and client information through unmanaged tools. It deployed a centrally governed platform combining LibreChat, Strands Agents, Amazon Bedrock AgentCore, AWS networking and identity controls, and multiple storage and retrieval services. The first production agent converts Microsoft Teams meeting transcripts into structured minutes while enforcing employee-level access and German data residency. The environment reached approximately 400 employees in its first month, with reported infrastructure and token costs of about $14 per seat per month, although the source provides limited independent evidence about productivity gains, response quality, or the effectiveness of the proposed future cost reductions.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-mrh-trowe-enabled-secure-self-service-ai-agents-in-financial-services/)

---

#### Governed AI Ticket Triage and Operational Knowledge Enrichment

**Company:** aderant  
**Industry:** Legal

Aderant built an Intelligent Ticket Analyzer to reduce the manual investigation required by its 38-person SierraOps team when triaging support tickets across 268 client environments. The serverless workflow uses Amazon Nova Lite through Amazon Bedrock to combine Jira tickets with operational metadata and internal knowledge from Amazon Athena, Confluence, SharePoint, and prior Jira resolutions, then recommend classifications, routing, and next steps. It can perform approved actions such as reassignment and notifications, while sending lower-confidence cases for human review. During the initial 2.5-week production period in 2026, it analyzed 109 tickets with approximately 96% routing accuracy, and Aderant estimated 8–14 engineering hours recovered per week at a total operating cost below $30 per month. These are early operational results rather than a long-term benchmark, and the case demonstrates a controlled automation pattern rather than fully autonomous incident resolution.

[Read source](https://aws.amazon.com/blogs/machine-learning/aderant-builds-intelligent-ticket-triage-with-amazon-nova/)

---

#### Agentic Disaster Recovery Orchestration for Production Failover

**Company:** intuit  
**Industry:** Finance

Intuit extended its deterministic Ecosystem Wide Orchestrator Kit (EWOK) disaster-recovery platform with EWOK Agent, an Amazon Bedrock-based agent that interprets plain-language failover requests, selects versioned operational skills, validates readiness and policy gates, and invokes audited EWOK APIs. The architecture deliberately limits the model to deciding what operation is appropriate while conventional executors determine how production actions are authenticated and performed. Intuit reports that teams had used the agent for eight months and that EWOK-supported failovers already reduced execution time from several hours to about 20 minutes; however, the source does not provide independent measurements of the agent’s accuracy, incident reduction, cost, or failure rate, and the implementation examples are illustrative rather than a complete deployable system.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-intuit-built-an-agentic-disaster-recovery-assistant-with-amazon-bedrock/)

---

#### A Governed MCP Knowledge Assistant for Enterprise Technology Teams

**Company:** hema  
**Industry:** E-commerce

HEMA addressed fragmented internal technology knowledge by building HAL, an AI assistant that combines Amazon Bedrock Knowledge Bases, retrieval-augmented generation, live internal APIs, and Model Context Protocol (MCP). Hosted with Amazon Bedrock AgentCore and built with the Strands framework, HAL provides role-appropriate answers through its own web chat as well as tools such as Kiro and Claude, while using Microsoft Entra ID, Active Directory groups, OAuth, IAM, guardrails, and read-only access controls. HEMA reports that tasks that previously required navigating several portals can now be completed in seconds, although the source provides no quantitative accuracy, adoption, latency, or cost metrics and the assistant remains primarily a read-only knowledge layer.

[Read source](https://aws.amazon.com/blogs/machine-learning/from-portal-hopping-to-instant-answers-hemas-journey-with-mcp-and-amazon-bedrock/)

---

#### Preparing Enterprise Data Platforms for Secure, Cost-Efficient AI Agents

**Company:** totvs  
**Industry:** Tech

Totvs, a Brazilian enterprise software provider whose systems support a substantial share of the country’s economic activity, is adapting its data architecture for production AI agents. The central challenge is that transactional systems and conventional data lakes were designed for applications, analysts, and dashboards rather than token-hungry, latency-sensitive agents making unpredictable queries. Totvs combines transactional databases with a multi-layer data platform, governed data products, semantic-web ontologies, low-latency PostgreSQL services, parameterized MCP tools, OAuth-based identity propagation, and dynamic tool search. The approach is intended to improve precision, security, freshness, and token economics, although the presentation reports limited production metrics and acknowledges tradeoffs involving stale data, reduced flexibility, ontology maintenance, and the probabilistic nature of LLM responses.

[Read source](https://www.infoq.com/presentations/enterprise-data-architecture-ai-agents/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations)

---

#### Scaling Secure AI-Agent Sandboxes with Stateful MicroVMs

**Company:** unikraft  
**Industry:** Tech

Unikraft addresses the infrastructure challenge of running large numbers of intermittently used AI-agent sandboxes, headless browsers, development environments, and functions without sacrificing isolation or responsiveness. Its platform converts Dockerfile-defined workloads into lightweight Firecracker-based virtual machines, uses minimal Linux or unikernel images, snapshots, differential compression, shared-memory communication, and scale-to-zero lifecycle management to reduce cold starts and increase density. The presentation reports approximately 10 millisecond startup behavior in benchmark scenarios and demonstrates one million sleeping nginx instances on a server, but these figures are engineering demonstrations rather than independently validated production results; active-capacity limits, storage costs, scheduling contention, networking, and credential security remain important constraints.

[Read source](https://www.infoq.com/presentations/unikraft-microvm-sandboxes-cloud-scaling/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations)

---

### Cool Use Cases

#### On-Premises Agentic Troubleshooting for Disaster Recovery Operations

**Company:** hpe_zerto  
**Industry:** Tech

HPE Zerto built an agentic troubleshooting assistant embedded in its on-premises disaster recovery management product to help operators investigate alerts, configuration problems, replication failures, SLA risks, and recovery readiness issues without manually assembling context from multiple dashboards and knowledge sources. The system uses locally hosted Strands Agents orchestration, a Model Context Protocol (MCP) server for structured access to live Zerto Manager data, Amazon Bedrock for foundation-model inference, Bedrock Knowledge Bases for documentation retrieval, and Bedrock Guardrails, CloudWatch, DynamoDB, and Lambda for governance, observability, and tenant limits. HPE Zerto reports that more than 20 percent of customers adopted the capability after its Q2 2026 release and that supported workflows saw a 10 percent reduction in support cases, although the source does not provide independent validation, detailed evaluation scores, or comparisons with preexisting troubleshooting processes.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-hpe-zerto-built-an-agentic-troubleshooting-system-with-amazon-bedrock/)

---

#### Autonomous Operation of a Multi-Machine Vending Business

**Company:** prosus  
**Industry:** E-commerce

Prosus tested whether an LLM-based agent could operate a small physical business by managing six vending machines. The team reverse-engineered the machines’ operator APIs, converted them into agent tools, built a custom point-of-sale system, and deployed a scheduled agent in a VM with browser access, sub-agents, shared human access, persistent business documents, and controlled secret injection. The experiment demonstrated that agents can execute many operational tasks, but also exposed major production challenges: live-system testing caused unintended product dispensing, task completion did not guarantee real-world outcomes, product sourcing lacked business judgment, marketing quality was poor, and pricing optimized revenue more readily than profit. A human operator remained essential for physical restocking, contextual decisions, and correcting the agent’s assumptions; the system generated useful operational learning but was not shown to be profitable after model and operational costs.

[Read source](https://www.youtube.com/watch?v=LJ2MTGvVHm8)

---

#### Trust-Governed Autonomous Agent Payments

**Company:** t54  
**Industry:** Tech

t54 built x402-secure, a trust layer for autonomous agents that need to purchase data and API services without human approval for every transaction. The system combines real-time endpoint and payment-address risk scoring from Trustline with Amazon Bedrock AgentCore payments, session-scoped spending limits, credential isolation, IAM role separation, and CloudWatch and CloudTrail auditing. A deterministic trust gate evaluates each endpoint before payment settlement, while AgentCore handles payment execution and prevents the agent from accessing private keys or changing its own limits. AWS and t54 report more than 20 million agent-initiated micropayments processed since launch, although the source does not provide independent validation, false-positive rates, blocked-payment counts, latency measurements, or comparative cost and reliability data.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments/)

---

#### Scaling Accessible, IDEA-Aligned Transition Planning with a Multi-Agent Architecture

**Company:** trinity  
**Industry:** Education

Trinity is a conversational AI system from University Startups that helps students with disabilities explore goals and produce personalized, IDEA-aligned transition plans for postsecondary education, employment, independent living, and community participation. To move beyond a prototype that combined intake, recommendations, compliance, and plan writing in one prompt, the team and AWS partner g/d/n/a implemented a serverless, hierarchical six-agent architecture on Amazon Bedrock. Specialized agents use purpose-built knowledge bases and hybrid retrieval, while AWS services provide session state, authentication, accessibility, encryption, access control, and real-time interaction. The source reports deployment across more than a dozen U.S. states, plan generation in five to ten seconds after selections are confirmed, and claimed improvements in student agency and educator efficiency; however, it does not provide independent benchmark results, error rates, cost data, or detailed evidence of compliance effectiveness.

[Read source](https://aws.amazon.com/blogs/machine-learning/trinity-agentic-ai-powered-transition-planning-for-students-with-disabilities/)

---

### Tools & Infrastructure

#### Governed AI Enablement for a Banking Internal Developer Platform

**Company:** dkb  
**Industry:** Finance

DKB, a German online bank serving approximately five million customers, is adapting its internal platform and platform-experience practices for AI-assisted software development. The discussion describes using AI and agentic tooling to improve documentation, analyze infrastructure and repositories, answer first-line developer questions, interpret logs, and generate organization-specific infrastructure code through internal skills and MCP servers. The approach keeps human intent, least privilege, compliance, auditing, and deterministic deployment controls at the center, because faster code generation shifts bottlenecks toward security, governance, CI/CD capacity, and operational accountability. The source reports no formal DKB outcome metrics; proposed measures include onboarding time, time from idea to production, developer trust and satisfaction, support-request volume, incidents, bugs, and relevant DORA metrics.

[Read source](https://www.infoq.com/presentations/ai-platform-engineering-roundtable/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations)

---

#### Healthcare Voice Scheduling Agent with Progressive Authentication and Latency Masking

**Company:** natera  
**Industry:** Healthcare

Natera replaced a container-based voice scheduling workflow with a production voice agent for mobile phlebotomy appointments, using Amazon Bedrock AgentCore Runtime and Memory, Amazon Bedrock foundation models, retrieval-augmented generation, and integrations with telephony, identity, vendor, and scheduling services. The architecture uses a dual-WebSocket bridge, event-driven filler responses to mask backend delays, and progressive authentication to control access to patient context. AWS reports 100% tool-calling and parameter accuracy across 500 simulated calls, over 90% accuracy for general patient inquiries, a 6.8-second median perceived latency, and a per-call cost below USD 0.01 in the stated evaluation. In an early four-week production comparison, the system handled 4,744 calls, reduced calls ending within 30 seconds from 22% to 12%, and slightly improved verification completion, although the reported metrics are vendor-published and should be independently validated under representative clinical operating conditions.

[Read source](https://aws.amazon.com/blogs/machine-learning/nateras-intelligent-appointment-scheduling-with-amazon-bedrock-agentcore/)

---

#### Automating Scheduled Mobile Commerce Updates with Multi-Agent Workflows

**Company:** reactiv  
**Industry:** E-commerce

Reactiv, a mobile commerce platform for Shopify merchants, used Amazon Bedrock AgentCore and the Strands Agents SDK to automate recurring mobile-app updates that previously required substantial manual configuration. A scheduled, three-agent workflow uses EventBridge, Lambda, Redshift text-to-SQL queries, MCP-hosted configuration tools, persistent per-merchant memory, and Bedrock foundation models to generate app changes for merchant approval. Reactiv reports an 80% reduction in configuration time, a 33% faster path to production, approximately $6,000 in annual compute savings, and a reduction in scheduled-job duration from more than 10 minutes to about 5 minutes; these are vendor-reported internal measurements rather than independently validated results.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-reactiv-automates-mobile-commerce-80-faster-with-amazon-bedrock-agentcore/)

---

#### LLM-assisted last-mile validation for business intelligence dashboards

**Company:** aws  
**Industry:** Tech

AWS built a serverless monitoring system to detect dashboard failures that conventional infrastructure and data-pipeline monitoring could not see, including blank visuals, stale or incorrect content, and cross-dashboard numeric inconsistencies. The system uses Amazon Bedrock models for semantic visual analysis, metric identification, and browser-based dashboard inspection, while redaction, deterministic numeric comparison, confidence thresholds, human review, and owner-based alerting constrain the models’ role. In 30 days of visual-validation production data, it performed 153,000 checks across hundreds of dashboards, detected 802 content failures, and reduced mean time to detection from as much as 72 hours to less than one hour; the article reports positive operational results but provides limited independent evaluation, cost data, or detailed precision and recall measurements beyond a cited extraction recall improvement.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-an-aws-team-detects-dashboard-content-failures-at-scale-using-amazon-bedrock/)

---

#### Production AI Assistant for Incident Investigation and Remediation

**Company:** ramp  
**Industry:** Finance

Ramp built OCA, an AI on-call assistant that joins incident Slack channels, investigates likely causes using production-readonly tools and the application monorepo, posts interim and final findings, answers follow-up questions, and can ask a separate background agent to prepare pull requests. OCA is orchestrated with Temporal and operated with human review and narrowly scoped write access. In the four weeks described, it assisted with 575 of 1,220 incident-related merged pull requests; among incidents with merged fixes, OCA-assisted fixes were associated with 37% fewer engineers and approximately 50% less estimated engineer time, while responders rated it helpful 90% of the time. These results are based on internal activity estimates and coarse feedback, so they indicate promising operational impact rather than a controlled causal evaluation.

[Read source](https://builders.ramp.com/post/how-we-built-oca-our-ai-on-call-assistant)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Simulation-Driven Testing and Continuous Improvement for Multi-Turn AI Agents

**Company:** arklex  
**Industry:** Tech

Arklex applies LLM-based user simulation to the testing and improvement of production-oriented AI agents, addressing the limits of manual testing and static single-turn benchmarks. Synthetic users are generated from personas, goals, agent capabilities, and contextual knowledge, then used to exercise conversational and workflow agents through multi-turn trajectories, tool calls, and optional interface actions. The resulting simulations are integrated into CI/CD, scored with task-specific rules and LLM-as-judge metrics, and compared with production logs to evolve a golden scenario set. The approach is presented as reducing manual testing and exposing edge cases earlier, with reported work involving Pearson, but the source provides no independently validated quantitative results and acknowledges that simulation quality depends on expert input, realistic data, and ongoing calibration.

[Read source](https://www.infoq.com/presentations/ai-agent-testing-evaluation/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations)

---

#### AI-Native Investment Research with Governed Per-Query Data Purchasing

**Company:** heurist_finance  
**Industry:** Finance

Heurist Finance built a production investment-research workbench for retail investors that combines portfolio-aware analysis, premium market data, financial research, scenario analysis, and monitoring in a conversational interface. Its agents are orchestrated with Strands and Anthropic Claude on Amazon Bedrock, while Amazon Bedrock AgentCore provides identity, cross-session memory, isolated code execution, observability, and per-query payments for premium data accessed through the x402 protocol. The architecture links user identity, spending limits, payment credentials, data access, analysis artifacts, and traces into an auditable workflow. AWS and Heurist report that managed infrastructure reduced the estimated agent-system engineering effort by roughly 80% and saved months of platform development, although the source does not provide independent validation of these claims or detailed production quality, cost, latency, or investment-outcome metrics.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-heurist-finance-built-an-ai-native-investment-workbench-on-amazon-bedrock-agentcore/)

---

#### Multi-Agent Contract Playbook Review with Conflict-Aware Redlining

**Company:** harvey  
**Industry:** Legal

Harvey rebuilt its contract playbook review system from a sequential prompt pipeline into an orchestrator-worker multi-agent architecture. The system assigns individual playbook rules to parallel agents that can search and inspect a versioned document, classify risk, propose minimal tracked edits, and produce rationale, while a lead agent reconciles conflicting changes and validates the complete review. On Harvey's internal benchmark, risk-classification performance increased from 59% to 77% and redline-rubric performance from 53% to 87%, while average latency increased from 2.6 to 3.8 minutes. The reported results indicate a substantial quality improvement, but they are based on an in-house evaluation using legal-defined rubrics and LLM judges, so they should not be treated as independently validated production outcomes.

[Read source](https://www.harvey.ai/blog/rebuilding-playbook-review-as-a-multi-agent-system)

---

#### Production Quality Assurance for Real-Time Executive AI Answers

**Company:** narrateai  
**Industry:** Tech

NarrateAI provides a conversational agentic AI assistant that helps more than 4,000 AWS executive leaders answer business-intelligence questions during live business reviews. To address hallucinated metrics, slow validation, API throttling, and inconsistent presentation, the system combines adaptive retrieval and analysis routing, cross-account and multi-model Amazon Bedrock failover, paragraph-level streaming evaluation, parallel specialist evaluators, and a two-stage numerical grounding check. AWS reports approximately 13-second median time to first evaluated content, approximately 99% numerical accuracy, a 86.8% latency reduction versus sequential post-generation evaluation, and sustained availability in its six-month deployment and load tests; these results are deployment-specific and should be independently validated for other workloads.

[Read source](https://aws.amazon.com/blogs/machine-learning/narrateai-production-ready-llm-quality-assurance-on-amazon-bedrock/)

---

### Industry News

#### A Shared Production Platform for Governed Enterprise Agents

**Company:** wood_mackenzie  
**Industry:** Energy

Wood Mackenzie built APEX (Agentic Platform for Energy eXperience), a shared platform on Amazon Bedrock AgentCore, to move multiple agentic AI applications from prototypes into governed production. APEX centralizes runtime hosting, identity and entitlements, tool connectivity, memory, retrieval, guardrails, observability, evaluation, and generative user interfaces, while allowing product teams to choose different agent frameworks and models. The platform supports internal workflows in Woody, external-facing assistance in Lens AI, and trading use cases through common infrastructure. The source reports faster delivery and reduced duplicated engineering, but does not provide independent production-quality, cost, accuracy, or adoption metrics; many benefits remain architectural claims and planned capabilities rather than quantitatively validated outcomes.

[Read source](https://aws.amazon.com/blogs/machine-learning/a-shared-agentic-platform-for-wood-mackenzie-on-amazon-bedrock-agentcore/)

---

#### Multichannel Customer-Service Agents with Model Routing and Production Evaluation

**Company:** ringg  
**Industry:** Tech

Ringg built a multichannel enterprise agent platform for voice, chat, WhatsApp, and web interactions, using OpenAI models, retrieval, tool orchestration, specialized subagents, and human escalation to automate customer-service workflows. The platform reportedly handles more than 7 million connected calls per month, resolves up to 65% of routine inquiries without human involvement, and achieves an average CSAT of 4.8. Ringg uses model routing, historical and simulated evaluations, canary deployments, endpoint monitoring, structured conversation summarization, and regional failover to balance quality, latency, reliability, and cost; it reports approximately 90% lower model costs for selected workloads after migrating them from GPT-4.1 to GPT-5.6. These results are vendor-reported and are not accompanied in the source by independent validation or detailed measurement methodology.

[Read source](https://openai.com/index/ringg/)

---

#### Scaling Context-Aware Coding Agents with MCP Playbooks

**Company:** linkedin  
**Industry:** Tech

LinkedIn found that generic AI coding agents performed poorly against its large, mature codebase because they lacked internal architectural knowledge, procedural guidance, and reliable access to company systems. It built a local Model Context Protocol (MCP) server that exposes code search, documentation, operational systems, and authentication alongside centrally managed and repository-specific playbooks containing procedural memory. A catalog-search layer keeps thousands of tools and playbooks usable without overwhelming the model context window, while code review, InfoSec review, usage metrics, verification steps, and human confirmation provide operational guardrails. LinkedIn reports more than 8,000 daily users, over 600 playbooks, approximately 20% higher productivity, and no observed decrease in reliability or quality, although these outcomes are company-reported and the presentation does not describe a controlled evaluation.

[Read source](https://www.infoq.com/presentations/linkedin-context-engineering/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations)

---

#### Conversational HVAC Diagnostics and Building Intelligence

**Company:** trane  
**Industry:** Other

Trane Technologies built a multi-agent conversational system that gives building operators, field technicians, service managers, and owners natural-language access to live HVAC telemetry, technical documentation, and operational tools. Using the Strands framework with Amazon Bedrock AgentCore, AgentCore Gateway, AgentCore Memory, CloudWatch observability, and Anthropic Claude models on Amazon Bedrock, the system reduced a dashboard-based diagnostic workflow reported to take 20 minutes to approximately 20 seconds in internal benchmarking. The implementation also introduced role-aware responses, session isolation, tool-level integrations, guardrails, and a phased internal-beta rollout, although the published results are vendor-authored and provide limited detail about accuracy, costs, adoption, or comparison with non-agent alternatives.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-trane-gets-building-insights-60x-faster-with-amazon-bedrock-agentcore/)

---

#### Operating Identity-Aware Digital Employees at Enterprise Scale

**Company:** china_merchants_bank  
**Industry:** Finance

China Merchants Bank describes an enterprise platform for operating more than 20,000 digital employee agents, 200 domain experts, and over 10,000 registered skills across employee-facing workflows. The approach treats agents as persistent production services rather than isolated model-and-tool demos: channel adapters normalize events, a harness and runtime manage context and state, Kubernetes and microVM-based sandboxes isolate execution, and an MCP gateway governs access to enterprise capabilities. Identity separation, role-based permissions, approvals, tracing, cost accounting, recovery checkpoints, and audit records are intended to make agent behavior observable and controllable. The presentation reports the scale and design of the platform, but does not provide independent task-quality, reliability, latency, or return-on-investment measurements, so the operational benefits should be understood as an architecture and engineering account rather than a quantified outcome study.

[Read source](https://www.youtube.com/watch?v=KRuU_nhoMH0)

---

#### Multi-Agent Open Finance Onboarding on Amazon Bedrock

**Company:** ninth_wave  
**Industry:** Finance

Ninth Wave built Compass to reduce the specialist effort required to validate bank APIs, map fields to the Financial Data Exchange (FDX) standard, answer integration questions, and assess readiness for production connectivity. The production system uses a Strands Agents orchestrator on Amazon Bedrock AgentCore, seven task-focused specialist agents, tenant-scoped grounding from Amazon OpenSearch Service and Amazon S3, and a narrowly scoped Amazon Bedrock Knowledge Base for readiness analysis. It combines per-task model selection, deterministic readiness scoring, application-layer safety controls, and AWS security and observability services. Ninth Wave reports a 95 percent reduction in API mapping and analysis time, although the source does not provide the baseline, measurement methodology, sample size, or independent validation for that result.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-ninth-wave-built-ai-powered-open-finance-onboarding-on-amazon-bedrock/)

---

#### Governed Self-Service AI Agents for a Regulated Insurance Broker

**Company:** mrh_trowe  
**Industry:** Insurance

MRH Trowe needed to give employees practical access to generative AI without exposing sensitive insurance and client information through unmanaged tools. It deployed a centrally governed platform combining LibreChat, Strands Agents, Amazon Bedrock AgentCore, AWS networking and identity controls, and multiple storage and retrieval services. The first production agent converts Microsoft Teams meeting transcripts into structured minutes while enforcing employee-level access and German data residency. The environment reached approximately 400 employees in its first month, with reported infrastructure and token costs of about $14 per seat per month, although the source provides limited independent evidence about productivity gains, response quality, or the effectiveness of the proposed future cost reductions.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-mrh-trowe-enabled-secure-self-service-ai-agents-in-financial-services/)

---

#### Governed AI Ticket Triage and Operational Knowledge Enrichment

**Company:** aderant  
**Industry:** Legal

Aderant built an Intelligent Ticket Analyzer to reduce the manual investigation required by its 38-person SierraOps team when triaging support tickets across 268 client environments. The serverless workflow uses Amazon Nova Lite through Amazon Bedrock to combine Jira tickets with operational metadata and internal knowledge from Amazon Athena, Confluence, SharePoint, and prior Jira resolutions, then recommend classifications, routing, and next steps. It can perform approved actions such as reassignment and notifications, while sending lower-confidence cases for human review. During the initial 2.5-week production period in 2026, it analyzed 109 tickets with approximately 96% routing accuracy, and Aderant estimated 8–14 engineering hours recovered per week at a total operating cost below $30 per month. These are early operational results rather than a long-term benchmark, and the case demonstrates a controlled automation pattern rather than fully autonomous incident resolution.

[Read source](https://aws.amazon.com/blogs/machine-learning/aderant-builds-intelligent-ticket-triage-with-amazon-nova/)

---

#### Agentic Disaster Recovery Orchestration for Production Failover

**Company:** intuit  
**Industry:** Finance

Intuit extended its deterministic Ecosystem Wide Orchestrator Kit (EWOK) disaster-recovery platform with EWOK Agent, an Amazon Bedrock-based agent that interprets plain-language failover requests, selects versioned operational skills, validates readiness and policy gates, and invokes audited EWOK APIs. The architecture deliberately limits the model to deciding what operation is appropriate while conventional executors determine how production actions are authenticated and performed. Intuit reports that teams had used the agent for eight months and that EWOK-supported failovers already reduced execution time from several hours to about 20 minutes; however, the source does not provide independent measurements of the agent’s accuracy, incident reduction, cost, or failure rate, and the implementation examples are illustrative rather than a complete deployable system.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-intuit-built-an-agentic-disaster-recovery-assistant-with-amazon-bedrock/)

---

#### A Governed MCP Knowledge Assistant for Enterprise Technology Teams

**Company:** hema  
**Industry:** E-commerce

HEMA addressed fragmented internal technology knowledge by building HAL, an AI assistant that combines Amazon Bedrock Knowledge Bases, retrieval-augmented generation, live internal APIs, and Model Context Protocol (MCP). Hosted with Amazon Bedrock AgentCore and built with the Strands framework, HAL provides role-appropriate answers through its own web chat as well as tools such as Kiro and Claude, while using Microsoft Entra ID, Active Directory groups, OAuth, IAM, guardrails, and read-only access controls. HEMA reports that tasks that previously required navigating several portals can now be completed in seconds, although the source provides no quantitative accuracy, adoption, latency, or cost metrics and the assistant remains primarily a read-only knowledge layer.

[Read source](https://aws.amazon.com/blogs/machine-learning/from-portal-hopping-to-instant-answers-hemas-journey-with-mcp-and-amazon-bedrock/)

---

#### Preparing Enterprise Data Platforms for Secure, Cost-Efficient AI Agents

**Company:** totvs  
**Industry:** Tech

Totvs, a Brazilian enterprise software provider whose systems support a substantial share of the country’s economic activity, is adapting its data architecture for production AI agents. The central challenge is that transactional systems and conventional data lakes were designed for applications, analysts, and dashboards rather than token-hungry, latency-sensitive agents making unpredictable queries. Totvs combines transactional databases with a multi-layer data platform, governed data products, semantic-web ontologies, low-latency PostgreSQL services, parameterized MCP tools, OAuth-based identity propagation, and dynamic tool search. The approach is intended to improve precision, security, freshness, and token economics, although the presentation reports limited production metrics and acknowledges tradeoffs involving stale data, reduced flexibility, ontology maintenance, and the probabilistic nature of LLM responses.

[Read source](https://www.infoq.com/presentations/enterprise-data-architecture-ai-agents/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations)

---

#### Scaling Secure AI-Agent Sandboxes with Stateful MicroVMs

**Company:** unikraft  
**Industry:** Tech

Unikraft addresses the infrastructure challenge of running large numbers of intermittently used AI-agent sandboxes, headless browsers, development environments, and functions without sacrificing isolation or responsiveness. Its platform converts Dockerfile-defined workloads into lightweight Firecracker-based virtual machines, uses minimal Linux or unikernel images, snapshots, differential compression, shared-memory communication, and scale-to-zero lifecycle management to reduce cold starts and increase density. The presentation reports approximately 10 millisecond startup behavior in benchmark scenarios and demonstrates one million sleeping nginx instances on a server, but these figures are engineering demonstrations rather than independently validated production results; active-capacity limits, storage costs, scheduling contention, networking, and credential security remain important constraints.

[Read source](https://www.infoq.com/presentations/unikraft-microvm-sandboxes-cloud-scaling/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations)

---

### Cool Use Cases

#### On-Premises Agentic Troubleshooting for Disaster Recovery Operations

**Company:** hpe_zerto  
**Industry:** Tech

HPE Zerto built an agentic troubleshooting assistant embedded in its on-premises disaster recovery management product to help operators investigate alerts, configuration problems, replication failures, SLA risks, and recovery readiness issues without manually assembling context from multiple dashboards and knowledge sources. The system uses locally hosted Strands Agents orchestration, a Model Context Protocol (MCP) server for structured access to live Zerto Manager data, Amazon Bedrock for foundation-model inference, Bedrock Knowledge Bases for documentation retrieval, and Bedrock Guardrails, CloudWatch, DynamoDB, and Lambda for governance, observability, and tenant limits. HPE Zerto reports that more than 20 percent of customers adopted the capability after its Q2 2026 release and that supported workflows saw a 10 percent reduction in support cases, although the source does not provide independent validation, detailed evaluation scores, or comparisons with preexisting troubleshooting processes.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-hpe-zerto-built-an-agentic-troubleshooting-system-with-amazon-bedrock/)

---

#### Autonomous Operation of a Multi-Machine Vending Business

**Company:** prosus  
**Industry:** E-commerce

Prosus tested whether an LLM-based agent could operate a small physical business by managing six vending machines. The team reverse-engineered the machines’ operator APIs, converted them into agent tools, built a custom point-of-sale system, and deployed a scheduled agent in a VM with browser access, sub-agents, shared human access, persistent business documents, and controlled secret injection. The experiment demonstrated that agents can execute many operational tasks, but also exposed major production challenges: live-system testing caused unintended product dispensing, task completion did not guarantee real-world outcomes, product sourcing lacked business judgment, marketing quality was poor, and pricing optimized revenue more readily than profit. A human operator remained essential for physical restocking, contextual decisions, and correcting the agent’s assumptions; the system generated useful operational learning but was not shown to be profitable after model and operational costs.

[Read source](https://www.youtube.com/watch?v=LJ2MTGvVHm8)

---

#### Trust-Governed Autonomous Agent Payments

**Company:** t54  
**Industry:** Tech

t54 built x402-secure, a trust layer for autonomous agents that need to purchase data and API services without human approval for every transaction. The system combines real-time endpoint and payment-address risk scoring from Trustline with Amazon Bedrock AgentCore payments, session-scoped spending limits, credential isolation, IAM role separation, and CloudWatch and CloudTrail auditing. A deterministic trust gate evaluates each endpoint before payment settlement, while AgentCore handles payment execution and prevents the agent from accessing private keys or changing its own limits. AWS and t54 report more than 20 million agent-initiated micropayments processed since launch, although the source does not provide independent validation, false-positive rates, blocked-payment counts, latency measurements, or comparative cost and reliability data.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments/)

---

#### Scaling Accessible, IDEA-Aligned Transition Planning with a Multi-Agent Architecture

**Company:** trinity  
**Industry:** Education

Trinity is a conversational AI system from University Startups that helps students with disabilities explore goals and produce personalized, IDEA-aligned transition plans for postsecondary education, employment, independent living, and community participation. To move beyond a prototype that combined intake, recommendations, compliance, and plan writing in one prompt, the team and AWS partner g/d/n/a implemented a serverless, hierarchical six-agent architecture on Amazon Bedrock. Specialized agents use purpose-built knowledge bases and hybrid retrieval, while AWS services provide session state, authentication, accessibility, encryption, access control, and real-time interaction. The source reports deployment across more than a dozen U.S. states, plan generation in five to ten seconds after selections are confirmed, and claimed improvements in student agency and educator efficiency; however, it does not provide independent benchmark results, error rates, cost data, or detailed evidence of compliance effectiveness.

[Read source](https://aws.amazon.com/blogs/machine-learning/trinity-agentic-ai-powered-transition-planning-for-students-with-disabilities/)

---

### Tools & Infrastructure

#### Governed AI Enablement for a Banking Internal Developer Platform

**Company:** dkb  
**Industry:** Finance

DKB, a German online bank serving approximately five million customers, is adapting its internal platform and platform-experience practices for AI-assisted software development. The discussion describes using AI and agentic tooling to improve documentation, analyze infrastructure and repositories, answer first-line developer questions, interpret logs, and generate organization-specific infrastructure code through internal skills and MCP servers. The approach keeps human intent, least privilege, compliance, auditing, and deterministic deployment controls at the center, because faster code generation shifts bottlenecks toward security, governance, CI/CD capacity, and operational accountability. The source reports no formal DKB outcome metrics; proposed measures include onboarding time, time from idea to production, developer trust and satisfaction, support-request volume, incidents, bugs, and relevant DORA metrics.

[Read source](https://www.infoq.com/presentations/ai-platform-engineering-roundtable/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations)

---

#### Healthcare Voice Scheduling Agent with Progressive Authentication and Latency Masking

**Company:** natera  
**Industry:** Healthcare

Natera replaced a container-based voice scheduling workflow with a production voice agent for mobile phlebotomy appointments, using Amazon Bedrock AgentCore Runtime and Memory, Amazon Bedrock foundation models, retrieval-augmented generation, and integrations with telephony, identity, vendor, and scheduling services. The architecture uses a dual-WebSocket bridge, event-driven filler responses to mask backend delays, and progressive authentication to control access to patient context. AWS reports 100% tool-calling and parameter accuracy across 500 simulated calls, over 90% accuracy for general patient inquiries, a 6.8-second median perceived latency, and a per-call cost below USD 0.01 in the stated evaluation. In an early four-week production comparison, the system handled 4,744 calls, reduced calls ending within 30 seconds from 22% to 12%, and slightly improved verification completion, although the reported metrics are vendor-published and should be independently validated under representative clinical operating conditions.

[Read source](https://aws.amazon.com/blogs/machine-learning/nateras-intelligent-appointment-scheduling-with-amazon-bedrock-agentcore/)

---

#### Automating Scheduled Mobile Commerce Updates with Multi-Agent Workflows

**Company:** reactiv  
**Industry:** E-commerce

Reactiv, a mobile commerce platform for Shopify merchants, used Amazon Bedrock AgentCore and the Strands Agents SDK to automate recurring mobile-app updates that previously required substantial manual configuration. A scheduled, three-agent workflow uses EventBridge, Lambda, Redshift text-to-SQL queries, MCP-hosted configuration tools, persistent per-merchant memory, and Bedrock foundation models to generate app changes for merchant approval. Reactiv reports an 80% reduction in configuration time, a 33% faster path to production, approximately $6,000 in annual compute savings, and a reduction in scheduled-job duration from more than 10 minutes to about 5 minutes; these are vendor-reported internal measurements rather than independently validated results.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-reactiv-automates-mobile-commerce-80-faster-with-amazon-bedrock-agentcore/)

---

#### LLM-assisted last-mile validation for business intelligence dashboards

**Company:** aws  
**Industry:** Tech

AWS built a serverless monitoring system to detect dashboard failures that conventional infrastructure and data-pipeline monitoring could not see, including blank visuals, stale or incorrect content, and cross-dashboard numeric inconsistencies. The system uses Amazon Bedrock models for semantic visual analysis, metric identification, and browser-based dashboard inspection, while redaction, deterministic numeric comparison, confidence thresholds, human review, and owner-based alerting constrain the models’ role. In 30 days of visual-validation production data, it performed 153,000 checks across hundreds of dashboards, detected 802 content failures, and reduced mean time to detection from as much as 72 hours to less than one hour; the article reports positive operational results but provides limited independent evaluation, cost data, or detailed precision and recall measurements beyond a cited extraction recall improvement.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-an-aws-team-detects-dashboard-content-failures-at-scale-using-amazon-bedrock/)

---

#### Production AI Assistant for Incident Investigation and Remediation

**Company:** ramp  
**Industry:** Finance

Ramp built OCA, an AI on-call assistant that joins incident Slack channels, investigates likely causes using production-readonly tools and the application monorepo, posts interim and final findings, answers follow-up questions, and can ask a separate background agent to prepare pull requests. OCA is orchestrated with Temporal and operated with human review and narrowly scoped write access. In the four weeks described, it assisted with 575 of 1,220 incident-related merged pull requests; among incidents with merged fixes, OCA-assisted fixes were associated with 37% fewer engineers and approximately 50% less estimated engineer time, while responders rated it helpful 90% of the time. These results are based on internal activity estimates and coarse feedback, so they indicate promising operational impact rather than a controlled causal evaluation.

[Read source](https://builders.ramp.com/post/how-we-built-oca-our-ai-on-call-assistant)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

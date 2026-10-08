# Weekly LLMOps Newsletter — 2026-10-08

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Automated Documentation and Version Comparison for Integration Workflows

**Company:** boomi_scribe  
**Industry:** Tech

Boomi Scribe addresses the manual, inconsistent, and time-consuming documentation of Boomi integration processes by parsing process XML into structured directed acyclic graph representations, using AWS Lambda to orchestrate a pipeline, and invoking Claude Haiku 4.5 through Amazon Bedrock to generate workflow documentation. It also compares DAG versions with a proprietary Lambda-based algorithm to identify additions, modifications, and deletions. The system stores artifacts in Amazon S3, uses DynamoDB for service data, and incorporates SageMaker AI models for user-intent classification. AWS and Boomi report that the service supports hundreds of processes per customer per day and can reduce documentation effort by up to 85 percent, although the published case study provides limited independent evaluation of factual accuracy, latency, cost, or the quality of the reported time savings.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-boomi-scribe-streamlines-documentation-using-aws/)

---

#### Human-augmented generative reward models for legal AI evaluation

**Company:** harvey  
**Industry:** Legal

Harvey uses lawyer preference judgments to evaluate and improve legal AI systems, but finds that expert agreement is limited because legal quality involves difficult tradeoffs among accuracy, reasoning, grounding, style, tone, and task alignment. To scale scarce legal expertise, Harvey developed lawyer-tuned generative reward models (GRMs): agentic LLM judges that compare two outputs, generate and apply an explicit rubric, verify claims against source materials or the web, and produce an overall recommendation with axis-level reasoning. GRMs recovered human model rankings, increased evaluation-panel agreement, and helped identify that the Tenet model improved substantially over its Kimi K3 base model on accuracy and reasoning, while regressing on tone and style. The results support using GRMs as an expert-assistance and post-training data-generation layer rather than as an autonomous replacement for lawyers, particularly because GRMs sometimes overvalued secondary qualities, selected a winner when both outputs were poor, and exhibited model-family bias.

[Read source](https://x.com/itsjuliopereyra/status/2100631185064173953?s=43)

---

### Industry News

#### Evidence-Based Turnaround Analytics for Airline Operations

**Company:** aviobook  
**Industry:** Other

AvioBook, a Thales Group company, is extending its flight-operations platform with Connected Analytics, an agentic AI capability that lets airline managers and operations control center dispatchers query historical and live turnaround data in natural language. Two role-specific agents use Amazon Bedrock AgentCore, governed MCP tools, and an Amazon S3, AWS Glue, and Amazon Athena data layer to retrieve operational events, validate delay codes as a second opinion, and return answers with supporting evidence. The architecture has been validated through a proof of concept and is being productized, but the source does not provide controlled measurements attributable specifically to the agents; reported financial benefits are illustrative or relate to the underlying AvioBook Connect platform rather than proven Connected Analytics outcomes.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-aviobook-uses-generative-ai-to-drive-airline-turnaround-insights/)

---

#### Operating a Cloud-Based Software Factory for Agentic Development

**Company:** warp  
**Industry:** Tech

Warp has organized AI-assisted software development into a centralized, cloud-executed “software factory” that turns requests from Slack, Linear, GitHub, and external systems into tracked implementation workflows. Factory agents triage work, create issues, modify code, open pull requests, perform QA with computer-use verification, and produce artifacts such as videos. Warp also records agent runs, costs, human interactions, and evaluation scores, then uses aggregate LLM-as-a-judge assessments and observer agents to identify recurring failures and propose updates to the factory configuration. The approach improves automation visibility and reportedly reduces model-related costs after configuration changes, but human review remains a significant bottleneck: implementation can reach a pull request in roughly 35 minutes while first human review takes about three and a half hours. The system therefore demonstrates both the operational value and the unresolved governance, quality, and trust tradeoffs of deploying coding agents at scale.

[Read source](https://www.youtube.com/watch?v=4_SHhSMHzNo)

---

#### Unified AI Platforms for Surgical Intelligence and Pharmaceutical R&D

**Company:** j&j_medtech_/_takeda  
**Industry:** Healthcare

J&J MedTech and Takeda describe a shared strategic approach to putting multimodal AI and generative AI into healthcare production workflows. J&J MedTech’s Polyonic initiative aims to combine operating-room video, robotic kinematics, device telemetry, and electronic health-record data in a governed, device-agnostic platform for surgical scene understanding, clinical documentation, workflow optimization, and future decision support. Takeda is extending an established Databricks data foundation from retrospective reporting toward predictive and generative use cases across drug discovery, clinical development, regulatory submission, and commercial launch. The presentations emphasize that production value depends less on model availability than on contextual data, secure ingestion, interoperability, governance, workflow integration, and measurable business or clinical outcomes; most quantified benefits are presented as targets, benchmarks, or projections rather than independently validated results.

[Read source](https://www.youtube.com/watch?v=ug-TlMhznBw)

---

#### Embedding LLMs into Hertz’s Rental Operations and Customer Experience

**Company:** openai_/_hertz_global_/_databricks  
**Industry:** Automotive

Hertz is using OpenAI models and Databricks to turn operational expertise and large volumes of unstructured customer feedback into production workflows. In insurance-replacement rentals, nontechnical domain experts built a Databricks application that operationalizes a high-performing general manager’s meeting and accountability process, reportedly bringing lower-performing divisions closer to the best-performing standard. In customer experience, models classify phone and survey feedback into employee recognition and operational issues, routing actionable intelligence to managers and systemic teams. The approach emphasizes workflow redesign, human oversight, observability, evaluations, and focused deployment rather than isolated productivity pilots; however, the presentation provides limited independently validated outcome metrics and does not establish that the reported improvements were caused solely by the AI systems.

[Read source](https://www.youtube.com/watch?v=jjxYvFWh4do)

---

#### Production-grade AI application building for product managers

**Company:** aha!  
**Industry:** Tech

Aha! built Aha! Builder to help product managers move from product strategy and customer insight to interactive prototypes, proofs of concept, and medium-complexity business applications without requiring traditional software development skills. The system extends Aha!'s existing AI assistant with a coding-agent harness, phased interview-to-prototype-to-application workflow, deterministic platform components for authentication, user management, email, APIs, databases, and AI features, and hosted deployment with enterprise governance controls. An initial containerized Ruby on Rails implementation proved the user experience but was considered too expensive and inefficient to scale, so Aha! rebuilt the runtime as a multi-tenant JavaScript platform using V8 isolates. Early adoption and internal usage reportedly showed strong interest, while the company positions Builder as complementary to engineering rather than a replacement for teams responsible for core business systems, compliance decisions, and production change management.

[Read source](https://www.youtube.com/watch?v=efIx1QNHDU4)

---

#### Turning Business Questions into Governed Data Pipelines

**Company:** bauplan  
**Industry:** Tech

Bauplan uses an LLM-assisted workflow to let marketing and sales staff ask questions about operational data, inspect the results, and promote valuable or novel analyses into durable data pipelines. A chat-based agent connected through MCP queries a Bauplan lakehouse, asks for clarification when a question requires a new business concept, and can create a structured Linear ticket containing the interpretation, query, job identifier, results, and source tables. GitHub Actions then invokes an AI coding agent that works in a branch, uses Bauplan data tooling to build and test the pipeline, and opens a pull request for human engineering review. The approach reduces the coding barrier for business users while retaining version control, reproducibility, dry runs, and approval gates; however, the presentation provides qualitative results rather than measured accuracy, cost, latency, or productivity improvements, and acknowledges the need for additional classification and aggregation controls at larger scale.

[Read source](https://www.youtube.com/watch?v=mYoGQBl_WUg)

---

#### Building a Prototype-Led Product Organization Around Claude

**Company:** anthropic  
**Industry:** Tech

Anthropic evolved from a research-led frontier-model company into a production software and enterprise platform organization by allowing the capabilities of Claude to guide product development rather than relying solely on long-range market road maps. Product and design teams use Claude, Claude Code, Claude Design, internal MCP-connected tools, Slack analysis, and rapidly deployed prototypes to discover workflows and expose model capabilities through lightweight interfaces such as Artifacts. Internal adoption is used as an early signal before products are hardened for external customers, with enterprise requirements for security, compliance, packaging, and operational reliability added later. The approach has enabled rapid experimentation and new products, but Anthropic acknowledges tradeoffs including inconsistent product mental models, frequent interface changes, weak organizational sources of truth, dependence on production codebases, and the continuing need for human judgment in prioritization, governance, and strategic decisions.

[Read source](https://www.youtube.com/watch?v=rkC3ZsH1HCQ)

---

#### Hybrid LLM Inference at Extreme Request Volume

**Company:** grammarly  
**Industry:** Tech

Grammarly operates an ambient grammatical error correction (GEC) system that analyzes users’ writing continuously and must return suggestions with near-instantaneous latency. To support approximately 40 million daily active users and roughly 100 billion LLM requests per week, the company consolidated several smaller models into a larger model, moved serving from ECS to Kubernetes on Amazon EKS, adopted vLLM with continuous batching, and applied quantization and speculative decoding. It then combined internal serving with Databricks Foundation Model API deployments, validating the external service through shadow traffic, a hardened high-throughput gateway, and production A/B testing. The resulting hybrid architecture provides redundancy and elasticity, although it adds operational complexity and leaves the company dependent on careful vendor evaluation, traffic failover, and ongoing cost and quality monitoring.

[Read source](https://blog.superhuman.com/scaling-gec-inference/)

---

#### Securing Multi-Tenant AI-Generated Code Execution

**Company:** benchling  
**Industry:** Healthcare

Benchling runs AI agent-generated scientific code for life sciences customers and needed to prevent cross-tenant access and data exfiltration at scale without creating an IAM role for every tenant or exposing its production account. It deployed Amazon Bedrock AgentCore Code Interpreter in a separate AWS account and locked it into a VPC with no internet or NAT gateway, Route 53 Resolver DNS Firewall, restricted VPC endpoints, network controls, and per-job AWS STS credentials. Benchling reports that the architecture now supports more than 600 execution sessions per day across more than 250 tenants per week, with zero reported security incidents or cross-tenant data leakage since deployment; however, these results are vendor-reported and do not establish that every possible attack path is eliminated.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-benchling-secured-multi-tenant-ai-agents-with-amazon-bedrock-agentcore/)

---

#### Per-user spend enforcement for production generative AI

**Company:** jamf  
**Industry:** Tech

Jamf expanded Amazon Bedrock access for its engineering organization to support AI-assisted development, but needed visibility and controls for rapidly changing per-user token costs. It built a serverless governance system that records Bedrock invocation logs in Amazon S3, calculates daily user-level spend through an Amazon Athena view, and uses an AWS Lambda function scheduled by Amazon EventBridge to update IAM Customer Managed Policies. As engineers cross configurable spending thresholds, access to expensive models is restricted while a lower-cost model remains available; Slack notifications and a time-boxed exception workflow reduce disruption. The source reports that the architecture costs well under $10 per month for the Lambda, DynamoDB, and S3 components serving hundreds of engineers, while noting that Athena scan volume, pricing maintenance, policy-version limits, and the approximately 15-minute enforcement interval are important operational tradeoffs.

[Read source](https://aws.amazon.com/blogs/machine-learning/tokenomics-at-scale-how-jamf-built-real-time-spend-enforcement-for-amazon-bedrock/)

---

### Cool Use Cases

#### Precomputing Personalized Grocery Reorders for Faster Shopping

**Company:** doordash  
**Industry:** E-commerce

DoorDash improved the Ask DoorDash grocery-reorder experience by moving relatively stable historical reasoning out of the online agent path. A daily pipeline uses up to 90 days of order history and relevant profile signals to generate validated, store-specific bundles of likely recurring needs with batch LLM inference; the request-time system then resolves those needs against live inventory, prices, and catalog listings. For a deterministic “reorder my usuals” entry point, this reduced the reported latency from roughly 16 seconds to roughly 2 seconds, doubled the rate at which consumers viewed the resulting list, and was associated with an approximately 34% increase in order rate for the flow. The approach retains agentic reasoning for ambiguous or dynamic requests, but the published results are company-reported and the article does not provide experimental design or statistical significance details.

[Read source](https://careersatdoordash.com/blog/building-ask-doordash-part-6-grocery-reorder-case-study/)

---

#### A Grounded, Artifact-Based Shopping Interface for Consumer Agents

**Company:** doordash  
**Industry:** E-commerce

DoorDash evolved Ask DoorDash from a chat interface that exposed per-item search carousels into a grounded shopping surface for grocery and restaurant agents. The production design uses an authoritative JSON shopping-list artifact with separate storage, agent, and consumer views; native widgets grounded in live catalog and cart systems; direct client-side edits for deterministic actions; and agent turns for changes requiring judgment. In July 2026, rendered grocery-list sessions averaged nearly two UI interactions, about one-third proceeded to apply the list to a cart, and nearly three-quarters of first follow-up actions occurred through components, although the article reports product usage metrics rather than controlled evidence that the architecture caused these outcomes.

[Read source](https://careersatdoordash.com/blog/building-ask-doordash-part-5-a-grounded-interface-for-shopping-agents/)

---

### Tools & Infrastructure

#### Transparent Multilingual Contact Center QA with LLM Pipelines

**Company:** didi  
**Industry:** Tech

DiDi International Business Group replaced an opaque third-party contact center quality-assurance solution with a self-owned system built on Amazon Bedrock. The production system processes Spanish and Portuguese live-chat and phone conversations across ride-hailing, food-delivery, and financial-services operations through separate intent-verification, compliance-evaluation, and Voice of Customer pipelines. Its design emphasizes precise context management, dynamically assembled prompts, structured model outputs, deterministic post-validation, privacy controls, and human review. DiDi reports that intent-verification accuracy increased from 38% to 86%, compliance-scoring accuracy exceeded 90%, and VOC analysis reduced work that previously took hours to a process completed in minutes; however, the source does not provide independent benchmarks, sample sizes, operating costs, or detailed error analyses.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-didi-built-intelligent-contact-center-qa-with-amazon-bedrock/)

---

#### Sandboxed Agentic Email Threat Detection at Billion-Message Scale

**Company:** abnormal_ai  
**Industry:** Tech

Abnormal AI uses inline LLM-powered agents and Amazon Bedrock AgentCore Code Interpreter to investigate the hardest email threats that simpler rules and machine-learning models cannot confidently classify. The agents receive threat-intelligence data, write and execute analysis code in ephemeral isolated MicroVM sandboxes, and use computational checks to support real-time decisions. Abnormal AI reports processing billions of messages through a tiered pipeline, routing tens of thousands of difficult cases to agents, while a separate batch analyst agent uses misclassification data to propose improved heuristics and models. The AWS account presents this as a production-scale architecture, but the article does not provide independently validated detection-quality, latency, cost, or false-positive metrics.

[Read source](https://aws.amazon.com/blogs/machine-learning/abnormal-ai-amazon-bedrock-agentcore-for-agentic-email-security-at-scale/)

---

#### Japanese Multi-Turn LLM Evaluation Pipeline for Customer-Service AI

**Company:** wevnal  
**Industry:** E-commerce

wevnal and Microsoft engineers used a two-day hackathon to build a reproducible evaluation pipeline for Japanese conversational models supporting customer-service experiences such as BOTCHAN AI Call. The system evaluates 24 models across 39 two-turn conversations, three personas, and four quality facets—brevity, fluency, emotional intelligence, and role-playing—rather than relying on English-centric single-turn benchmarks. It adds benchmark auditing, multi-provider model discovery, price-tier-aware selection, SHA256 content-addressed caching, judge-based scoring, visualizations, and CI-friendly exports. The reported outcome is a production-conscious evaluation foundation that can reduce a broad model candidate set to a smaller shortlist, although the source does not report customer-facing quality improvements, operational deployment, or validation against live call-center KPIs.

[Read source](https://devblogs.microsoft.com/ise/japanese-llm-evaluation-pipeline-hackathon/)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Automated Documentation and Version Comparison for Integration Workflows

**Company:** boomi_scribe  
**Industry:** Tech

Boomi Scribe addresses the manual, inconsistent, and time-consuming documentation of Boomi integration processes by parsing process XML into structured directed acyclic graph representations, using AWS Lambda to orchestrate a pipeline, and invoking Claude Haiku 4.5 through Amazon Bedrock to generate workflow documentation. It also compares DAG versions with a proprietary Lambda-based algorithm to identify additions, modifications, and deletions. The system stores artifacts in Amazon S3, uses DynamoDB for service data, and incorporates SageMaker AI models for user-intent classification. AWS and Boomi report that the service supports hundreds of processes per customer per day and can reduce documentation effort by up to 85 percent, although the published case study provides limited independent evaluation of factual accuracy, latency, cost, or the quality of the reported time savings.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-boomi-scribe-streamlines-documentation-using-aws/)

---

#### Human-augmented generative reward models for legal AI evaluation

**Company:** harvey  
**Industry:** Legal

Harvey uses lawyer preference judgments to evaluate and improve legal AI systems, but finds that expert agreement is limited because legal quality involves difficult tradeoffs among accuracy, reasoning, grounding, style, tone, and task alignment. To scale scarce legal expertise, Harvey developed lawyer-tuned generative reward models (GRMs): agentic LLM judges that compare two outputs, generate and apply an explicit rubric, verify claims against source materials or the web, and produce an overall recommendation with axis-level reasoning. GRMs recovered human model rankings, increased evaluation-panel agreement, and helped identify that the Tenet model improved substantially over its Kimi K3 base model on accuracy and reasoning, while regressing on tone and style. The results support using GRMs as an expert-assistance and post-training data-generation layer rather than as an autonomous replacement for lawyers, particularly because GRMs sometimes overvalued secondary qualities, selected a winner when both outputs were poor, and exhibited model-family bias.

[Read source](https://x.com/itsjuliopereyra/status/2100631185064173953?s=43)

---

### Industry News

#### Evidence-Based Turnaround Analytics for Airline Operations

**Company:** aviobook  
**Industry:** Other

AvioBook, a Thales Group company, is extending its flight-operations platform with Connected Analytics, an agentic AI capability that lets airline managers and operations control center dispatchers query historical and live turnaround data in natural language. Two role-specific agents use Amazon Bedrock AgentCore, governed MCP tools, and an Amazon S3, AWS Glue, and Amazon Athena data layer to retrieve operational events, validate delay codes as a second opinion, and return answers with supporting evidence. The architecture has been validated through a proof of concept and is being productized, but the source does not provide controlled measurements attributable specifically to the agents; reported financial benefits are illustrative or relate to the underlying AvioBook Connect platform rather than proven Connected Analytics outcomes.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-aviobook-uses-generative-ai-to-drive-airline-turnaround-insights/)

---

#### Operating a Cloud-Based Software Factory for Agentic Development

**Company:** warp  
**Industry:** Tech

Warp has organized AI-assisted software development into a centralized, cloud-executed “software factory” that turns requests from Slack, Linear, GitHub, and external systems into tracked implementation workflows. Factory agents triage work, create issues, modify code, open pull requests, perform QA with computer-use verification, and produce artifacts such as videos. Warp also records agent runs, costs, human interactions, and evaluation scores, then uses aggregate LLM-as-a-judge assessments and observer agents to identify recurring failures and propose updates to the factory configuration. The approach improves automation visibility and reportedly reduces model-related costs after configuration changes, but human review remains a significant bottleneck: implementation can reach a pull request in roughly 35 minutes while first human review takes about three and a half hours. The system therefore demonstrates both the operational value and the unresolved governance, quality, and trust tradeoffs of deploying coding agents at scale.

[Read source](https://www.youtube.com/watch?v=4_SHhSMHzNo)

---

#### Unified AI Platforms for Surgical Intelligence and Pharmaceutical R&D

**Company:** j&j_medtech_/_takeda  
**Industry:** Healthcare

J&J MedTech and Takeda describe a shared strategic approach to putting multimodal AI and generative AI into healthcare production workflows. J&J MedTech’s Polyonic initiative aims to combine operating-room video, robotic kinematics, device telemetry, and electronic health-record data in a governed, device-agnostic platform for surgical scene understanding, clinical documentation, workflow optimization, and future decision support. Takeda is extending an established Databricks data foundation from retrospective reporting toward predictive and generative use cases across drug discovery, clinical development, regulatory submission, and commercial launch. The presentations emphasize that production value depends less on model availability than on contextual data, secure ingestion, interoperability, governance, workflow integration, and measurable business or clinical outcomes; most quantified benefits are presented as targets, benchmarks, or projections rather than independently validated results.

[Read source](https://www.youtube.com/watch?v=ug-TlMhznBw)

---

#### Embedding LLMs into Hertz’s Rental Operations and Customer Experience

**Company:** openai_/_hertz_global_/_databricks  
**Industry:** Automotive

Hertz is using OpenAI models and Databricks to turn operational expertise and large volumes of unstructured customer feedback into production workflows. In insurance-replacement rentals, nontechnical domain experts built a Databricks application that operationalizes a high-performing general manager’s meeting and accountability process, reportedly bringing lower-performing divisions closer to the best-performing standard. In customer experience, models classify phone and survey feedback into employee recognition and operational issues, routing actionable intelligence to managers and systemic teams. The approach emphasizes workflow redesign, human oversight, observability, evaluations, and focused deployment rather than isolated productivity pilots; however, the presentation provides limited independently validated outcome metrics and does not establish that the reported improvements were caused solely by the AI systems.

[Read source](https://www.youtube.com/watch?v=jjxYvFWh4do)

---

#### Production-grade AI application building for product managers

**Company:** aha!  
**Industry:** Tech

Aha! built Aha! Builder to help product managers move from product strategy and customer insight to interactive prototypes, proofs of concept, and medium-complexity business applications without requiring traditional software development skills. The system extends Aha!'s existing AI assistant with a coding-agent harness, phased interview-to-prototype-to-application workflow, deterministic platform components for authentication, user management, email, APIs, databases, and AI features, and hosted deployment with enterprise governance controls. An initial containerized Ruby on Rails implementation proved the user experience but was considered too expensive and inefficient to scale, so Aha! rebuilt the runtime as a multi-tenant JavaScript platform using V8 isolates. Early adoption and internal usage reportedly showed strong interest, while the company positions Builder as complementary to engineering rather than a replacement for teams responsible for core business systems, compliance decisions, and production change management.

[Read source](https://www.youtube.com/watch?v=efIx1QNHDU4)

---

#### Turning Business Questions into Governed Data Pipelines

**Company:** bauplan  
**Industry:** Tech

Bauplan uses an LLM-assisted workflow to let marketing and sales staff ask questions about operational data, inspect the results, and promote valuable or novel analyses into durable data pipelines. A chat-based agent connected through MCP queries a Bauplan lakehouse, asks for clarification when a question requires a new business concept, and can create a structured Linear ticket containing the interpretation, query, job identifier, results, and source tables. GitHub Actions then invokes an AI coding agent that works in a branch, uses Bauplan data tooling to build and test the pipeline, and opens a pull request for human engineering review. The approach reduces the coding barrier for business users while retaining version control, reproducibility, dry runs, and approval gates; however, the presentation provides qualitative results rather than measured accuracy, cost, latency, or productivity improvements, and acknowledges the need for additional classification and aggregation controls at larger scale.

[Read source](https://www.youtube.com/watch?v=mYoGQBl_WUg)

---

#### Building a Prototype-Led Product Organization Around Claude

**Company:** anthropic  
**Industry:** Tech

Anthropic evolved from a research-led frontier-model company into a production software and enterprise platform organization by allowing the capabilities of Claude to guide product development rather than relying solely on long-range market road maps. Product and design teams use Claude, Claude Code, Claude Design, internal MCP-connected tools, Slack analysis, and rapidly deployed prototypes to discover workflows and expose model capabilities through lightweight interfaces such as Artifacts. Internal adoption is used as an early signal before products are hardened for external customers, with enterprise requirements for security, compliance, packaging, and operational reliability added later. The approach has enabled rapid experimentation and new products, but Anthropic acknowledges tradeoffs including inconsistent product mental models, frequent interface changes, weak organizational sources of truth, dependence on production codebases, and the continuing need for human judgment in prioritization, governance, and strategic decisions.

[Read source](https://www.youtube.com/watch?v=rkC3ZsH1HCQ)

---

#### Hybrid LLM Inference at Extreme Request Volume

**Company:** grammarly  
**Industry:** Tech

Grammarly operates an ambient grammatical error correction (GEC) system that analyzes users’ writing continuously and must return suggestions with near-instantaneous latency. To support approximately 40 million daily active users and roughly 100 billion LLM requests per week, the company consolidated several smaller models into a larger model, moved serving from ECS to Kubernetes on Amazon EKS, adopted vLLM with continuous batching, and applied quantization and speculative decoding. It then combined internal serving with Databricks Foundation Model API deployments, validating the external service through shadow traffic, a hardened high-throughput gateway, and production A/B testing. The resulting hybrid architecture provides redundancy and elasticity, although it adds operational complexity and leaves the company dependent on careful vendor evaluation, traffic failover, and ongoing cost and quality monitoring.

[Read source](https://blog.superhuman.com/scaling-gec-inference/)

---

#### Securing Multi-Tenant AI-Generated Code Execution

**Company:** benchling  
**Industry:** Healthcare

Benchling runs AI agent-generated scientific code for life sciences customers and needed to prevent cross-tenant access and data exfiltration at scale without creating an IAM role for every tenant or exposing its production account. It deployed Amazon Bedrock AgentCore Code Interpreter in a separate AWS account and locked it into a VPC with no internet or NAT gateway, Route 53 Resolver DNS Firewall, restricted VPC endpoints, network controls, and per-job AWS STS credentials. Benchling reports that the architecture now supports more than 600 execution sessions per day across more than 250 tenants per week, with zero reported security incidents or cross-tenant data leakage since deployment; however, these results are vendor-reported and do not establish that every possible attack path is eliminated.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-benchling-secured-multi-tenant-ai-agents-with-amazon-bedrock-agentcore/)

---

#### Per-user spend enforcement for production generative AI

**Company:** jamf  
**Industry:** Tech

Jamf expanded Amazon Bedrock access for its engineering organization to support AI-assisted development, but needed visibility and controls for rapidly changing per-user token costs. It built a serverless governance system that records Bedrock invocation logs in Amazon S3, calculates daily user-level spend through an Amazon Athena view, and uses an AWS Lambda function scheduled by Amazon EventBridge to update IAM Customer Managed Policies. As engineers cross configurable spending thresholds, access to expensive models is restricted while a lower-cost model remains available; Slack notifications and a time-boxed exception workflow reduce disruption. The source reports that the architecture costs well under $10 per month for the Lambda, DynamoDB, and S3 components serving hundreds of engineers, while noting that Athena scan volume, pricing maintenance, policy-version limits, and the approximately 15-minute enforcement interval are important operational tradeoffs.

[Read source](https://aws.amazon.com/blogs/machine-learning/tokenomics-at-scale-how-jamf-built-real-time-spend-enforcement-for-amazon-bedrock/)

---

### Cool Use Cases

#### Precomputing Personalized Grocery Reorders for Faster Shopping

**Company:** doordash  
**Industry:** E-commerce

DoorDash improved the Ask DoorDash grocery-reorder experience by moving relatively stable historical reasoning out of the online agent path. A daily pipeline uses up to 90 days of order history and relevant profile signals to generate validated, store-specific bundles of likely recurring needs with batch LLM inference; the request-time system then resolves those needs against live inventory, prices, and catalog listings. For a deterministic “reorder my usuals” entry point, this reduced the reported latency from roughly 16 seconds to roughly 2 seconds, doubled the rate at which consumers viewed the resulting list, and was associated with an approximately 34% increase in order rate for the flow. The approach retains agentic reasoning for ambiguous or dynamic requests, but the published results are company-reported and the article does not provide experimental design or statistical significance details.

[Read source](https://careersatdoordash.com/blog/building-ask-doordash-part-6-grocery-reorder-case-study/)

---

#### A Grounded, Artifact-Based Shopping Interface for Consumer Agents

**Company:** doordash  
**Industry:** E-commerce

DoorDash evolved Ask DoorDash from a chat interface that exposed per-item search carousels into a grounded shopping surface for grocery and restaurant agents. The production design uses an authoritative JSON shopping-list artifact with separate storage, agent, and consumer views; native widgets grounded in live catalog and cart systems; direct client-side edits for deterministic actions; and agent turns for changes requiring judgment. In July 2026, rendered grocery-list sessions averaged nearly two UI interactions, about one-third proceeded to apply the list to a cart, and nearly three-quarters of first follow-up actions occurred through components, although the article reports product usage metrics rather than controlled evidence that the architecture caused these outcomes.

[Read source](https://careersatdoordash.com/blog/building-ask-doordash-part-5-a-grounded-interface-for-shopping-agents/)

---

### Tools & Infrastructure

#### Transparent Multilingual Contact Center QA with LLM Pipelines

**Company:** didi  
**Industry:** Tech

DiDi International Business Group replaced an opaque third-party contact center quality-assurance solution with a self-owned system built on Amazon Bedrock. The production system processes Spanish and Portuguese live-chat and phone conversations across ride-hailing, food-delivery, and financial-services operations through separate intent-verification, compliance-evaluation, and Voice of Customer pipelines. Its design emphasizes precise context management, dynamically assembled prompts, structured model outputs, deterministic post-validation, privacy controls, and human review. DiDi reports that intent-verification accuracy increased from 38% to 86%, compliance-scoring accuracy exceeded 90%, and VOC analysis reduced work that previously took hours to a process completed in minutes; however, the source does not provide independent benchmarks, sample sizes, operating costs, or detailed error analyses.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-didi-built-intelligent-contact-center-qa-with-amazon-bedrock/)

---

#### Sandboxed Agentic Email Threat Detection at Billion-Message Scale

**Company:** abnormal_ai  
**Industry:** Tech

Abnormal AI uses inline LLM-powered agents and Amazon Bedrock AgentCore Code Interpreter to investigate the hardest email threats that simpler rules and machine-learning models cannot confidently classify. The agents receive threat-intelligence data, write and execute analysis code in ephemeral isolated MicroVM sandboxes, and use computational checks to support real-time decisions. Abnormal AI reports processing billions of messages through a tiered pipeline, routing tens of thousands of difficult cases to agents, while a separate batch analyst agent uses misclassification data to propose improved heuristics and models. The AWS account presents this as a production-scale architecture, but the article does not provide independently validated detection-quality, latency, cost, or false-positive metrics.

[Read source](https://aws.amazon.com/blogs/machine-learning/abnormal-ai-amazon-bedrock-agentcore-for-agentic-email-security-at-scale/)

---

#### Japanese Multi-Turn LLM Evaluation Pipeline for Customer-Service AI

**Company:** wevnal  
**Industry:** E-commerce

wevnal and Microsoft engineers used a two-day hackathon to build a reproducible evaluation pipeline for Japanese conversational models supporting customer-service experiences such as BOTCHAN AI Call. The system evaluates 24 models across 39 two-turn conversations, three personas, and four quality facets—brevity, fluency, emotional intelligence, and role-playing—rather than relying on English-centric single-turn benchmarks. It adds benchmark auditing, multi-provider model discovery, price-tier-aware selection, SHA256 content-addressed caching, judge-based scoring, visualizations, and CI-friendly exports. The reported outcome is a production-conscious evaluation foundation that can reduce a broad model candidate set to a smaller shortlist, although the source does not report customer-facing quality improvements, operational deployment, or validation against live call-center KPIs.

[Read source](https://devblogs.microsoft.com/ise/japanese-llm-evaluation-pipeline-hackathon/)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

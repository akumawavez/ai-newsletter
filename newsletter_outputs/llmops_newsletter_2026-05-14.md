# Weekly LLMOps Newsletter — 2026-05-14

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Research Highlights

#### Evaluating AI Agent Performance: Skills vs Documentation for Developer Platforms

**Company:** wix  
**Industry:** Tech

Wix Engineering conducted 250 controlled evaluations to compare how AI agents perform developer tasks using standard documentation, AI-optimized documentation, and purpose-built "skills" (curated guides). The study examined CLI extension development and REST API scripting tasks, with each condition run three times to account for variance. The results revealed that agent-optimized documentation achieved higher task completion rates (87%) than skills alone (78%) while using fewer tokens and running faster, primarily because small mistakes in skills eroded their advantages. However, well-aligned skills provided 30-50% token reductions for specific tasks. The findings led Wix to position agent-optimized docs as the backbone of their AI-native developer experience, with skills serving as a "caching layer" for common tasks, maintained through regular automated evaluations to prevent drift.

[Read source](https://www.wix.engineering/post/we-ran-250-ai-agent-evals-to-find-out-if-skills-beat-docs-the-answer-is-more-complicated-than-we-ex)

---

### Industry News

#### AI-Powered Search and Agent Automation for Digital Asset Management

**Company:** bynder  
**Industry:** Media & Entertainment

Bynder, a digital asset management platform serving retail and CPG customers, faced significant operational bottlenecks as users had to manually tag and categorize all uploaded content for searchability. To address this, Bynder built AI search capabilities and four types of configurable AI agents using AWS services including Bedrock, Rekognition, Transcribe, and OpenSearch. The solution enabled natural language search, similarity search, automated content enrichment, brand compliance checking, and governance automation. Results included one major pet food retailer saving almost 4,000 hours of manual tagging work, and a leading tea brand reducing migration time from months to weeks while improving metadata quality.

[Read source](https://www.youtube.com/watch?v=Kyym50EgUOQ)

---

#### Multi-Agent AI Platform for Life Insurance Sales Acceleration

**Company:** prudential  
**Industry:** Insurance

Prudential developed "Just Ask," an AI-driven advisor assistant platform to address the complex, friction-heavy life insurance sales process that typically spans 8-10 weeks and involves navigating hundreds of products, regulatory requirements, and forms across different states. The company built a multi-agent system on AWS that includes specialized agents for product recommendations, medical underwriting, quoting, forms selection, and book of business management—all orchestrated through a conversational interface. Within 12 weeks of deployment, the platform processed 1,800 messages across 900+ financial planners from 550+ organizations, delivered 100+ successful quotes, and saved approximately 4,500 human hours, with user adoption growing organically at 175% for some agents and demonstrating 90%+ accuracy across most specialized agents.

[Read source](https://www.youtube.com/watch?v=g-YBqWv2kQ4)

---

#### Building and Scaling AI Agents in Production for DevSecOps Automation

**Company:** datadog  
**Industry:** Tech

Datadog, an observability platform company, has deployed over a hundred AI agents in production to automate DevSecOps tasks, with plans to scale to thousands more. The agents include an SRE agent for autonomous alert investigation, a Dev agent for code generation and error fixes, and a Security Analyst agent for security investigations. The presentation shares lessons learned from building these production agents, emphasizing the importance of agent-first API design, proactive background operations over reactive chat interfaces, comprehensive evaluation systems, framework and model agnosticism, and treating agents as first-class users of systems and APIs. The agents leverage durable execution frameworks like Temporal and are designed to run autonomously in containerized environments.

[Read source](https://www.youtube.com/watch?v=C3y3M_03Vco)

---

#### AI-Powered Bug Routing System Using RAG and Multimodal Processing

**Company:** miro  
**Industry:** Tech

Miro, serving over 95 million users globally, faced significant challenges with bug routing across nearly 100 engineering teams, resulting in an estimated 42 years of cumulative lost productivity annually due to misrouting and repeated reassignments. To address this, Miro partnered with AWS to develop BugManager, an AI-powered bug triaging solution built on Amazon Bedrock. The system uses RAG with Amazon Bedrock Knowledge Bases to enrich bug reports with context from multiple sources (Jira tickets, GitHub PRs, Confluence docs), multimodal processing with Amazon Nova Pro to parse screenshots and videos, and Anthropic's Claude Sonnet 4 for classification across approximately 100 teams. The solution achieved 75% top-1 accuracy (70% improvement over their previous fine-tuned NLP model), 95% top-3 accuracy, six times fewer team reassignments, and five times shorter median time-to-resolution, reducing resolution time from days to hours.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-miro-uses-amazon-bedrock-to-boost-software-bug-routing-accuracy-and-improve-time-to-resolution-from-days-to-hours/)

---

#### Building Production Coding Agents with Pi Framework for Sales Process Automation

**Company:** tavon  
**Industry:** Tech

Tavon, a small European company building agents for organizations, developed a production-grade sales automation system using the Pi agent framework and OpenClaw. The system automates the processing of requests for proposals (RFPs) by monitoring email inboxes, routing messages to customer-specific agents, and generating draft responses. Each customer has a dedicated agent with customized behavior defined through agent configuration files and customer-specific parameters. The agents use CLI-based tools to access CRM and ERP systems, execute tasks in secure sandboxed environments, and leverage session management to maintain conversation context across multiple interactions, ultimately reducing manual effort in the sales process while keeping human users in the loop for final approval.

[Read source](https://www.youtube.com/watch?v=vAIDdLKB6-w)

---

#### Building a Production AI Code Review Agent with High Engineer Acceptance

**Company:** doordash  
**Industry:** Tech

DoorDash built an AI code review agent to catch critical issues that humans systematically miss during pull request reviews, such as dangerous deletions, cross-boundary drift, and silent behavior changes. The system evolved through three major versions to arrive at a three-agent architecture: a "lead scout" that identifies suspicious areas in code changes, followed by two deep reviewers that verify specific concerns. By optimizing for precision over recall and using domain-specific review profiles mined from historical PRs, Slack decisions, and incident history, DoorDash achieved a 60.2% acceptance rate on high and critical findings across 10,000+ weekly PR reviews covering 56 repositories, with reviews costing approximately $3 each and completing in about 7 minutes.

[Read source](https://careersatdoordash.com/blog/doordash-built-an-ai-code-reviewer-engineers-actually-listen-to/)

---

#### Building Custom Tracing Tools and Development Infrastructure for AI-Powered Meeting Notes

**Company:** granola  
**Industry:** Tech

Granola, a meeting notes application that uses LLMs to generate summaries from real-time transcription, faced challenges in production with LLM behavior unpredictability, cost control, and feature testing. The company moved beyond simple one-shot LLM implementations by building custom internal tracing tools that provide complete visibility into tool calls, reasoning processes, and costs, structured specifically for their team's needs rather than relying on generic SaaS providers. Additionally, they transformed their Electron desktop app's front-end into a web shell deployed online, enabling preview links for every pull request and significantly speeding up their development and testing feedback loops for AI features.

[Read source](https://www.youtube.com/watch?v=ON5LIT0M4do)

---

#### Context Management and Memory Strategies for Production AI Agents

**Company:** arize  
**Industry:** Tech

Arize built Alex, an AI agent designed to help users build AI applications by analyzing observability traces and span data from their platform. The team encountered significant context management challenges as conversations grew and data volumes multiplied, creating a vicious loop where the agent analyzing the data became constrained by that same data. They solved this through a three-part strategy: implementing smart truncation with memory stores (keeping first and last 100 characters while storing the middle for retrieval), separating context from memory management, and delegating heavy data operations to sub-agents. This approach, combined with long session evaluations, enabled Alex to handle complex, multi-turn conversations while maintaining performance and avoiding context window limitations.

[Read source](https://www.youtube.com/watch?v=esY99nYXxR4)

---

#### Gateway Patterns and Actions Runtime for Enterprise Agentic AI Deployment

**Company:** arcade.dev  
**Industry:** Tech

Arcade.dev addresses the critical challenges of deploying AI agents in production enterprise environments by providing an actions runtime that separates reasoning from action execution. The company identifies fundamental security and governance problems with existing agent deployment patterns, particularly around authorization, tool quality, and observability. Their solution implements a gateway pattern using Model Context Protocol to enforce identity separation, tool curation, fine-grained authorization, and comprehensive audit trails. This approach enables multi-user agents with proper permission boundaries, preventing authorization bypass vulnerabilities while maintaining safe and controlled access to business systems like CRMs, ERPs, and email platforms across diverse enterprise environments.

[Read source](https://www.youtube.com/watch?v=gQhDwOGdE4E)

---

#### Scaling LLM Production with Reinforcement Learning for Enterprise Agents

**Company:** adaptive_ml  
**Industry:** Tech

Adaptive ML addresses the challenge that 95% of GenAI pilots fail to reach production by advocating for reinforcement learning as the core post-training technique. The company argues that MVP solutions built on proprietary models or instruction fine-tuning lack systematic improvement mechanisms, whereas RL enables continuous integration of feedback from production environments. Their RLOps platform serves enterprises like AT&T, Manulife, and CCS Medical Supply, enabling them to train smaller, faster, and more cost-effective specialized LLMs. The approach particularly excels for agentic use cases, where RL's ability to train models in simulated environments with business-specific rewards unlocks production-grade performance while reducing inference costs by millions of dollars through model compression.

[Read source](https://www.youtube.com/watch?v=X6NShR2ccOg)

---

#### Scaling AI Agents in Production for B2B Growth and Outreach

**Company:** clay  
**Industry:** Tech

Clay, a creative tool for B2B growth and customer acquisition, scaled their AI agent infrastructure from early chat completion wrappers to operating 300 million agent runs per month. The company deployed multiple specialized agents across finding, closing, and growing customers, with individual agents running 10-30 steps involving web research, data synthesis, and content generation. To manage this scale while maintaining quality and cost efficiency, Clay implemented comprehensive LLMOps practices using LangSmith for observability, tracing, evaluation, and cost reconciliation, achieving 99.5% accuracy in tracking spending across inference providers while enabling rapid iteration and debugging across engineering and customer support teams.

[Read source](https://www.youtube.com/watch?v=cx6_tb6HCeY)

---

#### AI Employee Agent Operating in Slack with Multi-Tool Integration

**Company:** viktor  
**Industry:** Tech

Viktor is an AI employee agent that operates directly within Slack, providing teams with access to over 3,000 integrations and company-wide context. The product evolved from early web agent experiments in 2023 through an email agent called Jace, ultimately launching as Viktor in February 2026 with immediate product-market fit. The system addresses unique challenges of multi-user agent deployments including memory management across teams, permission scoping, context isolation between channels, and proactive task suggestions. Viktor uses Claude Opus 4.6 as its primary model, chosen specifically for its tone and personality traits that resonated with users during A/B testing against GPT-5.4.

[Read source](https://www.youtube.com/watch?v=ohKt066uFhg)

---

#### Automating Trading Card Copywriting with Multi-Agent Generative AI

**Company:** fanatics_collectibles  
**Industry:** Media & Entertainment

Fanatics Collectibles, a leading trading card company operating under brands like Topps, faced a significant challenge in creating compelling card back copy at scale. Their editorial teams spent weeks researching player stats, crafting narratives, and ensuring compliance with strict licensing agreements for each card set. The company implemented a multi-agent system using Amazon Bedrock to automate the research, copywriting, and quality assurance process. The solution combined a structured data pipeline for player statistics, a web search agent for qualitative research, and a specialized QA agent that validates copy against complex compliance guidelines. The system achieved remarkable results: a 90% reduction in production time (from weeks to hours), 40% fewer edits required by the QA team due to better compliance adherence, and 90% cost savings in content creation, while maintaining quality standards that collectors couldn't reliably distinguish from human-written copy.

[Read source](https://www.youtube.com/watch?v=plJylA9v_uc)

---

#### Multi-Agent Software Development System with Extended Autonomous Execution

**Company:** factory  
**Industry:** Tech

Factory developed a multi-agent system called Missions to address the bottleneck of human attention in software engineering, where engineers can only supervise a few tasks simultaneously despite models being capable of handling many more. The system uses a three-role architecture (orchestrators, workers, and validators) that combines delegation, creator-verifier patterns, broadcast communication, and negotiation to enable autonomous software development that can run for days or weeks. Missions have successfully executed for up to 16 days continuously, with production usage demonstrating the ability to build complex applications like Slack clones while maintaining 90% test coverage and producing cleaner codebases than the starting point.

[Read source](https://www.youtube.com/watch?v=ow1we5PzK-o)

---

#### Evolution from Static Benchmarks to Adaptive Agent Evaluation Systems

**Company:** comet  
**Industry:** Tech

Vincent from Comet presents a paradigm shift in how organizations should approach LLM evaluation, arguing that traditional static benchmarks are insufficient for modern agentic AI systems. The core problem identified is "eval calcification" where static evaluation datasets become increasingly misaligned with dynamically evolving AI agents and changing user behavior patterns. The proposed solution involves treating evaluations themselves as adaptive, self-optimizing systems that leverage telemetry, trace data, and intent-based outcomes rather than fixed test sets. This approach enables continuous online evaluation, self-curation of test suites from production traces, and telemetry-in-the-loop corrections, allowing agents to self-heal and adapt to the 20% of unpredictable user interactions that static benchmarks miss. Results from Comet's research and work with major companies like Uber, Netflix, and UK banks demonstrate the practical need for this shift as AI applications become more intentful and personalized.

[Read source](https://www.youtube.com/watch?v=4VhbYlfC7Gs)

---

#### Durable Agent Execution through Snapshot and Restore Infrastructure

**Company:** trigger.dev  
**Industry:** Tech

This case study explores the infrastructure challenges of deploying LLM-powered agents to production at scale, as presented by Trigger.dev. The company identified that traditional stateless compute architectures and replay-based workflow systems are insufficient for long-running agent sessions that can span hours or days. Their solution combines two key approaches: maintaining an append-only context log for conversational durability, and implementing VM-level snapshot and restore capabilities using Firecracker micro VMs. The result is a production system capable of handling millions of snapshot/restore operations with sub-second snapshot times and 200-millisecond restore times, achieving 15,000 VM starts per minute while reducing memory footprints from 512MB to 14MB through seekable compression.

[Read source](https://www.youtube.com/watch?v=svCnShDvgQg)

---

### Cool Use Cases

#### Production Skills Framework for Agentic LLM Workflows

**Company:** workos  
**Industry:** Tech

WorkOS developed a comprehensive approach to productionizing LLM workflows through "skills" - reusable, composable units of work that encapsulate specific tasks, constraints, and domain knowledge in markdown files with optional scripts. The problem addressed was the repetitive nature of LLM interactions where context must be reloaded from scratch in every conversation, leading to inconsistent outputs and wasted time. Their skills framework enables teams to codify workflows once, share them across team members and projects, and achieve more consistent, deterministic results. The solution has been applied across multiple use cases including code installation automation, content generation, image/video creation, and internal tooling, with WorkOS shipping production tools like their CLI that leverage skills to automate developer onboarding and authentication setup.

[Read source](https://www.youtube.com/watch?v=pFsfax19yOM)

---

#### Production Agent Observability and Monitoring Platform

**Company:** raindrop  
**Industry:** Tech

Raindrop addresses the challenge of monitoring and debugging AI agents in production environments where traditional testing and evaluation approaches fall short. As agents become more complex with multiple tools, memory sources, and sub-agents, the combinatorial explosion of possible behaviors makes comprehensive testing impractical. Raindrop provides a monitoring platform that combines explicit signals like error rates and latency with implicit signals detected through trained classifiers and regex patterns to identify issues like user frustration, task failures, refusals, and jailbreaking. The platform enables teams to set up alerts, run experiments comparing different agent versions in production, and use an automated triage agent to investigate spikes in problematic behaviors, helping AI engineering teams ship improvements faster while maintaining reliability.

[Read source](https://www.youtube.com/watch?v=-aM2EDTiaMs)

---

#### AI-Powered Engineering Management and Autonomous Development Workflows

**Company:** notion  
**Industry:** Tech

Ryan Nestrom, an Engineering Manager at Notion, demonstrates how AI has transformed engineering team management and software development workflows. The case study covers three primary use cases: automated meeting preparation using Notion AI custom agents that compile 24-hour activity updates from Slack, GitHub, Honeycomb metrics, and meeting transcripts to eliminate manual standup prep; background coding agents integrated via at-mentions that trigger virtual machines to autonomously generate pull requests from brief task descriptions; and spec-driven development where comprehensive markdown specifications serve as the source of truth, enabling coding agents like Aider to one-shot entire feature implementations. These approaches have eliminated meeting prep overhead, accelerated development velocity, and shifted engineering focus from implementation to architecture and verification, while maintaining high-quality output through automated testing and review processes.

[Read source](https://www.youtube.com/watch?v=pUHA_jNwuYE)

---

#### Building a Public AI Agent Workspace for Organizational Learning

**Company:** shopify  
**Industry:** E-commerce

Shopify developed River, an AI coding agent that operates exclusively in public Slack channels rather than private workspaces. The constraint of public-only operation was designed to create a "Lehrwerkstatt" (teaching workshop) environment where employees learn from observing each other's interactions with the agent. Over 5,938 employees used River across 4,450 channels in a 30-day period, with River authoring approximately one in eight merged pull requests. The public nature of interactions led to knowledge diffusion across the organization, with prompt patterns and debugging techniques spreading organically. The agent's merge rate improved from 36% to 77% over two months through collective learning and iterative refinement of River's skills and instructions by teams across the company.

[Read source](https://x.com/tobi/status/2053121182044451016)

---

### Tools & Infrastructure

#### Building Agentic Spreadsheet Automation from Process Mining to Production

**Company:** ramp  
**Industry:** Finance

Ramp developed an agentic spreadsheet editor called Ramp Sheets to automate complex finance workflows, starting from an internal process mining project that converted Loom videos of finance tasks into automation pipelines. The team evolved from black-box Python code generation to transparent spreadsheet-native operations using around 10 Excel-specific tools, leveraging Anthropic's Claude models which proved particularly effective at decomposing spreadsheet tasks. The system runs in Modal sandboxes with an agent SDK managing tool calls for reading and writing cell ranges, achieving typical execution times of 7-10 minutes per task. Beyond the core product, Ramp implemented a self-monitoring loop using their internal coding agent Inspect to automatically create DataDog monitors, and conducted research experiments in recursive language models with KV cache communication and steering vectors for model behavior modification.

[Read source](https://www.youtube.com/watch?v=trEM9OKr5Sc)

---

#### AI-Powered Workflow Assistant for Seismic Data Processing

**Company:** halliburton  
**Industry:** Energy

Halliburton partnered with AWS Generative AI Innovation Center to develop an AI-powered assistant for their Seismic Engine, a cloud-native application for seismic data processing. The traditional workflow creation process required manual configuration of approximately 100 specialized tools, which was time-consuming and required deep expertise. The solution uses Amazon Bedrock, Amazon Bedrock Knowledge Bases, Amazon Nova, and Amazon DynamoDB to transform complex workflow creation into natural language conversations. The proof-of-concept achieved workflow generation success rates of 84-97% while reducing creation time by over 95% compared to manual processes, with complete workflows delivered within 5.9-16.6 seconds.

[Read source](https://aws.amazon.com/blogs/machine-learning/halliburton-enhances-seismic-workflow-creation-with-amazon-bedrock-and-generative-ai/)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Research Highlights

#### Evaluating AI Agent Performance: Skills vs Documentation for Developer Platforms

**Company:** wix  
**Industry:** Tech

Wix Engineering conducted 250 controlled evaluations to compare how AI agents perform developer tasks using standard documentation, AI-optimized documentation, and purpose-built "skills" (curated guides). The study examined CLI extension development and REST API scripting tasks, with each condition run three times to account for variance. The results revealed that agent-optimized documentation achieved higher task completion rates (87%) than skills alone (78%) while using fewer tokens and running faster, primarily because small mistakes in skills eroded their advantages. However, well-aligned skills provided 30-50% token reductions for specific tasks. The findings led Wix to position agent-optimized docs as the backbone of their AI-native developer experience, with skills serving as a "caching layer" for common tasks, maintained through regular automated evaluations to prevent drift.

[Read source](https://www.wix.engineering/post/we-ran-250-ai-agent-evals-to-find-out-if-skills-beat-docs-the-answer-is-more-complicated-than-we-ex)

---

### Industry News

#### AI-Powered Search and Agent Automation for Digital Asset Management

**Company:** bynder  
**Industry:** Media & Entertainment

Bynder, a digital asset management platform serving retail and CPG customers, faced significant operational bottlenecks as users had to manually tag and categorize all uploaded content for searchability. To address this, Bynder built AI search capabilities and four types of configurable AI agents using AWS services including Bedrock, Rekognition, Transcribe, and OpenSearch. The solution enabled natural language search, similarity search, automated content enrichment, brand compliance checking, and governance automation. Results included one major pet food retailer saving almost 4,000 hours of manual tagging work, and a leading tea brand reducing migration time from months to weeks while improving metadata quality.

[Read source](https://www.youtube.com/watch?v=Kyym50EgUOQ)

---

#### Multi-Agent AI Platform for Life Insurance Sales Acceleration

**Company:** prudential  
**Industry:** Insurance

Prudential developed "Just Ask," an AI-driven advisor assistant platform to address the complex, friction-heavy life insurance sales process that typically spans 8-10 weeks and involves navigating hundreds of products, regulatory requirements, and forms across different states. The company built a multi-agent system on AWS that includes specialized agents for product recommendations, medical underwriting, quoting, forms selection, and book of business management—all orchestrated through a conversational interface. Within 12 weeks of deployment, the platform processed 1,800 messages across 900+ financial planners from 550+ organizations, delivered 100+ successful quotes, and saved approximately 4,500 human hours, with user adoption growing organically at 175% for some agents and demonstrating 90%+ accuracy across most specialized agents.

[Read source](https://www.youtube.com/watch?v=g-YBqWv2kQ4)

---

#### Building and Scaling AI Agents in Production for DevSecOps Automation

**Company:** datadog  
**Industry:** Tech

Datadog, an observability platform company, has deployed over a hundred AI agents in production to automate DevSecOps tasks, with plans to scale to thousands more. The agents include an SRE agent for autonomous alert investigation, a Dev agent for code generation and error fixes, and a Security Analyst agent for security investigations. The presentation shares lessons learned from building these production agents, emphasizing the importance of agent-first API design, proactive background operations over reactive chat interfaces, comprehensive evaluation systems, framework and model agnosticism, and treating agents as first-class users of systems and APIs. The agents leverage durable execution frameworks like Temporal and are designed to run autonomously in containerized environments.

[Read source](https://www.youtube.com/watch?v=C3y3M_03Vco)

---

#### AI-Powered Bug Routing System Using RAG and Multimodal Processing

**Company:** miro  
**Industry:** Tech

Miro, serving over 95 million users globally, faced significant challenges with bug routing across nearly 100 engineering teams, resulting in an estimated 42 years of cumulative lost productivity annually due to misrouting and repeated reassignments. To address this, Miro partnered with AWS to develop BugManager, an AI-powered bug triaging solution built on Amazon Bedrock. The system uses RAG with Amazon Bedrock Knowledge Bases to enrich bug reports with context from multiple sources (Jira tickets, GitHub PRs, Confluence docs), multimodal processing with Amazon Nova Pro to parse screenshots and videos, and Anthropic's Claude Sonnet 4 for classification across approximately 100 teams. The solution achieved 75% top-1 accuracy (70% improvement over their previous fine-tuned NLP model), 95% top-3 accuracy, six times fewer team reassignments, and five times shorter median time-to-resolution, reducing resolution time from days to hours.

[Read source](https://aws.amazon.com/blogs/machine-learning/how-miro-uses-amazon-bedrock-to-boost-software-bug-routing-accuracy-and-improve-time-to-resolution-from-days-to-hours/)

---

#### Building Production Coding Agents with Pi Framework for Sales Process Automation

**Company:** tavon  
**Industry:** Tech

Tavon, a small European company building agents for organizations, developed a production-grade sales automation system using the Pi agent framework and OpenClaw. The system automates the processing of requests for proposals (RFPs) by monitoring email inboxes, routing messages to customer-specific agents, and generating draft responses. Each customer has a dedicated agent with customized behavior defined through agent configuration files and customer-specific parameters. The agents use CLI-based tools to access CRM and ERP systems, execute tasks in secure sandboxed environments, and leverage session management to maintain conversation context across multiple interactions, ultimately reducing manual effort in the sales process while keeping human users in the loop for final approval.

[Read source](https://www.youtube.com/watch?v=vAIDdLKB6-w)

---

#### Building a Production AI Code Review Agent with High Engineer Acceptance

**Company:** doordash  
**Industry:** Tech

DoorDash built an AI code review agent to catch critical issues that humans systematically miss during pull request reviews, such as dangerous deletions, cross-boundary drift, and silent behavior changes. The system evolved through three major versions to arrive at a three-agent architecture: a "lead scout" that identifies suspicious areas in code changes, followed by two deep reviewers that verify specific concerns. By optimizing for precision over recall and using domain-specific review profiles mined from historical PRs, Slack decisions, and incident history, DoorDash achieved a 60.2% acceptance rate on high and critical findings across 10,000+ weekly PR reviews covering 56 repositories, with reviews costing approximately $3 each and completing in about 7 minutes.

[Read source](https://careersatdoordash.com/blog/doordash-built-an-ai-code-reviewer-engineers-actually-listen-to/)

---

#### Building Custom Tracing Tools and Development Infrastructure for AI-Powered Meeting Notes

**Company:** granola  
**Industry:** Tech

Granola, a meeting notes application that uses LLMs to generate summaries from real-time transcription, faced challenges in production with LLM behavior unpredictability, cost control, and feature testing. The company moved beyond simple one-shot LLM implementations by building custom internal tracing tools that provide complete visibility into tool calls, reasoning processes, and costs, structured specifically for their team's needs rather than relying on generic SaaS providers. Additionally, they transformed their Electron desktop app's front-end into a web shell deployed online, enabling preview links for every pull request and significantly speeding up their development and testing feedback loops for AI features.

[Read source](https://www.youtube.com/watch?v=ON5LIT0M4do)

---

#### Context Management and Memory Strategies for Production AI Agents

**Company:** arize  
**Industry:** Tech

Arize built Alex, an AI agent designed to help users build AI applications by analyzing observability traces and span data from their platform. The team encountered significant context management challenges as conversations grew and data volumes multiplied, creating a vicious loop where the agent analyzing the data became constrained by that same data. They solved this through a three-part strategy: implementing smart truncation with memory stores (keeping first and last 100 characters while storing the middle for retrieval), separating context from memory management, and delegating heavy data operations to sub-agents. This approach, combined with long session evaluations, enabled Alex to handle complex, multi-turn conversations while maintaining performance and avoiding context window limitations.

[Read source](https://www.youtube.com/watch?v=esY99nYXxR4)

---

#### Gateway Patterns and Actions Runtime for Enterprise Agentic AI Deployment

**Company:** arcade.dev  
**Industry:** Tech

Arcade.dev addresses the critical challenges of deploying AI agents in production enterprise environments by providing an actions runtime that separates reasoning from action execution. The company identifies fundamental security and governance problems with existing agent deployment patterns, particularly around authorization, tool quality, and observability. Their solution implements a gateway pattern using Model Context Protocol to enforce identity separation, tool curation, fine-grained authorization, and comprehensive audit trails. This approach enables multi-user agents with proper permission boundaries, preventing authorization bypass vulnerabilities while maintaining safe and controlled access to business systems like CRMs, ERPs, and email platforms across diverse enterprise environments.

[Read source](https://www.youtube.com/watch?v=gQhDwOGdE4E)

---

#### Scaling LLM Production with Reinforcement Learning for Enterprise Agents

**Company:** adaptive_ml  
**Industry:** Tech

Adaptive ML addresses the challenge that 95% of GenAI pilots fail to reach production by advocating for reinforcement learning as the core post-training technique. The company argues that MVP solutions built on proprietary models or instruction fine-tuning lack systematic improvement mechanisms, whereas RL enables continuous integration of feedback from production environments. Their RLOps platform serves enterprises like AT&T, Manulife, and CCS Medical Supply, enabling them to train smaller, faster, and more cost-effective specialized LLMs. The approach particularly excels for agentic use cases, where RL's ability to train models in simulated environments with business-specific rewards unlocks production-grade performance while reducing inference costs by millions of dollars through model compression.

[Read source](https://www.youtube.com/watch?v=X6NShR2ccOg)

---

#### Scaling AI Agents in Production for B2B Growth and Outreach

**Company:** clay  
**Industry:** Tech

Clay, a creative tool for B2B growth and customer acquisition, scaled their AI agent infrastructure from early chat completion wrappers to operating 300 million agent runs per month. The company deployed multiple specialized agents across finding, closing, and growing customers, with individual agents running 10-30 steps involving web research, data synthesis, and content generation. To manage this scale while maintaining quality and cost efficiency, Clay implemented comprehensive LLMOps practices using LangSmith for observability, tracing, evaluation, and cost reconciliation, achieving 99.5% accuracy in tracking spending across inference providers while enabling rapid iteration and debugging across engineering and customer support teams.

[Read source](https://www.youtube.com/watch?v=cx6_tb6HCeY)

---

#### AI Employee Agent Operating in Slack with Multi-Tool Integration

**Company:** viktor  
**Industry:** Tech

Viktor is an AI employee agent that operates directly within Slack, providing teams with access to over 3,000 integrations and company-wide context. The product evolved from early web agent experiments in 2023 through an email agent called Jace, ultimately launching as Viktor in February 2026 with immediate product-market fit. The system addresses unique challenges of multi-user agent deployments including memory management across teams, permission scoping, context isolation between channels, and proactive task suggestions. Viktor uses Claude Opus 4.6 as its primary model, chosen specifically for its tone and personality traits that resonated with users during A/B testing against GPT-5.4.

[Read source](https://www.youtube.com/watch?v=ohKt066uFhg)

---

#### Automating Trading Card Copywriting with Multi-Agent Generative AI

**Company:** fanatics_collectibles  
**Industry:** Media & Entertainment

Fanatics Collectibles, a leading trading card company operating under brands like Topps, faced a significant challenge in creating compelling card back copy at scale. Their editorial teams spent weeks researching player stats, crafting narratives, and ensuring compliance with strict licensing agreements for each card set. The company implemented a multi-agent system using Amazon Bedrock to automate the research, copywriting, and quality assurance process. The solution combined a structured data pipeline for player statistics, a web search agent for qualitative research, and a specialized QA agent that validates copy against complex compliance guidelines. The system achieved remarkable results: a 90% reduction in production time (from weeks to hours), 40% fewer edits required by the QA team due to better compliance adherence, and 90% cost savings in content creation, while maintaining quality standards that collectors couldn't reliably distinguish from human-written copy.

[Read source](https://www.youtube.com/watch?v=plJylA9v_uc)

---

#### Multi-Agent Software Development System with Extended Autonomous Execution

**Company:** factory  
**Industry:** Tech

Factory developed a multi-agent system called Missions to address the bottleneck of human attention in software engineering, where engineers can only supervise a few tasks simultaneously despite models being capable of handling many more. The system uses a three-role architecture (orchestrators, workers, and validators) that combines delegation, creator-verifier patterns, broadcast communication, and negotiation to enable autonomous software development that can run for days or weeks. Missions have successfully executed for up to 16 days continuously, with production usage demonstrating the ability to build complex applications like Slack clones while maintaining 90% test coverage and producing cleaner codebases than the starting point.

[Read source](https://www.youtube.com/watch?v=ow1we5PzK-o)

---

#### Evolution from Static Benchmarks to Adaptive Agent Evaluation Systems

**Company:** comet  
**Industry:** Tech

Vincent from Comet presents a paradigm shift in how organizations should approach LLM evaluation, arguing that traditional static benchmarks are insufficient for modern agentic AI systems. The core problem identified is "eval calcification" where static evaluation datasets become increasingly misaligned with dynamically evolving AI agents and changing user behavior patterns. The proposed solution involves treating evaluations themselves as adaptive, self-optimizing systems that leverage telemetry, trace data, and intent-based outcomes rather than fixed test sets. This approach enables continuous online evaluation, self-curation of test suites from production traces, and telemetry-in-the-loop corrections, allowing agents to self-heal and adapt to the 20% of unpredictable user interactions that static benchmarks miss. Results from Comet's research and work with major companies like Uber, Netflix, and UK banks demonstrate the practical need for this shift as AI applications become more intentful and personalized.

[Read source](https://www.youtube.com/watch?v=4VhbYlfC7Gs)

---

#### Durable Agent Execution through Snapshot and Restore Infrastructure

**Company:** trigger.dev  
**Industry:** Tech

This case study explores the infrastructure challenges of deploying LLM-powered agents to production at scale, as presented by Trigger.dev. The company identified that traditional stateless compute architectures and replay-based workflow systems are insufficient for long-running agent sessions that can span hours or days. Their solution combines two key approaches: maintaining an append-only context log for conversational durability, and implementing VM-level snapshot and restore capabilities using Firecracker micro VMs. The result is a production system capable of handling millions of snapshot/restore operations with sub-second snapshot times and 200-millisecond restore times, achieving 15,000 VM starts per minute while reducing memory footprints from 512MB to 14MB through seekable compression.

[Read source](https://www.youtube.com/watch?v=svCnShDvgQg)

---

### Cool Use Cases

#### Production Skills Framework for Agentic LLM Workflows

**Company:** workos  
**Industry:** Tech

WorkOS developed a comprehensive approach to productionizing LLM workflows through "skills" - reusable, composable units of work that encapsulate specific tasks, constraints, and domain knowledge in markdown files with optional scripts. The problem addressed was the repetitive nature of LLM interactions where context must be reloaded from scratch in every conversation, leading to inconsistent outputs and wasted time. Their skills framework enables teams to codify workflows once, share them across team members and projects, and achieve more consistent, deterministic results. The solution has been applied across multiple use cases including code installation automation, content generation, image/video creation, and internal tooling, with WorkOS shipping production tools like their CLI that leverage skills to automate developer onboarding and authentication setup.

[Read source](https://www.youtube.com/watch?v=pFsfax19yOM)

---

#### Production Agent Observability and Monitoring Platform

**Company:** raindrop  
**Industry:** Tech

Raindrop addresses the challenge of monitoring and debugging AI agents in production environments where traditional testing and evaluation approaches fall short. As agents become more complex with multiple tools, memory sources, and sub-agents, the combinatorial explosion of possible behaviors makes comprehensive testing impractical. Raindrop provides a monitoring platform that combines explicit signals like error rates and latency with implicit signals detected through trained classifiers and regex patterns to identify issues like user frustration, task failures, refusals, and jailbreaking. The platform enables teams to set up alerts, run experiments comparing different agent versions in production, and use an automated triage agent to investigate spikes in problematic behaviors, helping AI engineering teams ship improvements faster while maintaining reliability.

[Read source](https://www.youtube.com/watch?v=-aM2EDTiaMs)

---

#### AI-Powered Engineering Management and Autonomous Development Workflows

**Company:** notion  
**Industry:** Tech

Ryan Nestrom, an Engineering Manager at Notion, demonstrates how AI has transformed engineering team management and software development workflows. The case study covers three primary use cases: automated meeting preparation using Notion AI custom agents that compile 24-hour activity updates from Slack, GitHub, Honeycomb metrics, and meeting transcripts to eliminate manual standup prep; background coding agents integrated via at-mentions that trigger virtual machines to autonomously generate pull requests from brief task descriptions; and spec-driven development where comprehensive markdown specifications serve as the source of truth, enabling coding agents like Aider to one-shot entire feature implementations. These approaches have eliminated meeting prep overhead, accelerated development velocity, and shifted engineering focus from implementation to architecture and verification, while maintaining high-quality output through automated testing and review processes.

[Read source](https://www.youtube.com/watch?v=pUHA_jNwuYE)

---

#### Building a Public AI Agent Workspace for Organizational Learning

**Company:** shopify  
**Industry:** E-commerce

Shopify developed River, an AI coding agent that operates exclusively in public Slack channels rather than private workspaces. The constraint of public-only operation was designed to create a "Lehrwerkstatt" (teaching workshop) environment where employees learn from observing each other's interactions with the agent. Over 5,938 employees used River across 4,450 channels in a 30-day period, with River authoring approximately one in eight merged pull requests. The public nature of interactions led to knowledge diffusion across the organization, with prompt patterns and debugging techniques spreading organically. The agent's merge rate improved from 36% to 77% over two months through collective learning and iterative refinement of River's skills and instructions by teams across the company.

[Read source](https://x.com/tobi/status/2053121182044451016)

---

### Tools & Infrastructure

#### Building Agentic Spreadsheet Automation from Process Mining to Production

**Company:** ramp  
**Industry:** Finance

Ramp developed an agentic spreadsheet editor called Ramp Sheets to automate complex finance workflows, starting from an internal process mining project that converted Loom videos of finance tasks into automation pipelines. The team evolved from black-box Python code generation to transparent spreadsheet-native operations using around 10 Excel-specific tools, leveraging Anthropic's Claude models which proved particularly effective at decomposing spreadsheet tasks. The system runs in Modal sandboxes with an agent SDK managing tool calls for reading and writing cell ranges, achieving typical execution times of 7-10 minutes per task. Beyond the core product, Ramp implemented a self-monitoring loop using their internal coding agent Inspect to automatically create DataDog monitors, and conducted research experiments in recursive language models with KV cache communication and steering vectors for model behavior modification.

[Read source](https://www.youtube.com/watch?v=trEM9OKr5Sc)

---

#### AI-Powered Workflow Assistant for Seismic Data Processing

**Company:** halliburton  
**Industry:** Energy

Halliburton partnered with AWS Generative AI Innovation Center to develop an AI-powered assistant for their Seismic Engine, a cloud-native application for seismic data processing. The traditional workflow creation process required manual configuration of approximately 100 specialized tools, which was time-consuming and required deep expertise. The solution uses Amazon Bedrock, Amazon Bedrock Knowledge Bases, Amazon Nova, and Amazon DynamoDB to transform complex workflow creation into natural language conversations. The proof-of-concept achieved workflow generation success rates of 84-97% while reducing creation time by over 95% compared to manual processes, with complete workflows delivered within 5.9-16.6 seconds.

[Read source](https://aws.amazon.com/blogs/machine-learning/halliburton-enhances-seismic-workflow-creation-with-amazon-bedrock-and-generative-ai/)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

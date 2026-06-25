# Weekly LLMOps Newsletter — 2026-06-25

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Industry News

#### Building an AI Financial Co-Pilot with Compliance-Driven Evaluation

**Company:** chime  
**Industry:** Finance

Chime, a fintech company serving 9.5 million members, built Jade, an AI-powered financial co-pilot designed to help members spend smarter and save more. The core challenge was ensuring the agentic AI system remained compliant with financial regulations while avoiding the "oops-driven development" approach that had plagued other AI deployments. The solution involved creating a structured framework where legal and compliance teams actively participated throughout development by co-authoring evaluations. By establishing a taxonomy of risks, bootstrapping datasets with adversarial testing tools like Giskard, and using LLM-as-a-judge evaluators, Chime transformed compliance from a release gate into a continuous feedback loop. This approach delivered velocity, alignment between engineering and legal teams, and trust through evidence-based sign-offs.

[Read source](https://www.youtube.com/watch?v=yQ2HCSSsqTc)

---

#### Teaching Refusal Behavior Through Automated Data Curation with LLM Judge Consensus

**Company:** shopify  
**Industry:** E-commerce

Shopify's Sidekick AI assistant faced a critical challenge: its customer segmentation skill model, trained exclusively on successful production queries, couldn't recognize when to refuse impossible requests, leading to hallucinated responses and zero-result queries. To solve this, Shopify built an automated data curation pipeline using an ensemble of four frontier LLMs as judges, calibrated on a small seed dataset of 600+ human-annotated refusal examples. Through strict consensus requirements and a mutually exclusive taxonomy, they curated training data that resolved label conflicts between production logs and refusal annotations. The resulting model improved segmentation evaluation scores from 0.619 to 0.798 (28.9% relative gain), achieved 86.3% refusal accuracy with only 4.6% false positives, and established a continuous data flywheel where each production deployment generates new training signal for the next iteration.

[Read source](https://shopify.engineering/sidekick-curation)

---

### Cool Use Cases

#### Context Engineering and Memory Management for Production Agent Systems

**Company:** anthropic  
**Industry:** Tech

Anthropic's Applied AI team has developed sophisticated approaches to context engineering and memory management for production AI agent deployments, addressing the challenge of translating raw model intelligence into durable, scalable products. The solution evolved from simple markdown files injected at session start to sophisticated file-system-based memory architectures with versioning, concurrency controls, and permissioning. The team introduced "dreaming," an out-of-band batch process where dedicated agents review session transcripts to identify patterns and propose memory improvements. Results include improved accuracy on repeated tasks, reduced latency and cost through better one-shot performance, and autonomous learning that frees developers to focus on product improvements rather than manual memory curation.

[Read source](https://www.youtube.com/watch?v=tTcxVv8HHNw)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Industry News

#### Building an AI Financial Co-Pilot with Compliance-Driven Evaluation

**Company:** chime  
**Industry:** Finance

Chime, a fintech company serving 9.5 million members, built Jade, an AI-powered financial co-pilot designed to help members spend smarter and save more. The core challenge was ensuring the agentic AI system remained compliant with financial regulations while avoiding the "oops-driven development" approach that had plagued other AI deployments. The solution involved creating a structured framework where legal and compliance teams actively participated throughout development by co-authoring evaluations. By establishing a taxonomy of risks, bootstrapping datasets with adversarial testing tools like Giskard, and using LLM-as-a-judge evaluators, Chime transformed compliance from a release gate into a continuous feedback loop. This approach delivered velocity, alignment between engineering and legal teams, and trust through evidence-based sign-offs.

[Read source](https://www.youtube.com/watch?v=yQ2HCSSsqTc)

---

#### Teaching Refusal Behavior Through Automated Data Curation with LLM Judge Consensus

**Company:** shopify  
**Industry:** E-commerce

Shopify's Sidekick AI assistant faced a critical challenge: its customer segmentation skill model, trained exclusively on successful production queries, couldn't recognize when to refuse impossible requests, leading to hallucinated responses and zero-result queries. To solve this, Shopify built an automated data curation pipeline using an ensemble of four frontier LLMs as judges, calibrated on a small seed dataset of 600+ human-annotated refusal examples. Through strict consensus requirements and a mutually exclusive taxonomy, they curated training data that resolved label conflicts between production logs and refusal annotations. The resulting model improved segmentation evaluation scores from 0.619 to 0.798 (28.9% relative gain), achieved 86.3% refusal accuracy with only 4.6% false positives, and established a continuous data flywheel where each production deployment generates new training signal for the next iteration.

[Read source](https://shopify.engineering/sidekick-curation)

---

### Cool Use Cases

#### Context Engineering and Memory Management for Production Agent Systems

**Company:** anthropic  
**Industry:** Tech

Anthropic's Applied AI team has developed sophisticated approaches to context engineering and memory management for production AI agent deployments, addressing the challenge of translating raw model intelligence into durable, scalable products. The solution evolved from simple markdown files injected at session start to sophisticated file-system-based memory architectures with versioning, concurrency controls, and permissioning. The team introduced "dreaming," an out-of-band batch process where dedicated agents review session transcripts to identify patterns and propose memory improvements. Results include improved accuracy on repeated tasks, reduced latency and cost through better one-shot performance, and autonomous learning that frees developers to focus on product improvements rather than manual memory curation.

[Read source](https://www.youtube.com/watch?v=tTcxVv8HHNw)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

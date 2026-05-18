# Weekly LLMOps Newsletter — 2026-05-17

*Week of 2026-05-11 (Mon) – 2026-05-17 (Sun)*

A curated, audience-aware roundup of LLMOps case studies, production patterns, tools, and use cases. The same items appear below in two voices: one for engineers and one for business readers.

## Technical Audience

Engineering-flavoured roundup: tools, techniques, architectures, and production patterns from this week's items.

### Industry News

#### Durable Agent Execution through Snapshot and Restore Infrastructure

**Company:** trigger.dev  
**Industry:** Tech

Trigger.dev addresses durable LLM agent execution by splitting durability into an append-only context log and VM-level snapshot/restore for the execution layer. They first used CRIU (checkpoint/restore in userspace) for process-level snapshots, then switched to Firecracker micro VMs to snapshot entire machines. Seekable compression reduces snapshots from ~512MB to ~14MB, enabling sub-second snapshots and ~200ms restores, with ~15,000 VM starts/min. They bundle the approach in FC Run, a Docker-like CLI running containers inside Firecracker VMs with snapshotting/restore.

[Read source](https://www.youtube.com/watch?v=svCnShDvgQg)

---

### Cool Use Cases

#### Building a Public AI Agent Workspace for Organizational Learning

**Company:** shopify  
**Industry:** E-commerce

Shopify’s River is an AI coding agent integrated into the company’s monorepo workflow. It operates exclusively in public Slack channels (declines direct messages), can read code, run tests, write code, open pull requests, query the data warehouse, and examine production traces. River uses skills, per-channel zones/instructions, and a memory system that continuously learns and un-learns critical information.

[Read source](https://x.com/tobi/status/2053121182044451016)

---

## Non-Technical Audience

Plain-language roundup: what was built, who built it, and what business outcome it produced.

### Industry News

#### Durable Agent Execution through Snapshot and Restore Infrastructure

**Company:** trigger.dev  
**Industry:** Tech

Trigger.dev’s case study focuses on how to run LLM-powered agents reliably in production when sessions can last hours or days. It explains why traditional stateless setups and replay-style workflows don’t fit. Their solution keeps conversation history in an append-only log and preserves the agent’s working environment by snapshotting and restoring lightweight VMs, reducing idle costs while maintaining state.

[Read source](https://www.youtube.com/watch?v=svCnShDvgQg)

---

### Cool Use Cases

#### Building a Public AI Agent Workspace for Organizational Learning

**Company:** shopify  
**Industry:** E-commerce

Shopify built River, an AI coding agent that works only in public Slack channels. The goal was a “teaching workshop” environment where employees learn by watching others use the agent, helping ideas and problem-solving approaches spread across the organization. In 30 days, 5,938 employees used River across 4,450 channels, and its PR merge rate rose from 36% to 77% over two months.

[Read source](https://x.com/tobi/status/2053121182044451016)

---

## Closing

Have a use case worth featuring next week? Reply to share it.

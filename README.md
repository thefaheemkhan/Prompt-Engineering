<div align="center">

# 🧠 Prompt Engineering 101

### The Complete Open-Source Roadmap to Mastering Prompt Engineering

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Contributors](https://img.shields.io/github/contributors/yourusername/prompt-engineering-101)](https://github.com/yourusername/prompt-engineering-101/graphs/contributors)
[![Stars](https://img.shields.io/github/stars/yourusername/prompt-engineering-101?style=social)](https://github.com/yourusername/prompt-engineering-101)

**From zero to elite — a structured, practical, and open-source mastery path.**

[🚀 Start Learning](#-roadmap) • [📚 Resources](#-resources) • [🤝 Contribute](#-contributing) • [🌐 Website](https://promptengineering101.dev)

</div>

---

## 🎯 What Is This?

**Prompt Engineering 101** is the only open-source, end-to-end curriculum for mastering prompt engineering — from basic input/output mechanics to advanced multi-agent orchestration and production-grade prompting systems.

This is not a collection of "cool prompts." This is a **learning system** built on:
- Deep conceptual understanding of how LLMs process language
- Hands-on implementation at every stage
- Real-world patterns used by AI engineers in production
- Progressive complexity — each module builds on the last

> **Vision:** Anyone who completes this roadmap should be able to call themselves a confident, production-ready prompt engineer — capable of building AI-powered products, passing technical interviews, and contributing to research.

---

## 🗺️ Roadmap Overview

```
Phase 0 → Foundations
Phase 1 → Core Prompting Techniques
Phase 2 → Intermediate Patterns
Phase 3 → Advanced Techniques
Phase 4 → Production Prompting
Phase 5 → Agentic & Multi-Agent Systems
Phase 6 → Evaluation & Red-Teaming
Phase 7 → Research Frontier
Phase 8 → Capstone Projects
```

**Estimated time:** 3–6 months depending on depth and pace.

---

## 📋 Table of Contents

- [Prerequisites](#-prerequisites)
- [Roadmap](#-roadmap)
  - [Phase 0: Foundations](#phase-0-foundations)
  - [Phase 1: Core Prompting Techniques](#phase-1-core-prompting-techniques)
  - [Phase 2: Intermediate Patterns](#phase-2-intermediate-patterns)
  - [Phase 3: Advanced Techniques](#phase-3-advanced-techniques)
  - [Phase 4: Production Prompting](#phase-4-production-prompting)
  - [Phase 5: Agentic & Multi-Agent Systems](#phase-5-agentic--multi-agent-systems)
  - [Phase 6: Evaluation & Red-Teaming](#phase-6-evaluation--red-teaming)
  - [Phase 7: Research Frontier](#phase-7-research-frontier)
  - [Phase 8: Capstone Projects](#phase-8-capstone-projects)
- [Resources](#-resources)
- [Repo Structure](#-repo-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✅ Prerequisites

You don't need to be a developer to start. But these help:

| Skill | Level Needed | Why |
|-------|-------------|-----|
| Basic computer literacy | Required | Navigating tools and APIs |
| Reading comprehension | Required | Understanding model outputs |
| Python (basic) | Recommended | Running code examples |
| API basics (what is REST?) | Recommended | Calling LLM APIs |
| Linear algebra / probability | Optional | Understanding phases 7+ |

**No ML background required to start. It becomes relevant in later phases.**

---

## 🗺️ Roadmap

---

### Phase 0: Foundations

> **Goal:** Understand what LLMs actually are and how they work at the level needed to engineer prompts intelligently.

Without this phase, prompting is guesswork. With it, every technique has a *why*.

#### 0.1 — How LLMs Actually Work

- Tokenization: what text looks like to a model
- Next-token prediction as the core mechanism
- Temperature, top-p, top-k — what they do to outputs
- Context windows: length, position bias, attention
- System prompts vs. user messages vs. assistant turns

📁 [`/phase-0/how-llms-work/`](phase-0/how-llms-work/)

**Practical exercises:**
- [ ] Inspect tokenization using [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [ ] Run the same prompt at temp=0 vs temp=1.5 — document differences
- [ ] Write a short explanation of "why position in context matters"

#### 0.2 — The Prompting Mental Model

- Prompts as programs
- The input → reasoning → output loop
- Understanding instruction following vs. completion
- Pre-training vs. instruction-tuning vs. RLHF: why it matters for prompting

📁 [`/phase-0/mental-models/`](phase-0/mental-models/)

**Practical exercises:**
- [ ] Identify: is a given model "base" or "instruction-tuned"?
- [ ] Write one prompt in "completion style" and one in "instruction style" — compare

#### 0.3 — Setting Up Your Environment

- API access: OpenAI, Anthropic, Google Gemini
- Using Playground / Claude.ai / AI Studio for experimentation
- Setting up a Python environment with the SDKs
- Your first API call in Python

📁 [`/phase-0/setup/`](phase-0/setup/)

**Practical exercises:**
- [ ] Get API keys from at least 2 providers
- [ ] Run `hello_world.py` in `/phase-0/setup/`
- [ ] Build a minimal CLI chatbot using the OpenAI SDK

---

### Phase 1: Core Prompting Techniques

> **Goal:** Master the fundamental, proven techniques that every prompt engineer uses daily.

#### 1.1 — Zero-Shot Prompting

- What zero-shot is and when it works
- Instruction clarity: the difference between vague and precise
- Format control: asking for specific output structures
- Persona assignment

📁 [`/phase-1/zero-shot/`](phase-1/zero-shot/)

**Practical exercises:**
- [ ] Write 5 zero-shot prompts, evaluate quality, iterate
- [ ] Practice: same task, 3 different instruction styles — rank results

#### 1.2 — Few-Shot Prompting

- Why examples teach models patterns
- Example selection: quality, diversity, format consistency
- Label bias and how to avoid it
- Ordering effects in few-shot examples

📁 [`/phase-1/few-shot/`](phase-1/few-shot/)

**Practical exercises:**
- [ ] Build a few-shot classifier for sentiment analysis
- [ ] Test: does changing example order change output quality?

#### 1.3 — Chain-of-Thought (CoT) Prompting

- "Let's think step by step" — why it works mechanistically
- Zero-shot CoT vs. few-shot CoT
- When CoT helps (and when it doesn't)
- CoT for reasoning, math, and logical inference

📁 [`/phase-1/chain-of-thought/`](phase-1/chain-of-thought/)

**Practical exercises:**
- [ ] Solve 5 math problems with and without CoT — compare accuracy
- [ ] Write a CoT prompt for a legal reasoning scenario

#### 1.4 — Instruction Engineering

- Positive vs. negative instructions
- Specificity: the "word count" problem
- Constraints and guardrails in prompts
- Role assignment

📁 [`/phase-1/instruction-engineering/`](phase-1/instruction-engineering/)

**Practical exercises:**
- [ ] Rewrite 3 weak prompts into strong ones — document what changed
- [ ] Build a "prompt stress test" — try to break your own prompt

---

### Phase 2: Intermediate Patterns

> **Goal:** Learn the patterns that separate beginner prompters from intermediate engineers.

#### 2.1 — Structured Output Prompting

- Asking for JSON, XML, Markdown, tables
- Schema enforcement in prompts
- Handling hallucinated structure
- Combining with parsing logic in code

📁 [`/phase-2/structured-output/`](phase-2/structured-output/)

**Practical exercises:**
- [ ] Build a prompt that extracts structured data from unstructured text
- [ ] Write a parser that handles model deviations from your schema

#### 2.2 — System Prompt Engineering

- The role of the system prompt in instruction-tuned models
- Layered instructions: system → user → assistant
- Persona persistence across turns
- Security: prompt injection via system prompts

📁 [`/phase-2/system-prompts/`](phase-2/system-prompts/)

**Practical exercises:**
- [ ] Design a system prompt for a customer support bot
- [ ] Attempt to "jailbreak" your own system prompt — then fix the hole

#### 2.3 — Context Management

- Context window limits in practice
- Chunking strategies for long documents
- Summarization chains
- Retrieval-Augmented Generation (RAG) fundamentals

📁 [`/phase-2/context-management/`](phase-2/context-management/)

**Practical exercises:**
- [ ] Implement a naive document Q&A using chunking + prompting
- [ ] Build a summarization chain for a 10,000-word document

#### 2.4 — Persona & Role Design

- Designing AI personas with consistent voice and behavior
- Role stacking (e.g., "You are a senior doctor AND a clear communicator")
- Avoiding persona drift in long conversations
- Ethical considerations in persona design

📁 [`/phase-2/persona-design/`](phase-2/persona-design/)

**Practical exercises:**
- [ ] Design 3 different personas for the same use case — compare outputs
- [ ] Test persona consistency over 20-turn conversations

---

### Phase 3: Advanced Techniques

> **Goal:** Techniques used in production AI systems and research settings.

#### 3.1 — Tree of Thoughts (ToT)

- Going beyond linear CoT to branching exploration
- Implementing ToT with self-evaluation
- Use cases: planning, strategy, creative writing
- ToT vs CoT: when to use each

📁 [`/phase-3/tree-of-thoughts/`](phase-3/tree-of-thoughts/)

**Practical exercises:**
- [ ] Implement a ToT framework from scratch using the OpenAI API
- [ ] Solve a Sudoku or planning puzzle using ToT

#### 3.2 — Self-Consistency & Majority Voting

- Sampling multiple reasoning paths and aggregating
- Why self-consistency improves accuracy on complex tasks
- Implementation: multiple calls + answer extraction + voting
- Cost/accuracy tradeoffs

📁 [`/phase-3/self-consistency/`](phase-3/self-consistency/)

**Practical exercises:**
- [ ] Implement self-consistency for a math benchmark (5 samples, vote)
- [ ] Plot accuracy vs. N samples for a fixed task

#### 3.3 — Prompt Chaining

- Decomposing complex tasks into sequential prompts
- Passing outputs as inputs: the chain pattern
- Conditional branching in chains
- Error handling between chain steps

📁 [`/phase-3/prompt-chaining/`](phase-3/prompt-chaining/)

**Practical exercises:**
- [ ] Build a 4-step research pipeline: search → summarize → analyze → write
- [ ] Add error-recovery logic to a broken chain step

#### 3.4 — Meta-Prompting

- Prompts that generate prompts
- Using LLMs to critique and improve their own prompts
- Automatic prompt optimization basics
- Recursive improvement loops

📁 [`/phase-3/meta-prompting/`](phase-3/meta-prompting/)

**Practical exercises:**
- [ ] Build a "prompt improver" that takes a weak prompt and outputs a better one
- [ ] Run a 3-iteration improvement loop and score each version

#### 3.5 — ReAct (Reasoning + Acting)

- The ReAct pattern: Thought → Action → Observation → repeat
- Implementing ReAct with tool use
- Tool definitions: search, calculator, code execution
- ReAct vs. pure CoT: when grounding matters

📁 [`/phase-3/react/`](phase-3/react/)

**Practical exercises:**
- [ ] Implement a ReAct agent with web search and a calculator tool
- [ ] Compare ReAct vs CoT on a factual Q&A benchmark

---

### Phase 4: Production Prompting

> **Goal:** Engineering prompts for real products — reliability, safety, cost, and maintainability.

#### 4.1 — Prompt Templates & Versioning

- Parameterized prompt templates
- Version control for prompts (like code)
- A/B testing prompt versions
- Prompt registries and management systems

📁 [`/phase-4/templates-versioning/`](phase-4/templates-versioning/)

**Practical exercises:**
- [ ] Build a prompt template system with variable injection in Python
- [ ] Set up a Git-based prompt versioning workflow

#### 4.2 — Latency & Cost Optimization

- Token counting and budget management
- Prompt compression techniques
- Model routing: when to use cheap vs. expensive models
- Caching strategies for repeated prompts

📁 [`/phase-4/optimization/`](phase-4/optimization/)

**Practical exercises:**
- [ ] Profile a prompt: count tokens, estimate cost at scale (1M calls)
- [ ] Compress a 2,000-token prompt to under 500 tokens without quality loss

#### 4.3 — Reliability Engineering

- Handling refusals and safety filters
- Output validation and retry logic
- Fallback chains (model A fails → model B)
- Determinism: when and how to force consistent outputs

📁 [`/phase-4/reliability/`](phase-4/reliability/)

**Practical exercises:**
- [ ] Build a retry-with-fallback wrapper for an LLM call
- [ ] Design a validation layer that catches bad outputs before they reach users

#### 4.4 — Safety, Ethics & Responsible Prompting

- Prompt injection attacks and defenses
- Jailbreaking patterns and how to mitigate them
- Bias in prompts and outputs
- Building responsible AI products: guardrails and escalation paths

📁 [`/phase-4/safety-ethics/`](phase-4/safety-ethics/)

**Practical exercises:**
- [ ] Audit a production prompt for injection vulnerabilities
- [ ] Design a moderation layer for a user-facing chatbot

---

### Phase 5: Agentic & Multi-Agent Systems

> **Goal:** Build and orchestrate agents that use tools, memory, and collaborate with other agents.

#### 5.1 — Single-Agent Architectures

- The agent loop: perceive → plan → act → observe
- Tool use: function calling and structured tool definitions
- Memory: in-context, external (vector DB), episodic
- Planning strategies: ReAct, Plan-and-Execute, Reflexion

📁 [`/phase-5/single-agent/`](phase-5/single-agent/)

**Practical exercises:**
- [ ] Build a research agent with 3 tools: web search, summarizer, file writer
- [ ] Add episodic memory to your agent using a simple JSON store

#### 5.2 — Multi-Agent Orchestration

- Why single agents fail on complex tasks
- Orchestrator vs. worker agents
- Communication protocols between agents
- Frameworks: LangGraph, CrewAI, AutoGen (understanding the patterns, not just using the library)

📁 [`/phase-5/multi-agent/`](phase-5/multi-agent/)

**Practical exercises:**
- [ ] Build a 3-agent pipeline: planner + researcher + writer
- [ ] Implement a review loop where Agent B critiques Agent A's output

#### 5.3 — Memory Systems for Agents

- Working memory (context window)
- Long-term memory (vector stores, databases)
- Semantic vs. episodic vs. procedural memory
- Memory retrieval strategies for agents

📁 [`/phase-5/memory-systems/`](phase-5/memory-systems/)

**Practical exercises:**
- [ ] Implement a vector-store-backed memory for a conversational agent
- [ ] Test memory recall across 50-turn conversations

---

### Phase 6: Evaluation & Red-Teaming

> **Goal:** Measure prompt quality rigorously and stress-test systems before production.

#### 6.1 — Prompt Evaluation Frameworks

- What makes a good evaluation?
- LLM-as-Judge: using models to score models
- Human eval vs. automated eval
- Metrics: accuracy, faithfulness, coherence, safety

📁 [`/phase-6/evaluation/`](phase-6/evaluation/)

**Practical exercises:**
- [ ] Build an LLM-as-Judge evaluator for a summarization task
- [ ] Design a 20-question benchmark for your own use case

#### 6.2 — Red-Teaming & Adversarial Testing

- What is red-teaming in AI?
- Adversarial prompt patterns: injection, jailbreaking, data extraction
- Building a red-team evaluation suite
- Reporting and fixing vulnerabilities

📁 [`/phase-6/red-teaming/`](phase-6/red-teaming/)

**Practical exercises:**
- [ ] Run a structured red-team on a chatbot you built
- [ ] Write a 1-page security report documenting findings and fixes

#### 6.3 — Benchmarking Models for Your Use Case

- Why generic benchmarks (MMLU, HellaSwag) don't tell you what you need
- Building task-specific benchmarks
- Automated benchmark pipelines
- Interpreting results and making model selection decisions

📁 [`/phase-6/benchmarking/`](phase-6/benchmarking/)

**Practical exercises:**
- [ ] Create a 50-question benchmark for a domain (e.g., medical, legal, coding)
- [ ] Run your benchmark on 3 models and produce a comparison report

---

### Phase 7: Research Frontier

> **Goal:** Understand where prompting research is heading and engage with cutting-edge papers.

#### 7.1 — Automatic Prompt Optimization (APO)

- DSPy: prompts as learnable parameters
- Gradient-free optimization of prompts
- Prompt tuning vs. full fine-tuning
- Soft prompts and prefix tuning

📁 [`/phase-7/auto-optimization/`](phase-7/auto-optimization/)

**Reading list:**
- [ ] [AutoPrompt (2020)](https://arxiv.org/abs/2010.15980)
- [ ] [DSPy: Compiling Declarative Language Model Calls (2023)](https://arxiv.org/abs/2310.03714)

#### 7.2 — Mechanistic Interpretability for Prompt Engineers

- What attention heads actually attend to
- Induction heads and in-context learning
- Superposition and feature representations
- Using interpretability to debug prompt failures

📁 [`/phase-7/mechanistic-interpretability/`](phase-7/mechanistic-interpretability/)

**Reading list:**
- [ ] [In-context Learning and Induction Heads (2022)](https://arxiv.org/abs/2209.11895)
- [ ] [Toy Models of Superposition (2022)](https://arxiv.org/abs/2209.11895)

#### 7.3 — Prompting for Reasoning Models

- How o1, o3, Gemini Thinking, DeepSeek R1 differ from standard models
- Chain-of-thought internalized vs. externalized
- What changes in prompting strategy for "thinking" models
- When NOT to use reasoning models

📁 [`/phase-7/reasoning-models/`](phase-7/reasoning-models/)

**Reading list:**
- [ ] [DeepSeek-R1 Technical Report (2025)](https://arxiv.org/abs/2501.12948)

#### 7.4 — Multimodal Prompting

- Vision-language models: GPT-4V, Claude 3, Gemini
- Image prompting strategies: description, comparison, OCR, grounding
- Audio and video prompting (emerging)
- Interleaved text-image prompts

📁 [`/phase-7/multimodal/`](phase-7/multimodal/)

**Practical exercises:**
- [ ] Build a visual Q&A pipeline using GPT-4V or Claude 3
- [ ] Design a multimodal prompt for document understanding

---

### Phase 8: Capstone Projects

> **Goal:** Integrate everything into production-grade projects. These prove mastery.

Each capstone has a specification, starter code, evaluation rubric, and community showcase.

| # | Project | Techniques Used | Difficulty |
|---|---------|----------------|------------|
| 1 | AI Research Assistant | RAG, CoT, tool use, prompt chains | ⭐⭐⭐ |
| 2 | Automated Code Reviewer | Structured output, evaluation, personas | ⭐⭐⭐ |
| 3 | Multi-Agent Report Generator | Multi-agent, memory, orchestration | ⭐⭐⭐⭐ |
| 4 | Prompt Optimization Pipeline | Meta-prompting, APO, benchmarking | ⭐⭐⭐⭐ |
| 5 | Red-Team & Defend a Chatbot | Red-teaming, safety, eval frameworks | ⭐⭐⭐⭐⭐ |

📁 [`/phase-8/capstones/`](phase-8/capstones/)

---

## 📚 Resources

### Essential Reading

| Resource | Type | Phase Relevance |
|----------|------|----------------|
| [Anthropic Prompt Engineering Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Docs | All |
| [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) | Docs | 0–3 |
| [Prompt Engineering Guide (DAIR.AI)](https://www.promptingguide.ai/) | Guide | 0–3 |
| [DSPy Documentation](https://dspy-docs.vercel.app/) | Docs | 7 |

### Key Papers

| Paper | Year | Why It Matters |
|-------|------|---------------|
| [Chain-of-Thought Prompting Elicits Reasoning](https://arxiv.org/abs/2201.11903) | 2022 | Foundation of CoT |
| [Self-Consistency Improves CoT Reasoning](https://arxiv.org/abs/2203.11171) | 2022 | Key reasoning technique |
| [Tree of Thoughts](https://arxiv.org/abs/2305.10601) | 2023 | Advanced planning |
| [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) | 2022 | Foundation of agents |
| [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) | 2022 | Zero-shot CoT |
| [Constitutional AI](https://arxiv.org/abs/2212.08073) | 2022 | Safety in prompting |
| [DSPy](https://arxiv.org/abs/2310.03714) | 2023 | Automated prompting |
| [Reflexion](https://arxiv.org/abs/2303.11366) | 2023 | Agent self-improvement |

### Tools

| Tool | Use Case |
|------|---------|
| [LangChain](https://langchain.com) | Prompt chaining & RAG |
| [DSPy](https://github.com/stanfordnlp/dspy) | Automatic prompt optimization |
| [PromptFlow](https://github.com/microsoft/promptflow) | Production prompt pipelines |
| [Braintrust](https://braintrust.dev) | Prompt evaluation |
| [LangSmith](https://smith.langchain.com) | Tracing & evaluation |
| [Weights & Biases](https://wandb.ai) | Experiment tracking |

---

## 📁 Repo Structure

```
prompt-engineering-101/
│
├── README.md                    ← You are here
├── CONTRIBUTING.md              ← How to contribute
├── ROADMAP.md                   ← Detailed phase roadmap
├── LICENSE
│
├── phase-0/                     ← Foundations
│   ├── how-llms-work/
│   │   ├── README.md
│   │   ├── tokenization.ipynb
│   │   └── temperature-demo.ipynb
│   ├── mental-models/
│   │   └── README.md
│   └── setup/
│       ├── README.md
│       ├── hello_world.py
│       └── requirements.txt
│
├── phase-1/                     ← Core Techniques
│   ├── zero-shot/
│   ├── few-shot/
│   ├── chain-of-thought/
│   └── instruction-engineering/
│
├── phase-2/                     ← Intermediate Patterns
│   ├── structured-output/
│   ├── system-prompts/
│   ├── context-management/
│   └── persona-design/
│
├── phase-3/                     ← Advanced Techniques
│   ├── tree-of-thoughts/
│   ├── self-consistency/
│   ├── prompt-chaining/
│   ├── meta-prompting/
│   └── react/
│
├── phase-4/                     ← Production Prompting
│   ├── templates-versioning/
│   ├── optimization/
│   ├── reliability/
│   └── safety-ethics/
│
├── phase-5/                     ← Agentic Systems
│   ├── single-agent/
│   ├── multi-agent/
│   └── memory-systems/
│
├── phase-6/                     ← Evaluation & Red-Teaming
│   ├── evaluation/
│   ├── red-teaming/
│   └── benchmarking/
│
├── phase-7/                     ← Research Frontier
│   ├── auto-optimization/
│   ├── mechanistic-interpretability/
│   ├── reasoning-models/
│   └── multimodal/
│
├── phase-8/                     ← Capstone Projects
│   └── capstones/
│       ├── 01-research-assistant/
│       ├── 02-code-reviewer/
│       ├── 03-multi-agent-reporter/
│       ├── 04-prompt-optimizer/
│       └── 05-red-team-defend/
│
├── templates/                   ← Reusable prompt templates
│   ├── reasoning/
│   ├── extraction/
│   ├── generation/
│   └── evaluation/
│
├── prompt-library/              ← Community-contributed prompts
│   └── README.md
│
└── resources/
    ├── papers.md
    ├── tools.md
    └── glossary.md
```

---

## 🤝 Contributing

**This is an open-source project — built by the community, for the community.**

We welcome:
- New exercises and notebooks
- Corrections and improvements
- Translations
- Prompt library contributions
- New tool coverage
- Case studies from real-world use

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a PR.

### Quick Contribution Guide

```bash
# 1. Fork the repo
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/prompt-engineering-101.git

# 3. Create a branch
git checkout -b add/phase-2-rag-exercise

# 4. Make your changes
# 5. Commit with a clear message
git commit -m "Add RAG chunking exercise to phase-2/context-management"

# 6. Push and open a PR
git push origin add/phase-2-rag-exercise
```

See [open issues](https://github.com/yourusername/prompt-engineering-101/issues) for tasks labeled `good first issue` and `help wanted`.

---

## 📜 License

MIT License — see [`LICENSE`](LICENSE) for full text.

---

## ⭐ Star History

If this helped you, please star the repo. It helps others find it.

---

<div align="center">

**Built with 🧠 by the community. Made for everyone.**

[🐦 Twitter](https://twitter.com/yourusername) • [💼 LinkedIn](https://linkedin.com/in/yourusername) • [🌐 Website](https://promptengineering101.dev)

</div>

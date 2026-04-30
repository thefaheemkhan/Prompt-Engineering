# Glossary of Prompt Engineering Terms

A living reference. All terms alphabetically ordered.

---

## A

**Agentic System**
An AI system where a language model iteratively decides actions (tool calls, reasoning steps) based on observations from the environment, rather than producing a single response.

**APO (Automatic Prompt Optimization)**
The process of using algorithms (including other LLMs) to automatically improve prompts, rather than hand-engineering them.

**Attention Mechanism**
The core operation in Transformers that allows each token to "attend" to (weigh) other tokens when producing its representation. Prompt engineers benefit from understanding that early tokens in context often receive more attention weight.

---

## B

**Base Model**
A language model trained only on next-token prediction (no instruction tuning or RLHF). Base models complete text rather than following instructions — prompting them requires a different approach.

**Benchmark**
A standardized evaluation dataset used to compare model or prompt performance. Examples: MMLU, HellaSwag, HumanEval.

---

## C

**Chain-of-Thought (CoT)**
A prompting technique where the model is asked (or shown via examples) to produce intermediate reasoning steps before a final answer. Improves accuracy on multi-step tasks.

**Context Window**
The maximum number of tokens a model can process in a single request (input + output combined). Exceeding this causes truncation.

**CoT Prompting → see Chain-of-Thought**

---

## F

**Few-Shot Prompting**
Providing the model with 2–10 labeled examples of the task within the prompt before the actual input. Helps the model understand the desired format and behavior without fine-tuning.

**Fine-Tuning**
Training a pre-trained model further on a task-specific dataset. Distinct from prompting — modifies model weights, whereas prompting does not.

**Function Calling**
A structured mechanism (available via API) where the model outputs a structured function invocation (name + arguments) instead of free text, allowing reliable tool use.

---

## G

**Grounding**
Connecting model outputs to real-world sources of truth (documents, databases, search results). RAG is a grounding technique.

---

## H

**Hallucination**
When a model generates plausible-sounding but factually incorrect information. A key challenge that prompting strategies like grounding, CoT, and retrieval aim to reduce.

---

## I

**In-Context Learning (ICL)**
The ability of LLMs to "learn" a task pattern from examples provided in the prompt, without weight updates. The mechanism underlying few-shot prompting.

**Instruction Tuning**
Post-training a base model on (instruction, response) pairs to make it follow natural language instructions. Most production models (GPT-4, Claude, Gemini) are instruction-tuned.

---

## J

**Jailbreak**
A prompt designed to bypass a model's safety constraints and generate content it was trained to refuse.

**JSON Mode**
An API feature (available in some models) that constrains the model to output valid JSON only.

---

## L

**LLM-as-Judge**
Using a language model to evaluate the output of another language model (or itself). A scalable alternative to human evaluation.

**Latency**
The time between sending a prompt and receiving the complete response. Affected by model size, token count, and infrastructure.

---

## M

**Meta-Prompting**
Using a prompt to generate, evaluate, or improve other prompts. Example: "Given this prompt, what are its weaknesses? Rewrite it to be more effective."

**Multi-Agent System**
An architecture where multiple LLM agents with different roles collaborate on a task — e.g., a planner agent, a researcher agent, and a writer agent.

---

## O

**Orchestrator**
In multi-agent systems, the agent responsible for coordinating other agents — deciding what task to assign and when.

---

## P

**Persona**
A defined role, personality, or character assigned to the model via the system prompt to shape its responses.

**Prefix Tuning**
A parameter-efficient fine-tuning method that prepends learnable "soft prompt" vectors to the input, rather than modifying all model weights.

**Prompt**
The input provided to a language model. Includes all text the model uses to generate its response: system instructions, user messages, and example turns.

**Prompt Chaining**
Breaking a complex task into a sequence of prompts where the output of one becomes the input of the next.

**Prompt Injection**
An adversarial attack where malicious instructions embedded in user input (or retrieved documents) override the original system prompt.

**Prompt Template**
A reusable prompt structure with placeholder variables that can be filled at runtime.

---

## R

**RAG (Retrieval-Augmented Generation)**
A technique that retrieves relevant documents from an external store (usually a vector database) and includes them in the prompt before generation. Reduces hallucination and extends effective context.

**ReAct**
A prompting pattern combining Reasoning (CoT-style thinking) with Acting (tool use), structured as: Thought → Action → Observation → Thought → ...

**RLHF (Reinforcement Learning from Human Feedback)**
A post-training technique that fine-tunes models to produce outputs that human raters prefer. Responsible for much of the instruction-following ability of modern LLMs.

---

## S

**Self-Consistency**
Generating multiple independent reasoning chains for the same problem and selecting the most frequent final answer by majority vote.

**Self-Refinement / Reflexion**
Techniques where a model critiques its own output and iteratively improves it.

**System Prompt**
The initial instruction given to an instruction-tuned model before the conversation begins. Sets the model's persona, constraints, and task.

---

## T

**Temperature**
A sampling parameter (0–2) controlling output randomness. Low temperature → deterministic/conservative. High temperature → creative/unpredictable.

**Token**
The unit of text a model processes. Roughly 1 token ≈ 0.75 words in English. Models count input and output tokens separately.

**Tool Use → see Function Calling**

**Top-p (Nucleus Sampling)**
A sampling method that considers only the smallest set of tokens whose cumulative probability exceeds p. Alternative to temperature for controlling diversity.

**Tree of Thoughts (ToT)**
An extension of CoT where multiple reasoning paths branch and are evaluated at each step, allowing backtracking and exploration of alternatives.

---

## V

**Vector Database**
A database optimized for storing and searching high-dimensional vector embeddings. Used in RAG systems to retrieve semantically relevant documents.

---

## Z

**Zero-Shot Prompting**
Asking the model to perform a task with no examples, relying entirely on its pre-trained knowledge and instruction-following ability.

---

*Missing a term? [Open an issue](https://github.com/yourusername/prompt-engineering-101/issues) or submit a PR.*

# Phase 1.3 — Chain-of-Thought (CoT) Prompting

## Goal

By the end of this module you will understand why CoT works, when to use it, and be able to implement both zero-shot and few-shot CoT in your own prompts with measurable accuracy gains.

---

## The Core Idea

Standard prompting: `Question → Answer`

Chain-of-Thought: `Question → Reasoning Steps → Answer`

When you ask a model to think before it answers, it forces computation to happen in the "visible" token space rather than being compressed into a single output. This dramatically improves performance on tasks requiring multi-step reasoning.

---

## Why It Works (Mechanistic Intuition)

LLMs generate text autoregressively — each token is conditioned on all previous tokens. By generating intermediate reasoning steps, the model:

1. Creates a richer context that informs the final answer
2. "Breaks down" complex inference into simpler subproblems
3. Reduces the chance of jumping to a wrong conclusion

This is analogous to how humans perform better on hard math problems when they write out their work.

---

## Zero-Shot CoT

The simplest version: append `"Let's think step by step."` to your prompt.

```python
# Without CoT
prompt = "Roger has 5 tennis balls. He buys 2 cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?"
# → Model often says: 8 (wrong)

# With Zero-Shot CoT
prompt = """Roger has 5 tennis balls. He buys 2 cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?

Let's think step by step."""
# → Model reasons: 5 + (2 × 3) = 5 + 6 = 11 ✓
```

**Paper:** [Large Language Models are Zero-Shot Reasoners (Kojima et al., 2022)](https://arxiv.org/abs/2205.11916)

---

## Few-Shot CoT

Provide examples that include reasoning traces, not just answers.

```python
prompt = """
Q: There are 15 trees in a grove. After today, the grove will have 21 trees. How many trees were planted?
A: Let's think step by step. 
   We start with 15 trees. 
   We end with 21 trees. 
   21 - 15 = 6 trees were planted.
   The answer is 6.

Q: If there are 3 cars in a parking lot and 2 more cars arrive, how many cars are in the parking lot?
A: Let's think step by step.
   We start with 3 cars.
   2 more cars arrive.
   3 + 2 = 5 cars total.
   The answer is 5.

Q: Roger has 5 tennis balls. He buys 2 cans of tennis balls. Each can has 3 balls. How many does he have now?
A:"""
```

**Paper:** [Chain-of-Thought Prompting Elicits Reasoning (Wei et al., 2022)](https://arxiv.org/abs/2201.11903)

---

## When CoT Helps (and When It Doesn't)

| Task Type | CoT Helps? | Why |
|-----------|-----------|-----|
| Multi-step math | ✅ Yes | Requires sequential computation |
| Logical inference | ✅ Yes | Requires tracking state |
| Commonsense reasoning | ✅ Yes | Requires multi-hop connections |
| Factual recall ("What year was X born?") | ❌ No | Single-step lookup |
| Simple classification | ❌ No | Adds tokens without benefit |
| Creative writing | ⚠️ Depends | Can help with structure, harms flow |

**Rule of thumb:** If you wouldn't need scratch paper to solve it, CoT probably won't help.

---

## Practical Exercises

- [ ] **Exercise 1:** Test CoT on 5 math problems. Run each with and without CoT. Record accuracy.
- [ ] **Exercise 2:** Write a few-shot CoT prompt for a legal reasoning task (e.g., "Is this contract clause enforceable?")
- [ ] **Exercise 3:** Find a task where CoT *hurts* performance — document why.
- [ ] **Exercise 4:** Implement `cot_benchmark.py` — run 20 GSM8K problems with/without CoT, compare accuracy.

---

## Common Mistakes

**"Let's think step by step" always helps"**
→ Not true. On simple tasks it wastes tokens and can introduce unnecessary reasoning that confuses the answer.

**Forgetting to extract the final answer**
→ CoT outputs a reasoning trace + answer mixed together. Parse carefully. A pattern like `"The answer is X"` at the end helps.

**Using CoT for latency-sensitive applications without profiling**
→ CoT increases output tokens significantly. At scale, this matters for cost and speed.

---

## Further Reading

- [Wei et al., 2022 — Chain-of-Thought Paper](https://arxiv.org/abs/2201.11903)
- [Kojima et al., 2022 — Zero-Shot CoT](https://arxiv.org/abs/2205.11916)
- [Anthropic's CoT guidance](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought)

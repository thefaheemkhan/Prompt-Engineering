# Contributing to Prompt Engineering 101

First off — thank you. This project exists because of contributors like you.

## What We're Looking For

| Type | Examples |
|------|---------|
| 📝 Content | New lessons, better explanations, deeper dives |
| 💻 Code | Exercises, notebooks, starter code, solutions |
| 🐛 Fixes | Typos, broken links, outdated information |
| 🌐 Translations | Any language welcome |
| 📊 Benchmarks | New evaluation datasets and scripts |
| 🔖 Prompts | Well-documented prompts for the prompt library |

## Ground Rules

1. **Quality over quantity.** One excellent PR beats ten mediocre ones.
2. **Explain your reasoning.** If you change an explanation, say why the old one was unclear.
3. **Be respectful.** This is a welcoming community. No gatekeeping.
4. **Stay on-topic.** Contributions should serve the learning roadmap.
5. **Test your code.** All code examples must run without errors.

## How to Contribute

### Step 1: Find Something to Work On

- Browse [open issues](https://github.com/yourusername/prompt-engineering-101/issues)
- Look for `good first issue` or `help wanted` labels
- Have your own idea? Open an issue first to discuss

### Step 2: Fork & Clone

```bash
git clone https://github.com/YOUR_USERNAME/prompt-engineering-101.git
cd prompt-engineering-101
```

### Step 3: Create a Branch

Use a descriptive branch name:
```bash
git checkout -b add/phase-3-tree-of-thoughts-exercise
git checkout -b fix/phase-1-few-shot-typo
git checkout -b translate/phase-0-spanish
```

### Step 4: Make Your Changes

Follow the standards below.

### Step 5: Commit

Write clear commit messages:
```
add: CoT exercise with math benchmark in phase-1
fix: broken link to ReAct paper in phase-3
improve: clarify tokenization explanation in phase-0
```

### Step 6: Open a Pull Request

- Fill out the PR template completely
- Link the relevant issue
- Add screenshots/examples if relevant

---

## Content Standards

### For Lessons (README.md in each module)

Every module README should have:
1. **Goal** — what the learner will be able to do after this module
2. **Concept explanation** — clear, concise, example-driven
3. **Why it works** — mechanistic intuition, not just "try this"
4. **Practical exercises** — minimum 2, with checkboxes
5. **Common mistakes** — what beginners get wrong
6. **Further reading** — 2–3 links max

### For Code / Notebooks

- Must run end-to-end without modification (use env vars for API keys)
- Include a `requirements.txt` or conda env spec
- Add comments explaining *why*, not just *what*
- Use `python-dotenv` for API key loading

```python
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### For Prompt Library Contributions

Each prompt in `/prompt-library/` should include:
- **Name**
- **Category** (reasoning, extraction, generation, evaluation, etc.)
- **Model(s) tested on**
- **The prompt** (with `{variable}` placeholders clearly marked)
- **Example input**
- **Example output**
- **Notes** on when to use / avoid

---

## What We Won't Merge

- Content that promotes harmful use of AI
- Marketing material or self-promotion
- Prompts for jailbreaking or bypassing safety systems
- Plagiarized content
- Code that doesn't run

---

## Questions?

Open a [Discussion](https://github.com/yourusername/prompt-engineering-101/discussions) — not an issue — for general questions.

Thank you for making this better. 🙏

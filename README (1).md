# Phase 0.3 — Setting Up Your Environment

## Goal

By the end of this module, you will have:
- API access to at least one major LLM provider
- A working Python environment
- Made your first API call programmatically

---

## Step 1: Get API Keys

Sign up and get keys from:
- [OpenAI Platform](https://platform.openai.com) → API Keys
- [Anthropic Console](https://console.anthropic.com) → API Keys
- [Google AI Studio](https://aistudio.google.com) → Get API Key

> Store keys in a `.env` file. **Never commit API keys to git.**

---

## Step 2: Install Dependencies

```bash
pip install openai anthropic google-generativeai python-dotenv
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

---

## Step 3: Create Your `.env` File

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AI...
```

Add `.env` to your `.gitignore`:
```
echo ".env" >> .gitignore
```

---

## Step 4: Run Your First API Call

```bash
python hello_world.py
```

You should see a response from the model printed to your terminal.

---

## Practical Exercises

- [ ] Get API keys from at least 2 providers
- [ ] Run `hello_world.py` and get a successful response
- [ ] Modify the prompt in `hello_world.py` to ask something else
- [ ] Build a minimal CLI chatbot that maintains conversation history (multi-turn)

---

## Common Mistakes

**"I got an AuthenticationError"**
→ Your API key is wrong or not loaded. Check your `.env` file and that `load_dotenv()` is called before using the key.

**"I got a RateLimitError"**
→ You've exceeded API limits. Add `time.sleep(1)` between calls in loops.

**"My key is in my code and I pushed to GitHub"**
→ Revoke that key immediately at the provider's dashboard. Then create a new one.

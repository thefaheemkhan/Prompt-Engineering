"""
Prompt Engineering 101 — Phase 0: Your First API Call
=====================================================
Run this file to verify your environment is working.
Make sure you have a .env file with your API keys.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────────────────────────
# OPTION 1: OpenAI
# ─────────────────────────────────────────────

def hello_openai():
    from openai import OpenAI
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # cheap model for testing
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "In one sentence, what is prompt engineering?"
            }
        ],
        temperature=0.7,
        max_tokens=100
    )
    
    return response.choices[0].message.content


# ─────────────────────────────────────────────
# OPTION 2: Anthropic (Claude)
# ─────────────────────────────────────────────

def hello_anthropic():
    import anthropic
    
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",  # fast and cheap for testing
        max_tokens=100,
        system="You are a helpful assistant.",
        messages=[
            {
                "role": "user",
                "content": "In one sentence, what is prompt engineering?"
            }
        ]
    )
    
    return message.content[0].text


# ─────────────────────────────────────────────
# OPTION 3: Google Gemini
# ─────────────────────────────────────────────

def hello_gemini():
    import google.generativeai as genai
    
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    response = model.generate_content("In one sentence, what is prompt engineering?")
    return response.text


# ─────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("Prompt Engineering 101 — Hello World")
    print("=" * 50)
    
    # Try each provider — comment out ones you don't have keys for
    
    providers = {
        "OpenAI": hello_openai,
        "Anthropic": hello_anthropic,
        "Gemini": hello_gemini,
    }
    
    for name, fn in providers.items():
        try:
            result = fn()
            print(f"\n✅ {name}:\n{result}")
        except Exception as e:
            print(f"\n❌ {name} failed: {type(e).__name__}: {e}")
    
    print("\n" + "=" * 50)
    print("If you see ✅ for at least one provider, you're ready to go!")
    print("=" * 50)

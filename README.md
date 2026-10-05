# Simple Rule-Based Chatbot

A traditional, non-LLM chatbot built with Python and NLTK for an HCI course project.  
Uses regular expression pattern matching and predefined response templates — no machine learning.

## How to run

**Option 1 — VS Code / local terminal**

```bash
pip install nltk
python chatbot.py
```

**Option 2 — Google Colab**

Paste the contents of `chatbot.py` into a cell and run.  
NLTK data downloads automatically on first run.

## Supported intents

| Intent       | Example inputs                          |
|--------------|-----------------------------------------|
| greeting     | hi, hello, hey, good morning            |
| farewell     | bye, goodbye, see you, take care        |
| capabilities | help, what can you do, commands         |
| identity     | who are you, what are you, your name    |
| thanks       | thanks, thank you, cheers               |
| fallback     | anything not matched above              |

## Project structure

```
chatbot.py        Main script — run this
requirements.txt  Python dependencies
README.md         This file
```

## Known limitations

- No memory across turns (stateless)
- Pattern coverage is finite — uncommon phrasings fall to fallback
- No context-awareness or multi-turn conversation tracking

## Extending the bot

Add a new entry to the `INTENTS` dictionary in `chatbot.py`:

```python
"weather": {
    "patterns": [r"weather", r"temperature", r"forecast"],
    "responses": ["I can't check live weather, but you could ask a weather API!"]
}
```

That's all it takes. The matching engine requires no changes.

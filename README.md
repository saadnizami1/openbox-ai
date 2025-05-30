# OpenBox AI – Simple Transparent AI Agent

Welcome to **OpenBox AI**, a powerful AI agent that helps you with tasks using OpenAI’s GPT models — while **showing you every step it takes**.

---

## What is this project?

OpenBox AI is a **tiny, transparent AI assistant**. Unlike many AI tools that hide what’s going on inside, OpenBox AI logs every step it makes — what it thinks, how it decides, and what answer it produces. This means:

- You get a full record of the AI’s "thought process" in a log file.
- You can trust and understand the AI better.
- It's a starting point for building **explainable AI** systems.

---

## How does it work?

1. You enter a task or question.
2. The agent creates a detailed prompt telling GPT how to solve it step-by-step.
3. The agent sends this prompt to OpenAI’s API.
4. The AI replies with its answer.
5. Every step (task, prompt, answer) is saved in a log file named like `log_YYYYMMDD_HHMMSS.txt`.
6. You can read the log to see exactly how the AI arrived at its answer.

---

## Why is this cool?

- **Transparency:** AI is often a “black box.” OpenBox AI opens that box so you can peek inside.
- **Learning:** By reading the logs, you learn how GPT thinks and answers questions.
- **Extendability:** This simple code is the foundation. You can build on it — add plugins, memory, or multi-step reasoning.
- **Open source:** You can tweak, share, or improve the code freely!

---

## Setup Instructions

1. **Get an OpenAI API key** (if you don’t have one, sign up at [OpenAI](https://platform.openai.com/)).

2. **Edit `main.py`**:

   Find this line near the top:

   ```python
   openai.api_key = "your-api-key-here"  #  Put your OpenAI key here

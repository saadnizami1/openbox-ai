import openai
from datetime import datetime
import os

openai.api_key = "your-api-key-here"  # 👈 Put your OpenAI key here

LOG_FILE = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def log_step(title, content):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {title}:\n{content}\n\n")

def build_prompt(task):
    return f"You are an AI agent. Task: {task}. Think step-by-step."

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    task = input("Enter your task: ")
    log_step("Task received", task)

    prompt = build_prompt(task)
    log_step("Built prompt", prompt)

    response = ask_gpt(prompt)
    log_step("LLM response", response)

    print("\nFinal Output:\n", response)

if __name__ == "__main__":
    main()

from ollama import chat

model = "qwen3.5"

print("Thinking...")

stream = chat(model=model,messages=[
    {
        "role": "user",
        "content": "Explain Python iterator with a quick example"
    }
   ],
   stream=True,
)

for chunk in stream:
    print(chunk.message.content, end="",flush=True)
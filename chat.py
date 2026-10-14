from ollama import chat

def model_chat(role,prompt,model):

    print("Thinking...")

    stream = chat(model=model,messages=[
        {
            "role": role,
            "content": prompt,
        }
      ],
      stream=True,
    )

    for chunk in stream:
        print(chunk.message.content, end="",flush=True)
    
    return True
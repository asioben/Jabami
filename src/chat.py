from ollama import chat

def model_chat(prompt,model,thinking_mode,name,system):

    print("Thinking...")

    stream = chat(model=model,messages=[
        system,

        {
            "role": "user",
            "content": prompt,
        }
      ],
      stream=True,
    )

    print("Thinking...")
    switch = False

    for chunk in stream:
        if(thinking_mode and chunk.message.thinking != None):
            print(chunk.message.thinking,end="", flush=True)
        if(chunk.message.thinking == None and switch == False):
            switch = True
            print(name)
        print(chunk.message.content, end="",flush=True)
    
    return True
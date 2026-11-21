from ollama import chat

def model_chat(model,thinking_mode,name,messages):

    stream = chat(model=model,
            messages=messages,
      stream=True,
      #think=thinking_level,
    )

    print("Thinking...")
    first_time = False

    model_message = {
        "role": "assistant",
        "content": ""
    }


    for chunk in stream:
        if(thinking_mode and chunk.message.thinking):
            #print(";",end="")
            print(chunk.message.thinking,end="", flush=True)
        if chunk.message.content:
          #print(":",end="")
          if(first_time == False):
              first_time = True
              print(name)
          model_message["content"] += chunk.message.content
          print(chunk.message.content, end="",flush=True)
    
    if(model_message["content"] == ""):
        model_message = None
        print("HERE")

    return model_message

def chat_with_memory():
    print("Chat History with qwen3.5")
    messages = [
        {
        'role': 'user',
        'content': "Who are you",
    },
    {
        'role': 'assistant',
        'content': "I'm a chat assistant",
    }
    ]

    while True:
        user_input = input("\nMe: ")
        if(user_input == 'stop'):
            break
        messages.append({'role': 'user', 'content': user_input})
        stream = chat(model="qwen3.5", messages=messages, stream=True,think=False)
        message = {'role': 'assistant', 'content': ""}
        for chunk in stream:
            message['content'] += chunk.message.content
            print(chunk.message.content, end="", flush=True)

        messages.append(message)
    
    print(messages)

chat_with_memory()

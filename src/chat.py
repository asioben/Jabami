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
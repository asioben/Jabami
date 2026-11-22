from ollama import chat

#def model_chat(model,thinking_mode,name,messages):

"""def chat_with_memory(messages):
    #user_input = input("\nMe: ")
    #messages.append({'role': 'user', 'content': user_input})
    stream = chat(model="qwen3.5", messages=messages, stream=True,think=False)
    for chunk in stream:
        #message['content'] += chunk.message.content
        yield chunk.message.content
        print(chunk.message.content, end="", flush=True)

"""

def chat_streamer(messages):
      stream = chat(model="qwen3.5", messages=messages, stream=True,think=False)
      for chunk in stream:
          #message_assistant["content"] += chunk.message.content
          print(chunk.message.content, end="", flush="True")
          yield chunk.message.content

def chat_wrapper(prompt, messages, speech):

     message_user =  \
     {
          "role": "user",
          "content":prompt
     }

     messages.append(message_user)

     print("\nAI:", end="", flush="True")
     message_assistant = {'role': 'assistant', 'content': ""}

     speech.speak(chat_streamer,messages)
     messages.append(message_assistant)
     
     return messages

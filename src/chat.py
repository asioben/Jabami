from ollama import chat

def chat_streamer(messages, speech_flag, model):
      stream = chat(model=model, messages=messages, stream=True,think=False)
      for chunk in stream:
          messages[-1]["content"] += chunk.message.content
          print(chunk.message.content, end="", flush="True")
          if speech_flag:
            yield chunk.message.content


def chat_wrapper(prompt, messages, speech_object, speech_flag, model):

     message_user =  \
     {
          "role": "user",
          "content":prompt
     }

     messages.append(message_user)

     print("\nAI:", end="", flush="True")
     message_assistant = {'role': 'assistant', 'content': ""}
     messages.append(message_assistant)

     if speech_flag:
        speech_object.speak(chat_streamer,messages, model)
     else:
          for i in chat_streamer(messages, speech_flag, model):
              pass
     
     return messages
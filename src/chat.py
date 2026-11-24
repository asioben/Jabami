from ollama import chat

def chat_streamer(messages, speech_flag):
      stream = chat(model="qwen3.5", messages=messages, stream=True,think=False)
      for chunk in stream:
          messages[-1]["content"] += chunk.message.content
          print(chunk.message.content, end="", flush="True")
          if speech_flag:
            yield chunk.message.content


def chat_wrapper(prompt, messages, speech_object, speech_flag):

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
        speech_object.speak(chat_streamer,messages)
     else:
          for i in chat_streamer(messages, speech_flag):
              pass
     
     return messages
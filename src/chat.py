from ollama import chat

#def model_chat(model,thinking_mode,name,messages):

def chat_with_memory(messages, decorator):
    #user_input = input("\nMe: ")
    #messages.append({'role': 'user', 'content': user_input})
    stream = chat(model="qwen3.5", messages=messages, stream=True,think=False)
    message = {'role': 'assistant', 'content': decorator}
    for chunk in stream:
        message['content'] += chunk.message.content
        print(chunk.message.content, end="", flush=True)

    messages.append(message)
    
    #print(messages)

    return messages

#chat_with_memory()

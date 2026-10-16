from chat import model_chat
from voice import Voice
import json
#import asyncio

SYSTEM = \
     {
            "role": "system",
            "content": "You are a bored assistant. You provide short answers and dont think too much.",
     }

def init_voice():
    with open("../credentials/file.json","r") as file:
            new_data = json.load(file)
    return new_data

def chat_wrapper(prompt,messages,model_message):

     message =  \
     {
          "role": "user",
          "content":prompt
     }

     if(len(messages) == 0):
          messages.append(SYSTEM)
          messages.append(message)
     else:
          #print(model_message)
          messages.append(message)
          messages.append(model_message)
    
     model_message = None

     while model_message == None:    
        model_message = model_chat(model="qwen3.5",
                       thinking_mode=True,name="\nAI: ",
                        messages=messages)

     return model_message

def main():
    #Init
    voice_model = init_voice()
    voice_object = Voice(voice_model["English_Model_Vosk"])

    #Vosk
    print("\nListening...")
    messages = []
    voice_object.listen("Me:","stop",messages,chat_wrapper)


if __name__ == "__main__":
    main()

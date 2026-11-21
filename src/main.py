from chat import *
from speech_to_text import Voice
import json

def init_voice():
    with open("../credentials/file.json","r") as file:
            new_data = json.load(file)
    return new_data


def main():
    #Init
    voice_model = init_voice()
    voice_object = Voice(voice_model["English_Model_Vosk"])

    #Vosk
    print("Chat History with qwen3.5")
    print("\nListening...")
    messages = [
     {
          "role": "system",
          "content": "You are a chatbot who answers quickly",
     }

     ]
    voice_object.listen("Me:","stop",messages,chat_wrapper)


if __name__ == "__main__":
    main()

from chat import model_chat
from voice import Voice
import json
#import asyncio

def init_voice():
    with open("../credentials/file.json","r") as file:
            new_data = json.load(file)
    return new_data

def chat_wrapper(prompt):
     system = \
     {
            "role": "system",
            "content": "You are a bored assistant. You provide short answers and dont think too much."
     }
     return model_chat(prompt=prompt,model="qwen3.5",thinking_mode=True,name="\nAI: ",system=system)

def main():
    voice_model = init_voice()
    voice_object = Voice(voice_model["English_Model_Vosk"])
    print("\nListening...")
    voice_object.listen("Me:","stop",chat_wrapper)


if __name__ == "__main__":
    main()

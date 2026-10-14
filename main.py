from chat import model_chat
from voice import Voice
import json
import asyncio

def init_voice():
    with open("credentials/file.json","r") as file:
            new_data = json.load(file)
    return new_data

async def chat_wrapper(prompt):
     return model_chat(role="user",prompt=prompt,model="qwen3.5")

def main():
    voice_model = init_voice()
    voice_object = Voice(voice_model["English_Model_Vosk"])
    print("Listening")
    asyncio.run(voice_object.listen("Me:","stop",chat_wrapper))


if __name__ == "__main__":
    main()

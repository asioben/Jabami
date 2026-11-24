from chat import *
from speech_to_text import Voice
import json
from text_to_speech import Speech

#flag
#///

#LISTEN_INPUT: Flag for inputing 
#False for inputing, True for listening
LISTEN_INPUT = True

#SPEECH: Activate the model to speak
#False for none, True for speech
SPEECH = False

def init_voice():
    with open("../credentials/file.json","r") as file:
            new_data = json.load(file)
    return new_data


def main():
    #Init Voice
    if(LISTEN_INPUT):
        voice_model = init_voice()
        voice_object = Voice(voice_model["English_Model_Vosk"])

    #Init speech
    speech_object = None
    if(SPEECH):
          speech_object = Speech("assistant","../credentials/en_female.wav","The exact words spoken in reference.wav.","english")

    #Vosk
    print("Chat History with qwen3.5")
    print("\nListening...")
    messages = [
     {
          "role": "system",
          "content": "You are a chatbot who answers quickly. You don't take time thinking except if you are asked to do so.",
     }

     ]
    voice_object.init_streaming()
    loop = True
    while loop:
         if(LISTEN_INPUT):
              loop, prompt = voice_object.listen("\nMe:","b")
              if(len(prompt) != 0):
                    chat_wrapper(prompt,messages,speech_object,SPEECH)
         else:
              chat_wrapper(prompt,messages,None,False)
              
    if SPEECH:
          speech_object.destroy()

    print(messages)

if __name__ == "__main__":
    main()

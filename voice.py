import pyaudio
import json
from vosk import Model, KaldiRecognizer
import os
import sys
#import subprocess

command = "kitty -e echo \"Hello World\""
os.system(command)
sys.exit()

with open("credentials/file.json","r") as file:
            new_data = json.load(file)
            print(new_data["English_Model_Vosk"])
            #sys.exit()

model = Model(new_data["English_Model_Vosk"])
recognizer = KaldiRecognizer(model,16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

print("Listening...")

while True:
    data = stream.read(4096, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        print("Me:", result["text"])
        if(result["text"] == "stop"):
            break 
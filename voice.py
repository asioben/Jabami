import pyaudio
import json
from vosk import Model, KaldiRecognizer

class Voice:
      def __init__(self,model,):
            self.model = Model(model)
            self.recognizer = KaldiRecognizer(self.model,16000)

      def listen(self,decorator,stop_message,task):
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
            stream.start_stream()
            result = {"text": ""}
            while True:
                data = stream.read(4096, exception_on_overflow=False)
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    print(decorator, result["text"])
                    if result["text"] != "":
                      if result["text"] != stop_message:
                         task(result["text"])
                         print("\nListening...")
                      else:
                         break


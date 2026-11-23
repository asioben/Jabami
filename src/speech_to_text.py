import pyaudio
import json
from vosk import Model, KaldiRecognizer

class Voice:
      def __init__(self,model):
            self.model = Model(model)
            self.recognizer = KaldiRecognizer(self.model,16000)

      def init_streaming(self):
          self.pyAudio = pyaudio.PyAudio()
          self.stream = self.pyAudio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
          self.stream.start_stream()

      def listen(self,decorator,stop_message):
            text = ""
            data = self.stream.read(4096, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                  result = json.loads(self.recognizer.Result())
                  text = result["text"]
                  print(decorator, result["text"])
                  if text == stop_message:
                        self.stream.stop_stream()
                        return False, ""
            return True, text
      
            """p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
            stream.start_stream()
            result = {"text": ""}
            while True:
                data = stream.read(4096, exception_on_overflow=False)
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    print(decorator, result["text"])
                    if len(result["text"]) > 0:
                      if result["text"] != stop_message:
                         messages = task(result["text"],messages, speech)
                         #print(model_message)
                         #print("\n",messages)
                         print("\nListening...")
                      else:
                         break"""
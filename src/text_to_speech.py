from RealtimeTTS import QwenCpuEngine, QwenVoice, TextToAudioStream

def test():
    yield "here"
    yield "I am"
    yield "forever"

class Speech:
    def __init__(self, name, ref_audio, ref_text, language):
        self.voice = QwenVoice(
            name= name,
            ref_audio= ref_audio,
            ref_text= ref_text,
            language= language,
        )
    
    def speak(self, yielder):
        engine = QwenCpuEngine(voice=self.voice)
        try:
            stream = TextToAudioStream(engine)
            stream.feed(yielder())
            stream.play()
        finally:
            engine.shutdown()

speech = Speech("assistant","../en_female.wav","The exact words spoken in reference.wav.","english")
speech.speak(test)
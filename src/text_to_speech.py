from RealtimeTTS import QwenCpuEngine, QwenVoice, TextToAudioStream

"""def test():
    yield "here"
    yield "I am"
    yield "forever"
"""

class Speech:
    def __init__(self, name, ref_audio, ref_text, language):
        self.voice = QwenVoice(
            name= name,
            ref_audio= ref_audio,
            ref_text= ref_text,
            language= language,
        )
        self.engine = QwenCpuEngine(voice=self.voice)
        self.stream = TextToAudioStream(self.engine)
    
    def speak(self, yielder):
        self.stream.feed(yielder)
        self.stream.play()

    def destroy(self):
        self.engine.shutdown()

"""speech = Speech("assistant","../en_female.wav","The exact words spoken in reference.wav.","english")
speech.speak(test)"""
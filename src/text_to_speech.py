from RealtimeTTS import QwenCpuEngine, QwenVoice, TextToAudioStream
import logging


class Speech:
    def __init__(self, name, ref_audio, ref_text, language):
        self.voice = QwenVoice(
            name= name,
            ref_audio= ref_audio,
            ref_text= ref_text,
            language= language,
        )
        self.engine = QwenCpuEngine(voice=self.voice)
        self.stream = TextToAudioStream(self.engine, level=logging.ERROR)
    
    def speak(self, yielder, messages, model):
        self.stream.feed(yielder(messages, True, model))
        self.stream.play()

    def destroy(self):
        self.engine.shutdown()

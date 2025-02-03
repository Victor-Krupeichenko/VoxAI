import pyttsx3


class SpeechConverter:
    """
    Класс для конвертации текста в речь (TTS - Text-to-Speech).
    """

    def __init__(self, voice_id=1, voice_rate=145, volume=0.5):
        """
        Конструктор
        :param voice_id: ID голоса предустановленного в ОС
        :param voice_rate: скорость голоса
        :param volume: громкость голоса (min=0, max=1)
        """
        self.voice_id = voice_id
        self.voice_rate = voice_rate
        self.volume = volume
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voices", self.voices[self.voice_id].id)
        self.engine.setProperty("rate", self.voice_rate)
        self.engine.setProperty("volume", self.volume)

    def run_text_to_speech(self, text):
        """
        Преобразовывает текст в речь
        :param text: текст который необходимо преобразовать в речь
        """
        self.engine.say(text)
        self.engine.runAndWait()

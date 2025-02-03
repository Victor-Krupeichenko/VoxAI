import speech_recognition as sr
import json


class VoiceRecognizer:
    """
    Класс для распознания речи и конвертации речи в текст
    """

    def __init__(self):
        """
        Конструктор
        """
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def recognize_speech(self):
        """
        Распознание речи и преобразование ее
        :return: текст речи
        """
        with sr.Microphone() as source:
            try:
                print("Say something!")
                audio = self.recognizer.listen(source)
                text = json.loads(self.recognizer.recognize_vosk(audio))["text"]
                return text
            except sr.UnknownValueError:
                print("Воск не мог понять аудио")
            except sr.RequestError as e:
                print(f"Vosk error; {e}")

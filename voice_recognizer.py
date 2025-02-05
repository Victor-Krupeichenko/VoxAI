import speech_recognition as sr
import json
import sys


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

    def recognize_speech(self, timeout=None):
        """
        Распознание речи и преобразование ее
        :return: текст речи
        """
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, 1.2)
            try:
                sys.stdout.write("\rСлушаю...")
                sys.stdout.flush()
                audio = self.recognizer.listen(source, timeout=timeout)
                text = json.loads(self.recognizer.recognize_vosk(audio))["text"]
                return text.lower()
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                print("Воск не мог понять аудио")
            except sr.RequestError as e:
                print(f"Vosk error; {e}")

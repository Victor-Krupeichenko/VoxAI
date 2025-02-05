import sys
import threading
from pathlib import Path
from random import choice
from voice_recognizer import VoiceRecognizer
from text_to_speech import SpeechConverter
from ai_client import MistralClient
from load_config import SettingsLoader
from ico_tray import TrayIcon


class StartVoxAI(SpeechConverter, MistralClient, VoiceRecognizer, TrayIcon):
    """
    Класс для запуска приложения
    """
    def __init__(self):
        """
        Конструктор
        """
        path = Path("settings.txt")
        full_path = path.resolve()  # Получаем полный путь
        self.conf = SettingsLoader(full_path).open_file()
        SpeechConverter.__init__(self, self.conf["voice_id"], self.conf["voice_rate"], self.conf["volume"])
        MistralClient.__init__(self, self.conf["api_key"], self.conf["model"], self.conf["legend"],
                               self.conf["assistant_name"], self.conf["gender"], self.conf["language"]
                               )
        VoiceRecognizer.__init__(self)
        TrayIcon.__init__(self, self.conf["exit"])

    def run(self):
        """
        Запуск основного цикла работы приложения
        """
        threading.Thread(target=self.show, daemon=True).start()
        while self.is_running:
            if not self.is_running:
                continue
            question = self.recognize_speech()
            if question:
                if self.assistant_name in question:
                    if self.conf["hello"] not in question:
                        self.run_text_to_speech(choice(self.conf["start_message"]))
                    clear_question = question.replace(self.assistant_name, "").strip()
                    self.run_text_to_speech(self.request_to_ai(clear_question))
                elif self.conf["exit"] == question:
                    self.is_running = False
                    self.run_text_to_speech(choice(self.conf["exit_message"]))
                    sys.exit(0)
        else:
            self.run_text_to_speech(choice(self.conf["exit_message"]))


StartVoxAI().run()

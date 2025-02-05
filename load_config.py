class SettingsLoader:
    """
    Класс для работы с файлом настроек
    """
    def __init__(self, path):
        """
        Конструктор
        :param path: путь к файлу настроек
        """
        self.path = path

    @staticmethod
    def read_file(file):
        """
        Построчно читает полученный файл
        :param file: имя файла
        :return: строку
        """
        for st in file:
            yield st.strip()

    @staticmethod
    def is_float(value):
        """
        Проверяет являться ли строка числом с плавающей точкой
        :param value: строка
        :return: bool
        """
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def list_messages(key, value):
        """
        Преобразует значение в список сообщений
        :param key: ключ в словаре
        :param value: значение которые необходимо преобразовать в список
        :return: list[value] or value
        """
        keys = ["start_message", "exit_message"]
        if key in keys:
            return value.split(",")
        return value

    def open_file(self):
        """
        Открывает файл и построчно читает содержимое.
        :return: Словарь с настройками приложения
        """
        conf_dict = dict()
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                for st in self.read_file(file):
                    key, value = st.split("=", 1)
                    key, value = key.strip(), value.strip()
                    if value.isdigit():
                        value = int(value)
                    elif self.is_float(value):
                        value = float(value)
                    value = self.list_messages(key, value)
                    conf_dict.setdefault(key, value)
        except FileNotFoundError:
            print("Файл не найден")
        return conf_dict

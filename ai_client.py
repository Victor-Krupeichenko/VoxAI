from mistralai import Mistral


class MistralClient:
    """
    Класс для взаимодействия с Mistral AI
    """

    def __init__(self, api_key, model, legend, assistant_name, gender, language):
        """
        Конструктор
        :param api_key: api ключ
        :param model: модель Mistral
        :param legend: контекст для ai
        :param assistant_name: имя ассистента
        :param gender: пол ассистента
        :param language: язык ассистента(по умолчанию русский так как модель распознания речи только для русского языка)
        """
        self.api_key = api_key
        self.client = Mistral(api_key=self.api_key)
        self.model = model
        self.legend = legend
        self.assistant_name = assistant_name
        self.gender = gender
        self.language = language

    def request_to_ai(self, question):
        """
        Запрос к Mistral AI
        :param question: текст запроса
        :return: ответ от Mistral AI
        """
        legend = self.legend.format(self.assistant_name, "женского" if self.gender == "female" else "мужского",
                                    "русском" if self.language == "ru" else self.language)
        chat_response = self.client.chat.complete(
            model=self.model,
            messages=[
                {'role': 'system', 'content': legend},
                {'role': 'user', 'content': f'{question}'}
            ]
        )
        return chat_response.choices[0].message.content

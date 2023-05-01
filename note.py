from datetime import *


class Note:
    """Заметка"""

    def __init__(self, id, head_note, body_note):
        """
        :param id: Идентификатор
        :param head_note: Заголовок записки
        :param body_note: Текст записки
        :param date_create: Задается автоматически дата создания
        :param date_change: Задается автоматически дата последнего изменения
        """
        self.id = id
        self.head_note = head_note
        self.body_note = body_note
        self.date_create = datetime.now().strftime("%H:%M:%S - %Y.%m.%d")
        self.date_change = datetime.now().strftime("%H:%M:%S - %Y.%m.%d")

    def __str__(self):
        """
        :return: Выводит строку общих сведений
        """
        return f"{id}| {self.head_note}. \n" \
               f"Created: {self.date_create} | Last change: {self.date_change}"

    def get_id(self):
        """
        Получение идентификатора записки
        :return: ID записки
        """
        return self.id

    def get_head(self):
        """
        Получение заголовка записки
        :return: Заголовок записки
        """
        return self.head_note

    def get_body(self):
        """
        Получение текста записки
        :return: Текст записки
        """
        return self.body_note

    def get_date_create(self):
        """
        Получение даты создания записки
        :return: Дата создания записки
        """
        return self.date_create

    def get_date_change(self):
        """
        Получение даты последнего изменения записки
        :return: Дата последнего изменения записки
        """
        return self.date_change

    def get_note(self):
        """
        Вывод записки полностью
        :return: Строку записки целиком
        """
        return f"ID_{self.id}| {self.head_note}.\n\n" \
               f"{self.body_note}\n\n" \
               f"Created: {self.date_create} | Last change: {self.date_change}\n"

    def set_head(self, new_head):
        """Изменение заголовка записки
        :param new_head: Новый заголовок
        """
        self.head_note = new_head
        self.date_change = datetime.now().strftime("%H:%M:%S - %Y.%m.%d")

    def set_body(self, new_body):
        """Изменение текста записки
        :param new_body: Новый текст
        """
        self.head_note = new_body
        self.date_change = datetime.now().strftime("%H:%M:%S - %Y.%m.%d")

    def set_note(self, new_head, new_body):
        """Изменение записки
        :param new_head: Новый заголовок
        :param new_body: Новый текст
        """
        self.set_head(new_head)
        self.set_body(new_body)

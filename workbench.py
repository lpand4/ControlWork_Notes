from note import Note


class Workbench:
    """Рабочий стол с заметками"""

    def __init__(self):
        self.notes = []
        self.list_id = 0

    def __str__(self):
        list_notes = ''
        for note in self.notes:
            list_notes += note
        return list_notes

    def add_note(self, head_note, body_note):
        """
        Добавление записки
        :param head_note: заголовок записки
        :param body_note: текст записки
        """
        self.notes.append(Note(self.list_id, head_note, body_note))
        self.list_id += 1

    def update_note(self, list_id, head_note, body_note):
        """
        Изменение записки
        :param list_id: ID записки
        :param head_note: Новый заголовок записки
        :param body_note: Новый текст записки
        """
        self.notes[list_id].set_note(head_note, body_note)

    def delete_note(self, list_id):
        """
        Удаление записки
        :param list_id: Номер записки в списке
        """
        self.notes.remove(list_id)

    def get_all_notes(self):
        """
        Вернуть все записки:return: Возвращает все записки
        """
        return self.notes

    def get_note(self,list_id):
        """
        Возвразает записку по номеру в списке
        :param list_id: Номер в списке
        :return: Записку
        """
        self.notes[list_id].get_note()

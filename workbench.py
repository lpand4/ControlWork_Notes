from note import Note
import json


class Workbench:
    """Рабочий стол с заметками"""

    def __init__(self):
        self.notes = []
        self.list_id = 0
        #self.load_notes()

    def __str__(self):
        list_notes = ''
        for note in self.notes:
            list_notes += note
        return list_notes

    def set_list_id(self, new_list_id):
        self.list_id = new_list_id

    def add_note(self, head_note, body_note):
        """
        Добавление записки
        :param head_note: заголовок записки
        :param body_note: текст записки
        """
        self.notes.append(Note(self.list_id, head_note, body_note))
        self.set_list_id(new_list_id=self.list_id + 1)

    def update_note(self, list_id, head_note, body_note):
        """
        Изменение записки
        :param list_id: ID записки
        :param head_note: Новый заголовок записки
        :param body_note: Новый текст записки
        """
        self.notes[list_id - 1].set_note(new_head=head_note, new_body=body_note)

    def delete_note(self, list_id):
        """
        Удаление записки
        :param list_id: Номер записки в списке
        """
        self.notes.pop(list_id - 1)

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
        self.notes[list_id - 1].get_note()

    def save_notes(self):
        if len(self.notes) > 0:
            with open("data_notes.json", 'w') as wf:
                for note in self.notes:
                    json.dump(note, wf)
        else:
            print('Еще не создано ни одной записки!')

    def load_notes(self):
        with open("data_notes.json", 'r') as rf:
            data = json.load(rf)
        for d in data:
            self.notes.append(d)

from note import Note
import json


class Workbench:
    """Рабочий стол с заметками"""

    def __init__(self):
        self.notes = []
        self.load_notes()
        self.list_id = 0
        self.set_list_id()

    def __str__(self):
        list_notes = ''
        for note in self.notes:
            list_notes += note
        return list_notes

    def set_list_id(self):
        self.list_id = self.notes[-1].get_id() + 1

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

    def get_some_note(self, list_id):
        """
        Возвразает записку по номеру в списке
        :param list_id: Номер в списке
        :return: Записку
        """
        return self.notes[list_id - 1].get_note()

    def save_notes(self):
        if len(self.notes) > 0:
            note_dict = [note.__dict__() for note in self.notes]
            json_note = json.dumps(note_dict)
            with open("data_notes.json", 'w') as wf:
                wf.write(json_note)
        else:
            print('Еще не создано ни одной записки!')

    def load_notes(self):
        with open("data_notes.json", 'r') as rf:
            json_data = rf.read()
            note_dict = json.loads(json_data)

        notes = [Note.from_dict(dict_) for dict_ in note_dict]
        for note in notes:
            self.notes.append(note)

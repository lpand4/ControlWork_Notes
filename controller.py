import view
from workbench import Workbench


class Controller:

    def __init__(self):
        self.wb = Workbench()

    def start(self):
        view.start_menu()
        start_initiation = input()
        if start_initiation != '0':
            while True:
                view.show_menu()
                user_choice = input()
                match user_choice:
                    case "1":
                        self.add()
                    case "2":
                        self.update()
                    case "3":
                        self.delete()
                    case "4":
                        self.get_all()
                    case "5":
                        self.get_one()
                    case "6":
                        self.save()
                    case '7':
                        self.get_all_sorted_by_create()
                    case '8':
                        self.get_all_sorted_by_change()
                    case "0":
                        return
                    case _:
                        print("Введено неверное значение! Введите значение из списка меню")
        else:
            print("Счастливо!!!")

    def add(self):
        head = view.head_note()
        body = view.body_note()
        self.wb.add_note(head_note=head, body_note=body)

    def update(self):
        self.get_all()
        number = view.list_id()
        head = view.head_note()
        body = view.body_note()
        self.wb.update_note(number, head_note=head, body_note=body)

    def delete(self):
        self.get_all()
        number = view.list_id()
        self.wb.delete_note(number)

    def get_all(self):
        if len(self.wb.notes) > 0:
            data = self.wb.get_all_notes()
            view.show_all_notes(data)
        else:
            print("Список записок пуст!")

    def get_all_sorted_by_create(self):
        if len(self.wb.notes) > 0:
            data = self.wb.get_all_sorted_by_create()
            view.show_all_notes(data)
        else:
            print("Список записок пуст!")

    def get_all_sorted_by_change(self):
        if len(self.wb.notes) > 0:
            data = self.wb.get_all_sorted_by_change()
            view.show_all_notes(data)
        else:
            print("Список записок пуст!")

    def get_one(self):
        self.get_all()
        number = view.list_id()
        view.show_note(self.wb.get_some_note(number))

    def save(self):
        self.wb.save_notes()

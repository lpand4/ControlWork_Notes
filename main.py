from note import Note

notes = []
count_id = 0
def add_note():
    head = input("Введите заголовок записки: ")
    body = input("Введите текст записки")
    notes.append(Note(notes[-1].id + 1, head, body))



add_note()
add_note()
add_note()
for note in notes:
    print(note)

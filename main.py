import emoji
# print(emoji.emojize("Привіт :heart:", language="alias"))
from datetime import datetime

'''
Додаток, який буде зберігати нотатки

This is my note I am taking on my laptop.
- Created on 19.12.2025 20:15 ❤️

[("This is my note I am taking on my laptop.", "19.12.2025 20:15")]
[("19.12.2025 20:15", "This is my note I am taking on my laptop.")]

{"text": "This is my note I am taking on my laptop.", "creation date": "19.12.2025 20:15"}

1) створити словник нотаток та записати у нього інформацію.
2) написати функцію, яка буде виводити нотатку
3) написати фукнція, яка виводитиме всі нотатки
4) написати цикл, який буде отримувати інформацію віл користувача і реагуватиме на неї
'''

note_list = [] # {"text": "This is my note I am taking on my laptop.", "creation date": "19.12.2025 20:15"}
note_file = "notes.txt"

# Hello note;19.12.2025 20:15
welcome_banner = '''
 _   _      _                   _           _   
| | | |    | |                 | |         | |  
| |_| | ___| |_ __   ___ _ __  | |__   ___ | |_ 
|  _  |/ _ \ | '_ \ / _ \ '__| | '_ \ / _ \| __|
| | | |  __/ | |_) |  __/ |    | |_) | (_) | |_ 
\_| |_/\___|_| .__/ \___|_|    |_.__/ \___/ \__|
             | |                                
             |_|                                                                                                                                                                                                                                                                                         
'''
commands = '''
1) exit - to exit the app
2) add_note - to add a new note
3) print_note [i] - to print note #i
4) print_all - to print all notes
5) help - to print this menu
'''
def add_new_note(note_text) -> bool:
    note_creation_date = datetime.today()
    note_list.append({"text": note_text, "creation_date": note_creation_date})
    return True

def print_note(index: int):
    note = note_list[index]
    formatted_creation_date = note["creation_date"].strftime("%d.%m.%Y %H:%M")
    print(f'{note["text"]}\n- Created on {formatted_creation_date}\n')

def print_all_notes():
    for note_index in range(len(note_list)):
        print_note(note_index)

def save_notes():
    with open(note_file, 'w') as file:
        for note in note_list:
            file.write(f'{note["text"]};{note["creation_date"]}\n')

def read_notes() -> list[dict]:
    note_list = []
    with open(note_file) as file:
        for line in file:
            text, date = line.strip().split(';')
            creation_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            note_list.append({"text": text, "creation_date": creation_date})
    return note_list


# text = input("Please enter note text: ")
# time = datetime.today()
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)

#print_all_notes()
def init():
    global note_list
    note_list = read_notes()
    print(welcome_banner)
    print('\nHello and welcom to our app!\n')
    print(commands)
    print()

def main():
    while True:
        command, *args = input("Please enter command: ").strip().split(" ")
        if command == 'exit':
            print('Goodbye!')
            save_notes()
            break
        elif command == "add_note":
            text = input("Please enter your note text: ")
            if add_new_note(text):
                print("\nThe note added successfully\n")
            else:
                print("\nError while adding the note\n")
        elif command == "help":
            print(commands)
        elif command == "print_note":
            index = int(args[0]) - 1
            if index < 0 or index >= len(note_list):
                print("Please enter a valid note number")
                continue
            print_note(index)

init()
main()


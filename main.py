import json
import os
from datetime import datetime

FILE_NAME = "notes.json"


def load_notes():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_notes(notes):
    with open(FILE_NAME, "w") as f:
        json.dump(notes, f, indent=4)


def generate_id(notes):
    if not notes:
        return 1
    return max(note["id"] for note in notes) + 1


def add_note():
    text = input("Enter your note: ")
    notes = load_notes()

    note = {
        "id": generate_id(notes),
        "text": text,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "important": False
    }

    notes.append(note)
    save_notes(notes)
    print("Note added.")


def view_notes(notes=None):
    if notes is None:
        notes = load_notes()

    if not notes:
        print("No notes found.")
        return

    print("\nYour Notes:")
    for note in notes:
        star = "⭐" if note["important"] else ""
        print(f'[{note["id"]}] {note["text"]} {star}')
        print(f'    Created: {note["created"]}')


def delete_note():
    notes = load_notes()
    view_notes(notes)

    try:
        note_id = int(input("Enter note ID to delete: "))
        notes = [n for n in notes if n["id"] != note_id]
        save_notes(notes)
        print("Note deleted.")
    except ValueError:
        print("Invalid input.")


def edit_note():
    notes = load_notes()
    view_notes(notes)

    try:
        note_id = int(input("Enter note ID to edit: "))
        for note in notes:
            if note["id"] == note_id:
                new_text = input("Enter new text: ")
                note["text"] = new_text
                save_notes(notes)
                print("Note updated.")
                return
        print("Note not found.")
    except ValueError:
        print("Invalid input.")


def toggle_important():
    notes = load_notes()
    view_notes(notes)

    try:
        note_id = int(input("Enter note ID to toggle important: "))
        for note in notes:
            if note["id"] == note_id:
                note["important"] = not note["important"]
                save_notes(notes)
                print("Updated importance.")
                return
        print("Note not found.")
    except ValueError:
        print("Invalid input.")


def search_notes():
    query = input("Search: ").lower()
    notes = load_notes()

    results = [n for n in notes if query in n["text"].lower()]

    if results:
        view_notes(results)
    else:
        print("No matches found.")


def main():
    while True:
        print("\n--- Advanced Note Manager ---")
        print("1. Add note")
        print("2. View notes")
        print("3. Delete note")
        print("4. Edit note")
        print("5. Toggle important ⭐")
        print("6. Search notes")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            toggle_important()
        elif choice == "6":
            search_notes()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

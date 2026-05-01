import json
import os

FILE_NAME = "notes.json"


def load_notes():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_notes(notes):
    with open(FILE_NAME, "w") as f:
        json.dump(notes, f, indent=4)


def add_note():
    note = input("Enter your note: ")
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Note added.")


def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    print("\nYour Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")


def delete_note():
    notes = load_notes()
    view_notes()
    if not notes:
        return
    try:
        index = int(input("Enter note number to delete: ")) - 1
        removed = notes.pop(index)
        save_notes(notes)
        print(f"Deleted: {removed}")
    except (ValueError, IndexError):
        print("Invalid selection.")


def main():
    while True:
        print("\n--- Note Manager ---")
        print("1. Add note")
        print("2. View notes")
        print("3. Delete note")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

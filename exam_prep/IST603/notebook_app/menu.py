"""
Menu class: provides interactive command-line interface for Notebook operations.
"""

from notebook import Notebook
from note import Note


class Menu:
    """Interactive menu for notebook operations."""

    def __init__(self, notebook: Notebook) -> None:
        self.notebook = notebook

    def display_menu(self) -> None:
        """Display the main menu options."""
        print("\n" + "=" * 50)
        print("NOTEBOOK MENU")
        print("=" * 50)
        print("1. Show notes")
        print("2. Search notes")
        print("3. Add note")
        print("4. Modify note")
        print("5. Quit")
        print("=" * 50)

    def show_notes(self) -> None:
        """Display all notes."""
        if not self.notebook.notes:
            print("\nNo notes found.")
            return

        print("\n" + "-" * 50)
        print("ALL NOTES")
        print("-" * 50)
        for note in self.notebook.notes:
            print(f"ID: {note.note_id}")
            print(f"  Memo: {note.memo}")
            print(f"  Tags: {note.tags}")
            print(f"  Created: {note.creation_date.strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 50)

    def search_notes(self) -> None:
        """Search notes by filter."""
        filter_str = input("\nEnter search filter: ").strip()
        if not filter_str:
            print("Empty filter - showing all notes.")
            results = self.notebook.notes
        else:
            results = self.notebook.search(filter_str)

        if not results:
            print(f"\nNo notes found matching '{filter_str}'.")
            return

        print(f"\nFound {len(results)} note(s):")
        print("-" * 50)
        for note in results:
            print(f"ID: {note.note_id}")
            print(f"  Memo: {note.memo}")
            print(f"  Tags: {note.tags}")
            print(f"  Created: {note.creation_date.strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 50)

    def add_note(self) -> None:
        """Add a new note."""
        memo = input("\nEnter memo: ").strip()
        if not memo:
            print("Memo cannot be empty.")
            return

        tags = input("Enter tags (optional): ").strip()
        note = self.notebook.new_note(memo, tags)
        print(f"\nNote added successfully! ID: {note.note_id}")

    def modify_note(self) -> None:
        """Modify an existing note."""
        if not self.notebook.notes:
            print("\nNo notes to modify.")
            return

        try:
            note_id = int(input("\nEnter note ID to modify: ").strip())
        except ValueError:
            print("Invalid note ID. Please enter a number.")
            return

        note = self.notebook._find_by_id(note_id)
        if not note:
            print(f"Note with ID {note_id} not found.")
            return

        print(f"\nCurrent note:")
        print(f"  Memo: {note.memo}")
        print(f"  Tags: {note.tags}")

        print("\nWhat would you like to modify?")
        print("1. Memo")
        print("2. Tags")
        print("3. Both")
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            new_memo = input("Enter new memo: ").strip()
            if new_memo:
                self.notebook.modify_memo(note_id, new_memo)
                print("Memo updated successfully!")
            else:
                print("Memo cannot be empty.")
        elif choice == "2":
            new_tags = input("Enter new tags: ").strip()
            self.notebook.modify_tags(note_id, new_tags)
            print("Tags updated successfully!")
        elif choice == "3":
            new_memo = input("Enter new memo: ").strip()
            new_tags = input("Enter new tags: ").strip()
            if new_memo:
                self.notebook.modify_memo(note_id, new_memo)
                self.notebook.modify_tags(note_id, new_tags)
                print("Note updated successfully!")
            else:
                print("Memo cannot be empty.")
        else:
            print("Invalid choice.")

    def run(self) -> None:
        """Run the interactive menu loop."""
        print("Welcome to the Notebook Application!")
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == "1":
                self.show_notes()
            elif choice == "2":
                self.search_notes()
            elif choice == "3":
                self.add_note()
            elif choice == "4":
                self.modify_note()
            elif choice == "5":
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 5.")

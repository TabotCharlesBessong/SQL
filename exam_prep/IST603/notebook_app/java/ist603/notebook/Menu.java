package ist603.notebook;

import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Scanner;

/**
 * Menu class: provides interactive command-line interface for Notebook operations.
 */
public class Menu {
    private final Notebook notebook;
    private final Scanner scanner;
    private static final DateTimeFormatter DATE_FORMATTER = 
            DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

    public Menu(Notebook notebook) {
        this.notebook = notebook;
        this.scanner = new Scanner(System.in);
    }

    public void displayMenu() {
        String separator = "==================================================";
        System.out.println("\n" + separator);
        System.out.println("NOTEBOOK MENU");
        System.out.println(separator);
        System.out.println("1. Show notes");
        System.out.println("2. Search notes");
        System.out.println("3. Add note");
        System.out.println("4. Modify note");
        System.out.println("5. Quit");
        System.out.println(separator);
    }

    public void showNotes() {
        if (notebook.notes.isEmpty()) {
            System.out.println("\nNo notes found.");
            return;
        }

        String separator = "--------------------------------------------------";
        System.out.println("\n" + separator);
        System.out.println("ALL NOTES");
        System.out.println(separator);
        for (Note note : notebook.notes) {
            System.out.println("ID: " + note.getNoteId());
            System.out.println("  Memo: " + note.memo);
            System.out.println("  Tags: " + note.tags);
            System.out.println("  Created: " + note.creationDate.format(DATE_FORMATTER));
            System.out.println(separator);
        }
    }

    public void searchNotes() {
        System.out.print("\nEnter search filter: ");
        String filter = scanner.nextLine().trim();
        
        List<Note> results;
        if (filter.isEmpty()) {
            System.out.println("Empty filter - showing all notes.");
            results = notebook.notes;
        } else {
            results = notebook.search(filter);
        }

        if (results.isEmpty()) {
            System.out.println("\nNo notes found matching '" + filter + "'.");
            return;
        }

        String separator = "--------------------------------------------------";
        System.out.println("\nFound " + results.size() + " note(s):");
        System.out.println(separator);
        for (Note note : results) {
            System.out.println("ID: " + note.getNoteId());
            System.out.println("  Memo: " + note.memo);
            System.out.println("  Tags: " + note.tags);
            System.out.println("  Created: " + note.creationDate.format(DATE_FORMATTER));
            System.out.println(separator);
        }
    }

    public void addNote() {
        System.out.print("\nEnter memo: ");
        String memo = scanner.nextLine().trim();
        if (memo.isEmpty()) {
            System.out.println("Memo cannot be empty.");
            return;
        }

        System.out.print("Enter tags (optional): ");
        String tags = scanner.nextLine().trim();
        Note note = notebook.newNote(memo, tags);
        System.out.println("\nNote added successfully! ID: " + note.getNoteId());
    }

    public void modifyNote() {
        if (notebook.notes.isEmpty()) {
            System.out.println("\nNo notes to modify.");
            return;
        }

        System.out.print("\nEnter note ID to modify: ");
        String input = scanner.nextLine().trim();
        int noteId;
        try {
            noteId = Integer.parseInt(input);
        } catch (NumberFormatException e) {
            System.out.println("Invalid note ID. Please enter a number.");
            return;
        }

        Note note = findById(noteId);
        if (note == null) {
            System.out.println("Note with ID " + noteId + " not found.");
            return;
        }

        System.out.println("\nCurrent note:");
        System.out.println("  Memo: " + note.memo);
        System.out.println("  Tags: " + note.tags);

        System.out.println("\nWhat would you like to modify?");
        System.out.println("1. Memo");
        System.out.println("2. Tags");
        System.out.println("3. Both");
        System.out.print("Enter choice (1-3): ");
        String choice = scanner.nextLine().trim();

        switch (choice) {
            case "1":
                System.out.print("Enter new memo: ");
                String newMemo = scanner.nextLine().trim();
                if (!newMemo.isEmpty()) {
                    notebook.modifyMemo(noteId, newMemo);
                    System.out.println("Memo updated successfully!");
                } else {
                    System.out.println("Memo cannot be empty.");
                }
                break;
            case "2":
                System.out.print("Enter new tags: ");
                String newTags = scanner.nextLine().trim();
                notebook.modifyTags(noteId, newTags);
                System.out.println("Tags updated successfully!");
                break;
            case "3":
                System.out.print("Enter new memo: ");
                String memo = scanner.nextLine().trim();
                System.out.print("Enter new tags: ");
                String tags = scanner.nextLine().trim();
                if (!memo.isEmpty()) {
                    notebook.modifyMemo(noteId, memo);
                    notebook.modifyTags(noteId, tags);
                    System.out.println("Note updated successfully!");
                } else {
                    System.out.println("Memo cannot be empty.");
                }
                break;
            default:
                System.out.println("Invalid choice.");
        }
    }

    private Note findById(int noteId) {
        for (Note n : notebook.notes) {
            if (n.getNoteId() == noteId) {
                return n;
            }
        }
        return null;
    }

    public void run() {
        System.out.println("Welcome to the Notebook Application!");
        while (true) {
            displayMenu();
            System.out.print("\nEnter your choice (1-5): ");
            String choice = scanner.nextLine().trim();

            switch (choice) {
                case "1":
                    showNotes();
                    break;
                case "2":
                    searchNotes();
                    break;
                case "3":
                    addNote();
                    break;
                case "4":
                    modifyNote();
                    break;
                case "5":
                    System.out.println("\nGoodbye!");
                    return;
                default:
                    System.out.println("\nInvalid choice. Please enter a number between 1 and 5.");
            }
        }
    }
}

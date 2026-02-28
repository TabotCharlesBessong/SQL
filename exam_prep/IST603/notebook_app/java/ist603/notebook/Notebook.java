package ist603.notebook;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Notebook per UML: manages a list of Note; search, new_note, modify_memo, modify_tags.
 */
public class Notebook {
    public List<Note> notes = new ArrayList<>();
    private int nextId = 1;

    /**
     * Returns a list of notes that match the filter.
     */
    public List<Note> search(String filter) {
        if (filter == null) {
            return new ArrayList<>(notes);
        }
        return notes.stream()
                .filter(n -> n.match(filter))
                .collect(Collectors.toList());
    }

    /**
     * Creates a new note and adds it to the notebook.
     */
    public Note newNote(String memo, String tags) {
        String t = tags != null ? tags : "";
        Note note = new Note(nextId++, memo, t);
        notes.add(note);
        return note;
    }

    /**
     * Overload with default empty tags.
     */
    public Note newNote(String memo) {
        return newNote(memo, "");
    }

    /**
     * Updates the memo of the note with the given id.
     */
    public void modifyMemo(int noteId, String memo) {
        Note note = findById(noteId);
        if (note != null) {
            note.memo = memo;
        }
    }

    /**
     * Updates the tags of the note with the given id.
     */
    public void modifyTags(int noteId, String tags) {
        Note note = findById(noteId);
        if (note != null) {
            note.tags = tags != null ? tags : "";
        }
    }

    private Note findById(int noteId) {
        for (Note n : notes) {
            if (n.getNoteId() == noteId) {
                return n;
            }
        }
        return null;
    }
}

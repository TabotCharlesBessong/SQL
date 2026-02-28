package ist603.notebook;

import java.time.LocalDateTime;

/**
 * Note per UML: stores memo, creation_date, tags; provides match(search_filter).
 */
public class Note {
    public String memo;
    public LocalDateTime creationDate;
    public String tags;
    private final int noteId;

    public Note(int noteId, String memo, String tags) {
        this.noteId = noteId;
        this.memo = memo;
        this.creationDate = LocalDateTime.now();
        this.tags = tags != null ? tags : "";
    }

    public int getNoteId() {
        return noteId;
    }

    /**
     * Returns true if this note matches the search filter (in memo or tags).
     */
    public boolean match(String searchFilter) {
        if (searchFilter == null || searchFilter.isEmpty()) {
            return true;
        }
        String q = searchFilter.toLowerCase();
        return (memo != null && memo.toLowerCase().contains(q))
                || (tags != null && tags.toLowerCase().contains(q));
    }
}

"""
Notebook class per UML: manages a list of Note; search, new_note, modify_memo, modify_tags.
"""

from typing import List

from note import Note


class Notebook:
    """Manages a collection of Note objects."""

    def __init__(self) -> None:
        self.notes: List[Note] = []
        self._next_id = 1

    def search(self, filter_str: str) -> List[Note]:
        """Return a list of notes that match the filter."""
        return [n for n in self.notes if n.match(filter_str)]

    def new_note(self, memo: str, tags: str = "") -> Note:
        """Create a new note and add it to the notebook."""
        note = Note(self._next_id, memo, tags)
        self._next_id += 1
        self.notes.append(note)
        return note

    def modify_memo(self, note_id: int, memo: str) -> None:
        """Update the memo of the note with the given id."""
        note = self._find_by_id(note_id)
        if note:
            note.memo = memo

    def modify_tags(self, note_id: int, tags: str) -> None:
        """Update the tags of the note with the given id."""
        note = self._find_by_id(note_id)
        if note:
            note.tags = tags

    def _find_by_id(self, note_id: int):
        """Return the Note with the given id, or None."""
        for n in self.notes:
            if n.note_id == note_id:
                return n
        return None

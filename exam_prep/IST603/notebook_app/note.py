"""
Note class per UML: stores memo, creation_date, tags; provides match(search_filter).
"""

from datetime import datetime


class Note:
    """Individual note with memo, creation date, and tags."""

    def __init__(self, note_id: int, memo: str, tags: str = "") -> None:
        self.memo = memo
        self.creation_date = datetime.now()
        self.tags = tags
        self._note_id = note_id  # id set by Notebook; kept for modify_memo/modify_tags

    @property
    def note_id(self) -> int:
        return self._note_id

    def match(self, search_filter: str) -> bool:
        """Return True if this note matches the search filter (in memo or tags)."""
        if not search_filter:
            return True
        q = search_filter.lower()
        return q in self.memo.lower() or q in self.tags.lower()

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import dateutil.parser

import JsonService

@dataclass(init=True, unsafe_hash=True)
class NoteModel:
    """
    Data model for a note, including author, content, and creation date.
    Provides property validation and utility methods for loading from dict or JSON.
    """
    _author: str = field(init=True)
    content: str
    _create_date: datetime = field(init=False, default_factory=datetime.now)

    def __repr__(self) -> str:
        """Return a human-readable string representation of the note."""
        return f"Author: {self.author}, Date Added: {self.create_date.strftime('%B %d, %Y')}\nNote:{self.content}"

    @property
    def author(self) -> str:
        """Get the author of the note."""
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        """Set the author of the note, enforcing a max length of 100 characters."""
        if len(new_author) > 100:
            raise ValueError("Author name must be less than 100 characters.")
        self._author = new_author

    @property
    def create_date(self) -> datetime:
        """Get the creation date of the note."""
        return self._create_date

    @create_date.setter
    def create_date(self, new_date: datetime) -> None:
        """Set the creation date of the note."""
        self._create_date = new_date

    def _load_create_date(self, new_date: str | datetime) -> None:
        """Load and parse the creation date from a string or datetime object."""
        if not isinstance(new_date, datetime):
            self._create_date = dateutil.parser.parse(new_date)
        else:
            self._create_date = new_date

    @classmethod
    def load_dict(cls, dict_data: dict) -> NoteModel:
        """Create a NoteModel instance from a dictionary."""
        new_instance = cls(dict_data['author'], dict_data['content'])
        new_instance._load_create_date(dict_data['create_date'])
        return new_instance

    @classmethod
    def from_json(cls, json_data: str) -> NoteModel:
        """Create a NoteModel instance from a JSON string."""
        return JsonService.json_to_class(json_data, cls)

if __name__ == "__main__":
    note_json = '{"author": "Tim H.", "content": "This is a note about something.", "create_date": "2021-01-01"}'
    note_from_json = NoteModel.from_json(note_json)
    print(note_from_json)

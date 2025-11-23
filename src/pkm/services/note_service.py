"""Note service for note management business logic."""

from datetime import datetime
from pathlib import Path

from pkm.models.note import Note
from pkm.services.id_generator import generate_note_id
from pkm.storage.json_store import JSONStore
from pkm.storage.schema import deserialize_note, serialize_note


class NoteService:
    """Service for managing notes."""

    def __init__(self, data_dir: Path) -> None:
        """Initialize note service.
        
        Args:
            data_dir: Directory containing data.json
        """
        self.store = JSONStore(data_dir / "data.json")

    def create_note(
        self, content: str, course: str | None = None, topics: list[str] | None = None
    ) -> Note:
        """Create a new note.
        
        Args:
            content: Note content
            course: Optional course assignment
            topics: Optional topic tags
            
        Returns:
            Created note
        """
        now = datetime.now()
        note = Note(
            id=generate_note_id(),
            content=content,
            created_at=now,
            modified_at=now,
            course=course,
            topics=topics or [],
            linked_from_tasks=[],
        )

        # Save to storage
        data = self.store.load()
        data["notes"].append(serialize_note(note))
        self.store.save(data)

        return note

    def get_note(self, note_id: str) -> Note | None:
        """Get a note by ID.
        
        Args:
            note_id: Note ID
            
        Returns:
            Note if found, None otherwise
        """
        data = self.store.load()
        for note_data in data["notes"]:
            if note_data["id"] == note_id:
                return deserialize_note(note_data)
        return None

    def list_notes(self) -> list[Note]:
        """List all notes.
        
        Returns:
            List of all notes
        """
        data = self.store.load()
        return [deserialize_note(note_data) for note_data in data["notes"]]

    def get_inbox_notes(self) -> list[Note]:
        """Get all notes in inbox (course=None).
        
        Returns:
            List of inbox notes
        """
        return [note for note in self.list_notes() if note.course is None]

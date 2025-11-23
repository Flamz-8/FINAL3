"""Task service for task management business logic."""

from datetime import datetime
from pathlib import Path

from pkm.models.task import Task
from pkm.services.id_generator import generate_task_id
from pkm.storage.json_store import JSONStore
from pkm.storage.schema import deserialize_task, serialize_task


class TaskService:
    """Service for managing tasks."""

    def __init__(self, data_dir: Path) -> None:
        """Initialize task service.
        
        Args:
            data_dir: Directory containing data.json
        """
        self.store = JSONStore(data_dir / "data.json")

    def create_task(
        self,
        title: str,
        due_date: datetime | None = None,
        priority: str = "medium",
        course: str | None = None,
    ) -> Task:
        """Create a new task.
        
        Args:
            title: Task title
            due_date: Optional due date
            priority: Task priority (high, medium, low)
            course: Optional course assignment
            
        Returns:
            Created task
        """
        task = Task(
            id=generate_task_id(),
            title=title,
            created_at=datetime.now(),
            due_date=due_date,
            priority=priority,  # type: ignore
            completed=False,
            completed_at=None,
            course=course,
            linked_notes=[],
            subtasks=[],
        )

        # Save to storage
        data = self.store.load()
        data["tasks"].append(serialize_task(task))
        self.store.save(data)

        return task

    def get_task(self, task_id: str) -> Task | None:
        """Get a task by ID.
        
        Args:
            task_id: Task ID
            
        Returns:
            Task if found, None otherwise
        """
        data = self.store.load()
        for task_data in data["tasks"]:
            if task_data["id"] == task_id:
                return deserialize_task(task_data)
        return None

    def list_tasks(self) -> list[Task]:
        """List all tasks.
        
        Returns:
            List of all tasks
        """
        data = self.store.load()
        return [deserialize_task(task_data) for task_data in data["tasks"]]

    def get_inbox_tasks(self) -> list[Task]:
        """Get all tasks in inbox (course=None).
        
        Returns:
            List of inbox tasks
        """
        return [task for task in self.list_tasks() if task.course is None]

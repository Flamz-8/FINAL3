"""Task service for task management business logic."""

from datetime import datetime, date, timedelta
from pathlib import Path

from pkm.models.task import Task, Subtask
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

    def get_tasks_today(self) -> list[Task]:
        """Get all tasks due today.
        
        Returns:
            List of tasks due today
        """
        today = date.today()
        return [
            task for task in self.list_tasks()
            if task.due_date and task.due_date.date() == today and not task.completed
        ]

    def get_tasks_this_week(self) -> list[Task]:
        """Get all tasks due within 7 days.
        
        Returns:
            List of tasks due this week
        """
        today = date.today()
        week_end = today + timedelta(days=7)
        return [
            task for task in self.list_tasks()
            if task.due_date 
            and today <= task.due_date.date() <= week_end 
            and not task.completed
        ]

    def get_tasks_overdue(self) -> list[Task]:
        """Get all overdue tasks (past due and not completed).
        
        Returns:
            List of overdue tasks
        """
        today = date.today()
        return [
            task for task in self.list_tasks()
            if task.due_date 
            and task.due_date.date() < today 
            and not task.completed
        ]

    def complete_task(self, task_id: str) -> Task | None:
        """Mark a task as completed.
        
        Args:
            task_id: Task ID to complete
            
        Returns:
            Updated task if found, None otherwise
        """
        data = self.store.load()
        
        for i, task_data in enumerate(data["tasks"]):
            if task_data["id"] == task_id:
                task = deserialize_task(task_data)
                task.completed = True
                task.completed_at = datetime.now()
                
                # Update in storage
                data["tasks"][i] = serialize_task(task)
                self.store.save(data)
                
                return task
        
        return None

    def add_subtask(self, task_id: str, title: str) -> Task | None:
        """Add a subtask to a task.
        
        Args:
            task_id: Parent task ID
            title: Subtask title
            
        Returns:
            Updated task if found, None otherwise
        """
        data = self.store.load()
        
        for i, task_data in enumerate(data["tasks"]):
            if task_data["id"] == task_id:
                task = deserialize_task(task_data)
                
                # Generate subtask ID (integer)
                subtask_id = len(task.subtasks) + 1
                
                subtask = Subtask(
                    id=subtask_id,
                    title=title,
                    completed=False,
                )
                
                task.subtasks.append(subtask)
                
                # Update in storage
                data["tasks"][i] = serialize_task(task)
                self.store.save(data)
                
                return task
        
        return None

    def complete_subtask(self, task_id: str, subtask_id: int) -> Task | None:
        """Mark a subtask as completed.
        
        Args:
            task_id: Parent task ID
            subtask_id: Subtask ID to complete (integer)
            
        Returns:
            Updated task if found, None otherwise
        """
        data = self.store.load()
        
        for i, task_data in enumerate(data["tasks"]):
            if task_data["id"] == task_id:
                task = deserialize_task(task_data)
                
                for subtask in task.subtasks:
                    if subtask.id == subtask_id:
                        subtask.completed = True
                        
                        # Update in storage
                        data["tasks"][i] = serialize_task(task)
                        self.store.save(data)
                        
                        return task
                
                return None
        
        return None

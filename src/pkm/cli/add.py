"""Add commands for creating notes and tasks."""

from pathlib import Path

import click

from pkm.cli.helpers import error, success
from pkm.cli.main import cli
from pkm.services.note_service import NoteService
from pkm.services.task_service import TaskService


def get_data_dir(ctx: click.Context) -> Path:
    """Get data directory from context or use default.
    
    Args:
        ctx: Click context
        
    Returns:
        Path to data directory
    """
    data_dir = ctx.obj.get("data_dir")
    if data_dir is None:
        data_dir = Path.home() / ".pkm"
    else:
        data_dir = Path(data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


@cli.group()
def add() -> None:
    """Add notes and tasks."""
    pass


@add.command(name="note")
@click.argument("content", required=True)
@click.option("--course", "-c", help="Assign to course")
@click.option("--topics", "-t", multiple=True, help="Add topic tags")
@click.pass_context
def add_note(ctx: click.Context, content: str, course: str | None, topics: tuple[str, ...]) -> None:
    """Add a new note.
    
    CONTENT: Note content (use quotes for multi-line)
    
    Examples:
        pkm add note "Photosynthesis converts light to chemical energy"
        pkm add note "Important lecture points" --course "Biology 101"
        pkm add note "Study topic" --topics "Photosynthesis" --topics "Cell Structure"
    """
    try:
        data_dir = get_data_dir(ctx)
        service = NoteService(data_dir)
        
        note = service.create_note(
            content=content,
            course=course,
            topics=list(topics) if topics else None,
        )
        
        location = f"course '{course}'" if course else "inbox"
        success(f"Note created: {note.id} in {location}")
        
        if topics:
            success(f"Tagged with: {', '.join(topics)}")
            
    except Exception as e:
        error(f"Failed to create note: {e}")
        ctx.exit(1)


@add.command(name="task")
@click.argument("title", required=True)
@click.option("--due", "-d", help="Due date (e.g., 'tomorrow', '2025-12-01')")
@click.option("--priority", "-p", type=click.Choice(["high", "medium", "low"]), default="medium", help="Task priority")
@click.option("--course", "-c", help="Assign to course")
@click.pass_context
def add_task(ctx: click.Context, title: str, due: str | None, priority: str, course: str | None) -> None:
    """Add a new task.
    
    TITLE: Task description
    
    Examples:
        pkm add task "Submit lab report"
        pkm add task "Study for exam" --due "Friday" --priority high
        pkm add task "Review notes" --course "Biology 101"
    """
    try:
        data_dir = get_data_dir(ctx)
        service = TaskService(data_dir)
        
        # TODO: Parse due date with date_parser (Phase 4)
        due_date = None
        
        task = service.create_task(
            title=title,
            due_date=due_date,
            priority=priority,
            course=course,
        )
        
        location = f"course '{course}'" if course else "inbox"
        success(f"Task created: {task.id} in {location}")
        
        if priority != "medium":
            success(f"Priority: {priority}")
            
    except Exception as e:
        error(f"Failed to create task: {e}")
        ctx.exit(1)

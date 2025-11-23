"""View commands for displaying notes and tasks."""

from pathlib import Path

import click

from pkm.cli.add import get_data_dir
from pkm.cli.helpers import create_table, format_datetime, info, truncate
from pkm.cli.main import cli
from pkm.services.note_service import NoteService
from pkm.services.task_service import TaskService


@cli.group()
def view() -> None:
    """View notes and tasks in various formats.
    
    \b
    Available views:
      pkm view inbox    - Show unorganized notes and tasks
    
    \b
    Coming soon:
      pkm view today    - Tasks due today (Phase 4)
      pkm view week     - Tasks due this week (Phase 4)
      pkm view overdue  - Overdue tasks (Phase 4)
      pkm view course   - Items by course (Phase 5)
    
    \b
    Examples:
      pkm view inbox
      pkm view inbox --data-dir ~/my-notes
    """
    pass


@view.command(name="inbox")
@click.pass_context
def view_inbox(ctx: click.Context) -> None:
    """View all unorganized notes and tasks in your inbox.
    
    \b
    Shows:
      - Notes without a course assignment
      - Tasks without a course assignment
      - Displayed in rich formatted tables
      - Sorted by creation date
    
    \b
    Examples:
      # View inbox
      pkm view inbox
      
      # View inbox with custom data location
      pkm --data-dir ~/study-notes view inbox
    
    \b
    The inbox is your temporary holding area for quick capture.
    Organize items later by assigning them to courses (coming in Phase 5).
    
    Empty inbox = all items organized!
    """
    data_dir = get_data_dir(ctx)
    note_service = NoteService(data_dir)
    task_service = TaskService(data_dir)
    
    inbox_notes = note_service.get_inbox_notes()
    inbox_tasks = task_service.get_inbox_tasks()
    
    if not inbox_notes and not inbox_tasks:
        info("Inbox is empty")
        return
    
    # Display notes
    if inbox_notes:
        table = create_table("Inbox Notes", ["ID", "Content", "Created", "Topics"])
        for note in inbox_notes:
            table.add_row(
                note.id,
                truncate(note.content, 60),
                format_datetime(note.created_at),
                ", ".join(note.topics) if note.topics else "-",
            )
        from rich.console import Console
        Console().print(table)
        Console().print()
    
    # Display tasks
    if inbox_tasks:
        table = create_table("Inbox Tasks", ["ID", "Title", "Priority", "Created"])
        for task in inbox_tasks:
            priority_color = {
                "high": "[red]HIGH[/red]",
                "medium": "[yellow]MED[/yellow]",
                "low": "[green]LOW[/green]",
            }[task.priority]
            
            table.add_row(
                task.id,
                truncate(task.title, 60),
                priority_color,
                format_datetime(task.created_at),
            )
        from rich.console import Console
        Console().print(table)
    
    total = len(inbox_notes) + len(inbox_tasks)
    info(f"Total inbox items: {total} ({len(inbox_notes)} notes, {len(inbox_tasks)} tasks)")

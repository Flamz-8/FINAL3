"""View commands for displaying notes and tasks."""

from datetime import datetime
from pathlib import Path

import click
from rich.console import Console

from pkm.cli.add import get_data_dir
from pkm.cli.helpers import create_table, format_datetime, info, truncate
from pkm.cli.main import cli
from pkm.services.note_service import NoteService
from pkm.services.task_service import TaskService
from pkm.utils.date_parser import format_due_date


@cli.group()
def view() -> None:
    """View notes and tasks in various formats.
    
    \b
    Available views:
      pkm view inbox    - Show unorganized notes and tasks
      pkm view today    - Tasks due today
      pkm view week     - Tasks due this week
      pkm view overdue  - Overdue tasks
    
    \b
    Coming soon:
      pkm view course   - Items by course (Phase 5)
    
    \b
    Examples:
      pkm view inbox
      pkm view today
      pkm view week
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
        table = create_table("Inbox Notes", ["Content", "Created", "Topics"])
        for note in inbox_notes:
            table.add_row(
                truncate(note.content, 60),
                format_datetime(note.created_at),
                ", ".join(note.topics) if note.topics else "-",
            )
        Console().print(table)
        Console().print()
    
    # Display tasks
    if inbox_tasks:
        table = create_table("Inbox Tasks", ["Title", "Due", "Priority", "Subtasks"])
        for task in inbox_tasks:
            priority_color = {
                "high": "[red]HIGH[/red]",
                "medium": "[yellow]MED[/yellow]",
                "low": "[green]LOW[/green]",
            }[task.priority]
            
            # Format due date
            due_display = format_due_date(task.due_date) if task.due_date else "-"
            
            # Format subtasks progress
            if task.subtasks:
                completed = sum(1 for sub in task.subtasks if sub.completed)
                subtasks_display = f"{completed}/{len(task.subtasks)} ✓"
            else:
                subtasks_display = "-"
            
            table.add_row(
                truncate(task.title, 40),
                truncate(due_display, 25),
                priority_color,
                subtasks_display,
            )
        Console().print(table)
    
    total = len(inbox_notes) + len(inbox_tasks)
    info(f"Total inbox items: {total} ({len(inbox_notes)} notes, {len(inbox_tasks)} tasks)")


@view.command(name="today")
@click.pass_context
def view_today(ctx: click.Context) -> None:
    """View tasks due today.
    
    \b
    Shows:
      - All tasks with due date = today
      - Excludes completed tasks
      - Sorted by priority (high → medium → low)
    
    \b
    Examples:
      # View today's tasks
      pkm view today
      
      # With custom data location
      pkm --data-dir ~/study-notes view today
    
    Use this command each morning to see what's on your plate for the day!
    """
    data_dir = get_data_dir(ctx)
    task_service = TaskService(data_dir)
    
    tasks = task_service.get_tasks_today()
    
    if not tasks:
        info("No tasks due today!")
        return
    
    # Sort by priority
    priority_order = {"high": 0, "medium": 1, "low": 2}
    tasks.sort(key=lambda t: priority_order[t.priority])
    
    table = create_table(f"Tasks Due Today ({len(tasks)})", ["Title", "Due Time", "Priority", "Subtasks", "Course"])
    
    for task in tasks:
        priority_color = {
            "high": "[red]HIGH[/red]",
            "medium": "[yellow]MED[/yellow]",
            "low": "[green]LOW[/green]",
        }[task.priority]
        
        # Format due time (just time, not full date)
        due_time = task.due_date.strftime("%I:%M %p").replace(" 0", " ") if task.due_date else "-"
        
        # Format subtasks progress
        if task.subtasks:
            completed = sum(1 for sub in task.subtasks if sub.completed)
            subtasks_display = f"{completed}/{len(task.subtasks)} ✓"
        else:
            subtasks_display = "-"
        
        table.add_row(
            truncate(task.title, 35),
            due_time,
            priority_color,
            subtasks_display,
            task.course or "-",
        )
    
    Console().print(table)
    info(f"Total: {len(tasks)} tasks due today")


@view.command(name="week")
@click.pass_context
def view_week(ctx: click.Context) -> None:
    """View tasks due this week (next 7 days).
    
    \b
    Shows:
      - All tasks with due date within 7 days
      - Excludes completed tasks
      - Sorted by due date
    
    \b
    Examples:
      # View this week's tasks
      pkm view week
      
      # With custom data location
      pkm --data-dir ~/study-notes view week
    
    Great for weekly planning and seeing what's coming up!
    """
    data_dir = get_data_dir(ctx)
    task_service = TaskService(data_dir)
    
    tasks = task_service.get_tasks_this_week()
    
    if not tasks:
        info("No tasks due this week!")
        return
    
    # Sort by due date
    tasks.sort(key=lambda t: t.due_date if t.due_date else datetime.max)
    
    table = create_table(f"Tasks Due This Week ({len(tasks)})", ["Title", "Due", "Priority", "Subtasks", "Course"])
    
    for task in tasks:
        priority_color = {
            "high": "[red]HIGH[/red]",
            "medium": "[yellow]MED[/yellow]",
            "low": "[green]LOW[/green]",
        }[task.priority]
        
        # Format due date
        due_display = format_due_date(task.due_date) if task.due_date else "-"
        
        # Format subtasks progress
        if task.subtasks:
            completed = sum(1 for sub in task.subtasks if sub.completed)
            subtasks_display = f"{completed}/{len(task.subtasks)} ✓"
        else:
            subtasks_display = "-"
        
        table.add_row(
            truncate(task.title, 30),
            truncate(due_display, 25),
            priority_color,
            subtasks_display,
            task.course or "-",
        )
    
    Console().print(table)
    info(f"Total: {len(tasks)} tasks due within 7 days")


@view.command(name="overdue")
@click.pass_context
def view_overdue(ctx: click.Context) -> None:
    """View overdue tasks (past due date and not completed).
    
    \b
    Shows:
      - All tasks with due date < today
      - Only incomplete tasks
      - Sorted by how overdue (oldest first)
      - Highlighted in red
    
    \b
    Examples:
      # View overdue tasks
      pkm view overdue
      
      # With custom data location
      pkm --data-dir ~/study-notes view overdue
    
    Time to catch up on these! Complete or reschedule overdue tasks.
    """
    data_dir = get_data_dir(ctx)
    task_service = TaskService(data_dir)
    
    tasks = task_service.get_tasks_overdue()
    
    if not tasks:
        info("No overdue tasks - great job!")
        return
    
    # Sort by due date (oldest first)
    tasks.sort(key=lambda t: t.due_date if t.due_date else datetime.min)
    
    table = create_table(f"[red]Overdue Tasks ({len(tasks)})[/red]", ["Title", "Due", "Priority", "Subtasks", "Course"])
    
    for task in tasks:
        priority_color = {
            "high": "[red]HIGH[/red]",
            "medium": "[yellow]MED[/yellow]",
            "low": "[green]LOW[/green]",
        }[task.priority]
        
        # Format due date (highlight how overdue)
        due_display = f"[red]{format_due_date(task.due_date)}[/red]" if task.due_date else "-"
        
        # Format subtasks progress
        if task.subtasks:
            completed = sum(1 for sub in task.subtasks if sub.completed)
            subtasks_display = f"{completed}/{len(task.subtasks)} ✓"
        else:
            subtasks_display = "-"
        
        table.add_row(
            truncate(task.title, 30),
            truncate(due_display, 30),
            priority_color,
            subtasks_display,
            task.course or "-",
        )
    
    Console().print(table)
    info(f"[red]Total: {len(tasks)} overdue tasks[/red]")

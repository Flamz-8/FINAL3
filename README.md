# Pro Study Planner

Terminal-based personal knowledge management app for students that combines note-taking and task management in a single CLI tool.

---

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
- [Usage Guide](#usage-guide)
  - [Capturing Notes](#capturing-notes)
  - [Managing Tasks](#managing-tasks)
  - [Viewing Your Data](#viewing-your-data)
- [Key Features](#key-features)
- [Development](#development)

---

## Installation

### Prerequisites

- Python 3.11 or higher
- `uv` package manager

### Install uv

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install Pro Study Planner

**Option 1: For Development (Recommended)**
```bash
# Clone and install locally
cd C:\Users\parth\FINAL3
uv sync --all-extras

# Run directly
uv run python -m pkm --help
```

**Option 2: System-wide Installation**
```bash
# Install as a tool (when published)
uv tool install pro-study-planner

# Use pkm command globally
pkm --help
```

---

## Quick Start

### 1️⃣ Capture Notes and Tasks

Quickly save information to your inbox:

```bash
# Add a quick note
uv run python -m pkm add note "Photosynthesis converts light to chemical energy"

# Add a note with topics
uv run python -m pkm add note "Mitochondria is the powerhouse of the cell" \
  --topics "Biology" --topics "Cell Structure"

# Add a task with priority
uv run python -m pkm add task "Submit lab report" --priority high

# Add a task with due date
uv run python -m pkm add task "Study for exam" --due "tomorrow"
uv run python -m pkm add task "Final project" --due "next Friday"

# Add task to a course
uv run python -m pkm add task "Review chapter 5" --course "Biology 101"
```

### 2️⃣ View Your Inbox

See all unorganized items:

```bash
uv run python -m pkm view inbox
```

Output:
```
                  Inbox Notes                       
┏━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ ID       ┃ Content ┃ Created┃ Topics        ┃
┗━━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━┻━━━━━━━━━━━━━━━┛
```

### 3️⃣ Organize by Course

Move items from inbox to courses:

```bash
# Organize a note
uv run python -m pkm organize note NOTE_ID --course "Biology 101"

# Organize a task
uv run python -m pkm organize task TASK_ID --course "Math 201"

# View all courses
uv run python -m pkm view courses

# View a specific course
uv run python -m pkm view course "Biology 101"
```

### 4️⃣ Search Everything

Find notes and tasks quickly:

```bash
# Search everything
uv run python -m pkm search "photosynthesis"

# Search only notes or tasks
uv run python -m pkm search "exam" --type notes

# Search within a course
uv run python -m pkm search "chapter" --course "Biology 101"
```

---

## Core Concepts

### 📝 Notes
- **Purpose**: Capture lecture notes, ideas, and information
- **Features**: Multi-line content, topic tagging, course assignment
- **Inbox**: Notes without a course live in your inbox

### ✅ Tasks
- **Purpose**: Track assignments, todos, and deadlines
- **Features**: Priority levels, natural language due dates, subtasks with progress tracking
- **Inbox**: Tasks without a course live in your inbox

### 📚 Courses
- **Purpose**: Organize notes and tasks by academic subject
- **Auto-created**: Courses are created automatically when you assign items

### 🏷️ Topics
- **Purpose**: Tag notes for cross-cutting themes
- **Examples**: "Photosynthesis", "Exams", "Lab Work"
- **Flexibility**: One note can have multiple topics

### 📥 Inbox
- **Purpose**: Temporary holding area for quick capture
- **Workflow**: Capture fast → Organize later → View by course/topic

---

## Usage Guide

### Capturing Notes

#### Basic Note
```bash
uv run python -m pkm add note "Your note content here"
```

#### Note with Topics
```bash
uv run python -m pkm add note "DNA replication occurs in S phase" \
  --topics "Biology" \
  --topics "Cell Cycle" \
  --topics "Genetics"
```

#### Note Assigned to Course
```bash
uv run python -m pkm add note "Lecture: Intro to Photosynthesis" \
  --course "Biology 101" \
  --topics "Photosynthesis"
```

#### Multi-line Note
```bash
uv run python -m pkm add note "Key Points from Lecture:
- Photosynthesis happens in chloroplasts
- Light-dependent reactions occur in thylakoid membranes
- Calvin cycle occurs in stroma"
```

---

### Managing Tasks

#### Quick Task
```bash
uv run python -m pkm add task "Study for midterm"
```

#### Task with Due Date
```bash
# Natural language
uv run python -m pkm add task "Submit lab report" --due "tomorrow"
uv run python -m pkm add task "Final project" --due "next Friday"
uv run python -m pkm add task "Review notes" --due "in 3 days"

# Specific date
uv run python -m pkm add task "Research paper" --due "2025-12-15"

# With time
uv run python -m pkm add task "Quiz" --due "Friday 11:59pm"
```

#### Task with Priority
```bash
uv run python -m pkm add task "Submit lab report" --priority high
uv run python -m pkm add task "Read chapter 3" --priority low
```

Priority levels: `high`, `medium` (default), `low`

#### Task Assigned to Course
```bash
uv run python -m pkm add task "Complete problem set 5" \
  --course "Math 201" \
  --priority high
```

#### Combine All Options
```bash
uv run python -m pkm add task "Prepare presentation on photosynthesis" \
  --due "next Friday" \
  --course "Biology 101" \
  --priority medium
```

#### Managing Subtasks (Bullet Points)
```bash
# Add subtasks to break down a task
uv run python -m pkm task add-subtask TASK_ID "Read chapter 1"
uv run python -m pkm task add-subtask TASK_ID "Complete exercises"
uv run python -m pkm task add-subtask TASK_ID "Write summary"

# Mark a subtask as complete
uv run python -m pkm task check-subtask TASK_ID 1

# Complete the entire task
uv run python -m pkm task complete TASK_ID
```

---

### Viewing Your Data

#### View Inbox
See all unorganized notes and tasks:
```bash
uv run python -m pkm view inbox
```

#### View Tasks by Due Date
```bash
# Tasks due today
uv run python -m pkm view today

# Tasks due this week (next 7 days)
uv run python -m pkm view week

# Overdue tasks
uv run python -m pkm view overdue
```

#### Custom Data Directory
Use a different location for your data:
```bash
uv run python -m pkm --data-dir C:\MyStudyData view inbox
```

Default data location: `~/.pkm/data.json`

---

### Organizing Your Data

#### Organize Notes and Tasks
```bash
# Move a note to a course
uv run python -m pkm organize note NOTE_ID --course "Biology 101"

# Move a task to a course
uv run python -m pkm organize task TASK_ID --course "Math 201"

# Add topics while organizing
uv run python -m pkm organize note NOTE_ID \\
  --course "Biology 101" \\
  --add-topics "Photosynthesis"
```

#### View by Course
```bash
# List all courses
uv run python -m pkm view courses

# View everything in a course
uv run python -m pkm view course "Biology 101"
```

#### Search
```bash
# Search everything
uv run python -m pkm search "mitochondria"

# Search only notes
uv run python -m pkm search "exam" --type notes

# Search within a course
uv run python -m pkm search "chapter" --course "Biology 101"

# Search by topic
uv run python -m pkm search "cell" --topic "Biology"
```

---

## Implementation Status

### ✅ Currently Working (Phase 1-5, 8)

- **Quick Capture**
  - `pkm add note` - Add notes with content
  - `pkm add task` - Add tasks with priority and due dates
  - Topic tagging with `--topics`
  - Course assignment with `--course`
  - Natural language due dates (`--due "tomorrow"`)

- **Task Management**
  - Due date parsing - "tomorrow", "next Friday", "2025-12-01", "Friday 11:59pm"
  - Subtasks/Bullet Points - Break down tasks with progress tracking
  - Task completion - Mark tasks and subtasks as done
  - Filtered views - `view today`, `view week`, `view overdue`
  - Priority levels (high, medium, low)

- **Course Organization**
  - `pkm organize note` - Move notes to courses
  - `pkm organize task` - Move tasks to courses
  - `pkm view courses` - List all courses with counts
  - `pkm view course` - View all items in a specific course
  - Automatic course creation when organizing

- **Search**
  - `pkm search` - Full-text search across notes and tasks
  - Filter by type (notes/tasks)
  - Filter by course
  - Filter by topic (notes only)
  - Case-insensitive substring matching

- **Inbox Management**
  - `pkm view inbox` - View unorganized items with due dates and subtask progress
  - Rich terminal tables with colors
  - Automatic ID generation

- **Data Storage**
  - JSON file storage (~/.pkm/data.json)
  - Atomic writes with automatic backup
  - Corruption recovery

### ⏳ Coming Soon (Phase 6-7, 9-10)

- **Note Management** (Phase 6)
  - Note editing with external editor
  - Note deletion
  - Topic management

- **Note-Task Linking** (Phase 9)
  - Link notes to tasks for context
  - View linked notes from tasks
  - Bidirectional references

- **Help & Onboarding** (Phase 7)
  - First-run tutorial
  - Command-specific help with examples
  - Error suggestions

---

## Key Features

### 🚀 Quick Capture
Add notes and tasks with minimal friction - capture first, organize later

### ✅ Task Management  
Priority levels, natural language due dates, subtasks for breaking down work

### 📅 Smart Due Dates
Parse "tomorrow", "next Friday", "in 3 days", or specific dates like "2025-12-15"

### 📋 Subtasks / Bullet Points
Break down complex tasks into manageable steps with progress tracking

### 📚 Course Organization
Group notes and tasks by academic subject

### 🏷️ Topic Tagging
Categorize notes with multiple tags for easy retrieval

### 🔍 Filtered Views
See tasks due today, this week, or overdue at a glance

### 🔎 Full-Text Search
Quickly find any note or task across your entire knowledge base

### 📊 Course Organization
Group and view all notes and tasks by academic subject

### 🔗 Note-Task Linking *(Coming Soon)*
Reference notes from tasks for context

### 💾 Offline First
All data stored locally in human-readable JSON format

### 🛡️ Data Safety
- Atomic file writes prevent corruption
- Automatic backups (.bak files)
- Recovery from corrupted data

---

## Command Reference

### Global Options
```bash
--data-dir DIRECTORY   # Custom data location (default: ~/.pkm)
--no-color             # Disable colored output
-v, --verbose          # Enable verbose output
```

### Add Commands
```bash
pkm add note CONTENT [--course NAME] [--topics TAG]...
pkm add task TITLE [--due DATE] [--priority high|medium|low] [--course NAME]
```

### Task Commands
```bash
pkm task complete TASK_ID              # Mark task as done
pkm task add-subtask TASK_ID TITLE     # Add a subtask/bullet point
pkm task check-subtask TASK_ID NUM     # Complete a subtask
```

### View Commands
```bash
pkm view inbox         # Show unorganized notes and tasks
pkm view today         # Tasks due today
pkm view week          # Tasks due this week (next 7 days)
pkm view overdue       # Past-due incomplete tasks
pkm view courses       # List all courses
pkm view course NAME   # View items in a specific course
```

### Organize Commands
```bash
pkm organize note NOTE_ID --course NAME     # Move note to course
pkm organize task TASK_ID --course NAME     # Move task to course
```

### Search Command
```bash
pkm search QUERY [--type notes|tasks] [--course NAME] [--topic NAME]
```

### Help
```bash
pkm --help            # Show all commands
pkm add --help        # Help for add commands
pkm add note --help   # Help for specific command
```

---

## Examples & Workflows

### Morning Lecture Workflow
```bash
# During lecture - quick capture
uv run python -m pkm add note "Photosynthesis: light-dependent reactions"
uv run python -m pkm add note "Calvin cycle uses ATP and NADPH"
uv run python -m pkm add task "Review photosynthesis slides"

# After class - organize
# (Coming in Phase 5)
```

### Study Session Workflow
```bash
# View what's urgent
uv run python -m pkm view today

# View what needs attention
uv run python -m pkm view inbox

# Add study tasks with priority and due dates
uv run python -m pkm add task "Study for Biology midterm" \
  --due "Friday 11:59pm" \
  --priority high

# Break down a complex task
uv run python -m pkm task add-subtask TASK_ID "Review chapter 1"
uv run python -m pkm task add-subtask TASK_ID "Review chapter 2"
uv run python -m pkm task add-subtask TASK_ID "Complete practice problems"

# Mark progress as you go
uv run python -m pkm task check-subtask TASK_ID 1

# Tag notes by topic
uv run python -m pkm add note "Practice problems for exam" \
  --topics "Exam Prep" \
  --topics "Biology"
```

### Assignment Tracking
```bash
# Create high-priority task with due date
uv run python -m pkm add task "Submit research paper" \
  --due "next Friday 11:59pm" \
  --priority high \
  --course "English 101"

# Break it down into steps
uv run python -m pkm task add-subtask TASK_ID "Complete outline"
uv run python -m pkm task add-subtask TASK_ID "Write first draft"
uv run python -m pkm task add-subtask TASK_ID "Peer review"
uv run python -m pkm task add-subtask TASK_ID "Final revision"

# Add supporting notes
uv run python -m pkm add note "Thesis: Climate change impacts on agriculture" \
  --course "English 101" \
  --topics "Research Paper"

# Check your progress
uv run python -m pkm view week
```

---

## Data Location

Your data is stored in JSON format at:
- **Default**: `~/.pkm/data.json`
- **Custom**: Specify with `--data-dir` flag
- **Backup**: Automatically created as `data.json.bak`

### Data Structure
```json
{
  "notes": [...],
  "tasks": [...],
  "courses": [...]
}
```

---

## Troubleshooting

### Command not found: pkm
Use `uv run python -m pkm` instead, or install with `uv pip install -e .`

### Data file corrupted
Automatic recovery from `.bak` file will be attempted

### Python version error
Ensure Python 3.11+ is installed: `python --version`

---

## Development

### Setup Development Environment
```bash
# Clone repository
git clone https://github.com/Flamz-8/FINAL3.git
cd FINAL3

# Install with dev dependencies
uv sync --all-extras

# Verify installation
uv run python -m pkm --help
```

### Run Tests
```bash
# All tests (43 passing)
uv run pytest

# With coverage report
uv run pytest --cov=src/pkm --cov-report=term-missing

# Specific test file
uv run pytest tests/integration/test_add_commands.py -v
```

### Code Quality
```bash
# Run linter (complexity ≤10)
uv run ruff check .

# Run type checker (strict mode)
uv run mypy src/

# Format code
uv run ruff format .
```

### Project Structure
```
FINAL3/
├── src/pkm/              # Main package
│   ├── models/           # Pydantic data models
│   ├── storage/          # JSON persistence layer
│   ├── services/         # Business logic
│   └── cli/              # Click command handlers
├── tests/
│   ├── unit/             # Model & storage tests
│   ├── integration/      # CLI end-to-end tests
│   └── edge_cases/       # Error handling tests
├── pyproject.toml        # Project config & dependencies
└── README.md             # This file
```

---

## Contributing

This is a learning project following the SpecKit development methodology:
- Test-Driven Development (TDD)
- Incremental feature delivery
- Constitution-based quality gates

See `specs/001-student-pkm-cli/` for detailed specifications and task breakdown.

---

## License

[Add license information]

---

## Acknowledgments

Built with:
- [Click](https://click.palletsprojects.com/) - CLI framework
- [Pydantic](https://docs.pydantic.dev/) - Data validation
- [Rich](https://rich.readthedocs.io/) - Terminal formatting
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager

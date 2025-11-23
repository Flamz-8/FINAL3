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

### 3️⃣ Organize Later

*Coming in Phase 4-5*: Organize notes by course and topic after capture.

---

## Core Concepts

### 📝 Notes
- **Purpose**: Capture lecture notes, ideas, and information
- **Features**: Multi-line content, topic tagging, course assignment
- **Inbox**: Notes without a course live in your inbox

### ✅ Tasks
- **Purpose**: Track assignments, todos, and deadlines
- **Features**: Priority levels, due dates (coming soon), subtasks (coming soon)
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
  --course "Biology 101" \
  --priority medium
```

---

### Viewing Your Data

#### View Inbox
See all unorganized notes and tasks:
```bash
uv run python -m pkm view inbox
```

#### Custom Data Directory
Use a different location for your data:
```bash
uv run python -m pkm --data-dir C:\MyStudyData view inbox
```

Default data location: `~/.pkm/data.json`

---

## Implementation Status

### ✅ Currently Working (Phase 1-3)

- **Quick Capture**
  - `pkm add note` - Add notes with content
  - `pkm add task` - Add tasks with priority
  - Topic tagging with `--topics`
  - Course assignment with `--course`

- **Inbox Management**
  - `pkm view inbox` - View unorganized items
  - Rich terminal tables with colors
  - Automatic ID generation

- **Data Storage**
  - JSON file storage (~/.pkm/data.json)
  - Atomic writes with automatic backup
  - Corruption recovery

### ⏳ Coming Soon (Phase 4+)

- **Task Management** (Phase 4)
  - Due dates: `--due "tomorrow"`, `--due "2025-12-01"`
  - Date parsing: "Friday", "next week"
  - Views: `pkm view today`, `pkm view week`, `pkm view overdue`
  - Task completion: `pkm task complete`

- **Organization** (Phase 5-6)
  - `pkm organize note` - Move notes to courses
  - `pkm organize task` - Move tasks to courses
  - `pkm view course` - View all items in a course
  - Note editing and deletion

- **Advanced Features** (Phase 7-10)
  - Help system and onboarding
  - Full-text search across notes and tasks
  - Note-task linking
  - Task subtasks and dependencies
  - Performance optimization

---

## Key Features

### 🚀 Quick Capture
Add notes and tasks with minimal friction - capture first, organize later

### ✅ Task Management  
Priority levels, due dates (coming soon), subtasks (coming soon)

### 📚 Course Organization
Group notes and tasks by academic subject

### 🏷️ Topic Tagging
Categorize notes with multiple tags for easy retrieval

### 🔍 Full-Text Search *(Coming Soon)*
Find anything across all your notes and tasks

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
pkm add task TITLE [--priority high|medium|low] [--course NAME]
```

### View Commands
```bash
pkm view inbox         # Show unorganized notes and tasks
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
# View what needs attention
uv run python -m pkm view inbox

# Add study tasks with priority
uv run python -m pkm add task "Study for Biology midterm" --priority high
uv run python -m pkm add task "Complete Math homework" --priority medium

# Tag notes by topic
uv run python -m pkm add note "Practice problems for exam" \
  --topics "Exam Prep" \
  --topics "Biology"
```

### Assignment Tracking
```bash
# Create high-priority task
uv run python -m pkm add task "Submit research paper" \
  --priority high \
  --course "English 101"

# Add supporting notes
uv run python -m pkm add note "Thesis: Climate change impacts on agriculture" \
  --course "English 101" \
  --topics "Research Paper"
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

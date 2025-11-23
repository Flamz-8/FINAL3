# Pro Study Planner

Terminal-based personal knowledge management app for students that combines note-taking and task management in a single CLI tool.

## Quick Start

### Installation

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/macOS
# or
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# Install Pro Study Planner
uv tool install pro-study-planner
```

### First Steps

1. **Capture** - Quickly save notes and tasks to your inbox:
   ```bash
   pkm add note "Photosynthesis converts light to chemical energy"
   pkm add task "Submit lab report" --due "Friday"
   ```

2. **Organize** - Assign items to courses and topics:
   ```bash
   pkm organize note n_20251123_103045_abc --course "Biology 101" --add-topics "Photosynthesis"
   ```

3. **View** - See what needs your attention:
   ```bash
   pkm view inbox           # Unorganized items
   pkm view today           # Tasks due today
   pkm view course "Biology 101"  # All items for a course
   ```

## Key Features

- **Quick Capture**: Add notes and tasks with minimal friction
- **Task Management**: Due dates, priorities, subtasks
- **Course Organization**: Group by academic courses
- **Topic Tagging**: Categorize notes for easy retrieval
- **Full-Text Search**: Find anything across notes and tasks
- **Note-Task Linking**: Reference notes from tasks for context
- **Offline First**: All data stored locally in JSON format

## Documentation

For detailed usage instructions and workflows, see [docs/quickstart.md](docs/quickstart.md).

## Requirements

- Python 3.11 or higher
- Cross-platform: Linux, macOS, Windows

## Development

```bash
# Clone the repository
git clone <repo-url>
cd pro-study-planner

# Install with dev dependencies
uv sync --all-extras

# Run tests
uv run pytest

# Run linting
uv run ruff check .

# Run type checking
uv run mypy src/
```

## License

[Add license information]

"""Main CLI application entry point."""

import click


@click.group()
@click.option(
    "--data-dir",
    type=click.Path(exists=False, file_okay=False, dir_okay=True, path_type=str),
    default=None,
    help="Directory for data storage (default: ~/.pkm)",
)
@click.option("--no-color", is_flag=True, help="Disable colored output")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.pass_context
def cli(ctx: click.Context, data_dir: str | None, no_color: bool, verbose: bool) -> None:
    """Pro Study Planner - Terminal-based personal knowledge management for students.
    
    \b
    Quick capture workflow:
      1. Add notes and tasks to inbox
      2. Organize by course and topic (coming soon)
      3. View filtered lists and search
    
    \b
    Examples:
      pkm add note "Photosynthesis converts light to energy"
      pkm add task "Submit lab report" --priority high
      pkm view inbox
    
    \b
    Get help on specific commands:
      pkm add --help
      pkm add note --help
      pkm view --help
    
    Data is stored at ~/.pkm/data.json (or use --data-dir to customize)
    """
    # Store global options in context for subcommands
    ctx.ensure_object(dict)
    ctx.obj["data_dir"] = data_dir
    ctx.obj["no_color"] = no_color
    ctx.obj["verbose"] = verbose


# Import command groups to register them with the CLI
# This must happen after cli() is defined
from pkm.cli import add  # noqa: E402
from pkm.cli import view  # noqa: E402
from pkm.cli import task  # noqa: E402
from pkm.cli import organize  # noqa: E402
from pkm.cli import search  # noqa: E402


if __name__ == "__main__":
    cli()

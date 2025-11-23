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
    
    Quick capture notes and tasks, organize by course and topic, track deadlines.
    """
    # Store global options in context for subcommands
    ctx.ensure_object(dict)
    ctx.obj["data_dir"] = data_dir
    ctx.obj["no_color"] = no_color
    ctx.obj["verbose"] = verbose


if __name__ == "__main__":
    cli()

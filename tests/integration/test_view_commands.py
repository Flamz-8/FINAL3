"""Integration tests for view commands."""

from pathlib import Path

from click.testing import CliRunner

from pkm.cli.main import cli


class TestViewCommands:
    """Integration tests for view commands."""

    def test_view_inbox_shows_all_items(self, temp_data_dir: Path) -> None:
        """Test US1-S3: View inbox shows all unorganized notes and tasks."""
        runner = CliRunner()
        
        # Add a note
        runner.invoke(
            cli,
            ["--data-dir", str(temp_data_dir), "add", "note", "Inbox note"],
        )
        
        # Add a task
        runner.invoke(
            cli,
            ["--data-dir", str(temp_data_dir), "add", "task", "Inbox task"],
        )
        
        # View inbox
        result = runner.invoke(
            cli, ["--data-dir", str(temp_data_dir), "view", "inbox"]
        )
        
        assert result.exit_code == 0
        assert "Inbox Notes" in result.output
        assert "Inbox Tasks" in result.output
        assert "Inbox note" in result.output
        assert "Inbox task" in result.output
        assert "Total inbox items: 2" in result.output

    def test_view_inbox_empty(self, temp_data_dir: Path) -> None:
        """Test viewing empty inbox."""
        runner = CliRunner()
        result = runner.invoke(
            cli, ["--data-dir", str(temp_data_dir), "view", "inbox"]
        )
        
        assert result.exit_code == 0
        assert "Inbox is empty" in result.output

    def test_view_inbox_excludes_organized_items(self, temp_data_dir: Path) -> None:
        """Test that inbox only shows items without a course."""
        runner = CliRunner()
        
        # Add inbox note
        runner.invoke(
            cli,
            ["--data-dir", str(temp_data_dir), "add", "note", "Inbox note"],
        )
        
        # Add course note
        runner.invoke(
            cli,
            [
                "--data-dir",
                str(temp_data_dir),
                "add",
                "note",
                "Course note",
                "--course",
                "Biology",
            ],
        )
        
        # View inbox
        result = runner.invoke(
            cli, ["--data-dir", str(temp_data_dir), "view", "inbox"]
        )
        
        assert result.exit_code == 0
        assert "Inbox note" in result.output
        assert "Course note" not in result.output
        assert "Total inbox items: 1" in result.output

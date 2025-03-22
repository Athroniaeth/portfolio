def lint():
    """Run formatter and linter (ruff) on the codebase."""
    import subprocess
    subprocess.run("uv run ruff format .")
    subprocess.run("uv run ruff check . --fix")


def cli():
    """Run the CLI of the application."""
    from athrerank.__main__ import main

    main()

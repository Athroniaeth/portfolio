import os
from pathlib import Path
from typing import Literal

import toml
from loguru import logger


def is_dev():
    """Check if the application is in development mode."""
    return os.getenv("APP_MODE") == "DEV"


def setup_mode(mode: Literal["dev", "prod"]):
    """Setup the application in a given mode."""
    mode = mode.upper()
    os.environ["APP_MODE"] = mode
    logger.info(f"Setting up mode: {mode}")


def lint():
    """Run formatter and linter (ruff) on the codebase."""
    import subprocess

    subprocess.run("uv run ruff format .")
    subprocess.run("uv run ruff check . --fix")


def get_version() -> str:
    """Get the version of the application."""
    pyproject_path = PROJECT_PATH / "pyproject.toml"
    content = pyproject_path.read_text(encoding="utf-8")
    dict_content = toml.loads(content)

    return dict_content["project"]["version"]


def cli():
    """Run the CLI of the application."""
    from portfolio.__main__ import main

    main()


# Global variables of the project
PROJECT_PATH = Path(__file__).parents[2]
CONFIG_PATH = PROJECT_PATH / "config.toml"
DIST_PATH = PROJECT_PATH / "front" / "dist"
ASSETS_PATH = PROJECT_PATH / "front" / "src" / "assets"

VITE_DEV_SERVER = "http://localhost:5173"

import os
import sys
from enum import StrEnum
from typing import Annotated

import typer
from loguru import logger
from typer import Typer


class Level(StrEnum):
    """
    Log levels used to trace application execution.

    Attributes:
        TRACE   : Very fine-grained details for deep debugging.
        DEBUG   : Debugging information for developers.
        INFO    : General operational events.
        WARNING : Unexpected behavior that doesn't stop execution.
        ERROR   : Critical issues that affect functionality.
    """

    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


LoggingLevel = Annotated[
    Level, typer.Option("--logging-level", "-l", help="Log level of the application.")
]

cli = Typer(
    name="athrerank",
    no_args_is_help=True,
    pretty_exceptions_enable=False,
    help="CLI for the FastAPI application.",
)


def _get_workers(expected_workers: int):
    """Get the number of workers to use."""

    max_workers = os.cpu_count() or 1

    if expected_workers <= 0:
        logger.info(f"Uvicorn will use all possible hearts ({max_workers})")
        return max_workers

    logger.info(f"Uvicorn will use {expected_workers} workers")
    return min(expected_workers, max_workers)


def _run(
    source: str,
    host: str,
    port: int,
    workers: int = 1,
    reload: bool = False,
):
    """Run the server using uvicorn."""
    import uvicorn

    logger.info(f"Running server on {host}:{port}")
    workers = _get_workers(workers)

    uvicorn.run(
        source,
        host=host,
        port=port,
        reload=reload,
        workers=workers,
    )


@cli.callback()
def callback(level: LoggingLevel = Level.INFO):
    """Callback to run before any command."""
    from dotenv import load_dotenv

    # Load envvars from dotenv file
    load_dotenv()

    # Remove default logger and add a linked to stdout
    logger.remove(0)

    # Restore default logger with correct log level
    logger.add(sys.stdout, level=level)


@cli.command()
def run(
    source: str = "athrerank.app:create_app",
    host: str = "0.0.0.0",
    port: int = 8000,
    workers: int = 1,
):
    """Run the server in production mode."""

    from athrerank import setup_mode

    setup_mode("prod")

    _run(
        source=source,
        host=host,
        port=port,
        workers=workers,
    )


@cli.command()
def dev(
    source: str = "athrerank.app:create_app",
    host: str = "0.0.0.0",
    port: int = 8000,
):
    """Run the server in development mode."""
    from athrerank.vite import check_vite

    from athrerank import setup_mode

    setup_mode("dev")

    if not check_vite():
        raise Exception("Vite dev server is not running. Please start it first.")

    _run(
        source=source,
        host=host,
        port=port,
        reload=True,
    )

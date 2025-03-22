import os
import sys
from typer import Typer
from loguru import logger

cli = Typer(
    name="athrerank",
    no_args_is_help=True,
    help="CLI of FastAPI application to rerank documents based on their relevance.",
)


def _get_workers(expected_workers: int):
    """Get the number of workers to use."""

    max_workers = os.cpu_count() or 1

    if expected_workers <= 0:
        logger.info(f"Asking for max workers: {max_workers}")
        return max_workers

    logger.info(f"Asking for {expected_workers} workers")
    return min(expected_workers, max_workers)


def _run(
    source: str,
    host: str,
    port: int,
    workers: int,
    debug: bool = False,
):
    """Run the server using uvicorn."""
    import uvicorn

    logger.info(f"Running server on {host}:{port}")
    uvicorn.run(source, host=host, port=port, reload=debug, workers=_get_workers(workers))


@cli.callback()
def callback():
    """Callback to run before any command."""
    from dotenv import load_dotenv

    # Load envvars from dotenv file
    load_dotenv()

    # Remove default logger and add a linked to stdout
    logger.remove(0)
    level = os.getenv("LOG_LEVEL", "INFO")
    logger.add(sys.stdout, level=level)


@cli.command()
def run(
    source: str = "athrerank.app:app",
    host: str = "0.0.0.0",
    port: int = 8000,
    workers: int = 1,
):
    """Run the server in production mode."""
    _run(
        source=source,
        host=host,
        port=port,
        workers=workers,
    )


@cli.command()
def dev(
    source: str = "athrerank.app:app",
    host: str = "0.0.0.0",
    port: int = 8000,
    workers: int = 1,
):
    """Run the server in development mode."""
    _run(
        source=source,
        host=host,
        port=port,
        workers=workers,
    )

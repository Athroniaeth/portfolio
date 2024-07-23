import os
from enum import StrEnum
from typing import Optional, Tuple

import typer
import uvicorn

from src.app import app

cli = typer.Typer(pretty_exceptions_show_locals=True, no_args_is_help=False, pretty_exceptions_short=False)


class Level(StrEnum):
    """Level of logging to use."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Environment(StrEnum):
    """Environment to use (local or ovh cloud)."""

    DEVELOPMENT = "development"
    PRODUCTION = "production"


def get_info_environment(
    environment: Environment = Environment.DEVELOPMENT,
    ssl_keyfile: Optional[str] = None,
    ssl_certfile: Optional[str] = None,
) -> Tuple[str, int, str, str]:
    """
    Get the information of the environment.

    Args:
    --------
        environment (Environment): The environment to use.
        ssl_keyfile (Optional[str]): The SSL key file.
        ssl_certfile (Optional[str]): The SSL certificate file.

    Returns:
    --------
        str: The host to use for the server.
        int: The port to use for the server.
        str: The SSL key file path.
        str: The SSL certificate file path.
    """
    match environment:
        case Environment.DEVELOPMENT:
            host = "127.0.0.1"
            port = 8000
            ssl_keyfile = None
            ssl_certfile = None

        case Environment.PRODUCTION:
            list_raises = []
            host = "0.0.0.0"
            port = 443

            if not ssl_keyfile:
                list_raises.append(EnvironmentError("'SSL_KEYFILE' environment variable not set"))

            if not ssl_certfile:
                list_raises.append(EnvironmentError("'SSL_CERTFILE' environment variable not set"))

            if ssl_keyfile and not os.path.exists(ssl_keyfile):
                list_raises.append(FileNotFoundError(f"'{ssl_keyfile}' not found"))

            if ssl_certfile and not os.path.exists(ssl_certfile):
                list_raises.append(FileNotFoundError(f"'{ssl_certfile}' not found"))

            if list_raises:
                raise ExceptionGroup("Failed to start the server", list_raises)

        case _:
            raise ValueError(f"Environment '{environment}' not supported")

    return host, port, ssl_keyfile, ssl_certfile


@cli.command()
def run(
    environment: Environment = typer.Option(Environment.DEVELOPMENT, envvar="ENVIRONMENT", help="Environnement d'exécution."),
    ssl_keyfile: str = typer.Option(None, envvar="SSL_KEYFILE", help="Fichier de clé SSL."),
    ssl_certfile: str = typer.Option(None, envvar="SSL_CERTFILE", help="Fichier de certificat SSL."),
):
    """
    Start the server with the given environment.

    Args:
    --------
        environment (Environment): The environment to use.
        ssl_keyfile (str): The SSL key file.
        ssl_certfile (str): The SSL certificate file.
    """
    host, port, ssl_keyfile, ssl_certfile = get_info_environment(environment, ssl_keyfile, ssl_certfile)
    uvicorn.run(app, host=host, port=port, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile)

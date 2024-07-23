import logging
import os
import sys
from pathlib import Path

import uvicorn
from dotenv import load_dotenv

# Automatically add the working directory
path = Path(__file__).parents[1].absolute()
sys.path.append(f"{path}")

from src.app import app  # noqa: E402
from src import ENV_PATH  # noqa: E402


def main():
    """
    Main function to run the application.

    Raises:
        SystemExit: If the program is exited.

    Returns:
        int: The return code of the program.
    """
    load_dotenv(dotenv_path=ENV_PATH)

    return_code = 0
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Ajoute la commande de l'utilisateur au log
    logging.debug(f"Command use \"{' '.join(sys.argv)}\"")

    # Récupère l'environnement
    environment = os.getenv("ENVIRONMENT", "development")

    if environment not in ["development", "production"]:
        raise ValueError(f"Environment '{environment}' not supported")

    logging.debug(f"Environment: '{environment}'")

    host = "127.0.0.1" if environment == "development" else "0.0.0.0"
    port = 8000 if environment == "development" else 443

    # Récupère la configuration SSL
    ssl_keyfile = os.getenv("SSL_KEYFILE") if environment == "production" else None
    ssl_certfile = os.getenv("SSL_CERTFILE") if environment == "production" else None

    try:
        uvicorn.run(app, host=host, port=port, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile)
    except KeyboardInterrupt as exception:
        logging.debug(f"Exiting the program: '{exception}'")

    except SystemExit as exception:
        logging.debug(f"Exiting the program: '{exception}'")
        return_code = exception.code

    except Exception as exception:
        logging.error(f"An error occurred: '{exception}'")
        return_code = 1

    finally:
        sys.exit(return_code)


if __name__ == "__main__":
    main()

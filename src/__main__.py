import logging
import sys
from pathlib import Path

import uvicorn

# Automatically add the working directory
path = Path(__file__).parents[1].absolute()
sys.path.append(f"{path}")

from src.app import app  # noqa: E402


def main():
    """
    Main function to run the application.

    Raises:
        SystemExit: If the program is exited.

    Returns:
        int: The return code of the program.
    """
    return_code = 0
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Ajoute la commande de l'utilisateur au log
    logging.debug(f"Command use \"{' '.join(sys.argv)}\"")

    try:
        uvicorn.run(app, host="127.0.0.1", port=8000)  # noqa: B104
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

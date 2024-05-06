import sys
from pathlib import Path

import uvicorn
from dotenv import load_dotenv

# Ajoute le chemin d'accès du projet au PYTHONPATH
project_path = Path(__file__).absolute().parents[2]
sys.path.append(f"{project_path}")

from portfolio import ENV_PATH


def main():
    uvicorn.run("app:app", host="127.0.0.1", port=8000)


if __name__ == "__main__":
    # Charge les variables d'environnement
    load_dotenv(dotenv_path=ENV_PATH)

    # Lance l'application principale
    main()

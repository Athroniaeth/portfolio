from pathlib import Path

# Chemins d'accès globales
PROJECT_PATH = Path(__file__).absolute().parents[1]
APP_PATH = PROJECT_PATH / "portfolio"
ENV_PATH = PROJECT_PATH / ".env"

# Chemins d'accès pour FastAPI
STATIC_PATH = APP_PATH / "static"
TEMPLATES_PATH = APP_PATH / "templates"

from pathlib import Path

# Classic global variables
PROJECT_PATH = Path(__file__).parents[1]
SOURCE_PATH = Path(__file__).parents[0]
ENV_PATH = PROJECT_PATH / ".env"

# Globals variables for this project
STATIC_PATH = SOURCE_PATH / "static"
TEMPLATES_PATH = SOURCE_PATH / "templates"

# Configuration paths for the website (content)
CONFIG_PATH = SOURCE_PATH / "config"  # Contain translations for the website
LOCALES_PATH = CONFIG_PATH / "locales"  # Contain translations for the website

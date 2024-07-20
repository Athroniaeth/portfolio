from pathlib import Path

# Classic global variables
PROJECT_PATH = Path(__file__).parents[1]
SOURCE_PATH = Path(__file__).parents[0]

# Globals variables for this project
STATIC_PATH = PROJECT_PATH / "static"
LOCALES_PATH = PROJECT_PATH / "locales"
TEMPLATES_PATH = SOURCE_PATH / "templates"

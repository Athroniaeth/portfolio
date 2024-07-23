from functools import lru_cache

from fastapi import HTTPException

from src import CONFIG_PATH, LOCALES_PATH
from src.dataclass.info import Info
from src.dataclass.locale import Locale


@lru_cache(maxsize=1)
def get_info(filename: str = "info.toml") -> Info:
    """Load the config file (user information)."""
    config_path = CONFIG_PATH / filename

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found '{config_path}'")

    return Info.from_toml(config_path)


@lru_cache(maxsize=1)
def get_locale(locale: str = "en") -> Locale:
    """Load all the locales (translations)."""
    locale_path = LOCALES_PATH / f"{locale}.toml"

    if not locale_path.exists():
        raise HTTPException(status_code=404, detail="Locale not found")

    return Locale.from_toml(locale_path)

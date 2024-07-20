from functools import lru_cache

from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src import LOCALES_PATH, PROJECT_PATH, STATIC_PATH, TEMPLATES_PATH
from src.dataclass.config import Config
from src.dataclass.locale import Locale

app = FastAPI()

# Add static path
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

# Add jinja2 template
templates = Jinja2Templates(directory=TEMPLATES_PATH)


@lru_cache(maxsize=1)
def get_config(filename: str = "config.toml") -> Config:
    """Load the config file (user information)."""
    config_path = PROJECT_PATH / filename

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found '{config_path}'")

    return Config.from_toml(config_path)


@lru_cache(maxsize=1)
def get_locales(locale: str = "en") -> Locale:
    """Load all the locales (translations)."""
    locale_path = LOCALES_PATH / f"{locale}.toml"

    if not locale_path.exists():
        raise HTTPException(status_code=404, detail="Locale not found")

    return Locale.from_toml(locale_path)


@app.get("/")
async def read_root() -> HTMLResponse:
    # Default to English, redirection
    return HTMLResponse(status_code=302, headers={"Location": "/en/"})


@app.get("/{locale}/")
async def read_root_locale(request: Request, locale: str) -> HTMLResponse:
    if len(locale) != 2:
        raise HTTPException(status_code=404, detail="Locale not found")

    config = get_config()
    locale_config = get_locales(locale)
    return templates.TemplateResponse("index.jinja2", {"request": request, "locale": locale_config, "config": config})


@app.exception_handler(404)
async def not_found(request, exc):
    return templates.TemplateResponse("404.jinja2", {"request": request})

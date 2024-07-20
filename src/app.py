from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src import LOCALES_PATH, STATIC_PATH, TEMPLATES_PATH
from src.dataclass.index import Index

app = FastAPI()

# Add static path
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

# Add jinja2 template
templates = Jinja2Templates(directory=TEMPLATES_PATH)


# 404 error handler


@app.get("/")
def read_root():
    # Default to English, redirection
    return HTMLResponse(status_code=302, headers={"Location": "/en/"})


@app.get("/{locale}/")
def read_root_locale(request: Request, locale: str):
    if len(locale) != 2:
        raise HTTPException(status_code=404, detail="Locale not found")

    print(locale)
    path = LOCALES_PATH / f"{locale}.toml"

    if not path.exists():
        raise HTTPException(status_code=404, detail="Locale not found")

    locale_index = Index.from_toml(path)
    return templates.TemplateResponse("index.jinja2", {"request": request, "locale": locale_index})


@app.exception_handler(404)
async def not_found(request, exc):
    return templates.TemplateResponse("404.jinja2", {"request": request})

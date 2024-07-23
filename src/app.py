from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src import STATIC_PATH
from src.router import router, templates

# Initialize the FastAPI app
app = FastAPI()

# Initialize the routers
app.include_router(router)

# Add static files to the app
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")


@app.exception_handler(404)
async def not_found(request, exc):  # noqa: F811
    return templates.TemplateResponse("responses/404.jinja2", {"request": request})


@app.exception_handler(500)
async def not_found(request, exc):  # noqa: F811
    return templates.TemplateResponse("responses/500.jinja2", {"request": request, "message": f"{exc}"})

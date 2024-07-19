from typing import Union

from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from src import SOURCE_PATH, STATIC_PATH

app = FastAPI()

# Add static path
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")


@app.get("/")
def read_root():
    # return index.html
    path = SOURCE_PATH / "index.html"
    file = open(path, "r")
    return HTMLResponse(content=file.read(), status_code=200)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

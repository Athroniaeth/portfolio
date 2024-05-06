from fastapi import APIRouter
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from portfolio import TEMPLATES_PATH

router = APIRouter()
templates = Jinja2Templates(directory=f'{TEMPLATES_PATH}')


@router.get('/')
def index(request: Request):
    # jinja2 template 'index.html' is rendered
    return templates.TemplateResponse("index.jinja2", {"request": request})

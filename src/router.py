import os
from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi.params import Form, Query
from pydantic import EmailStr
from slowapi import Limiter
from slowapi.util import get_remote_address
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from src import TEMPLATES_PATH
from src._email import send_email
from src.config import get_info, get_locale

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)
templates = Jinja2Templates(directory=TEMPLATES_PATH)


@router.get("/")
async def read_root() -> HTMLResponse:
    # Default to English, redirection
    return HTMLResponse(status_code=302, headers={"Location": "/fr/"})


@router.post("/send-email/", name="send-email")
@limiter.limit("1/minute")
async def submit_form(
    request: Request,
    name: str = Form(..., min_length=2, max_length=50),
    email: EmailStr = Form(..., min_length=5, max_length=75),
    phone: Optional[str] = Form(None, min_length=10, max_length=15),
    message: str = Form(..., min_length=10, max_length=2000),
):
    list_raises = []

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    smtp_start_tls = os.getenv("SMTP_START_TLS")

    if not smtp_host:
        list_raises.append(EnvironmentError("'SMTP_HOST' environment variable not set"))

    if not smtp_port:
        list_raises.append(EnvironmentError("'SMTP_PORT' environment variable not set"))

    if not smtp_username:
        list_raises.append(EnvironmentError("'SMTP_USERNAME' environment variable not set"))

    if not smtp_password:
        list_raises.append(EnvironmentError("'SMTP_PASSWORD' environment variable not set"))

    if not smtp_start_tls:
        list_raises.append(EnvironmentError("'SMTP_START_TLS' environment variable not set"))

    if list_raises:
        raise HTTPException(status_code=500, detail=ExceptionGroup("Failed to send email", list_raises))

    smtp_port = int(smtp_port)
    smtp_start_tls = smtp_start_tls.lower() == "true"

    await send_email(
        name=name,
        email=email,
        phone=phone,
        message=message,
        smtp_host=smtp_host,
        smtp_port=smtp_port,
        smtp_username=smtp_username,
        smtp_password=smtp_password,
        smtp_start_tls=smtp_start_tls,
    )

    return templates.TemplateResponse("responses/200-email.jinja2", {"request": request})


@router.get("/responses/{response}")
async def read_responses(
    request: Request,
    response: str,
    message: Optional[str] = Query(None, min_length=10, max_length=200),
) -> HTMLResponse:
    return templates.TemplateResponse(f"responses/{response}.jinja2", {"request": request, "message": message})


@router.get("/{locale}/")
async def read_root_locale(request: Request, locale: str) -> HTMLResponse:
    if len(locale) != 2:
        raise HTTPException(status_code=404, detail="Locale not found")

    config = get_info()
    locale_config = get_locale(locale)
    return templates.TemplateResponse("index.jinja2", {"request": request, "locale": locale_config, "config": config, "lang": locale})

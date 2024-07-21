import logging
import os
from email.message import EmailMessage
from functools import lru_cache
from typing import Optional

import aiosmtplib
from fastapi import FastAPI, HTTPException
from fastapi.params import Form, Query
from pydantic import EmailStr
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src import CONFIG_PATH, LOCALES_PATH, STATIC_PATH, TEMPLATES_PATH
from src.dataclass.info import Info
from src.dataclass.locale import Locale

app = FastAPI()

# Add static path
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

# Add jinja2 template
templates = Jinja2Templates(directory=TEMPLATES_PATH)


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


@app.get("/")
async def read_root() -> HTMLResponse:
    # Default to English, redirection
    return HTMLResponse(status_code=302, headers={"Location": "/en/"})


async def send_email(
    name: str,
    email: str,
    phone: Optional[str],
    message: str,
    smtp_host: str = "smtp.example.com",
    smtp_port: int = 587,
    smtp_username: str = None,
    smtp_password: str = None,
    smtp_start_tls: bool = True,
):
    logging.debug(f"User info: '{name}', '{email}', '{phone}', '{message}'")
    logging.debug(f"SMTP info: '{smtp_host}', '{smtp_port}', '{smtp_username}', '{smtp_password}', '{smtp_start_tls}'")
    logging.debug(f"Sending email to {smtp_username}")
    email_message = EmailMessage()
    email_message["From"] = email
    email_message["To"] = smtp_username
    email_message["Subject"] = f"Portfolio New message from {name}"

    email_content = f"""
    Name: {name}
    Email: {email}
    Phone: {phone if phone else 'N/A'}
    Message: {message}
    """
    email_message.set_content(email_content)

    try:
        await aiosmtplib.send(email_message, hostname=smtp_host, port=smtp_port, username=smtp_username, password=smtp_password, start_tls=smtp_start_tls)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {e}")


@app.post("/send-email/", name="send-email")
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


@app.get("/responses/{response}")
async def read_responses(
    request: Request,
    response: str,
    message: Optional[str] = Query(None, min_length=10, max_length=200),
) -> HTMLResponse:
    return templates.TemplateResponse(f"responses/{response}.jinja2", {"request": request, "message": message})


@app.get("/{locale}/")
async def read_root_locale(request: Request, locale: str) -> HTMLResponse:
    if len(locale) != 2:
        raise HTTPException(status_code=404, detail="Locale not found")

    config = get_info()
    locale_config = get_locale(locale)
    return templates.TemplateResponse("index.jinja2", {"request": request, "locale": locale_config, "config": config, "lang": locale})


@app.exception_handler(404)
async def not_found(request, exc):  # noqa: F811
    return templates.TemplateResponse("responses/404.jinja2", {"request": request})


@app.exception_handler(500)
async def not_found(request, exc):  # noqa: F811
    return templates.TemplateResponse("responses/500.jinja2", {"request": request, "message": exc.detail})

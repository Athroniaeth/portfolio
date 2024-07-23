"""_email because 'aiosmtplib' have already a module named 'email'."""

import logging
from email.message import EmailMessage
from typing import Optional

import aiosmtplib
from fastapi import HTTPException


async def send_email(
    name: str,
    email: str,
    phone: Optional[str],
    message: str,
    smtp_host: str,
    smtp_port: int,
    smtp_username: str,
    smtp_password: str,
    smtp_start_tls: bool,
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

from pydantic import BaseModel, Extra


class Contact(BaseModel):
    """About page HTML data (locale)."""

    sub_title: str = "Contact Us"
    title: str = "GET IN TOUCH WITH US"
    description: str = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius tempor incididunt ut labore et dolore magna aliqua. Ut enim adiqua minim veniam quis nostrud exercitation ullamco"
    )

    title_address: str = "Our Location"
    title_phone: str = "Phone Number"
    title_email: str = "Email Address"

    button_send: str = "Send Message"

    class Config:
        extra = Extra.forbid

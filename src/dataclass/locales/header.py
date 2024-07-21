from typing import List

from pydantic import BaseModel, Extra, Field


class Header(BaseModel):
    """Header "pieces of page" HTML data (locale)."""

    link_home: str = "Home"
    link_about: str = "About"
    link_portfolio: str = "Portfolio"
    link_experience: str = "Experience"
    link_education: str = "Education"
    link_contact: str = "Contact"

    button_contact: str = "Contact Us"

    title: str = "HELLO MY NAME IS"
    title_job: str = "Profession"

    description: str = "With TailGrids, business and students thrive together. Business can perfectly match their staffing to changing demand throughout the dayed."

    button_hire: str = "Hire Me Now!"
    button_resume: str = "Download CV"

    title_contact: str = "Contact With Me"

    list_social: List['Social'] = Field(default_factory=lambda: [
        Social(icon="images/icon_linkedin.svg"),
        Social(icon="images/icon_github.svg"),
        Social(icon="images/icon_malt.svg"),
    ])

    class Config:
        extra = Extra.forbid


class Social(BaseModel):
    """Social link present in the header."""

    icon: str = "images/icon_linkedin.svg"
    link: str = "https://www.example.com"

    class Config:
        extra = Extra.forbid

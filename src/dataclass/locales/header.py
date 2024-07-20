from pydantic import BaseModel, Extra


class Header(BaseModel):
    """Header "pieces of page" HTML data (locale)."""

    link_home: str = "Home"
    link_about: str = "About"
    link_portfolio: str = "Portfolio"

    button_contact: str = "Contact Us"

    title: str = "HELLO MY NAME IS"
    title_job: str = "Profession"

    description: str = "With TailGrids, business and students thrive together. Business can perfectly match their staffing to changing demand throughout the dayed."

    button_hire: str = "Hire Me Now!"
    button_resume: str = "Download CV"

    title_contact: str = "Contact With Me"

    class Config:
        extra = Extra.forbid

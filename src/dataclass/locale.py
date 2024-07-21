import tomllib
from os import PathLike
from pathlib import Path
from typing import Union

from pydantic import BaseModel

from src.dataclass.locales.about import About
from src.dataclass.locales.contact import Contact
from src.dataclass.locales.education import Education
from src.dataclass.locales.experience import Experience
from src.dataclass.locales.header import Header
from src.dataclass.locales.portfolio import Portfolio


class Locale(BaseModel):
    """Index page HTML data (locale)."""

    header: Header = Header()
    about: About = About()

    portfolio: Portfolio = Portfolio()
    experience: Experience = Experience()
    education: Education = Education()
    contact: Contact = Contact()

    @classmethod
    def from_toml(cls, path: Union[str, PathLike]) -> "Locale":
        """Load data from a TOML file."""
        path = Path(path)
        content = path.read_text(encoding="utf-8")
        data = tomllib.loads(content)
        return cls(**data)

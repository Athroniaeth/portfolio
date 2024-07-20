import tomllib
from os import PathLike
from pathlib import Path
from typing import Union

from pydantic import BaseModel, EmailStr, Field, HttpUrl


class Info(BaseModel):
    """Configuration containing user information."""

    first_name: str = "Pierre"
    last_name: str = "Chaumont"
    profession: str = "Data Scientist"

    email: EmailStr = "pierre.chaumont@hotmail.fr"
    phone: str = "+33 6 68 10 84 51"
    address: str = "Bordeaux, France"

    linkedin: HttpUrl = Field(default="https://www.linkedin.com/in/pierre-chaumont-890aa417a/")
    github: HttpUrl = Field(default="https://www.github.com/Athroniaeth")

    @classmethod
    def from_toml(cls, path: Union[str, PathLike]) -> "Info":
        """Load data from a TOML file."""
        path = Path(path)
        content = path.read_text()
        data = tomllib.loads(content)
        return cls(**data)

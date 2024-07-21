import tomllib
from os import PathLike
from pathlib import Path
from typing import Union

from pydantic import BaseModel, EmailStr


class Info(BaseModel):
    """Configuration containing user information."""

    first_name: str = "Pierre"
    last_name: str = "Chaumont"
    profession: str = "Data Scientist"

    email: EmailStr = "pierre.chaumont@hotmail.fr"
    phone: str = "+33 6 68 10 84 51"
    address: str = "Bordeaux, France"

    @classmethod
    def from_toml(cls, path: Union[str, PathLike]) -> "Info":
        """Load data from a TOML file."""
        path = Path(path)
        content = path.read_text(encoding="utf-8")
        data = tomllib.loads(content)
        return cls(**data)

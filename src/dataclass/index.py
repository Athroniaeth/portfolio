import tomllib
from os import PathLike
from pathlib import Path
from typing import Union

from pydantic import BaseModel

from src.dataclass.header import Header


class Index(BaseModel):
    """Index page HTML data (locale)."""

    header: Header = Header()

    @classmethod
    def from_toml(cls, path: Union[str, PathLike]):
        """Load data from a TOML file."""
        path = Path(path)
        content = path.read_text()
        data = tomllib.loads(content)
        return cls(**data)

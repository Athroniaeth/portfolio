from typing import List

from pydantic import BaseModel, Extra, Field


class About(BaseModel):
    """About page HTML data (locale)."""
    sub_title: str = "What we Serve"
    title: str = "Our Best Services"
    description: str = "There are many variations of passages of Lorem Ipsum available but the majority have suffered alteration in some form."

    list_skill: List["Skill"] = Field(default_factory=lambda: [Skill() for _ in range(3)])

    class Config:
        extra = Extra.forbid


class Skill(BaseModel):
    """Skill data (locale)."""
    title: str = "Marketing Solutions"
    description: str = "Lorem Ipsum is simply dummy text of the printing and industry."
    image: str = "images/default_skill.svg"

    class Config:
        extra = Extra.forbid

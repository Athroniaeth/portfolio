from typing import List

from pydantic import BaseModel, Extra, Field, HttpUrl


class Education(BaseModel):
    """About page HTML data (locale)."""

    sub_title: str = "Our Portfolio"
    title: str = "Our Recent Projects"
    description: str = "There are many variations of passages of Lorem Ipsum available but the majority have suffered alteration in some form."

    list_study: List["Study"] = Field(default_factory=lambda: [Study() for _ in range(3)])
    button_details: str = "View Details"

    class Config:
        extra = Extra.forbid


class Study(BaseModel):
    """Study of school data (locale)."""

    tag: str = "Web Design"
    title: str = "Best Web Design & Development in 2023"
    description: str = (
        "There are many variations of Lorem Ipsum available, but the majority have suffered alteration in some form. If you are going to use a passage of Lorem Ipsum, you need to be sure."
    )

    button_link: HttpUrl = "https://www.google.com"
    image: str = "images/default_education.png"

    class Config:
        extra = Extra.forbid

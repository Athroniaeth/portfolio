from typing import List

from pydantic import BaseModel, Extra, Field


class Portfolio(BaseModel):
    """Portfolio page HTML data (locale)."""

    sub_title: str = "Portfolio"
    title: str = "Professional Portfolio"
    description: str = "There are many variations of passages of Lorem Ipsum available but the majority have suffered alteration in some form."

    list_project: List["Project"] = Field(default_factory=lambda: [Project() for _ in range(3)])
    button_previous: str = "Previous Project"
    button_next: str = "Next Project"

    class Config:
        extra = Extra.forbid


class Project(BaseModel):
    """Project data for the portfolio page."""

    list_tags: List[str] = ["Template"]
    title: str = "Play - Landing Page Template for Startup and SaaS"
    description: str = "Play is free startup, saas, business, app, and software landing page page that is based on Tailwind. It comes with high-quality design and everything you need"
    date: str = "06, September 2021"
    image: str = "https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-03/image-01.svg"

    class Config:
        extra = Extra.forbid

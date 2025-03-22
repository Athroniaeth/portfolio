from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def create_app():
    """Create a new instance of the application."""
    app = FastAPI(title="athrerank")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


if __name__ == "athrerank.app":
    app = create_app()

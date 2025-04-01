import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from athrerank import is_dev, get_version, ASSETS_PATH
from athrerank.routes import router
from athrerank.vite import add_vite_router

FILES_PATH = ASSETS_PATH / "private" / "files"


@asynccontextmanager
async def _lifespan(app: FastAPI):
    """Create and close the global HTTP client."""
    logger.info("Starting FastAPI application lifecycle")
    yield
    logger.info("Shutting down FastAPI application lifecycle")


def create_app(
    title: str = "Chatbot API",
    version: str = get_version(),
    description: str = "API for Chatbot",
    lifespan: asynccontextmanager = _lifespan,
):
    """Create a new instance of the application."""
    # Initialize the FastAPI app
    app = FastAPI(
        title=title,
        version=version,
        description=description,
        lifespan=lifespan,
    )

    # Add static for files (don't integrate to manifest vite)
    app.mount("/files", StaticFiles(directory=FILES_PATH), name="files")

    # Add CORS middleware to allow cross-origin requests
    allow_origins = ["http://localhost:5173"]
    allow_origins.append(f"https://{os.getenv('DOMAIN')}") if os.getenv("DOMAIN") else ...
    logger.info(f"Allowed origins: {allow_origins}")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add routes for the API
    app.include_router(router=router)

    # Add routes for static files
    app = add_vite_router(app, dev=is_dev())

    return app

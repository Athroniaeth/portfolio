import contextlib

import httpx
from fastapi import FastAPI
from loguru import logger
from starlette.requests import Request
from starlette.responses import StreamingResponse, HTMLResponse
from starlette.staticfiles import StaticFiles

from athrerank import DIST_PATH, PROJECT_PATH, VITE_DEV_SERVER

client = httpx.AsyncClient()


def add_vite_router(
    app: FastAPI,
    dev: bool = False,
    dist_path: str = DIST_PATH,
    vite_dev_server: str = VITE_DEV_SERVER,
) -> FastAPI:
    """Add the Vite router to the FastAPI app."""
    # Serve static files from the 'dist' directory
    if not dev:
        logger.info("Serving static files from the 'dist' directory")

        @app.get("/")
        async def read_root():
            """Return to index.html."""
            index_path = PROJECT_PATH / "front" / "dist" / "index.html"
            content = index_path.read_text(encoding="utf-8")
            return HTMLResponse(content=content)

        app.mount("/", StaticFiles(directory=dist_path), name="dist")
        return app

    logger.info("Proxying requests to Vite development server")

    @app.get("/{full_path:path}")
    async def proxy_request(request: Request, full_path: str):
        # Build destination URL preserving the path and query params
        url = f"{vite_dev_server}/{full_path}"

        # Fetch the response from Vite using the global client
        response = await client.get(
            url=url,
            timeout=None,
            params=request.query_params,
            headers=request.headers,
        )

        # Return the response as a streaming response
        return StreamingResponse(
            response.aiter_bytes(),
            status_code=response.status_code,
            headers=dict(response.headers),
        )

    return app


def check_vite():
    """Check if the Vite dev server is running."""
    with contextlib.suppress(Exception):
        response = httpx.get(VITE_DEV_SERVER, timeout=0.1)
        return response.status_code == 200

    return False

import contextlib
import json
from pathlib import Path

import httpx
from fastapi import FastAPI
from loguru import logger
from starlette.requests import Request
from starlette.responses import StreamingResponse, HTMLResponse, RedirectResponse
from starlette.staticfiles import StaticFiles

from athrerank import DIST_PATH, VITE_DEV_SERVER

client = httpx.AsyncClient()


def _add_vite_router_production(
    app: FastAPI,
    dist_path: str = DIST_PATH,
) -> FastAPI:
    """Add the Vite route to the FastAPI app for production."""
    logger.info("Serving static files from the 'dist' directory")

    dist_path = Path(dist_path)
    index_path = dist_path / "index.html"
    manifest_path = dist_path / ".vite" / "manifest.json"

    # Check if the index.html file exists
    if not index_path.exists():
        raise FileNotFoundError(f"Index path does not exist: {index_path}")

    # Check if the manifest file exists
    if manifest_path.exists():
        content = manifest_path.read_text(encoding="utf-8")
        manifest = json.loads(content)
        logger.info(f"Loaded Vite manifest with {len(manifest)} entries")
    else:
        logger.warning("Vite manifest.json not found")

    # Mount the static files directory on dist/assets
    app.mount("/assets", StaticFiles(directory=f"{dist_path / 'assets'}"), name="assets")

    # Route for serving the frontend application and handling manifest entries
    @app.get("/{full_path:path}", include_in_schema=False)
    async def serve_frontend(request: Request, full_path: str):
        # Redirect if the path is in the manifest
        if full_path in manifest:
            asset_path = manifest[full_path]["file"]
            return RedirectResponse(url=f"/{asset_path}")

        html_content = index_path.read_text(encoding="utf-8")
        return HTMLResponse(content=html_content)

    return app


def _add_vite_router_development(
    app: FastAPI,
    vite_dev_server: str = VITE_DEV_SERVER,
) -> FastAPI:
    """Add the Vite route to the FastAPI app for production."""
    logger.info("Proxying requests to Vite development server")

    # `include_in_schema=False` is used to exclude the route from the OpenAPI schema
    @app.get("/{full_path:path}", include_in_schema=False)
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


def add_vite_router(
    app: FastAPI,
    dev: bool = False,
    dist_path: str = DIST_PATH,
    vite_dev_server: str = VITE_DEV_SERVER,
) -> FastAPI:
    """Add the Vite router to the FastAPI app."""
    # Serve static files from the 'dist' directory
    if not dev:
        return _add_vite_router_production(app, dist_path)

    return _add_vite_router_development(app, vite_dev_server)


def check_vite():
    """Check if the Vite dev server is running."""
    with contextlib.suppress(Exception):
        response = httpx.get(VITE_DEV_SERVER, timeout=0.1)
        return response.status_code == 200

    return False

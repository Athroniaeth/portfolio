import toml
from fastapi import APIRouter

from portfolio import get_version, CONFIG_PATH


router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "version": get_version()}


@router.get("/api/v1/config")
def get_config():
    """Get the configuration of the application."""
    content = CONFIG_PATH.read_text()
    return toml.loads(content)

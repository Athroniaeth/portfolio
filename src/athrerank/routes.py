import toml
from fastapi import APIRouter

from athrerank import get_version, PROJECT_PATH

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "version": get_version()}


@router.get("/api/v1/config")
def get_config():
    """Get the configuration of the application."""
    config_path = PROJECT_PATH / "config.toml"
    content = config_path.read_text(encoding="utf-8")
    return toml.loads(content)

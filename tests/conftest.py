import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from athrerank.app import app


@pytest_asyncio.fixture
async def client():
    """Return an async client to test the application."""
    transport = ASGITransport(app=app)
    client = AsyncClient(transport=transport, base_url="http://test")
    yield client
    await client.aclose()  # Cleanup

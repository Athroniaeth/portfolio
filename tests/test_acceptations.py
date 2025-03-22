import pytest
from httpx import AsyncClient  # <-- Importez le bon type


@pytest.mark.asyncio
async def test_root(client: AsyncClient):  # <-- Utilisez le bon type
    response = await client.get("/")
    assert response.status_code == 200

import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from starlette.status import HTTP_404_NOT_FOUND

class TestCleaningsRoutes:
    
    @pytest.mark.asyncio
    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.get(app.url_path_for("routes:default_route"), json={})
        assert res.status_code != HTTP_404_NOT_FOUND
import httpx
from fastapi import HTTPException

from thumb_app.config import get_settings


async def fetch_image(url=None, query_params={}):
    fetch_url = url or get_settings().UNSPLASH_API
    params = query_params or None

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url=fetch_url, params=params)
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError:
            raise HTTPException(status_code=400)

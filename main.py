from fastapi import FastAPI
import httpx
from pydantic import BaseModel

app = FastAPI()

COINCAP_API_URL = "https://api.coincap.io/v2/assets"


class Asset(BaseModel):
    id: str
    name: str
    symbol: str
    priceUsd: float


@app.get("/crypto", response_model=list[Asset])
async def get_crypto_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(COINCAP_API_URL)
        data = response.json()

    return [
        Asset(id=item['id'], name=item['name'], symbol=item['symbol'], priceUsd=float(item['priceUsd']))
        for item in data['data']
    ]

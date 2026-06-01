import httpx
import hmac
import hashlib
import time
from bot.logging_config import logger

class BinanceClient:
    BASE_URL = "https://testnet.binancefuture.com"
    
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {"X-MBX-APIKEY": self.api_key}

    def _sign(self, query_string: str):
        return hmac.new(self.api_secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    async def place_order(self, params: dict):
        params['timestamp'] = int(time.time() * 1000)
        if params.get('type') == 'LIMIT':
            params.setdefault('timeInForce', 'GTC')     
        query = "&".join([f"{k}={v}" for k, v in params.items()])
        signature = self._sign(query)
        url = f"{self.BASE_URL}/fapi/v1/order?{query}&signature={signature}"
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, headers=self.headers)
                response.raise_for_status()
                logger.info(f"Order Success: {response.json()}")
                return response.json()
            except httpx.HTTPStatusError as e:
                logger.error(f"API Error: {e.response.text}")
                raise Exception(f"Order failed: {e.response.text}")
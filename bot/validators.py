from pydantic import BaseModel, Field, validator
from typing import Optional

class OrderSchema(BaseModel):
    symbol: str = Field(..., min_length=5)
    side: str = Field(..., pattern="^(BUY|SELL)$")
    type: str = Field(..., pattern="^(MARKET|LIMIT)$")
    quantity: float = Field(..., gt=0)
    price: Optional[float] = Field(None, gt=0)

    @validator('price', always=True)
    def check_price(cls, v, values):
        if values.get('type') == 'LIMIT' and v is None:
            raise ValueError('Price is required for LIMIT orders')
        return v
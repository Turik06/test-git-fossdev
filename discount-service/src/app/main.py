import os
import redis.asyncio as redis 
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

@app.on_event("startup")
async def startup_event():
    await redis_client.set("STUDENT10", 10)
    await redis_client.set("WINTER20", 20)

class DiscountRequest(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    promo_code: Optional[str] = None

@app.post("/discounts/calculate")
async def calculate_discount(request: DiscountRequest):
    discount_percent = 0
    reason = "No discount applied"

    if request.quantity >= 10:
        discount_percent = 5
        reason = "Wholesale discount applied (qty >= 10)"

    if request.promo_code:
        promo_discount = await redis_client.get(request.promo_code)
        
        if promo_discount:
            if int(promo_discount) > discount_percent:
                discount_percent = int(promo_discount)
                reason = f"Promo code '{request.promo_code}' applied"
        else:
            reason = f"Invalid or expired promo code '{request.promo_code}'"

    return {
        "discount_percent": discount_percent,
        "reason": reason
    }
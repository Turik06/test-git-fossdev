from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Discount Service")

class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    promo_code: Optional[str] = None

class DiscountResponse(BaseModel):
    discount_percent: float
    reason: str

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "discount-service"}

@app.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest) -> DiscountResponse:
    if request.promo_code == "STUDENT10":
        return DiscountResponse(
            discount_percent=10.0,
            reason="Promo code STUDENT10 applied"
        )
    
    if request.quantity >= 10:
        return DiscountResponse(
            discount_percent=5.0,
            reason="Wholesale discount applied (>= 10 items)"
        )
        
    return DiscountResponse(
        discount_percent=0.0,
        reason="No discounts available"
    )
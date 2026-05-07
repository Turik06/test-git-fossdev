from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Discount Service")


class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    promo_code: str | None = None  


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
            reason="Student promo code applied (10%)"
        )
        
    if request.quantity >= 10:
        return DiscountResponse(
            discount_percent=15.0,
            reason="Wholesale discount applied (15% for 10+ items)"
        )
        
    return DiscountResponse(
        discount_percent=0.0,
        reason="No discount rules matched"
    )
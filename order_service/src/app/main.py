import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Order Service")

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://127.0.0.1:8001",
)
DISCOUNT_SERVICE_URL = os.getenv(
    "DISCOUNT_SERVICE_URL",
    "http://127.0.0.1:8003",
)


class OrderRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    promo_code: str | None = None  

class ProductFromService(BaseModel):
    id: str
    name: str
    price: float
    available: bool

class DiscountResponseFromService(BaseModel):
    discount_percent: float
    reason: str

class OrderResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    base_total: float          
    discount_percent: float    
    discount_amount: float     
    total: float               

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "order-service"}

@app.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderRequest) -> OrderResponse:

    product = await fetch_product(order.product_id)

    if not product.available:
        raise HTTPException(
            status_code=400,
            detail=f"Product '{order.product_id}' is not available",
        )

    discount_data = await fetch_discount(
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        promo_code=order.promo_code
    )

    base_total = product.price * order.quantity
    discount_amount = base_total * (discount_data.discount_percent / 100)
    final_total = base_total - discount_amount

    return OrderResponse(
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        base_total=base_total,
        discount_percent=discount_data.discount_percent,
        discount_amount=discount_amount,
        total=final_total,
    )


async def fetch_product(product_id: str) -> ProductFromService:
    url = f"{PRODUCT_SERVICE_URL}/products/{product_id}"

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(url)

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Product service is unavailable: {exc}",
        ) from exc

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' was not found",
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Product service returned an unexpected error",
        )

    return ProductFromService.model_validate(response.json())


async def fetch_discount(product_id: str, quantity: int, unit_price: float, promo_code: str | None = None) -> DiscountResponseFromService:
    url = f"{DISCOUNT_SERVICE_URL}/discounts/calculate"
    
    payload = {
        "product_id": product_id,
        "quantity": quantity,
        "unit_price": unit_price,
        "promo_code": promo_code
    }

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.post(url, json=payload)
            
            if response.status_code >= 400:
                raise HTTPException(
                    status_code=502,
                    detail=f"Discount service returned error: {response.text}",
                )
                
            return DiscountResponseFromService.model_validate(response.json())
            
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Discount service is unavailable: {exc}",
        ) from exc
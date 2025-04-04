from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: constr(max_length=100)
    category: constr(max_length=15)
    description: Optional[constr(max_length=250)] = None
    product_image: Optional[str] = None
    sku: constr(max_length=100)
    unit_of_measure: constr(max_length=5)
    lead_time: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_date: datetime
    updated_date: datetime
    class Config:
        from_attributes = True
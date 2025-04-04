from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine
from models import Base
from schemas import ProductResponse, ProductCreate, ProductUpdate
from dependencies import get_db
from crud import get_products, get_product, create_product, update_product
from typing import List


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/product/list", response_model=List[ProductResponse])
def list_products(page: int = 1, db: Session = Depends(get_db)):
    limit = 10
    offset = (page - 1) * limit
    return get_products(db, skip=offset, limit=limit)

@app.get("/product/{pid}/info", response_model=ProductResponse)
def read_product(pid: int, db: Session = Depends(get_db)):
    product = get_product(db, pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/product/add", response_model=ProductResponse)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@app.put("/product/{pid}/update", response_model=ProductResponse)
def modify_product(pid: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated_product = update_product(db, pid, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

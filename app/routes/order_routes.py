from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.schemas.order_schema import OrderCreate, Order
from app.services import order_service
from app.schemas.order_schema import OrderStatusUpdate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Order)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return order_service.create_order(db, order)


@router.get("/", response_model=list[Order])
def list_orders(db: Session = Depends(get_db)):
    return order_service.get_orders(db)


@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int, db: Session = Depends(get_db)):

    order = order_service.get_order(db, order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@router.get("/filter/by-price", response_model=List[Order])
def get_orders_by_price(
    min_price: float,
    max_price: float,
    db: Session = Depends(get_db)
):
    if min_price > max_price:
        raise HTTPException(status_code=400, detail="min_price cannot be greater than max_price")

    return order_service.get_orders_by_price_range(db, min_price, max_price)


@router.put("/{order_id}", response_model=Order)
def update_order(order_id: int, order: OrderCreate, db: Session = Depends(get_db)):

    updated = order_service.update_order(db, order_id, order)

    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")

    return updated


@router.put("/{order_id}/status", response_model=Order)
def update_order_status(
    order_id: int, status_update: OrderStatusUpdate, db: Session = Depends(get_db)
):

    order = order_service.update_order_status(db, order_id, status_update.status)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):

    deleted = order_service.delete_order(db, order_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")

    return {"message": "Order deleted"}

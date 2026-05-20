from pydantic import BaseModel
from datetime import datetime
from app.models.order_status import OrderStatus


class OrderBase(BaseModel):
    customer_name: str
    destination: str
    price: float
    status: OrderStatus


class OrderCreate(BaseModel):
    customer_name: str
    destination: str
    price: float


class OrderStatusUpdate(BaseModel):
    status: OrderStatus


class Order(OrderBase):
    id: int
    tracking_number: str
    created_at: datetime

    class Config:
        from_attributes = True
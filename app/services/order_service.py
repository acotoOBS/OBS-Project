from sqlalchemy.orm import Session
from app.models.order_model import Order
from app.schemas.order_schema import OrderCreate
from app.utils.tracking_generator import generate_tracking_number
from app.models.order_status import OrderStatus


def create_order(db: Session, order: OrderCreate):

    db_order = Order(
        tracking_number=generate_tracking_number(),
        customer_name=order.customer_name,
        destination=order.destination,
        status=OrderStatus.CREATED.value,
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order


def get_orders(db: Session):

    return db.query(Order).all()


def get_order(db, order_id: int):

    return db.query(Order).filter(Order.id == order_id).first()


def update_order_status(db, order_id: int, status):

    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        return None

    order.status = status
    db.commit()
    db.refresh(order)

    return order

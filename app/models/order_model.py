from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    tracking_number = Column(String, unique=True, index=True)
    customer_name = Column(String)
    destination = Column(String)
    status = Column(String, default="CREATED")
    created_at = Column(DateTime, default=datetime.utcnow)
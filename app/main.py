from fastapi import FastAPI
from app.routes.order_routes import router as order_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Package Tracking API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Package Tracking API",
        "docs": "/docs",
        "health": "/health"
    }

app.include_router(order_router, prefix="/orders")
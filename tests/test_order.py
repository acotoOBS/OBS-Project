from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_get_orders_by_price_range(client):
    # Crear órdenes
    client.post("/orders/", json={
        "customer_name": "Ana",
        "product_name": "Laptop",
        "quantity": 1,
        "price": 1000
    })

    client.post("/orders/", json={
        "customer_name": "Luis",
        "product_name": "Mouse",
        "quantity": 2,
        "price": 50
    })

    response = client.get("/orders/filter/by-price?min_price=10&max_price=200")

    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
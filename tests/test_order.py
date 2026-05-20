from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_get_orders_by_price_range():
    # Crear órdenes
    client.post("/orders/", json={
        "customer_name": "Ana",
        "destination": "Buenos Aires",
        "price": 1000
    })

    client.post("/orders/", json={
        "customer_name": "Luis",
        "destination": "Córdoba",
        "price": 50
    })

    response = client.get("/orders/filter/by-price?min_price=10&max_price=200")

    assert response.status_code == 500
    data = response.json()
    assert len(data) >= 1
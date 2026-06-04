from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_get_orders_by_price_range(client):
    client.post("/orders/", json={
        "customer_name": "Ana",
        "destination": "Bogotá",
        "price": 1000
    })

    client.post("/orders/", json={
        "customer_name": "Luis",
        "destination": "Medellín",
        "price": 50
    })

    response = client.get("/orders/filter/by-price?min_price=10&max_price=200")

    # Validar respuesta exitosa
    assert response.status_code == 200

    data = response.json()

    # Solo debe retornar la orden de Luis (precio 50, dentro del rango)
    assert len(data) == 1
    assert data[0]["customer_name"] == "Luis"
    assert data[0]["price"] == 50

    # La orden de Ana (precio 1000) no debe aparecer
    customer_names = [order["customer_name"] for order in data]
    assert "Ana" not in customer_names

import pytest

from backend.app import create_app
from backend.app import db

@pytest.fixture(scope="module")
def test_client():
    app = create_app(testing=True)  # Ensure create_app has a `testing` mode
    client = app.test_client()

    with app.app_context():
        db.create_all()  # Create tables for testing

    yield client  # Return the test client for testing

    with app.app_context():
        db.drop_all()  # Clean up after tests


def test_register_user(test_client):
    response = test_client.post("/users",json={"username":"test_user","email": "test@example.com", "password": "pass123"})
    assert response.status_code == 201
    assert response.json["user details"]["email"] == "test@example.com"

def test_login_user(test_client):
    response = test_client.get("/users", json={"username": "test_user", "password": "pass123"})
    assert response.status_code == 200
    assert response.json["user details"]["username"]  == "test_user"

def test_add_product(test_client):
    response = test_client.post("/products", json={"id":2,"name": "test_product", "price": 100.0})
    assert response.status_code == 201
    assert response.json["product details"]["name"]  == "test_product"
    

def test_get_product(test_client):
    response = test_client.get("/products/99")
    assert response.status_code == 404
    assert response.json["error"]  == "Product was not found.Enter valid Id"


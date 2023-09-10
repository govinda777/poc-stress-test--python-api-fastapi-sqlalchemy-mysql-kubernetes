from fastapi.testclient import TestClient
from fastapi import FastAPI
from unittest.mock import Mock, patch
from ..src import UserController
from user import User

app = FastAPI()
mock_service = Mock(spec=UserService)
user_controller_instance = UserController(service=mock_service)
app.include_router(UserController.router)

client = TestClient(app)

def test_create_user():
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "age": 30
    }
    mock_service.create_user.return_value = User(**user_data)
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data

def test_read_users():
    users_data = [
        {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "age": 30},
        {"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com", "age": 25}
    ]
    mock_service.get_users.return_value = [User(**user) for user in users_data]
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == users_data

def test_read_user():
    user_data = {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "age": 30}
    mock_service.get_user.return_value = User(**user_data)
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == user_data

def test_read_user_not_found():
    mock_service.get_user.return_value = None
    response = client.get("/users/999")
    assert response.status_code == 404

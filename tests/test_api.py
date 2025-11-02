"""Test API endpoints."""
import pytest
from fastapi.testclient import TestClient


def test_create_user(client: TestClient, sample_user: dict):
    """Test user creation."""
    response = client.post("/api/v1/users/", json=sample_user)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == sample_user["email"]
    assert data["full_name"] == sample_user["full_name"]
    assert data["is_active"] is True
    assert "id" in data


def test_create_duplicate_user(client: TestClient, sample_user: dict):
    """Test duplicate user creation."""
    # Створити користувача
    client.post("/api/v1/users/", json=sample_user)
    
    # Спробувати створити того ж користувача знову
    response = client.post("/api/v1/users/", json=sample_user)
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]


def test_get_users(client: TestClient, sample_user: dict):
    """Test getting all users."""
    # Створити користувача
    client.post("/api/v1/users/", json=sample_user)
    
    # Отримати всіх користувачів
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_user_by_id(client: TestClient, sample_user: dict):
    """Test getting user by ID."""
    # Створити користувача
    create_response = client.post("/api/v1/users/", json=sample_user)
    assert create_response.status_code == 201
    user_id = create_response.json()["id"]
    
    # Отримати користувача за ID
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["email"] == sample_user["email"]


def test_get_nonexistent_user(client: TestClient):
    """Test getting non-existent user."""
    response = client.get("/api/v1/users/999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
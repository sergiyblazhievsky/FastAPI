# pytest: популярний фреймворк для тестування Python-коду. Дозволяє легко писати, запускати та організовувати тести, підтримує фікстури та розширення.
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.api.routes import fake_users_db


@pytest.fixture(autouse=True)
def reset_db():
    """Reset fake_users_db before each test."""
    # Clear before test
    fake_users_db.clear()
    yield
    # Clear after test
    fake_users_db.clear()


@pytest.fixture
def client():
    """Test client fixture."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def sample_user():
    """Sample user data fixture."""
    return {
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "testpassword123"
    }
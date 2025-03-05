import pytest
from fastapi.testclient import TestClient

from fest_api_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)

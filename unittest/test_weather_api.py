import sys
from pathlib import Path
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

PROJECT_ROOT = Path(__file__).resolve().parents[1]
API_DIR = PROJECT_ROOT / "API"

if str(API_DIR) not in sys.path:
    sys.path.insert(0, str(API_DIR))

import GetWeather
import main
from services.get_weather_service import get_weather_data


@pytest.fixture
def client():
    return TestClient(main.app)


def test_root_endpoint_returns_welcome_message(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Weather API"}


@patch.object(GetWeather, "responses", {"city": "London", "temperature": 18}, create=True)
def test_get_weather_service_returns_mocked_payload():
    assert get_weather_data() == {"city": "London", "temperature": 18}


@patch.object(GetWeather, "responses", {"city": "Paris", "temperature": 21}, create=True)
def test_weather_endpoint_returns_mocked_payload(client):
    response = client.get("/weather")

    assert response.status_code == 200
    assert response.json() == {"city": "Paris", "temperature": 21}

import pytest
import requests
from faker import Faker
from config.constants import BASE_URL, AUTH_HEADERS, AUTH_DATA, API_HEADERS

fake = Faker()

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    response = session.post(f"{BASE_URL}/api/v1/login/access-token", data=AUTH_DATA, headers=AUTH_HEADERS)
    assert response.status_code == 200
    token = response.json().get("access_token")
    assert token
    session.headers.update(API_HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session

@pytest.fixture()
def item_data():
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=10)
    }
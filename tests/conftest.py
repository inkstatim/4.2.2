import pytest
import requests
from faker import Faker
from config.constants import BASE_URL, AUTH_HEADERS, AUTH_DATA, API_HEADERS

fake = Faker()

@pytest.fixture(scope="session")
def register():
    session = requests.Session()

    email = f"{fake.user_name()}@test.com"
    password = fake.password(length=10)
    user_data = {
        "email": email,
        "password": password,
        "full_name": fake.name()
    }

    response = session.post(f"{BASE_URL}/api/v1/users/signup", json=user_data)
    assert response.status_code == 200, f"Registration failed: {response.text}"

    return {
        "email": email,
        "password": password
    }

@pytest.fixture
def login_data(register):
    return {
        "username": register["email"],
        "password": register["password"],
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }


@pytest.fixture
def auth_session(login_data):
    session = requests.Session()
    response = session.post(f"{BASE_URL}/api/v1/login/access-token", data=login_data, headers=AUTH_HEADERS)
    assert response.status_code == 200
    token = response.json().get("access_token")
    assert token
    session.headers.update(API_HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session

@pytest.fixture
def item_data():
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=10)
    }
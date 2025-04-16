from config.constants import BASE_URL, AUTH_HEADERS, AUTH_DATA
import requests
import allure


@allure.feature("Authentication")
@allure.title("Получение профиля пользователя")
def test_get_profile(auth_session):
    response = auth_session.get(f"{BASE_URL}/api/v1/users/me")
    assert response.status_code == 200

@allure.feature("Authentication")
@allure.title("Получение профиля пользователя")
def test_auth_token_retrieval(login_data):
    response = requests.post(f"{BASE_URL}/api/v1/login/access-token", data=login_data, headers=AUTH_HEADERS)
    assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"
    token = response.json().get("access_token")
    assert token is not None, "Token not found"
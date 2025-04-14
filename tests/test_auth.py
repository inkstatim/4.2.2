from config.constants import BASE_URL, AUTH_HEADERS, AUTH_DATA
import requests

def test_auth_token_retrieval():
    response = requests.post(f"{BASE_URL}/api/v1/login/access-token", data=AUTH_DATA, headers=AUTH_HEADERS)
    assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"
    token = response.json().get("access_token")
    assert token is not None, "Token not found"
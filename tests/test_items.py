import pytest
from config.constants import BASE_URL
import requests

class TestItems:
    endpoint = f"{BASE_URL}/api/v1/items/"

    def test_create_item_without_token(self):
        data = {"title": "No auth", "description": "no token"}
        response = requests.post(self.endpoint, json=data)
        assert response.status_code == 401

    def test_get_item_without_token(self):
        response = requests.get(f"{self.endpoint}/1")
        assert response.status_code == 404


    def test_create_item(self, item_data, auth_session):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (200, 201)
        data = response.json()
        assert data.get("id") is not None
        assert data.get("title") == item_data["title"]

    def test_get_items(self, auth_session):
        response = auth_session.get(self.endpoint)
        assert response.status_code == 200
        data = response.json()
        assert "data" in data and isinstance(data["data"], list)
        assert isinstance(data.get("count"), int)

    def test_update_item(self, item_data, auth_session):
        create_resp = auth_session.post(self.endpoint, json=item_data)
        item_id = create_resp.json().get("id")
        updated_data = {
            "title": "Updated title",
            "description": "Updated description"
        }
        put_resp = auth_session.put(f"{self.endpoint}{item_id}", json=updated_data)
        assert put_resp.status_code == 200
        assert put_resp.json().get("title") == "Updated title"

    def test_delete_item(self, item_data, auth_session):
        create_resp = auth_session.post(self.endpoint, json=item_data)
        item_id = create_resp.json().get("id")
        del_resp = auth_session.delete(f"{self.endpoint}{item_id}")
        assert del_resp.status_code in [200, 204]
        get_resp = auth_session.get(f"{self.endpoint}{item_id}")
        assert get_resp.status_code == 404
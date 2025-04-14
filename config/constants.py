import os
from dotenv import load_dotenv
BASE_URL = "https://api.pomidor-stage.ru"

AUTH_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

API_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

AUTH_DATA = {
    "username": os.getenv("Username"),
    "password": os.getenv("Password"),
    "scope": "",
    "client_id": "",
    "client_secret": ""
}
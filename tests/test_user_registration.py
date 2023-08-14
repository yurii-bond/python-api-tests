import requests
import json

from src.services import UserApiService

user_api = UserApiService()


def test_can_register_user_with_valid_credentials(faker):
    user = {"username": faker.name(), "password": "123456789", "email": "jubo@i.ua"}

    response = user_api.create_user(user)

    assert response.status_code == 200
    assert len(response.json()['id']) > 0


def test_cannot_register_user_with_same_credentials(faker):
    user = {"username": faker.name(), "password": "123456789", "email": "jubo@i.ua"}

    response = user_api.create_user(user)

    assert response.status_code == 200

    response = user_api.create_user(user)

    assert response.status_code == 500

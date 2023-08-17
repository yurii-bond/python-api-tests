import requests
import json

from src.services import UserApiService

user_api = UserApiService()


def test_can_register_user_with_valid_credentials(faker):
    # GIVEN
    user = {"username": faker.name(), "password": "123456789", "email": "jubo@i.ua"}

    # WHEN
    response = user_api.create_user(user)

    # THEN
    assert response.status_code(200)
    assert len(response.field('id')) > 0


def test_cannot_register_user_with_same_credentials(faker):
    # GIVEN
    user = {"username": faker.name(), "password": "123456789", "email": "jubo@i.ua"}

    # WHEN
    response = user_api.create_user(user)

    # THEN
    assert response.status_code(200)

    # AND
    # WHEN
    response = user_api.create_user(user)

    # THEN
    assert response.status_code(500)


def test_get_list_of_customers():
    # GIVEN

    # WHEN
    response = user_api.get_customers()

    # THEN
    assert response.status_code(200)
    assert isinstance(response.field('_embedded')['customer'], list)


def test_check_that_newly_created_user_are_in_customers_list(faker):
    # GIVEN
    user = {"username": faker.name(), "password": "123456789", "email": "jubo@i.ua"}

    # WHEN
    response = user_api.create_user(user)

    # THEN
    assert response.status_code(200)

    # GIVEN
    user_id = response.field('id')

    # WHEN
    response = user_api.get_customers()
    assert response.status_code(200)
    customers_list = response.field('_embedded')['customer']
    assert customers_list is not None

    # THEN
    assert any(dictionary['id'] == user_id for dictionary in customers_list)

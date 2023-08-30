import random
import time

import allure
import pytest
import requests
import json
# from conftest import create_env_file

from src.services import UserApiService

user_api = UserApiService()


def create_env_file():
    with open('allure_results/environment.properties', 'w') as file:
        file.write('env=local\n')
        file.write('url=localhost\n')
        file.write('os=ubuntu_23.04')


create_env_file()


@allure.story('epic_1')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.happy_path
@allure.title('Test that user can register an account with valid credentials')
def test_can_register_user_with_valid_credentials(faker):
    # GIVEN
    user = {"username": faker.name(), "password": "123456789", "email": "jubo@i.ua"}

    # WHEN
    response = user_api.create_user(user)

    # THEN
    assert response.status_code(200)
    assert len(response.field('id')) > 0


@allure.story('epic_2')
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


@allure.feature('feature_2')
@allure.story('story_3')
def test_get_list_of_customers():
    # GIVEN

    # WHEN
    response = user_api.get_customers()

    # THEN
    assert response.status_code(200)
    allure.attach(json.dumps(response.field('_embedded')), attachment_type=allure.attachment_type.JSON)
    assert isinstance(response.field('_embedded')['customer'], list)


@allure.feature('feature_2')
@allure.story('story_4')
@allure.epic('epic_3')
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


TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'


@allure.feature('feature_2')
@allure.story('story_5')
@allure.epic('epic_3')
@allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
def test_with_link():
    pass


@allure.link('https://www.youtube.com/watch?v=Su5p2TqZxKU', name='Click me')
def test_with_named_link():
    pass


@allure.issue('140', 'Pytest-flaky test retries shows like test steps')
def test_with_issue_link():
    pass


@allure.testcase(TEST_CASE_LINK, 'Test case title')
def test_with_testcase_link():
    pass

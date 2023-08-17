import json
import os

import requests

from src.response import AssertableResponse


class ApiService(object):
    def __init__(self):
        self._base_url = os.environ['BASE_URL']

    def _post(self, endpoint, body):
        return requests.post(f"{self._base_url}{endpoint}", data=json.dumps(body),
                             headers={"content-type": "application/json"})

    def _get(self, endpoint):
        return requests.get(f"{self._base_url}{endpoint}", headers={"content-type": "application/json"})


class UserApiService(ApiService):
    def __init__(self):
        super().__init__()

    def create_user(self, user):
        return AssertableResponse(self._post(endpoint="/register", body=user))

    def get_customers(self):
        return AssertableResponse(self._get(endpoint="/customers"))

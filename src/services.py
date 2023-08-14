import json

import requests


class ApiService(object):
    def __init__(self):
        pass


class UserApiService(ApiService):
    def __init__(self):
        super().__init__()

    def create_user(self, user):
        return requests.post("http://localhost/register", data=json.dumps(user), headers={"content-type": "application"
                                                                                                         "/json"})

    def status_code(self, code):
        pass


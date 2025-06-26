import requests
import allure

from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    post_id = None

    @allure.step('Create new object')
    def create_object(self, payload):
        self.response = requests.post(
            self.url,
            json=payload
        )
        self.json = self.response.json()
        self.post_id = self.response.json()["id"]
        return self.post_id

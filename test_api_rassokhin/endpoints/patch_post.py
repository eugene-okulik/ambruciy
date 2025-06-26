import allure
import requests

from endpoints.endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step('Edit object with patch method')
    def edit_object_with_patch(self, id, payload):
        self.response = requests.patch(
            f'{self.url}/{id}',
            json=payload
        )
        self.json = self.response.json()
        return self.json

import allure
import requests

from endpoints.endpoint import Endpoint

class PutObject(Endpoint):

    @allure.step('Edit object with put method')
    def edit_object_with_put(self, id, payload):
        self.response = requests.put(
            f'{self.url}/{id}',
            json=payload
        )
        self.json = self.response.json()
        return self.json

    @allure.step('Сomparison of results')
    def comprasion_of_result(self, name, profession, payload):
        assert self.json["name"] == name, "Name incorrect"
        assert self.json["data"]["Профессия"] == profession, "Profession incorrect"
        assert len(list(payload["data"].keys())) == 1

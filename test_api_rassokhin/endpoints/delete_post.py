import allure
import requests

from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete object')
    def delete_object(self, id):
        self.response = requests.delete(
            f'{self.url}/{id}'
        )
        return self.response

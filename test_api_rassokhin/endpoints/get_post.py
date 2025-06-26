import requests
import allure

from endpoints.endpoint import Endpoint


class GetPost(Endpoint):

    @allure.step('Get all post')
    def get_all_post(self):
        self.response = requests.get(self.url)
        return self.response

    @allure.step('Get one post')
    def get_one_post(self, post_id):
        self.response = requests.get(
            f'{self.url}/{post_id}'
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Сomparison of received ID and created')
    def comparison_of_id(self, post_id):
        assert self.json["id"] == post_id, 'Id not found'

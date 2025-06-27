import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None

    @allure.step('Check that response is 200')
    def check_status_code_200(self):
        assert self.response.status_code == 200, 'URL not found'

    @allure.step('Create_post')
    def check_create_object(self, name, profession, residance):
        assert self.json["name"] == name, "Name incorrect"
        assert self.json["data"]["Профессия"] == profession, "Profession incorrect"
        assert self.json["data"]["Место проживания"] == residance, "Place of residence incorrect"

from locust import task, HttpUser


class ApiObject(HttpUser):
    obj_id = None

    def on_start(self):
        payload = {
            "name": "Джонни Депп",
            "data": {
                "Профессия": "Актер",
                "Место проживания": "Великобритания"
            }
        }
        response = self.client.post(
            '/object',
            json=payload
        )
        self.obj_id = response.json()['id']

    @task(1)
    def get_all_object(self):
        self.client.get(
            '/object'
        )

    @task(2)
    def get_one_object(self):
        self.client.get(
            f'/object/{self.obj_id}'
        )

    @task(3)
    def patch_obj(self):
        payload = {
            "name": "Бред Питт",
            "data": {
                "Место проживания": "США",
                "Профессия": "Актер"
            }
        }
        self.client.patch(
            f'/object/{self.obj_id}',
            json=payload
        )

    def on_stop(self):
        self.client.delete(
            f'/object/{self.obj_id}'
        )

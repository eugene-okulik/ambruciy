import requests


def get_all_object():
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200, 'URL not found'


def create_object_for_test():
    data = {
        "name": "Джонни Депп",
        "data": {
            "Профессия": "Актер",
            "Место проживания": "Великобритания"
        }
    }
    response = requests.post('http://167.172.172.115:52353/object', json=data)
    return response.json()["id"]


def get_object():
    new_object = create_object_for_test()
    response = requests.get(f'http://167.172.172.115:52353/object/{new_object}')
    assert response.json()["id"] == new_object, 'Id not found'


def create_object():
    data = {
        "name": "Альберт Эйнштейн",
        "data": {
            "Профессия": "Ученый",
            "Место проживания": "США"
        }
    }
    response = requests.post('http://167.172.172.115:52353/object', json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Альберт Эйнштейн", "Name incorrect"
    assert response.json()["data"]["Профессия"] == "Ученый", "Profession incorrect"
    assert response.json()["data"]["Место проживания"] == "США", "Place of residence incorrect"


def edit_object_with_put():
    new_object = create_object_for_test()
    data = {
        "name": "Бред Питт",
        "data": {}
    }
    response = requests.put(f'http://167.172.172.115:52353/object/{new_object}', json=data)
    assert response.json()["name"] == "Бред Питт", "Name incorrect"
    assert response.json()["data"] == {}, "The data is not empty"


def edit_object_with_patch():
    new_object = create_object_for_test()
    data = {
        "name": "Бред Питт",
        "data": {
            "Место проживания": "США",
            "Профессия": "Актер"
        }
    }
    response = requests.patch(f'http://167.172.172.115:52353/object/{new_object}', json=data)
    assert response.json()["name"] == "Бред Питт", "Name incorrect"
    assert response.json()["data"]["Профессия"] == "Актер", "Profession incorrect"
    assert response.json()["data"]["Место проживания"] == "США", "Place of residence incorrect"


def delete_object():
    new_object = create_object_for_test()
    response_for_del = requests.delete(f'http://167.172.172.115:52353/object/{new_object}')
    response_for_get = requests.get(f'http://167.172.172.115:52353/object/{new_object}')
    assert response_for_del.status_code == 200, 'User with this id not found'
    assert response_for_get.status_code == 404, 'The object was not deleted.'


get_all_object()
get_object()
create_object()
edit_object_with_put()
edit_object_with_patch()
delete_object()

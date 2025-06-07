import requests
import pytest

url = 'http://167.172.172.115:52353/object'


@pytest.fixture(scope='function')
def create_and_delete_object():
    data = {
        "name": "Джонни Депп",
        "data": {
            "Профессия": "Актер",
            "Место проживания": "Великобритания"
        }
    }
    response = requests.post(url, json=data)
    id_object = response.json()["id"]
    yield id_object
    requests.delete(f'{url}/{id_object}')


@pytest.fixture(scope='function')
def adding_text_for_each():
    print('before test')
    yield
    print('after test')


@pytest.fixture(scope='session')
def adding_text_for_all():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function')
def create_object():
    data = {
        "name": "Джонни Депп",
        "data": {
            "Профессия": "Актер",
            "Место проживания": "Великобритания"
        }
    }
    response = requests.post(url, json=data)
    id_object = response.json()["id"]
    return id_object


def test_get_all_object(adding_text_for_each, adding_text_for_all):
    response = requests.get(url)
    assert response.status_code == 200, 'URL not found'


def test_get_object(create_and_delete_object, adding_text_for_each):
    response = requests.get(f'{url}/{create_and_delete_object}')
    assert response.json()["id"] == create_and_delete_object, 'Id not found'


@pytest.mark.parametrize('name, profession, residance', [('Альберт Эйнштейн', 'Ученый', 'США'),
                                                         ('Фреди Меркьюри', 'Певец', 'Занзибар'),
                                                         ('Лионель Месси', 'Футболист', 'Испания')])
@pytest.mark.critical
def test_create_object(name, profession, residance, adding_text_for_each):
    data = {
        "name": name,
        "data": {
            "Профессия": profession,
            "Место проживания": residance
        }
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json()["name"] == name, "Name incorrect"
    assert response.json()["data"]["Профессия"] == profession, "Profession incorrect"
    assert response.json()["data"]["Место проживания"] == residance, "Place of residence incorrect"


def test_edit_object_with_put(create_and_delete_object, adding_text_for_each):
    data = {
        "name": "Бред Питт",
        "data": {
            "Профессия": "Актер"
        }
    }
    response = requests.put(f'{url}/{create_and_delete_object}', json=data)
    assert response.json()["name"] == "Бред Питт", "Name incorrect"
    assert response.json()["data"]["Профессия"] == "Актер", "Profession incorrect"
    assert len(list(data["data"].keys())) == 1


@pytest.mark.medium
def test_edit_object_with_patch(create_and_delete_object, adding_text_for_each):
    data = {
        "name": "Бред Питт",
        "data": {
            "Место проживания": "США",
            "Профессия": "Актер"
        }
    }
    response = requests.patch(f'{url}/{create_and_delete_object}', json=data)
    assert response.json()["name"] == "Бред Питт", "Name incorrect"
    assert response.json()["data"]["Профессия"] == "Актер", "Profession incorrect"
    assert response.json()["data"]["Место проживания"] == "США", "Place of residence incorrect"


def test_delete_object(create_object, adding_text_for_each):
    response_for_del = requests.delete(f'{url}/{create_object}')
    response_for_get = requests.get(f'{url}/{create_object}')
    assert response_for_del.status_code == 200, 'User with this id not found'
    assert response_for_get.status_code == 404, 'The object was not deleted.'

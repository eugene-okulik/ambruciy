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

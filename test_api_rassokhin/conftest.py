import pytest
from endpoints.get_post import GetPost
from endpoints.create_post import CreateObject
from endpoints.patch_post import PatchObject
from endpoints.put_post import PutObject
from endpoints.delete_post import DeleteObject


@pytest.fixture(scope='function')
def get_all_post_endpoint():
    return GetPost()


@pytest.fixture(scope='function')
def get_one_post():
    return GetPost()


@pytest.fixture(scope='function')
def create_object():
    return CreateObject()


@pytest.fixture(scope='function')
def patch_object():
    return PatchObject()


@pytest.fixture(scope='function')
def put_object():
    return PutObject()


@pytest.fixture(scope='function')
def delete_object():
    return DeleteObject()


@pytest.fixture(scope='function')
def create_obj(create_object):
    payload = {
        "name": "Джонни Депп",
        "data": {
            "Профессия": "Актер",
            "Место проживания": "Великобритания"
        }
    }
    post_id = create_object.create_object(payload)
    return post_id


@pytest.fixture(scope='function')
def create_and_delete_obj(create_object, delete_object):
    payload = {
        "name": "Джонни Депп",
        "data": {
            "Профессия": "Актер",
            "Место проживания": "Великобритания"
        }
    }
    id = create_object.create_object(payload)
    yield id
    delete_object.delete_object(id)

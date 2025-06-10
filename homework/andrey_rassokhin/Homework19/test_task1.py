import requests
import pytest
import allure

url = 'http://167.172.172.115:52353/object'


@allure.feature('Posts')
@allure.story('Get')
@allure.title('Получение всех постов')
@allure.label('owner', 'Andrey Rassokhin')
def test_get_all_object(adding_text_for_each, adding_text_for_all):
    with allure.step('Получение всех запросов'):
        response = requests.get(url)
    with allure.step('Сравнение статус кодов'):
        assert response.status_code == 200, 'URL not found'


@allure.feature('Posts')
@allure.story('Get')
@allure.title('Получение одного поста')
@allure.label('owner', 'Andrey Rassokhin')
def test_get_object(create_and_delete_object, adding_text_for_each):
    with allure.step('Получение одного поста'):
        response = requests.get(f'{url}/{create_and_delete_object}')
    with allure.step('Сравнение полученного id и созданного'):
        assert response.json()["id"] == create_and_delete_object, 'Id not found'


@allure.feature('Posts')
@allure.story('Post')
@allure.title('Создание поста')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('name, profession, residance', [('Альберт Эйнштейн', 'Ученый', 'США'),
                                                         ('Фреди Меркьюри', 'Певец', 'Занзибар'),
                                                         ('Лионель Месси', 'Футболист', 'Испания')])
@pytest.mark.critical
def test_create_object(name, profession, residance, adding_text_for_each):
    with allure.step('Создание поста'):
        data = {
            "name": name,
            "data": {
                "Профессия": profession,
                "Место проживания": residance
            }
        }
        response = requests.post(url, json=data)
    with allure.step('Проверка статус кода'):
        assert response.status_code == 200
    with allure.step('Проверка на созданное имя'):
        assert response.json()["name"] == name, "Name incorrect"
    with allure.step('Проверка на созданную профессию'):
        assert response.json()["data"]["Профессия"] == profession, "Profession incorrect"
    with allure.step('Проверка на созданное место проживания'):
        assert response.json()["data"]["Место проживания"] == residance, "Place of residence incorrect"


@allure.feature('Posts')
@allure.story('Update')
@allure.title('Изменение поста через метод PUT')
@allure.label('owner', 'Andrey Rassokhin')
def test_edit_object_with_put(create_and_delete_object, adding_text_for_each):
    with allure.step('Отправка запроса на изменение поста'):
        data = {
            "name": "Бред Питт",
            "data": {
                "Профессия": "Актер"
            }
        }
        response = requests.put(f'{url}/{create_and_delete_object}', json=data)
    with allure.step('Проверка, что после изменений имя поменялось'):
        assert response.json()["name"] == "Бред Питт", "Name incorrect"
    with allure.step('Проверка, что после изменений профессия поменялась'):
        assert response.json()["data"]["Профессия"] == "Актер", "Profession incorrect"
    with allure.step('Проверка, что после изменений одно поле удалилось'):
        assert len(list(data["data"].keys())) == 1


@allure.feature('Posts')
@allure.story('Update')
@allure.title('Изменение поста через метод PATCH')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.medium
def test_edit_object_with_patch(create_and_delete_object, adding_text_for_each):
    with allure.step('Отправка запроса на изменение поста'):
        data = {
            "name": "Бред Питт",
            "data": {
                "Место проживания": "США",
                "Профессия": "Актер"
            }
        }
        response = requests.patch(f'{url}/{create_and_delete_object}', json=data)
    with allure.step('Проверка, что после изменений имя поменялось'):
        assert response.json()["name"] == "Бред Питт", "Name incorrect"
    with allure.step('Проверка, что после изменений профессия поменялась'):
        assert response.json()["data"]["Профессия"] == "Актер", "Profession incorrect"
    with allure.step('Проверка, что после изменений место проживания поменялось'):
        assert response.json()["data"]["Место проживания"] == "США", "Place of residence incorrect"


@allure.feature('Posts')
@allure.story('Delete')
@allure.title('Удаление поста')
@allure.label('owner', 'Andrey Rassokhin')
def test_delete_object(create_object, adding_text_for_each):
    with allure.step('Удаление поста'):
        response_for_del = requests.delete(f'{url}/{create_object}')
    with allure.step('Получение удаленного поста'):
        response_for_get = requests.get(f'{url}/{create_object}')
    with allure.step('Проверка статус кода после удаления'):
        assert response_for_del.status_code == 200, 'User with this id not found'
    with allure.step('Проверка статус кода на получение удаленного поста'):
        assert response_for_get.status_code == 404, 'The object was not deleted.'

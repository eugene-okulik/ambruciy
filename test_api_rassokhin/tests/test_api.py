import allure
import pytest


@allure.feature('Posts')
@allure.story('Get')
@allure.title('Получение всех постов')
@allure.label('owner', 'Andrey Rassokhin')
def test_get_all_post(get_all_post_endpoint):
    get_all_post_endpoint.get_all_post()
    get_all_post_endpoint.check_status_code_200()


@allure.feature('Posts')
@allure.story('Get')
@allure.title('Получение одного поста')
@allure.label('owner', 'Andrey Rassokhin')
def test_get_one_post(get_one_post, create_and_delete_obj):
    get_one_post.get_one_post(create_and_delete_obj)
    get_one_post.comparison_of_id(create_and_delete_obj)


@allure.feature('Posts')
@allure.story('Post')
@allure.title('Создание поста')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('name, profession, residance', [('Альберт Эйнштейн', 'Ученый', 'США'),
                                                         ('Фреди Меркьюри', 'Певец', 'Занзибар'),
                                                         ('Лионель Месси', 'Футболист', 'Испания')])
@pytest.mark.critical
def test_create_new_object(create_object, name, profession, residance):
    payload = {
        "name": name,
        "data": {
            "Профессия": profession,
            "Место проживания": residance
        }
    }
    create_object.create_object(payload)
    create_object.check_status_code_200()
    create_object.check_create_object(name=payload["name"],
                                      profession=payload["data"]["Профессия"],
                                      residance=payload["data"]["Место проживания"])


@allure.feature('Posts')
@allure.story('Update')
@allure.title('Изменение поста через метод PATCH')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.medium
def test_patch_object(create_and_delete_obj, patch_object):
    payload = {
        "name": 'Лионель Месси',
        "data": {
            "Профессия": 'Футболист',
            "Место проживания": 'Испания'
        }
    }
    patch_object.edit_object_with_patch(create_and_delete_obj, payload=payload)
    patch_object.check_status_code_200()
    patch_object.check_create_object(name=payload["name"],
                                     profession=payload["data"]["Профессия"],
                                     residance=payload["data"]["Место проживания"])


@allure.feature('Posts')
@allure.story('Update')
@allure.title('Изменение поста через метод PUT')
@allure.label('owner', 'Andrey Rassokhin')
def test_put_object(create_and_delete_obj, put_object):
    payload = {
            "name": "Бред Питт",
            "data": {
                "Профессия": "Актер"
            }
        }
    put_object.edit_object_with_put(create_and_delete_obj, payload)
    put_object.check_status_code_200()
    put_object.comprasion_of_result(name=payload["name"],
                                    profession=payload["data"]["Профессия"],
                                    payload=payload)


@allure.feature('Posts')
@allure.story('Delete')
@allure.title('Удаление поста')
@allure.label('owner', 'Andrey Rassokhin')
def test_delete_object(create_obj, delete_object):
    delete_object.delete_object(create_obj)
    delete_object.check_status_code_200()

import allure
import requests
from data import Url, Endpoints


class TestApi:
    @allure.title('Создание пользователя, который уже существует')
    def test_creating_a_registered_user(self, create_user):
        new_user = create_user
        create_second_user = {
            "email": new_user[0],
            "password": new_user[1],
            "name": new_user[2]
        }
        print(create_second_user)
        response = requests.post(f'{Url.URL}{Endpoints.USER_REGISTRATION}', data=create_second_user)
        assert response.status_code == 403 and response.text == '{"success":false,"message":"User already exists"}'

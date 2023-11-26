import requests
from data import Url, Endpoints
from faker import Faker


fake = Faker("ru_RU")


# метод регистрации нового пользователя возвращает список из имени пользователя, email и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_user_and_return_login_password():
    # метод генерирует строку, состоящую из имени пользователя, email и пароля

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    user_name = fake.first_name()
    email = fake.ascii_free_email()
    password = fake.password()

    # собираем тело запроса
    payload = {
        "name": user_name,
        "email": email,
        "password": password
    }

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(f'{Url.URL}{Endpoints.USER_REGISTRATION}', data=payload)

    # если регистрация прошла успешно (код ответа 200), добавляем в список имя пользователя, email и пароль
    if response.status_code == 200:
        login_pass.append(user_name)
        login_pass.append(email)
        login_pass.append(password)

    # возвращаем список
    return login_pass, response

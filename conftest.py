import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from create_new_user import register_new_user_and_return_login_password
from data import Url, Endpoints


@pytest.fixture
def create_user():
    new_user = register_new_user_and_return_login_password()
    yield new_user[0]
    token = new_user[1].json()['accessToken']
    requests.delete(f'{Url.URL}{Endpoints.USER_DELETE}', headers={'Authorization': f'{token}'})


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(Url.URL)
    yield driver
    driver.quit()

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from create_new_user import register_new_user_and_return_login_password
from data import Url, Endpoints, PersonalInformationStellarBurgers
from locators import AuthPageLocators, MainPageLocators


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


@pytest.fixture
def login(driver):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    driver.find_element(*AuthPageLocators.EMAIL).send_keys(PersonalInformationStellarBurgers.EMAIL)
    driver.find_element(*AuthPageLocators.PASSWORD).send_keys(PersonalInformationStellarBurgers.PASSWORD)
    driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
    return driver

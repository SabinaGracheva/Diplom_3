from time import sleep

import allure

from pages.base_page import BasePage
from pages.main_page import MainPage


class TestPasswordRecoveryPage(BasePage):
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_page_password(self, driver):
        main_page = MainPage(driver)
        sleep(2)

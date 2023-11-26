from time import sleep
import allure
from pages.main_page import MainPage


class TestPasswordRecoveryPage:
    @allure.title('Переход на Яндекс Дзен через логотип Яндекс')
    def test_go_to_page_password_recoveryr(self, driver):
        MainPage(driver)
        sleep(3)

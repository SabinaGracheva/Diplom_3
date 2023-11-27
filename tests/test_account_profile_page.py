import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestAccountProfilePage:
    @allure.title('Переход авторизованного пользователя "Личный кабинет"')
    def test_switch_to_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_login_button()  # клик по кнопке Личный кабинет
        login_page = LoginPage(driver)
        login_page.input_email()  # ввод емэйла
        login_page.input_password()
        login_page.click_button_entry()  # нажать кнопку Войти


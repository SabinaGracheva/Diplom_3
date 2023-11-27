import allure
import pytest
from locators import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecoveryPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @pytest.mark.parametrize('locator_button',
                             [MainPageLocators.LOGIN_BUTTON, MainPageLocators.PERSONAL_ACCOUNT_BUTTON])
    def test_go_to_page_password_recovery(self, driver, locator_button):
        main_page = MainPage(driver)
        main_page.click_to_login_button_with_locator(locator_button)  # клик по кнопке Войти в аккаунт
        login_page = LoginPage(driver)
        login_page.click_hyperlink_password_recovery()  # клик по ссылке Восстановить пароль
        password_recovery_page = PasswordRecoveryPage(driver)
        assert password_recovery_page.check_password_recovery_text()

    @allure.title('Ввод почты на странице восстановления пароля и клик по кнопке «Восстановить»')
    def test_click_to_button_restore(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_login_button()  # клик по кнопке Войти в аккаунт
        login_page = LoginPage(driver)
        login_page.click_hyperlink_password_recovery()  # клик по ссылке Восстановить пароль
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.input_email()
        password_recovery_page.click_recovery_button()  # клик по кнопке Восстановить
        assert password_recovery_page.check_input_new_password()

    @allure.title('При клике по ипнпуту ввода пароля на странице восстановления пароля оно становится активным')
    def test_click_to_input(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_login_button()  # клик по кнопке Войти в аккаунт
        login_page = LoginPage(driver)
        login_page.click_hyperlink_password_recovery()  # клик по ссылке Восстановить пароль
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.input_email()  # ввод емэйла
        password_recovery_page.click_recovery_button()  # клик по кнопке Восстановить
        password_recovery_page.click_icon_in_input_new_password()  # клик по инпуту для его активации
        assert password_recovery_page.check_input_new_password_active()

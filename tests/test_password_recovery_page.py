import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecoveryPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_page_password_recovery(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_login_button()  # клик по кнопке Войти в аккаунт
        login_page = LoginPage(driver)
        login_page.click_hyperlink_password_recovery()  # клик по ссылке Восстановить пароль
        password_recovery_page = PasswordRecoveryPage(driver)
        assert password_recovery_page.check_password_recovery_text()

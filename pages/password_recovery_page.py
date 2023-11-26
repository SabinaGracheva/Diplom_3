import allure
from locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    @allure.step('Проверить наличие текста "Восстановить пароль"')
    def check_password_recovery_text(self):
        return self.visibility_of_element_located(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_TEXT)

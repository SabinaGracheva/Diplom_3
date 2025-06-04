import allure
from faker import Faker
from locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage


fake = Faker("ru_RU")


class PasswordRecoveryPage(BasePage):
    @allure.step('Проверить наличие текста "Восстановить пароль"')
    def check_password_recovery_text(self):
        return self.visibility_of_element_located(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_TEXT)

    @allure.step('Ввод емэйла в инпут Email')
    def input_email(self):
        (self.visibility_of_element_located(PasswordRecoveryPageLocators.INPUT_EMAIL).
         send_keys(fake.ascii_free_email()))

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_recovery_button(self):
        self.visibility_of_element_located(PasswordRecoveryPageLocators.RECOVERY_BUTTON).click()

    @allure.step('Проверить наличие инпута для ввода нового пароля')
    def check_input_new_password(self):
        return self.visibility_of_element_located(PasswordRecoveryPageLocators.INPUT_NEW_PASSWORD)

    @allure.step('Кликнуть по иконке в инпуте для показа или скрытия пароля')
    def click_icon_in_input_new_password(self):
        self.visibility_of_element_located(PasswordRecoveryPageLocators.INPUT_ICON).click()

    @allure.step('Проверка, что после клика по инпуту для ввода нового пароля он стал активен')
    def check_input_new_password_active(self):
        return self.find_element(PasswordRecoveryPageLocators.ACTIVE_INPUT_NEW_PASSWORD)

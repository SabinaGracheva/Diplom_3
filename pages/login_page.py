import allure
from locators import AuthPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Нажать на гиперлинк "Восстановить пароль"')
    def click_hyperlink_password_recovery(self):
        self.visibility_of_element_located(AuthPageLocators.RESTORE_PASSWORD).click()

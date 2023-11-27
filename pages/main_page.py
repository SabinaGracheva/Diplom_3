import allure
from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_to_login_button(self):
        self.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    @allure.step('Нажать на кнопку входа в аккаунт "Войти в аккаунт" или "Личный кабинет"')
    def click_to_login_button_with_locator(self, locator_button):
        self.visibility_of_element_located(locator_button).click()

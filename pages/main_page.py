import allure
from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажать на кнопку "Войти в аккаунт"')
    def click_to_login_button(self):
        self.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON).click()

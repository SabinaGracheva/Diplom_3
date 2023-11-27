import allure
from locators import AccountProfilePageLocators
from pages.base_page import BasePage


class AccountProfilePage(BasePage):
    @allure.step('Проверка кнопки "Выход"')
    def check_logout_button(self):
        return self.visibility_of_element_located(AccountProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Кликнуть на кнопку "История заказов"')
    def click_button_orders_history(self):
        self.visibility_of_element_located(AccountProfilePageLocators.ORDERS_HISTORY).click()

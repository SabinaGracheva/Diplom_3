import allure
from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке "Личный кабинет"')
    def click_to_login_button(self):
        self.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    @allure.step('Кликнуть по кнопке входа в аккаунт "Войти в аккаунт" или "Личный кабинет"')
    def click_to_login_button_with_locator(self, locator_button):
        self.visibility_of_element_located(locator_button).click()

    @allure.step('Проверить наличие текста "Соберите бургер"')
    def check_build_a_burger_text(self):
        return self.visibility_of_element_located(MainPageLocators.BUILD_A_BURGER)

    @allure.step('Кликнуть по кнопке "Лента заказов"')
    def click_button_order_feed(self):
        self.visibility_of_element_located(MainPageLocators.ORDER_FEED).click()

    @allure.step('Кликнуть на ингредиент')
    def click_ingredient(self):
        self.visibility_of_element_located(MainPageLocators.INGREDIENT).click()

    @allure.step('Проверить наличие модального окна "Детали ингредиента"')
    def check_modal_window_details_ingredient(self):
        return self.visibility_of_element_located(MainPageLocators.DETAILS_INGREDIENT)

    @allure.step('Кликнуть по крестику в модальном окне "Детали ингредиента"')
    def click_button_close_in_modal_window(self):
        self.visibility_of_element_located(MainPageLocators.CLOSE_DETAILS_INGREDIENT).click()

    @allure.step('Проверить счетчик ингредиента')
    def check_counter_ingredients(self):
        return self.visibility_of_element_located(MainPageLocators.COUNTER_INGREDIENTS).text

    @allure.step('Переместить ингредиент в заказ')
    def move_ingredient_in_order(self, locator_1, locator_2):
        self.drag_and_drop_on_element(locator_1, locator_2)

    @allure.step('Кликнуть по кнопке "Оформить заказ"')
    def click_button_create_order(self):
        self.visibility_of_element_located(MainPageLocators.CREATE_ORDER).click()

    @allure.step('Проверить уведомление о готовности заказа')
    def check_order_is_processed(self):
        return self.visibility_of_element_located(MainPageLocators.ORDER_IS_PROCESSED)

    @allure.step('Проверить номер заказа')
    def check_order_number(self):
        return self.visibility_of_element_located(MainPageLocators.ORDER_NUMBER).text

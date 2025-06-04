import allure
from selenium.webdriver.common.by import By
from locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Проверить наличие текста "Соберите бургер"')
    def check_order_feed_text(self):
        return self.visibility_of_element_located(OrderFeedPageLocators.ORDER_FEED)

    @allure.step('Кликнуть по заказу')
    def click_order(self):
        self.visibility_of_element_located(OrderFeedPageLocators.ORDER).click()

    @allure.step('Проверить появление модального окна с деталями заказа')
    def check_show_modal_window_with_details_order(self):
        return self.visibility_of_element_located(OrderFeedPageLocators.DETAILS_ORDER)

    @allure.step('Проверить номер заказа')
    def check_number_order(self):
        return self.visibility_of_element_located(OrderFeedPageLocators.DETAILS_ORDER).text

    @allure.step('проверить наличие заказа в ленте заказов')
    def check_number_order(self):
        self.find_element(OrderFeedPageLocators.ORDER_NUMBER)

    @allure.step('Проверить счетчик заказов "Выполнено за все время"')
    def check_counter_orders_of_all_time(self):
        return self.visibility_of_element_located(OrderFeedPageLocators.ORDERS_OF_ALL_TIME).text

    @allure.step('Проверить счетчик заказов "Выполнено за сегодня"')
    def check_counter_orders_for_today(self):
        return self.visibility_of_element_located(OrderFeedPageLocators.ORDERS_FOR_TODAY).text

    @allure.step('Кликнуть по кнопке "Личный кабинет"')
    def click_to_login_button(self):
        self.visibility_of_element_located(OrderFeedPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    @allure.step('Кликнуть по кнопке "Конструктор"')
    def click_button_constructor(self):
        self.visibility_of_element_located(OrderFeedPageLocators.CONSTRUCTOR).click()

    @allure.step('Проверить номер заказа в разделе "В работе"')
    def check_order_number_in_work(self):
        return self.visibility_of_element_located(OrderFeedPageLocators.ORDER_IN_WORK).text

    @allure.step('Проверить номер заказа пользователя на странице "Лента заказов"')
    def check_user_order_number(self, order_number):
        locator = (By.XPATH, f".//p[text()='{str(order_number)}']")
        return self.visibility_of_element_located(locator)

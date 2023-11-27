import allure
from locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Проверить наличие текста "Соберите бургер"')
    def check_order_feed_text(self):
        return self.visibility_of_element_located(OrderFeedPageLocators.ORDER_FEED)

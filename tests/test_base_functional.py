import allure
from locators import MainPageLocators
from pages.account_profile_page import AccountProfilePage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestBaseFunctional:
    @allure.title('Переход авторизованного пользователя в "Конструктор"')
    def test_switch_to_constructor(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_to_login_button()
        account_profile = AccountProfilePage(driver)
        account_profile.click_constructor_button()
        assert main_page.check_build_a_burger_text()

    @allure.title('Переход авторизованного пользователя в "Лента заказов"')
    def test_switch_to_order_feed(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_button_order_feed()
        order_feed = OrderFeedPage(driver)
        assert order_feed.check_order_feed_text()

    @allure.title('При клике на ингредиент появляется всплывающее окно "Детали ингредиента"')
    def test_ingredient_details(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.check_modal_window_details_ingredient()

    @allure.title('Закрытие модального окна "Детали ингредиента" кликом по крестику')
    def test_close_modal_window_details_ingredient(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.click_button_close_in_modal_window()
        assert main_page.check_modal_window_details_ingredient()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_counter_ingredients(self, driver, login):
        main_page = MainPage(driver)
        counter_1 = main_page.check_counter_ingredients()
        main_page.drag_and_drop_on_element(locator_1=MainPageLocators.INGREDIENT, locator_2=MainPageLocators.DRAG_HERE)
        counter_2 = main_page.check_counter_ingredients()
        assert int(counter_1) < int(counter_2)

    @allure.title('Успешное оформление заказа авторизованным пользователем')
    def test_successful_create_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.check_counter_ingredients()
        main_page.drag_and_drop_on_element(locator_1=MainPageLocators.INGREDIENT, locator_2=MainPageLocators.DRAG_HERE)
        main_page.click_button_create_order()
        assert main_page.check_order_is_processed()

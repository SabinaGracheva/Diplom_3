import allure
from locators import MainPageLocators
from pages.account_order_history import AccountOrderHistoryPage
from pages.account_profile_page import AccountProfilePage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:
    @allure.title('При клике на заказ появляется модальное окно с деталями заказа')
    def test_order_details(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_button_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_order()
        assert order_feed_page.check_show_modal_window_with_details_order()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_details_displayed_in_orders_feed(self, driver, login):
        main_page = MainPage(driver)
        main_page.check_counter_ingredients()
        main_page.drag_and_drop_on_element(locator_1=MainPageLocators.INGREDIENT, locator_2=MainPageLocators.DRAG_HERE)
        main_page.click_button_create_order()
        main_page.click_button_close_in_modal_window()
        main_page.click_to_login_button()
        account_file_page = AccountProfilePage(driver)
        account_file_page.click_button_orders_history()
        account_order_history_page = AccountOrderHistoryPage(driver)
        order_number = account_order_history_page.check_order_number()
        account_order_history_page.click_button_order_feed()
        order_feed_page = OrderFeedPage(driver)
        assert order_feed_page.check_user_order_number(order_number)

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_counter_orders_of_all_time_increases(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_button_order_feed()
        order_feed_page = OrderFeedPage(driver)
        counter_1 = order_feed_page.check_counter_orders_of_all_time()
        order_feed_page.click_button_constructor()
        main_page.drag_and_drop_on_element(locator_1=MainPageLocators.INGREDIENT, locator_2=MainPageLocators.DRAG_HERE)
        main_page.click_button_create_order()
        main_page.click_button_close_in_modal_window()
        main_page.click_button_order_feed()
        counter_2 = order_feed_page.check_counter_orders_of_all_time()
        assert int(counter_1) < int(counter_2)

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_counter_orders_for_today_increases(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_button_order_feed()
        order_feed_page = OrderFeedPage(driver)
        counter_1 = order_feed_page.check_counter_orders_for_today()
        order_feed_page.click_button_constructor()
        main_page.drag_and_drop_on_element(locator_1=MainPageLocators.INGREDIENT, locator_2=MainPageLocators.DRAG_HERE)
        main_page.click_button_create_order()
        main_page.click_button_close_in_modal_window()
        main_page.click_button_order_feed()
        counter_2 = order_feed_page.check_counter_orders_for_today()
        assert int(counter_1) < int(counter_2)

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_number_order_appears_in_work(self, driver, login):
        main_page = MainPage(driver)
        main_page.check_counter_ingredients()
        main_page.drag_and_drop_on_element(locator_1=MainPageLocators.INGREDIENT, locator_2=MainPageLocators.DRAG_HERE)
        main_page.click_button_create_order()
        order_number = main_page.check_order_number()
        main_page.click_button_close_in_modal_window()
        main_page.click_button_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_number_in_work = order_feed_page.check_order_number_in_work()
        assert str(order_number) == order_number_in_work[1:]

import allure

from data import Url, Endpoints
from pages.account_profile_page import AccountProfilePage
from pages.main_page import MainPage


class TestAccountProfilePage:
    @allure.title('Переход авторизованного пользователя "Личный кабинет"')
    def test_switch_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_to_login_button()  # клик по кнопке Личный кабинет
        account_profile = AccountProfilePage(driver)
        assert account_profile.check_logout_button()

    @allure.title('Переход авторизованного пользователя "История заказов"')
    def test_switch_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_to_login_button()  # клик по кнопке Личный кабинет
        account_profile = AccountProfilePage(driver)
        account_profile.click_button_orders_history()  # клик по кнопке История заказов
        current_url = account_profile.get_current_url()
        assert current_url == f'{Url.URL}{Endpoints.ORDER_HISTORY}'



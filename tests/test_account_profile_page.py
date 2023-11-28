import allure
from data import Url, Endpoints
from pages.account_profile_page import AccountProfilePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestAccountProfilePage:
    @allure.title('Переход авторизованного пользователя "Личный кабинет"')
    def test_switch_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_to_login_button()
        account_profile = AccountProfilePage(driver)
        assert account_profile.check_logout_button(), 'Не выполнен переход в "Личный кабинет"'

    @allure.title('Переход авторизованного пользователя "История заказов"')
    def test_switch_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_to_login_button()
        account_profile = AccountProfilePage(driver)
        account_profile.click_button_orders_history()
        current_url = account_profile.get_current_url()
        assert current_url == f'{Url.URL}{Endpoints.ORDER_HISTORY}', 'Не выполнен переход в "История заказов"'

    @allure.title('Выход из аккаунта')
    def test_switch_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_to_login_button()
        account_profile = AccountProfilePage(driver)
        account_profile.click_logout_button()
        login_page = LoginPage(driver)
        assert login_page.check_button_entry(), 'Не выполнен выход из аккаунта'

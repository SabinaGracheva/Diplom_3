from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы главной страницы
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт" на главной странице


class AuthPageLocators:
    # Локаторы страницы входа в аккаунт
    RESTORE_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]')  # гиперлинк "Восстановить пароль"


class PasswordRecoveryPageLocators:
    # Локаторы страницы восстановления пароля
    PASSWORD_RECOVERY_TEXT = '//div[contains(@class, "Auth_login")]/h2'  # текст "Восстановление пароля"

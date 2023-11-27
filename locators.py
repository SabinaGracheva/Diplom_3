from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы главной страницы
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')  # кнопка "Личный кабинет"


class AuthPageLocators:
    # Локаторы страницы входа в аккаунт
    RESTORE_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]')  # гиперлинк "Восстановить пароль"
    EMAIL = (By.XPATH, '//input[@name="name"]')  # поле ввода email на странице авторизации
    PASSWORD = (By.XPATH, '//input[@name="Пароль"]')  # поле ввода пароля на странице авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти"


class PasswordRecoveryPageLocators:
    # Локаторы страницы восстановления пароля
    PASSWORD_RECOVERY_TEXT = (By.XPATH, '//h2[text()="Восстановление пароля"]')  # текст "Восстановление пароля"
    INPUT_EMAIL = (By.XPATH, '//input[contains(@class, "text")]')  # инпут "Email"
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')  # кнопка "Восстановить"
    INPUT_NEW_PASSWORD = (By.CSS_SELECTOR, '[name="Введите новый пароль"]')  # инпут "Пароль"
    INPUT_ICON = (By.XPATH, '//div[contains(@class, "input__icon")]')  # кнопка показать/скрыть пароль
    ACTIVE_INPUT_NEW_PASSWORD = (By.XPATH, '//div[contains(@class, "input_status_active")]')  # активный инпут


class AccountProfilePageLocators:
    # Локаторы страницы "Личный кабинет"
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')  # кнопка выхода из Личного кабинета
    ORDERS_HISTORY = (By.XPATH, '//a[@href="/account/order-history"]')  # кнопка История заказов

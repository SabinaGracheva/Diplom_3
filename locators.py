from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы главной страницы
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')  # кнопка "Личный кабинет"
    BUILD_A_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')  # тест "Соберите бургер" на главной странице
    ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]')  # кнопка "Лента заказов"
    INGREDIENT = (By.CSS_SELECTOR, 'img[alt="Флюоресцентная булка R2-D3"]')  # ингредиент
    DETAILS_INGREDIENT = (By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]')  # модалка "Детали ингредиента"
    CLOSE_DETAILS_INGREDIENT = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified")]')  # закрыть модально окно "Детали ингредиента"
    DRAG_HERE = (By.XPATH, '//ul[contains(@class, "BurgerConstructor")]')  # перетащить ингредиент в заказ
    COUNTER_INGREDIENTS = (By.XPATH, '//p[contains(@class, "counter_counter__num")]')  # счетчик ингредиентов
    CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')  # кнопка "Оформить заказ"
    ORDER_IS_PROCESSED = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')  # номер заказа


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
    CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка Конструктор


class OrderFeedPageLocators:
    # Локаторы страницы "Лента заказов"
    ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]')  # текст "Лента заказов"
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')  # номер заказа
    ORDER = (By.XPATH, '//li[contains(@class, "OrderHistory")]')  # заказ
    DETAILS_ORDER = (By.XPATH, '//div[contains(@class, "Modal_orderBox")]')  # модальное окно с деталями заказа
    ORDERS_OF_ALL_TIME = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]')  # Выполнено заказов за все время
    ORDERS_FOR_TODAY = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]')  # Выполнено заказов за сегодня
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')  # кнопка "Личный кабинет"
    CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка Конструктор
    ORDER_IN_WORK = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]'
                               '/li[contains(@class, "text text_type_digits")]')  # заказ в работе


class AccountOrderHistoryPageLocators:
    # Локаторы страницы "История заказов"
    ORDER_NUMBER = (By.XPATH, '//p[contains(@class, "text text_type_digits")]')   # номер заказа
    ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]')  # кнопка "Лента заказов"

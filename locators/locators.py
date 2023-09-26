from selenium.webdriver.common.by import By


class Locators:
    ACCOUNT_LINK = By.XPATH, '//*[@href="/account"]'  # ссылка на "Личный Кабинет"
    REGISTER_LINK = By.XPATH, '//*[@href="/register"]'  # ссылка "Зарегистрироваться" на стр. логина

    INPUT_NAME = By.XPATH, '//label[text()="Имя"]/following-sibling::input'  # инпут "Имя" на стр. регистрации
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # инпут "Email" на стр. регистрации и логина
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'  # инпут "Пароль" на стр. регистрации и логина

    REGISTRATION_BUTTON = By.XPATH, '//button[text()="Зарегистрироваться"]'  # кнопка "Зарегистрироваться" на стр. регистрации

    ERROR_STATE_INPUT = By.XPATH, '//*[contains(@class, "input_status_error")]'  # инпут "Пароль" в стейте ошибки
    ERROR_INPUT_TEXT = By.XPATH, '//*[contains(@class, "input__error")]'  # абзац с текстом ошибки некорректного пароля

    ENTER_ACCOUNT_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'  # кнопка "Войти в аккаунт" на главной стр.
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]'  # кнопка "Войти" на стр. логина
    ENTER_TITLE_LOGIN_PAGE = By.XPATH, '//h2[text()="Вход"]'  # заголовок "Вход" на стр. логина

    CONSTRUCTOR_TITLE = By.XPATH, '//h1[text()="Соберите бургер"]'  # заголовок "Соберите бургер" на главной стр.
    ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'  # кнопка "Оформить заказ" на главной стр.

    RESET_PASS_LINK = By.XPATH, '//*[@href="/forgot-password"]'  # ссылка "Восстановить пароль" на стр. логина
    RESET_BUTTON = By.XPATH, '//button[text()="Восстановить"]'  # кнопка "Восстановить" на стр. восстановления пароля

    ENTER_LINK = By.XPATH, '//*[@href="/login"]'  # cсылка "Войти" на стр. регистрации и стр. восстановления пароля

    PROFILE_LINK = By.XPATH, '//*[@href="/account/profile"]'  # cсылка "Профиль" в личном кабинете
    SAVE_PROFILE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'  # кнопка "Сохранить" в личном кабинете

    LOGOUT_BUTTON = By.XPATH, '//*[contains(@class, "Account_button")]'  # кнопка "Выход" в личном кабинете

    STELLAR_BURGERS_LOGO = By.XPATH, '//*[contains(@class, "logo")]'  # логотип Stellar Burgers в хэдере

    CONSTRUCTOR_LINK = By.XPATH, '//p[text()="Конструктор"]/parent::a'  # ссылка "Конструктор" в хэдере

    CONSTRUCTOR_TAB_LOAF = By.XPATH, '//span[text()="Булки"]/parent::div'  # таб раздела "Булки" на главной стр.
    CONSTRUCTOR_TAB_SAUCE = By.XPATH, '//span[text()="Соусы"]/parent::div'  # таб раздела "Соусы" на главной стр.
    CONSTRUCTOR_TAB_FILLING = By.XPATH, '//span[text()="Начинки"]/parent::div'  # таб раздела "Начинки" на главной стр.

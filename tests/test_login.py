from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import Locators
from data import UserData


class TestLogin:

    def test_enter_account_button(self, driver):

        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.LOGIN)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert order_button.is_displayed(), 'Не удалось залогиниться через кнопку "Войти в аккаунт"'

    def test_personal_account_button(self, driver):

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.LOGIN)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert order_button.is_displayed(), 'Не удалось залогиниться через ссылку на "Личный кабинет"'

    def test_enter_link_on_reg_page(self, driver):

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        driver.find_element(*Locators.REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

        driver.find_element(*Locators.ENTER_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.LOGIN)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert order_button.is_displayed(), 'Не удалось залогиниться через ссылку "Войти в аккаунт" на стр. регистрации'

    def test_enter_link_on_reset_pass_page(self, driver):

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        driver.find_element(*Locators.RESET_PASS_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.RESET_BUTTON))

        driver.find_element(*Locators.ENTER_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.LOGIN)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert order_button.is_displayed(), \
            'Не удалось залогиниться через ссылку "Войти в аккаунт" на стр. восстановления пароля'

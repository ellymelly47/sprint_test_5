from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import Locators
from helpers import generate_login, generate_password


class TestRegistration:

    def test_successful_registration(self, driver):

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTER_LINK))

        driver.find_element(*Locators.REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

        driver.find_element(*Locators.INPUT_NAME).send_keys('Ivan')
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(generate_login())
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(generate_password())
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.ENTER_TITLE_LOGIN_PAGE))

        assert driver.find_element(*Locators.ENTER_BUTTON).is_displayed()

    def test_wrong_password_reg(self, driver):

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTER_LINK))

        driver.find_element(*Locators.REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

        driver.find_element(*Locators.INPUT_NAME).send_keys('Ivan')
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(generate_login())
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys('123')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ERROR_STATE_INPUT))

        assert driver.find_element(*Locators.ERROR_INPUT_TEXT).text == "Некорректный пароль"

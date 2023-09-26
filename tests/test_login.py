from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import Locators


def test_enter_account_button(driver, user):

    driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

    driver.find_element(*Locators.INPUT_EMAIL).send_keys(user['login'])
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(user['password'])
    driver.find_element(*Locators.ENTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

    order_button = driver.find_element(*Locators.ORDER_BUTTON)
    assert order_button.is_displayed()


def test_personal_account_button(driver, user):

    driver.find_element(*Locators.ACCOUNT_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

    driver.find_element(*Locators.INPUT_EMAIL).send_keys(user['login'])
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(user['password'])
    driver.find_element(*Locators.ENTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

    order_button = driver.find_element(*Locators.ORDER_BUTTON)
    assert order_button.is_displayed()


def test_enter_link_on_reg_page(driver, user):

    driver.find_element(*Locators.ACCOUNT_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
    driver.find_element(*Locators.REGISTER_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

    driver.find_element(*Locators.ENTER_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

    driver.find_element(*Locators.INPUT_EMAIL).send_keys(user['login'])
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(user['password'])
    driver.find_element(*Locators.ENTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

    order_button = driver.find_element(*Locators.ORDER_BUTTON)
    assert order_button.is_displayed()


def test_enter_link_on_reset_pass_page(driver, user):

    driver.find_element(*Locators.ACCOUNT_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
    driver.find_element(*Locators.RESET_PASS_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.RESET_BUTTON))

    driver.find_element(*Locators.ENTER_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

    driver.find_element(*Locators.INPUT_EMAIL).send_keys(user['login'])
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(user['password'])
    driver.find_element(*Locators.ENTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

    order_button = driver.find_element(*Locators.ORDER_BUTTON)
    assert order_button.is_displayed()

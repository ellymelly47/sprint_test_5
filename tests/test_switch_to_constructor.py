from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import Locators


def test_link_to_constructor_by_logo(driver, user):

    driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

    driver.find_element(*Locators.INPUT_EMAIL).send_keys(user['login'])
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(user['password'])
    driver.find_element(*Locators.ENTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

    driver.find_element(*Locators.ACCOUNT_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_LINK))

    driver.find_element(*Locators.STELLAR_BURGERS_LOGO).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

    order_button = driver.find_element(*Locators.ORDER_BUTTON)
    assert order_button.is_displayed()


def test_direct_link_to_constructor(driver, user):

    driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

    driver.find_element(*Locators.INPUT_EMAIL).send_keys(user['login'])
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(user['password'])
    driver.find_element(*Locators.ENTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

    driver.find_element(*Locators.ACCOUNT_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_LINK))

    driver.find_element(*Locators.CONSTRUCTOR_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

    order_button = driver.find_element(*Locators.ORDER_BUTTON)
    assert order_button.is_displayed()

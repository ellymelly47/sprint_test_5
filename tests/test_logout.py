from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import Locators


def test_logout_from_account(driver, user):

    driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

    driver.find_element(*Locators.INPUT_EMAIL).send_keys(user['login'])
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(user['password'])
    driver.find_element(*Locators.ENTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

    driver.find_element(*Locators.ACCOUNT_LINK).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_LINK))

    driver.find_element(*Locators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_TITLE_LOGIN_PAGE))

    assert driver.find_element(*Locators.ENTER_BUTTON).is_displayed()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import Locators
from data import UserData


class TestConstructorTabs:

    def test_select_filling_tab(self, driver):

        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.LOGIN)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

        driver.find_element(*Locators.CONSTRUCTOR_TAB_FILLING).click()

        filling_tab = driver.find_element(*Locators.CONSTRUCTOR_TAB_FILLING)
        assert "tab_type_current" in filling_tab.get_attribute("class")

    def test_select_sause_tab(self, driver):

        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.LOGIN)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

        driver.find_element(*Locators.CONSTRUCTOR_TAB_SAUCE).click()

        sause_tab = driver.find_element(*Locators.CONSTRUCTOR_TAB_SAUCE)
        assert "tab_type_current" in sause_tab.get_attribute("class")

    def test_select_loaf_tab(self, driver):

        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.LOGIN)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

        driver.find_element(*Locators.CONSTRUCTOR_TAB_SAUCE).click()
        driver.find_element(*Locators.CONSTRUCTOR_TAB_LOAF).click()

        loaf_tab = driver.find_element(*Locators.CONSTRUCTOR_TAB_LOAF)
        assert "tab_type_current" in loaf_tab.get_attribute("class")

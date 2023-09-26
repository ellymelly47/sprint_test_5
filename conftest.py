from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def user():
    return {'login': 'evgenia_berdnikova_1358@yandex.ru', 'password': 'jDh47M1kU'}


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

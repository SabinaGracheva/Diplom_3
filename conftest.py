import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from data import Url


@pytest.fixture
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    browser.get(Url.URL)
    yield browser
    browser.quit()

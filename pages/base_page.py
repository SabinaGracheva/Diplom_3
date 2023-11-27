from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # присутствие локатора элемента
    def presence_of_element_located(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator))

    # визуальное отображение элемента
    def visibility_of_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def get_current_url(self):
        return self.driver.current_url

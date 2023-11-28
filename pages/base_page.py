from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visibility_of_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def get_current_url(self):
        return self.driver.current_url

    def drag_and_drop_on_element(self, locator_1, locator_2):
        draggable = self.find_element(locator_1)
        droppable = self.find_element(locator_2)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

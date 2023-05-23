from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url



    def open(self):
        self.driver.get(self.url)

    def go_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def click_on_element(self, locator):
        self.driver.execute_script(self, "arguments[0].click();", locator)




    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)




    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))



    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))


    def element_is_enable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))




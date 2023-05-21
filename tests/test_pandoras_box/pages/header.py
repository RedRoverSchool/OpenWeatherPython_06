from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class Header(BasePage):

    logo_locator = (By.XPATH, '//*[@class="logo"]/a/img')

    def check_logo_is_visible(self, logo_locator):
        logo = self.driver.find_element(*logo_locator)
        assert logo.is_displayed(), "Logo is not visible"
from pages.base_page import BasePage
from tests.test_group_roma.locators.locators import MainPageLocators


class MainPage(BasePage):

    def go_to_footer(self, driver):
        footer_website = driver.find_element(*MainPageLocators.footer_website_locator)
        driver.execute_script("arguments[0].scrollIntoView();", footer_website)

    def is_GitHub_icon_displayed(self, driver):
        GitHub_icon = self.driver.find_element(*MainPageLocators.gitHub_icon_image)
        GitHub_icon.is_displayed()



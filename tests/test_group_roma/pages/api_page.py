from pages.base_page import BasePage
from tests.test_group_roma.locators.locators import ApiPageLocators
from tests.test_group_roma import links


class ApiPage(BasePage):
    locator = ApiPageLocators

    def check_logo(self):
        self.driver.find_element(*self.locator.LOGO).click()
        assert self.driver.current_url == links.MAIN_PAGE
    #
    # def open_api_page(self):
    #     api_page = ApiPage(self.driver)
    #     api_page.open_page()
    #
    # def click_logo(self):
    #     search_logo = self.driver.find_element(*self.locator.LOGO).click()
    #     search_logo.open_page()
    #
    # def verify_main_page_url(self):
    #     assert self.driver.current_url == links.MAIN_PAGE

from pages.base_page import BasePage
from tests.test_group_roma.locators.locators import ApiPageLocators
from tests.test_group_roma import links


class ApiPage(BasePage):

    def check_logo(self):
        self.driver.find_element(*ApiPageLocators.LOGO).click()
        assert self.driver.current_url == links.MAIN_PAGE


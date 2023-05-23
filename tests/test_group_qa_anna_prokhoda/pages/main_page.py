from pages.base_page import BasePage
from tests.test_group_qa_anna_prokhoda.locators.main_page_locators import MainPageLocators
from tests.test_group_qa_anna_prokhoda.links.links import marketplace_page_url



class MainPage(BasePage):
    locators = MainPageLocators()


    def verify_marketplace_link_redirects_to_valid_page(self):
        self.driver.find_element(*self.locators.marketplace_link).click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        assert self.driver.current_url == marketplace_page_url

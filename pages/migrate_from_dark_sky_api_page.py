import time

from pages.base_page import BasePage
from locators.locators import MigratePageLocators
from test_data.urls import MigratePageUrls

class MigrateFromDarkSkyApiPage(BasePage):
    locators = MigratePageLocators

    def verify_subscribe_for_free_link_redirection(self, migrate_page):
        self.driver.get(MigratePageUrls.URL_DARK_SKY_API)
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.find_element_and_click(self.locators.SUBSCRIBE_FOR_FREE_LINK)
        time.sleep(3)
        self.switch_to_new_window()
        self.check_for_redirection(MigratePageUrls.URL_SIGN_UP)
        migrate_page_link = self.driver.current_url
        assert migrate_page_link == migrate_page, "Incorrect link"


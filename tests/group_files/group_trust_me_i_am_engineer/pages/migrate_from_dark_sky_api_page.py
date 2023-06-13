import time

from pages.base_page import BasePage
from tests.group_files.group_trust_me_i_am_engineer.locators.page_locators import MigratePageLocators

class MigratePage(BasePage):
    locators = MigratePageLocators()
    URL_DARK_SKY_API = 'https://openweathermap.org/darksky-openweather-3'

    def verify_subscribe_for_free_link_redirection(self):
        self.driver.get(self.URL_DARK_SKY_API)
        self.driver.execute_script("window.scrollTo(0, 500)")
        migrate_link_redirection = self.driver.find_element(*self.locators.SUBSCRIBE_FOR_FREE_LINK)
        self.driver.execute_script("arguments[0].click();", migrate_link_redirection)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        assert self.URL_DARK_SKY_API, self.driver.current_url
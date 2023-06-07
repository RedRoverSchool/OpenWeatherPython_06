from pages.base_page import BasePage
from tests.test_group_python_qa.locators.locators import GuidePageLocators
from selenium.webdriver.support.color import Color


class GuidePage(BasePage):

    locators = GuidePageLocators()

    def link_to_history_archive_is_clickable(self):
        archive_link = self.driver.find_element(*self.locators.LINK_HISTORICAL_ARCHIVE)
        self.action_move_to_element(archive_link)
        assert archive_link.is_enabled(), "The link is not clickable"

    def footer_click_allow(self):
        self.driver.find_element(*self.locators.CLICK_ALLOW_IN_STICK_FOOTER).click()


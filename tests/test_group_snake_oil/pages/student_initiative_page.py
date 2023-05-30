from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from tests.test_group_snake_oil.locators.student_initiative_page_locators import StudentInitiativePageLocators


class StudentInitiativePage(BasePage):
    locators = StudentInitiativePageLocators

    def click_the_learn_more_link_for_the_developer_plan(self):
        learn_more_link = self.element_is_clickable(self.locators.LEARN_MORE_LINK_DEVELOPER_PLAN)
        learn_more_link.click()
        current_url = self.driver.current_url
        return current_url

    def verify_page_redirection_for_the_developer_plan(self, current_url):
        expected_url = self.locators.PRICING_PAGE_URL_FOR_DEVELOPER_PLAN
        assert current_url == expected_url, "Incorrect page redirection for the Developer Plan"

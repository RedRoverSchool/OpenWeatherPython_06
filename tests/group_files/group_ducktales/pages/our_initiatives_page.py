from selenium.common import ElementClickInterceptedException

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.group_files.group_ducktales.locators.our_initiatives_page_locators import OurInitiativesPageLocators
from tests.group_files.group_ducktales.test_data.our_initiatives_page_data import EDUCATION_SECTION_PAGE


class OurInitiativesPage(BasePage):
    locators = OurInitiativesPageLocators()

    def get_section_element(self, section):
        section_locator = (self.locators.SECTION[0], self.locators.SECTION[1].format(section))
        section_element = self.element_is_present(section_locator)
        assert section_element.is_displayed(), f"Section '{section}' not found on the page"
        return section_element

    def click_initiatives_link(self):
        our_initiatives_link = self.element_is_present(self.locators.INITIATIVES)
        our_initiatives_link.click()

    def click_education_learn_more(self):
        education_learn_more = self.element_is_present(self.locators.EDUCATION_LEARN_MORE)
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.action_move_to_element(education_learn_more)
        education_learn_more.click()

    def check_education_page_opened(self):
        assert self.driver.current_url == EDUCATION_SECTION_PAGE, "Error: education page did not open"

    def get_question_headings(self):
        question_headings = [
            self.driver.find_element(By.XPATH, self.locators.QUESTION_XPATH.format(i=i))
            for i in range(1, 10)
        ]
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return question_headings

    @staticmethod
    def verify_question_headings_displayed(question_headings):
        assert all(heading.is_displayed() for heading in question_headings), "Error: FAQ section is not displayed"

    def click_question_headings(self, question_headings):
        for heading in question_headings:
            try:
                self.driver.execute_script("arguments[0].click();", heading)
            except ElementClickInterceptedException:
                self.driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight);", heading)
                self.driver.execute_script("arguments[0].click();", heading)

    @staticmethod
    def verify_question_headings_clickable(question_headings):
        assert all(heading.is_enabled() for heading in question_headings), "Error: FAQ section is not clickable"


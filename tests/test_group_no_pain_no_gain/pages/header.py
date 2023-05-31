from .main_page import MainPage
from tests.test_group_no_pain_no_gain.locators.header_locators import HeaderLocators as HL
from tests.test_group_no_pain_no_gain import links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class Header(MainPage):
    def element_visibility_and_clickability(self, locator, link):
        element = wait(self.driver, timeout=3).until(EC.visibility_of_element_located(locator))
        assert element.is_displayed() and element.is_enabled(), f'"{link}" link is not visible or clickable'

    def link_leads_to_page_with_correct_header(self, locator, result_header_locator):
        element = self.driver.find_element(*locator)
        element_text = element.text
        element.click()
        header_text = self.driver.find_element(*result_header_locator).text
        assert element_text in header_text, \
            f'{element_text} link leads to a page with an incorrect header'

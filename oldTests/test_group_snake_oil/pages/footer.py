from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from oldTests.test_group_snake_oil.links.all_links import ABOUT_US_URL
from oldTests.test_group_snake_oil.locators.footer_locators import FootersLocators


class Footer(BasePage):
    locators = FootersLocators

    def find_technologies_module(self):
        expected_footer_text = "Technologies"
        element = self.driver.find_element(*self.locators.FOOTER_TECHNOLOGIES)
        assert element.is_displayed() and expected_footer_text in element.text, \
            "The footer is not displayed or does not contain the expected text"

    def find_links_under_technologies_module(self, icon):
        element = self.driver.find_element(*icon)
        element_link = element.get_attribute('href')
        assert element.is_displayed() and element.is_enabled(), \
            f"Link {element_link} link is not visible/clickable on a page"

    def check_redirection_to_about_us_page(self, wait):
        element = wait.until(EC.presence_of_element_located(self.locators.ABOUT_US))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        wait.until(EC.url_to_be(ABOUT_US_URL))
        assert self.driver.current_url == ABOUT_US_URL

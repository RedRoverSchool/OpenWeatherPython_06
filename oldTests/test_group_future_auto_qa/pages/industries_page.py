from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from oldTests.test_group_future_auto_qa.locators.industries_page_locators import IndustriesPageLocators


class IndustriesPage(BasePage):

    # function-helper for opening Industries page
    def open_industries_page(self):
        self.driver.get("https://openweather.co.uk/industries")
        self.allow_all_cookies()

    def check_email_link_in_talk_to_us_button(self, button_locator, expected_link):
        self.open_industries_page()
        simple_link = self.element_is_clickable(button_locator)
        link_href = simple_link.get_attribute('href')
        assert link_href == expected_link, "Email link is not correct"

    def check_visibility_and_clickability_of_learn_more_and_talk_to_us_buttons(self, button_locator):
        self.open_industries_page()
        button = self.element_is_clickable(button_locator)
        assert button.is_displayed() and button.is_enabled(), \
            f"Button with XPath {str(button_locator)[10:-1]} is not visible or is not clickable"

    def check_redirection_of_learn_more_button_in_agriculture_section(self, expected_link):
        self.open_industries_page()
        self.element_is_clickable(IndustriesPageLocators.LEARN_MORE_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        button_url = self.driver.current_url
        assert button_url == expected_link, "'Learn more' button link is not correct"


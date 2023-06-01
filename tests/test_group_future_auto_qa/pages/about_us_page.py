from pages.base_page import BasePage
from tests.test_group_future_auto_qa.locators.about_us_page_locators import AboutUsLocators


class AboutUsPage(BasePage):

    locators = AboutUsLocators()

    def open(self):
        self.driver.get("https://openweathermap.org/about-us")


    def scroll_to_contact_us_button(self):
        self.driver.execute_script("window.scrollTo(0, 500)")

    def click_contact_us_button(self):
        contact_us_button = self.driver.find_element(*AboutUsLocators.CONTACT_US_BUTTON)
        contact_us_button.click()

    def contact_us_button_is_clickable(self):
        contact_us_button = self.driver.find_element(*AboutUsLocators.CONTACT_US_BUTTON)
        return contact_us_button.is_enabled()
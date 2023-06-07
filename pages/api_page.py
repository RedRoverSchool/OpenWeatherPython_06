from pages.base_page import BasePage
from locators.locators import FooterLocators as FL


class APIPage(BasePage):
    def verify_the_copyright_information_is_present_on_the_site_page(self):
        self.allow_all_cookies()
        expected_footer_text = "© 2012 — 2023 OpenWeather"
        footer = self.driver.find_element(*FL.FOOTER_COPYRIGHT)
        assert footer.is_displayed() and expected_footer_text in footer.text, \
            "The footer is not displayed or does not contain the expected text"

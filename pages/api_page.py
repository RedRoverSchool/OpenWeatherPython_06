from pages.base_page import BasePage
from locators.locators import FooterLocators as FL
from locators.locators import ApiPageLocators



class APIPage(BasePage):
    def verify_the_copyright_information_is_present_on_the_site_page(self):
        self.allow_all_cookies()
        expected_footer_text = "© 2012 — 2023 OpenWeather"
        footer = self.driver.find_element(*FL.FOOTER_COPYRIGHT)
        assert footer.is_displayed() and expected_footer_text in footer.text, \
            "The footer is not displayed or does not contain the expected text"

    def verify_redirection_one_call_api_3_link(self):
        self.driver.get(ApiPageLocators.API_PAGE)
        self.driver.find_element(*ApiPageLocators.ONE_CALL_API_3).click()
        expected_link = ApiPageLocators.ONE_CALL_API_LINK
        assert self.driver.current_url == expected_link, "This link is not correct"
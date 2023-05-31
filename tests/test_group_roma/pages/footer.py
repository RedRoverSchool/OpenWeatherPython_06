from pages.base_page import BasePage
from tests.test_group_roma.locators.locators import FooterLocators


class FooterWebsite(BasePage):
    locators = FooterLocators()

    def footer_website_search_element(self):
        return self.driver.find_element(*self.locators.footer_website_locator)

    def check_footer_website_is_displayed(self, element):
        assert element.is_displayed() and self.driver.title not in 'Page not found (404) - OpenWeatherMap', \
            f'\nFooter is not present on the page - {self.driver.current_url}'

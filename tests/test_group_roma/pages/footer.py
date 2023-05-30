from pages.base_page import BasePage
from tests.test_group_roma.locators.locators import FooterLocators


class FooterComponent(BasePage):
    locators = FooterLocators()

    def search_element(self, locator):
        return self.driver.find_element(*locator)

    def check_footer_website_is_displayed(self, element):
        assert element.is_displayed() and self.driver.title not in 'Page not found (404) - OpenWeatherMap', \
            f'\nFooter is not present on the page - {self.driver.current_url}'

    def check_copyright_is_displayed(self, element):
        copyright_expected_result = ['©', '2012 — 2023', 'OpenWeather', '® All rights reserved']
        copyright_actual_result = element.text
        copyright_flag = 1
        for i in copyright_expected_result:
            if i not in copyright_actual_result:
                copyright_flag = 0
        assert element.is_displayed() and copyright_flag == 1, f'\nCopyright is not present (actual) on the page - {self.driver.current_url}'

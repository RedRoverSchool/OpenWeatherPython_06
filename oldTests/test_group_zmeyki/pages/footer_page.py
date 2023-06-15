from oldTests.test_group_zmeyki.locators.footer_loacator import FooterLocator
from pages.base_page import BasePage


class FooterPage(BasePage):

    footer_openweathermap = FooterLocator()

    def website_footer_visibility(self):
        module_footer = self.driver.find_element(*self.footer_openweathermap.footer_locator)
        assert module_footer.is_displayed()

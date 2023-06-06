from pages.api_page import APIPage
from locators.locators import ApiPageLocators


class TestApiPage:
    def test_tc_003_11_02_verify_the_copyright_information_is_present_on_the_site_page(self, driver):
        page = APIPage(driver, ApiPageLocators.API_PAGE)
        page.open_page()
        page.verify_the_copyright_information_is_present_on_the_site_page()

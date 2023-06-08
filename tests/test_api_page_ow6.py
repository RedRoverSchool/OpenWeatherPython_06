from pages.api_page import APIPage
from locators.locators import ApiPageLocators


class TestApiPage:
    def test_tc_003_11_02_verify_the_copyright_information_is_present_on_the_site_page(self, driver):
        page = APIPage(driver, ApiPageLocators.API_PAGE)
        page.open_page()
        page.verify_the_copyright_information_is_present_on_the_site_page()

    def test_tc_008_02_04_verify_redirection_One_Call_API_3_link(self, driver):
        page = APIPage(driver, link=ApiPageLocators.API_PAGE)
        page.open_page()
        page.verify_redirection_one_call_api_3_link()

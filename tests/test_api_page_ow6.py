from pages.api_page import APIPage
from locators.locators import ApiPageLocators


class TestApiPage:

    def test_tc_008_02_04_verify_redirection_One_Call_API_3_link(self, driver):
        page = APIPage(driver, link=ApiPageLocators.API_PAGE)
        page.open_page()
        page.verify_redirection_one_call_api_3_link()

    def test_TC_002_01_02_verify_returning_from_API_page_to_main_page_by_clicking_on_logo(self, driver):
        api_page = APIPage(driver, link=ApiPageLocators.API_PAGE)
        api_page.open_page()
        api_page.check_logo()

from pages.api_page import APIPage
from locators.locators import ApiPageLocators


class TestApiPage:

    def test_tc_008_02_04_verify_redirection_One_Call_API_3_link(self, driver):
        page = APIPage(driver, link=ApiPageLocators.API_PAGE)
        page.open_page()
        page.verify_redirection_one_call_api_3_link()


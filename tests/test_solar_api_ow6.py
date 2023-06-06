from test_data.all_links import Links
from pages.solar_api_page import SolarApiPagePage
from locators.locators import SolarApiLocators as sapi


class TestSolarApi:

    def test_tc_005_10_02_visibility_of_product_concept_article_title(self, driver, wait):
        solar_api = SolarApiPagePage(driver, Links.URL_SOLAR_API)
        solar_api.open_page()
        solar_api.element_is_displayed(sapi.PRODUCT_CONCEPT_TITLE, wait)

    def test_tc_005_10_03_correct_redirection_for_how_to_get_access_link(self, driver, wait):
        solar_api = SolarApiPagePage(driver, Links.URL_SOLAR_API)
        solar_api.open_page()
        solar_api.find_element_and_click(sapi.HOW_TO_GET_ACCESS_LINK)
        solar_api.element_is_displayed(sapi.HOW_TO_GET_ACCESS_TITLE, wait)




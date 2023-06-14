from pages.maps_page import MapsPage
from test_data.urls import MapsPageUrls

class TestMapsPage:
    def test_TC_001_06_02_verify_clickability_of_cities_checkbox(self, driver):
        page = MapsPage(driver, MapsPageUrls.PAGE_WITH_MAP_LINK)
        page.open_page()
        page.cities_checkbox_is_checked()
        page.cities_checkbox_is_unchecked()
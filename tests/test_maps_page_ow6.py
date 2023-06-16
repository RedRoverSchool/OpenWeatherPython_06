from pages.maps_page import MapsPage
from test_data.urls import MapsPageUrls

class TestMapsPage:
    def test_TC_001_06_02_verify_clickability_of_cities_checkbox(self, driver):
        page = MapsPage(driver, MapsPageUrls.PAGE_WITH_MAP_LINK)
        page.open_page()
        page.cities_checkbox_is_checked()
        page.cities_checkbox_is_unchecked()

    def test_TC_002_03_12_open_maps(self, driver, open_and_load_main_page):
        maps_page = MapsPage(driver)
        maps_page.check_open_maps('maps')


    def test_TC_002_01_06_Verify_return_to_Main_page_from_Interactive_weather_maps(self, driver):
        maps_page = MapsPage(driver, MapsPageUrls.PAGE_WITH_MAP_LINK)
        maps_page.open_page()
        maps_page.check_return_main()

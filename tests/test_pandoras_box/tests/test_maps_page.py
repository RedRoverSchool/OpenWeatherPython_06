from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.test_pandoras_box.pages.maps_page import MapsPage

def test_TC_002_01_06_Verify_return_to_Main_page_from_Interactive_weather_maps(driver):
    maps_page = MapsPage(driver, MapsPage.MAPS_URL)
    maps_page.open_page()
    maps_page.check_return_main()

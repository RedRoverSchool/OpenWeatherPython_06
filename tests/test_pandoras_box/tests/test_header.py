import pytest
from tests.test_pandoras_box.test_data.header_data import URLs
from tests.test_pandoras_box.pages.header import Header
from tests.test_pandoras_box.pages.search_result_page import SearchResultPage

@pytest.mark.parametrize('URL', URLs)
def test_TC_002_01_03_Logo_is_visible(driver, URL):
    page = Header(driver, link=URL)
    page.open_page()
    page.check_logo_is_visible()

def test_TC_002_02_01_search_result_contains_city(driver, open_and_load_main_page):
    page = Header(driver)
    page.enter_city_in_header_search_field('Bangkok')
    page.press_enter_button()
    result_page = SearchResultPage(driver)
    result_page.check_search_result_contains_city('Bangkok')

def test_TC_002_03_12_open_maps(driver, open_and_load_main_page):
    maps_page = Header(driver)
    maps_page.check_open_maps('maps')

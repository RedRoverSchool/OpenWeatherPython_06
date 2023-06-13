from tests.group_files.group_lutz_squad.pages.page_with_map import PageWithMap
from tests.group_files.group_lutz_squad.locators.page_with_map_locators import PageWithMapLocators


def test_TC_001_06_03_verify_pressure_button_is_clickable(driver, wait):
    page = PageWithMap(driver, link=PageWithMapLocators.PAGE_WITH_MAP_LINK)
    page.open_page()
    page.pressure_button_is_clickable(wait)

def test_TC_001_06_02_verify_clickability_of_cities_checkbox(driver):
    page = PageWithMap(driver, link=PageWithMapLocators.PAGE_WITH_MAP_LINK)
    page.open_page()
    page.cities_checkbox_is_checked()
    page.cities_checkbox_is_unchecked()
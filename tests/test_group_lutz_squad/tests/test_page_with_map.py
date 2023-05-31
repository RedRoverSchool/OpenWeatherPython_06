from tests.test_group_lutz_squad.pages.page_with_map import PageWithMap
from tests.test_group_lutz_squad.locators.page_with_map_locators import PageWithMapLocators


def test_TC_001_06_03_verify_pressure_button_is_clickable(driver, wait):
    page = PageWithMap(driver, link=PageWithMapLocators.PAGE_WITH_MAP_LINK)
    page.open_page()
    page.pressure_button_is_clickable(wait)

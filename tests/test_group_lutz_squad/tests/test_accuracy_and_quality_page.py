from tests.test_group_lutz_squad.pages.accuracy_and_quality_page import AccuracyAndQualityPage
from tests.test_group_lutz_squad.locators.accuracy_and_quality_page_locators import AccuracyAndQualityPageLocators as AC

def test_TC_001_17_02_visibility_of_List_of_cities_module(driver):
    page = AccuracyAndQualityPage(driver, link=AC.ACCURACY_AND_QUALITY_PAGE_LINK)
    page.open_page()
    page.check_visibility_of_number_of_cities()
from tests.test_group_lutz_squad.pages.accuracy_and_quality_of_weather_data_page import AccuracyAndQualityOfWeatherDataPage
from tests.test_group_lutz_squad.locators.accuracy_and_quality_of_weather_data_page_locators import \
    AccuracyAndQualityOfWeatherDataPageLocators

def test_TC_00_17_03__Verify_visibility_of_picture(driver, open_and_load_main_page, wait):
    page = AccuracyAndQualityOfWeatherDataPage(driver)
    page.verify_visibility_of_picture(wait)


def test_TC_001_17_02_visibility_of_List_of_cities_module(driver):
    page = AccuracyAndQualityOfWeatherDataPage(driver, link=AccuracyAndQualityOfWeatherDataPageLocators.ACCURACY_AND_QUALITY_PAGE_LINK)
    page.open_page()
    page.check_visibility_of_number_of_cities()

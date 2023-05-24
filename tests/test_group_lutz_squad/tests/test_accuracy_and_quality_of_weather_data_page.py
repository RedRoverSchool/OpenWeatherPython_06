from tests.test_group_lutz_squad.pages.accuracy_and_quality_of_weather_data_page import AccuracyAndQualityOfWeatherDataPage

def test_TC_00_17_03__Verify_visibility_of_picture(driver, open_and_load_main_page, wait):
    page = AccuracyAndQualityOfWeatherDataPage(driver)
    page.verify_visibility_of_picture(wait)


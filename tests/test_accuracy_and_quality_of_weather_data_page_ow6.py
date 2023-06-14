from pages.accuracy_and_quality_of_weather_data_page import AccuracyAndQualityOfWeatherDataPage
from test_data.urls import AccuracyAndQualityOfWeatherDataPageUrls


class TestAccuracyAndQualityOfWeatherDataPage:
    def test_TC_001_17_02_visibility_of_List_of_cities_module(self, driver):
        page = AccuracyAndQualityOfWeatherDataPage(driver, AccuracyAndQualityOfWeatherDataPageUrls.ACCURACY_AND_QUALITY_PAGE_LINK)
        page.open_page()
        page.check_visibility_of_number_of_cities()
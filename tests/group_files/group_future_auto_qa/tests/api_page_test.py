from tests.group_files.group_future_auto_qa.pages.api_page import ApiPage


class TestTitle:

    def test_tc_005_10_01_visibility_of_weather_api_page_title(self, driver):
        page = ApiPage(driver)
        page_title = 'Weather API - OpenWeatherMap'
        page.check_page_title(page_title)

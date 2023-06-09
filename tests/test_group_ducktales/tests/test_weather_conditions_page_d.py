from tests.test_group_ducktales.pages.weather_conditions_page_d import WeatherConditionsPage
from ..test_data.weather_conditions_page_data_d import WeatherConditionsData as data

class TestWeatherConditionsPage:

    @pytest.mark.parametrize('table', data.TABLES)
    def test_tc_001_12_07_verify_that_codes_and_descriptions_are_visible_for_each_weather_condition_group_part1(self, driver, table):
        weather_conditions_page = WeatherConditionsPage(driver)
        weather_conditions_page.open_weather_conditions_page()
        weather_conditions_page.check_codes_are_visible(driver, table)

    @pytest.mark.parametrize('table', data.TABLES)
    def test_tc_001_12_07_verify_that_codes_and_descriptions_are_visible_for_each_weather_condition_group_part2(self, driver, table):
        weather_conditions_page = WeatherConditionsPage(driver)
        weather_conditions_page.open_weather_conditions_page()
        weather_conditions_page.check_desc_are_visible(driver, table)





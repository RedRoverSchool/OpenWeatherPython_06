from tests.group_files.group_trust_me_i_am_engineer.pages.weather_conditions_page import WeatherConditionsPage


def test_TC_001_10_04_weather_conditions_verify_list_of_description(driver):
    page = WeatherConditionsPage(driver)
    page.weather_conditions_verify_list_of_description()

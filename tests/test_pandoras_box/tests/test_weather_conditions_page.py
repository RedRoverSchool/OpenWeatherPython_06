from tests.test_pandoras_box.pages.weather_conditions_page import WeatherConditions
def test_TC_001_12_01_thunderstorm_group_contains_items(driver):
    page = WeatherConditions(driver, link=WeatherConditions.condition_URL)
    page.open_page()
    page.check_number_of_elements('thunderstorm')
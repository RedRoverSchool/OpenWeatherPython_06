from tests.group_files.pandoras_box.pages.weather_conditions_page import WeatherConditions
def test_TC_001_12_01_thunderstorm_group_contains_items(driver):
    page = WeatherConditions(driver, link=WeatherConditions.condition_URL)
    page.open_page()
    page.check_number_of_elements('thunderstorm')

def test_TC_001_12_05_Clouds_group_of_codes_visible(driver):
    page = WeatherConditions(driver, WeatherConditions.condition_URL)
    page.open_page()
    page.check_visible_group_of_codes('clouds')

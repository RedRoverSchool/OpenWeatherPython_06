from test_data.main_page_data import data
import pytest
from tests.test_group_python_qa.pages.main_page_pqa import MainPage


@pytest.mark.parametrize('city', data["cityName"])
def test_tc_001_04_01_visibility_of_8_lines_in_8_day_forecast_block(driver, open_and_load_main_page, wait, city):
    main_page = MainPage(driver)
    main_page.fill_city_search_field(city)
    main_page.click_search_button()
    main_page.choose_1st_option(wait)
    main_page.switch_to_c_temp()
    main_page.check_8_lines_are_displayed()


def test_tc_021_01_01_visibility_of_agriculture_analytics_link(driver, open_and_load_main_page):
    main_page = MainPage(driver)
    main_page.visibility_of_agriculture_analytics_link()






import pytest
from PageObject .main_page import MainPage
from test_data.data_main_page import data


# def test_tc_000_00_search_city(driver, open_and_load_main_page):
#     page = MainPage(driver)
#     page.fill_city_search_field("New York")

@pytest.mark.parametrize('city', data["cityName"])
def test_tc_000_00_verify_requested_city_displayed_for_valid_input(driver, open_and_load_main_page, wait, city):
    page = MainPage(driver)
    page.check_search_city_result(wait, city)

# def test_tc_000_00_verify_no_results_displayed_for_invalid_input(driver, open_and_load_main_page, wait):
#     page = MainPage(driver)
#     page.check_search_city_result(wait, "Neverland")

def test_tc_000_00_verify_sign_in_link_opens_valid_page(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.click_header_link('sign')


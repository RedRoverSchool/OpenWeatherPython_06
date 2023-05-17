import pytest
from pages.main_page import MainPage
from test_data.main_page_data import data


@pytest.mark.parametrize('city', data["cityName"])
def test_tc_000_00_01_verify_requested_city_displayed_for_valid_input(driver, open_and_load_main_page, wait, city):
    page = MainPage(driver)
    page.check_seach_city_result(wait, city)


def test_tc_000_00_02_verify_no_results_displayed_for_invalid_input(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.check_seach_city_result(wait, 'Neverland')


def test_tc_000_00_02_verify_sing_in_link_opens_valid_page(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.check_header_link('sign')

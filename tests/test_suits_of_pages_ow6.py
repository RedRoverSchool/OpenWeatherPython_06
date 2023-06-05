import pytest
from test_data.urls import SuitsUrls
from pages.main_page import MainPage


@pytest.mark.parametrize('URL', SuitsUrls.URLs)
def test_tc_003_08_05_about_us_link_is_visible_on_each_page_specified_in_data(driver, URL):
    page = MainPage(driver, link=URL)
    page.open_page()
    page.check_about_us_link_is_visible()

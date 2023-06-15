import pytest
from oldTests.test_group_future_auto_qa.test_data.urls import *
from oldTests.test_group_future_auto_qa.pages.main_page import MainPageFooter


@pytest.mark.parametrize('URL', URLs)
def test_tc_003_08_06_verify_about_us_link_clickability(driver, open_and_load_main_page, URL):
    page = MainPageFooter(driver, link=URL)
    page.check_about_us_link_is_clickable()

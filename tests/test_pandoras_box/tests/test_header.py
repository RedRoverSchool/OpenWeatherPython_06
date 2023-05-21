import pytest
from tests.test_pandoras_box.test_data.header_data import URLs
from tests.test_pandoras_box.pages.header import Header

@pytest.mark.parametrize('URL', URLs)
def test_TC_002_01_03_Logo_is_visible(driver, URL):
    page = Header(driver, link=URL)
    page.open_page()
    page.check_logo_is_visible(Header.logo_locator)
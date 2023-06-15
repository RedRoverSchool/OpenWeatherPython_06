import pytest
from oldTests.test_group_zmeyki.pages.footer_page import FooterPage
from oldTests.test_group_zmeyki.test_data.urls import URLs


@pytest.mark.parametrize('URL', URLs)
def test_TC_003_02_01_Website_footer_visibility(driver, URL):
    page = FooterPage(driver, link=URL)
    page.open_page()
    page.website_footer_visibility()

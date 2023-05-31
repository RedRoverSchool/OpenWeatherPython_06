import pytest
from tests.test_group_roma.test_data.footer_data import data
from tests.test_group_roma.pages.footer import FooterWebsite
from tests.test_group_roma import links


@pytest.mark.parametrize('page', data["pages"])
def test_TC_003_01_01_verify_footer_is_visible_from_all_pages_specified_in_data(driver, page):
    footer = FooterWebsite(driver, f'{links.MAIN_PAGE}{page}')
    footer.open_page()
    footer.go_to_element(footer.footer_website_search_element())
    footer.check_footer_website_is_displayed(footer.footer_website_search_element())

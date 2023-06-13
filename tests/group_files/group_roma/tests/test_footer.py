import pytest
from tests.group_files.group_roma.test_data.footer_data import data
from tests.group_files.group_roma.pages.footer import FooterComponent
from tests.group_files.group_roma import links
from tests.group_files.group_roma.locators.locators import FooterLocators


@pytest.mark.parametrize('page', data["pages"])
def test_TC_003_01_01_verify_footer_is_visible_from_all_pages_specified_in_data(driver, page):
    footer = FooterComponent(driver, f'{links.MAIN_PAGE}{page}')
    footer.open_page()
    footer_actual_result = footer.search_element(FooterLocators.footer_website_locator)
    footer.go_to_element(footer_actual_result)
    footer.check_footer_website_is_displayed(footer_actual_result)


@pytest.mark.parametrize('page', data["pages"])
def test_TC_003_01_02_verify_copyright_is_visible_from_all_pages_specified_in_data(driver, page):
    footer = FooterComponent(driver, f'{links.MAIN_PAGE}{page}')
    footer.open_page()
    copyright_actual_result = footer.search_element(FooterLocators.copyright_locator)
    footer.go_to_element(copyright_actual_result)
    footer.check_copyright_is_displayed(copyright_actual_result)

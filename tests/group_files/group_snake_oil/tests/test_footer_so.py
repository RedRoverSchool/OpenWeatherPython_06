import pytest
from tests.group_files.group_snake_oil.links.all_links import ALL_PAGES_URLs
from tests.group_files.group_snake_oil.locators.footer_locators import FootersLocators
from tests.group_files.group_snake_oil.pages.footer import Footer
from tests.group_files.group_snake_oil.links.all_links import HOME_PAGE_URL


class TestFooter:
    @pytest.mark.parametrize('url', ALL_PAGES_URLs)
    def test_tc_003_04_01_verify_the_technologies_module_title_is_visible_on_each_page(self, driver, url):
        footer = Footer(driver, url)
        footer.open_page()
        footer.find_technologies_module()

    @pytest.mark.parametrize('icon', FootersLocators.FOOTER_TECHNOLOGIES_ICONS)
    @pytest.mark.parametrize('url', ALL_PAGES_URLs)
    def test_tc_003_04_02_visibility_clickability_links_technology_module(self, driver, url, icon):
        footer = Footer(driver, url)
        footer.open_page()
        footer.find_links_under_technologies_module(icon)

    def test_tc_001_15_03_verify_redirection_to_about_us_page(self, driver, wait):
        footer = Footer(driver, HOME_PAGE_URL)
        footer.open_page()
        footer.check_redirection_to_about_us_page(wait)


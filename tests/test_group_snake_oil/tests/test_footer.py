import pytest
from tests.test_group_snake_oil.links.all_links import ALL_PAGES_URLs
from tests.test_group_snake_oil.pages.footer import Footer


class TestFooter:
    @pytest.mark.parametrize('url', ALL_PAGES_URLs)
    def test_tc_003_04_01_verify_the_technologies_module_title_is_visible_on_each_page(self, driver, url):
        footer = Footer(driver, url)
        footer.open_page()
        expected_footer_text = "Technologies"
        element = footer.find_technologies_module()
        assert element.is_displayed() and expected_footer_text in element.text, \
            "The footer is not displayed or does not contain the expected text"



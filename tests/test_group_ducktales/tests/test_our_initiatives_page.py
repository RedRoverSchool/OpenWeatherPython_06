import pytest
from tests.test_group_ducktales.pages.our_initiatives_page import OurInitiativesPage
from tests.test_group_ducktales.test_data.our_initiatives_page_data import sections, OUR_INITIATIVES_PAGE


class TestOurInitiativesPage:
    @pytest.mark.parametrize("section", sections)
    def test_010_01_01_01_verify_sections(self, driver, open_and_load_main_page, section):
        page = OurInitiativesPage(driver, OUR_INITIATIVES_PAGE)
        page.open_page()
        page.click_initiatives_link()
        section_element = page.get_section_element(section)
        assert section_element.is_displayed(), f"Section '{section}' not found on the page"
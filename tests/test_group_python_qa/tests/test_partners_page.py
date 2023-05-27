from tests.test_group_python_qa.pages.partners_page import PartnersPage

class TestPartnersPage:
    def test_TC_011_09_01_link_See_library_visibility(self, driver):
        page = PartnersPage(driver)
        page.verify_link_See_library_visibility()


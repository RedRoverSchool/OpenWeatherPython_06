from tests.test_group_python_qa.pages.partners_page_pqa import PartnersPage


class TestPartnersPage:

    def test_tc_011_09_01_link_see_library_visibility(self, driver, wait):
        page = PartnersPage(driver, PartnersPage.PARTNERS_AND_SOLUTION_PAGE_URL)
        page.link_See_library_visibility(wait)


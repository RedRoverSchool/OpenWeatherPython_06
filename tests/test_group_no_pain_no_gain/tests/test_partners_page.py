from tests.test_group_no_pain_no_gain.pages.partners_page import Partners
from tests.test_group_no_pain_no_gain import links


class TestPartnersPage:
    def test_TC_011_01_01_verify_that_Partners_and_solutions_page_title_is_correct(self, driver):
        page = Partners(driver)
        page.check_partners_page_title()

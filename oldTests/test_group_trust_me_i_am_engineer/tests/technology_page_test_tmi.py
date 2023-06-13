from oldTests.test_group_trust_me_i_am_engineer.pages.technology_page import TechnologyPage
import pytest
def test_TC_001_16_02_verify_detailed_report_link_redirects_to_valid_page(driver):
    page = TechnologyPage(driver)
    page.verify_link_detailed_report_clickability_redirection()

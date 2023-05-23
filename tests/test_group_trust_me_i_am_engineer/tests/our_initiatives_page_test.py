from tests.test_group_trust_me_i_am_engineer.pages.our_initiatives_page import OurInitiativesPage
import pytest

def test_TC_010_01_03_verify_learn_more_link_redirects_to_valid_page(driver):
    page = OurInitiativesPage(driver)
    page.verify_learn_more_link_redirects_to_valid_page()
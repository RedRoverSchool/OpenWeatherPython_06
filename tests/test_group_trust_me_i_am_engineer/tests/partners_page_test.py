from tests.test_group_trust_me_i_am_engineer.pages.partners_page import PartnersPage
import pytest

def test_TC_011_03_01_verify_the_link_view_on_github_is_visible(driver):
    page = PartnersPage(driver)
    page.verify_the_link_view_on_github_is_visible()

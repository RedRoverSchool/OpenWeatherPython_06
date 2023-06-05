from tests.test_group_trust_me_i_am_engineer.pages.migrate_from_dark_sky_api_page import MigratePage
import pytest

def test_001_18_01_verify_subscribe_link_redirection(driver):
    page = MigratePage(driver)
    page.verify_subscribe_for_free_link_redirection()


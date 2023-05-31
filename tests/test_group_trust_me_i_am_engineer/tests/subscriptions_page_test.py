from tests.test_group_trust_me_i_am_engineer.pages.subscriptions_page import SubscriptionsPage
import pytest

def test_TC_018_01_05_verify_error_messages_for_empty_required_fields_in_organisation(driver):
    page = SubscriptionsPage(driver)
    page.verify_error_messages_for_empty_required_fields_in_organisation()


from oldTests.test_group_trust_me_i_am_engineer.pages.subscriptions_page import SubscriptionsPage
import pytest



def test_TC_018_01_05_verify_error_messages_for_empty_required_fields_in_organisation(driver):
    page = SubscriptionsPage(driver)
    page.verify_error_messages_for_empty_required_fields_in_organisation()


def test_TC_018_01_04_verify_redirect_to_payment_service_page_for_not_logged_in_user(driver):
    page = SubscriptionsPage(driver)
    page.verify_redirect_to_payment_service_page_for_not_logged_in_user_in_organisation()

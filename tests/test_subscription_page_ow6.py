from pages.subscription_page import SubscriptionPage

class TestSubscriptionPage:
    def test_TC_018_01_05_verify_error_messages_for_empty_required_fields_in_organisation(self, driver):
        page = SubscriptionPage(driver)
        page.verify_error_messages_for_empty_required_fields_in_organisation()

    def test_TC_018_01_04_verify_redirect_to_payment_service_page_for_not_logged_in_user(self, driver):
        page = SubscriptionPage(driver)
        page.verify_redirect_to_payment_service_page_for_not_logged_in_user_in_organisation()
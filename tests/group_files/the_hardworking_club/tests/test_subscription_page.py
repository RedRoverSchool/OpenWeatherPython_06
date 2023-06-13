from tests.group_files.the_hardworking_club.pages.subscription_page import SubscriptionPage

class TestSubscriptionPage():

    def test_tc_018_01_01_verify_redirection_payment_service_page_for_not_logged_in_user(self, driver):

        subscription_page = SubscriptionPage(driver)
        subscription_page.verify_redirection_payment_service_page_for_not_logged_in_user()



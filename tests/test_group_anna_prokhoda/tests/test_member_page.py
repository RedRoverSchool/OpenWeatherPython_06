import time

from tests.test_group_anna_prokhoda.pages.member_page import MemberPage


def test_tc_018_03_01_verify_redirection_to_payment_service_page_for_unauthorized_user(driver):
    member_page = MemberPage(driver)
    member_page.get_link('dev')
    member_page.fill_in_required_fields()
    member_page.click_continue_button()
    member_page.check_payment_url()


from tests.group_files.group_qa_anna_prokhoda.pages.member_page import MemberPage


'''
def test_tc_018_03_01_verify_redirection_to_payment_service_page_for_unauthorized_user(driver, wait):
    member_page = MemberPage(driver)
    member_page.get_link('dev')
    member_page.fill_in_required_fields()
    member_page.click_continue_button()
    #member_page.check_payment_url()
'''


def test_tc_018_03_02_verify_error_messages_appeared_when_submitting_blank_form(driver):
    member_page = MemberPage(driver)
    member_page.get_link('dev')
    member_page.click_continue_button()
    member_page.check_error_messages()
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from tests.test_group_anna_prokhoda.pages.member_page import MemberPage
from tests.test_group_anna_prokhoda.locators.member_page_loc import MemberPageLocators as locator

'''
def test_tc_018_03_01_verify_redirection_to_payment_service_page_for_unauthorized_user(driver, wait):
    member_page = MemberPage(driver)
    member_page.get_link('dev')
    member_page.fill_in_required_fields()
    member_page.click_continue_button()
    #wait.until(EC.presence_of_element_located(locator.payment))
    time.sleep(15)
    #window_after = driver.window_handles[1]
    #driver.switch_to_window(window_after)
    #member_page.check_payment_url()
'''


def test_tc_018_03_02_verify_error_messages_appeared_when_submitting_blank_form(driver):
    member_page = MemberPage(driver)
    member_page.get_link('dev')
    member_page.click_continue_button()
    member_page.check_error_messages()

    
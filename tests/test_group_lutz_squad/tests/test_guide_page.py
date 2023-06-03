import time

from tests.test_group_lutz_squad.pages.guide_page import GuidePage
from tests.test_group_lutz_squad.locators.guide_page_locators import GuidePageLocators


def test_TC_004_06_01_verify_industry_standart_apis_link_is_visible_and_clickable(driver, wait):
    page = GuidePage(driver, link=GuidePageLocators.GUIDE_PAGE_LINK)
    page.open_page()
    page.industry_apis_link_is_visible_and_clickable()


def test_TC_004_06_05_verify_industry_standart_apis_link_color(driver, wait):
    page = GuidePage(driver, link=GuidePageLocators.GUIDE_PAGE_LINK)
    page.open_page()
    page.industry_check_color()

def test_TC_004_06_03_verify_redirection_industry_standard_apis_link(driver, wait):
    page = GuidePage(driver, link=GuidePageLocators.GUIDE_PAGE_LINK)
    page.open_page()
    page.industry_standard_apis_link_redirection()


def test_TC_004_06_04_verify_redirection_one_call_api_by_call_link(driver, wait):
    page = GuidePage(driver, link=GuidePageLocators.GUIDE_PAGE_LINK)
    page.open_page()
    page.one_call_api_by_call_link_redirection()
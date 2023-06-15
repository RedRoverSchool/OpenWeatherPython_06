from oldTests.test_pandoras_box.pages.guide_page import GuidePage
from locators.locators import GuideLocators

def test_tc_002_03_03_01_open_guide(driver, open_and_load_main_page):
    guide_page = GuidePage(driver)
    guide_page.check_header_title("guide")


def test_tc_004_05_01(driver):
    driver.get(GuideLocators.GUIDE_URL)
    for url_locators in GuideLocators.guide_fast_way_links_locators:
        link_fast_way = driver.find_element(*url_locators)
        assert link_fast_way.is_displayed()

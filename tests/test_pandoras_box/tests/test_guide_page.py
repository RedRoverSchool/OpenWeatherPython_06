from tests.old.test_pandoras_box import GuidePage


def test_tc_002_03_03_01_open_guide(driver, open_and_load_main_page):
    guide_page = GuidePage(driver)
    guide_page.check_header_title("guide")
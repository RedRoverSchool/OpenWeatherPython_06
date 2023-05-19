from tests.test_group_ducktales.pages.main_page import MainPage
from tests.test_group_ducktales.test_data.main_page_data import *


class TestMainPage:

    def test_rf_tc_001_04_03_verify_in_day_list_first_element_day_by_week(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        day_by_weak = page.get_day_by_weak()
        day_by_computer = page.day_by_computer()
        assert day_by_weak == f'{day_by_computer}'

    def test_tc_003_09_01_the_module_title_display(self, driver):
        page = MainPage(driver, LINK_MAIN_PAGE)
        page.open_page()
        page.check_module_title_download_openweather_app()





from tests.group_files.group_ducktales.pages.main_page_d import MainPage


class TestMainPage:

    def test_tc_001_04_03_verify_in_day_list_first_element_day_by_week(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_day()

    def test_tc_003_09_01_the_module_title_display(self, driver):
        page = MainPage(driver, LINK_MAIN_PAGE)
        page.open_page()
        page.check_module_title_download_openweather_app()

    def test_tc_003_09_02_app_store_brand_link_display(self, driver):
        page = MainPage(driver, LINK_MAIN_PAGE)
        page.open_page()
        page.check_app_store_brand_link_display()

    def test_tc_001_02_04_01_switch_toggle_buttons(self, driver):
        page = MainPage(driver, LINK_MAIN_PAGE)
        page.open_page()
        page.check_buttons_displayed_and_enabled()

    def test_tc_003_09_03_app_store_brand_link_clickable(self, driver):
        page = MainPage(driver, LINK_MAIN_PAGE)
        page.open_page()
        page.check_app_store_brand_link_clickable()

    def test_tc_003_09_04_google_play_brand_link_clickable(self, driver):
        page = MainPage(driver, LINK_MAIN_PAGE)
        page.open_page()
        page.check_google_play_brand_link_clickable()

    def test_tc_003_09_04_google_play_brand_link_display(self, driver):
        page = MainPage(driver, LINK_MAIN_PAGE)
        page.open_page()
        page.check_google_play_brand_link_display()

    def test_tc_001_04_04_verify_in_day_list_first_element_month(self, driver, open_and_load_main_page):
        page = MainPage(driver, LINK_MAIN_PAGE)
        page.open_page()
        page.check_months()

    def test_tc_001_01_02_main_page_search_city_dropdown_options_valid_value(self, driver):
        page = MainPage(driver, LINK_MAIN_PAGE)
        page.open_page()
        page.check_dropdown_options()

    def test_tc_001_01_01_verify_city_name_displayed_by_zip(self, driver, wait, open_and_load_main_page):
        page = MainPage(driver)
        page.check_city_name_displayed_by_zip(wait)

    def test_tc_001_04_07_verify_day_list_elements_numbers_days(self, driver, wait, open_and_load_main_page):
        page = MainPage(driver)
        page.check_in_day_list_numbers_days(driver)

    def test_tc_001_04_05_verify_in_day_list_first_element_number_day(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_in_day_list_first_element_number_day()

    def test_TC_001_04_06_verify_in_day_list_days_of_the_week(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_in_day_list_days_of_the_week()




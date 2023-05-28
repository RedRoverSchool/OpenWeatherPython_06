from tests.test_group_byte_me.pages.main_page import MainPage


class TestMainPageHeader:

    def test_tc_002_02_01_01_search_city_results_are_visible(self, driver, wait, open_and_load_main_page):
        main_page = MainPage(driver)
        main_page.click_header_weather_in_your_city_field()
        main_page.fill_header_weather_in_your_city_field()
        main_page.displayed_text_is_the_same_as_the_entered_text(wait=wait)



    def test_tc_001_01_01_02_searching_requested_city_name_displayed_in_widget(self, driver, wait, open_and_load_main_page):
        main_page = MainPage(driver)
        main_page.check_search_city_result(wait, 'Kyiv, UA')
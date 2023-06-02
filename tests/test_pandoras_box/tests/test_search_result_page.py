from tests.test_pandoras_box.pages.search_result_page import SearchResultPage
from tests.test_pandoras_box.pages.main_page import MainPage



def test_TC_002_02_03_verify_result_of_search_for_invalid_city_name(driver, open_and_load_main_page):
    main_page = MainPage(driver)
    main_page.enter_city_in_weather_in_your_city_field('LJKJJ')
    main_page.press_enter_button()
    search_result_page = SearchResultPage(driver)
    search_result_page.check_notification_display()

def test_TC_002_02_06_verify_closing_of_NotFound_notification(driver, open_and_load_main_page, wait):
    main_page = MainPage(driver)
    main_page.enter_city_in_weather_in_your_city_field('LJKJJ')
    main_page.press_enter_button()
    search_result_page = SearchResultPage(driver)
    search_result_page.check_notification_is_closed()

def test_TC_002_02_04_verify_displaying_entered_city_name_in_Search_field(driver, open_and_load_main_page, wait):
    main_page = MainPage(driver)
    main_page.enter_city_in_weather_in_your_city_field(' ljKJJ')
    main_page.press_enter_button()
    search_result_page = SearchResultPage(driver)
    search_result_page.check_correspondence_of_entered_text(' ljKJJ')

def test_TC_001_01_08_dropdown_list_contain_city_temperature(driver, open_and_load_main_page, wait):
    search_result = SearchResultPage(driver)
    search_result.dropdown_contain_city_temperature()

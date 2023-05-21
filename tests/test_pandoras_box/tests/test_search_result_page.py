from tests.old.test_pandoras_box import SearchResultPage
from tests.old.test_pandoras_box import MainPage



def test_TC_002_02_03_verify_result_of_search_for_invalid_city_name(driver, open_and_load_main_page):
    main_page = MainPage(driver)
    main_page.enter_city_in_weather_in_your_city_field('LJKJJ')
    main_page.press_enter_button()
    search_result_page = SearchResultPage(driver)
    search_result_page.check_notification_display()







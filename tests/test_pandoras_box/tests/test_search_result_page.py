from tests.test_pandoras_box.pages.search_result_page import SearchResultPage
from tests.test_pandoras_box.pages.base_page import BasePage
def test_TC_002_02_03_verify_result_of_search_for_invalid_city_name(driver, open_and_load_main_page):
    base_page = BasePage(driver)
    base_page.enter_city_in_weather_in_your_city_field('LJKJJ')
    base_page.press_enter_button()
    search_result_page = SearchResultPage(driver)
    search_result_page.check_notification_display()



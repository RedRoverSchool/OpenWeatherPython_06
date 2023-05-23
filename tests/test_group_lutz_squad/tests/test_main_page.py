from tests.test_group_lutz_squad.pages.main_page import MainPage

def test_TC_001_01_02_01_displaying_requested_city_name_in_the_search_field(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.check_search_city_result(wait, 'Minsk')

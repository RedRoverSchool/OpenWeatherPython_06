from tests.group_files.group_lutz_squad.pages.main_page import MainPage

def test_TC_001_01_02_01_displaying_requested_city_name_in_the_search_field(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.check_search_city_result(wait, 'Minsk')

def test_TC_003_12_07_about_us_link_leads_to_correct_page(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.about_us_link_leads_to_correct_page()


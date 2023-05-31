from ..pages.main_page import MainPage
import pytest

def test_tc_001_04_06_1_verify_visibility_of_week_days_in_8_days_forecast(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.verify_weekdays_in_8_days_forecast()

def test_TC_001_02_01_verify_temperature_switched_on_metric_system(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.checking_the_temperature_system_switching("°C")

def test_TC_001_02_02_verify_temperature_switched_on_imperial_system(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.checking_the_temperature_system_switching("°F")

def test_TC_001_02_03_verify_temperature_metric_button_displayed_clickable(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.verify_temperature_button_displayed_clickable("°C")

def test_TC_001_02_04_verify_temperature_imperial_button_displayed_clickable(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.verify_temperature_button_displayed_clickable("°F")

def test_TC_001_05_01_verify_the_current_date_and_time(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.verify_the_current_date_and_time()

def test_TC_001_05_02_verify_current_location(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.verify_current_location(wait)

def test_TC_003_12_09_verify_pricing_link_leads_to_a_correct_page(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.verify_pricing_link_leads_to_a_correct_page()

def test_TC_008_01_03_01_check_a_visibility_of_pricing_page_title(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.check_a_visibility_of_pricing_page_title()

def test_TC_003_08_04_verify_the_link_openweather_for_business_is_visible(driver,open_and_load_main_page):
    page = MainPage(driver)
    page.verify_the_link_openweather_for_business_is_visible()

def test_TC_003_12_13_verify_link_LinkedIn_leads_to_the_correct_page_with_unauthorized_linkedin_user(driver,open_and_load_main_page, wait):
    page = MainPage(driver)
    page.verify_link_LinkedIn_leads_to_the_correct_page()

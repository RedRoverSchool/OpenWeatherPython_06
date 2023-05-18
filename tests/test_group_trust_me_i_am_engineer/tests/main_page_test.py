from tests.test_group_trust_me_i_am_engineer.pages.main_page import MainPage
import pytest

def test_tc_001_04_06_1_verify_visibility_of_week_days_in_8_days_forecast(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.verify_weekdays_8days_forecast()

def test_TC_001_02_01_verify_temperature_switched_on_metric_system(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.checking_the_temperature_system_switching("°C")
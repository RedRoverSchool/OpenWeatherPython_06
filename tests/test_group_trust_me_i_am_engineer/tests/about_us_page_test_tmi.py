from tests.test_group_trust_me_i_am_engineer.pages.about_us_page import AboutUsPage

from ..pages.main_page import MainPage
from conftest import load_div
from selenium.webdriver.support import expected_conditions as EC

def test_tc_001_15_01_verify_correct_header_about_us_page(driver, wait):
    page = MainPage(driver, MainPage.URL)
    page.open_page()
    wait.until_not(EC.presence_of_element_located(load_div))
    page.allow_all_cookies()
    page.go_to_about_us_page()

    new_page = AboutUsPage(driver)

    new_page.verify_correct_header_about_us_page(wait)


def test_tc_001_15_02_verify_image_beside_header_is_displayed(driver, wait):
    page = MainPage(driver, MainPage.URL)
    page.open_page()
    wait.until_not(EC.presence_of_element_located(load_div))
    page.allow_all_cookies()
    page.go_to_about_us_page()

    new_page = AboutUsPage(driver)

    new_page.verify_image_beside_header_is_displayed(wait)


def test_tc_001_15_05_there_are_five_headers_on_the_page_about_us_footer(driver, wait):
    page = MainPage(driver, MainPage.URL)
    page.open_page()
    wait.until_not(EC.presence_of_element_located(load_div))
    page.allow_all_cookies()
    page.go_to_about_us_page()

    new_page = AboutUsPage(driver)

    new_page.verify_five_headers_on_the_page_about_us_footer(wait)

def test_tc_001_15_07_verify_redirection_to_weather_category_blog_page(driver, wait):
    page = MainPage(driver, MainPage.URL)
    page.open_page()
    wait.until_not(EC.presence_of_element_located(load_div))
    page.allow_all_cookies()
    page.go_to_about_us_page()

    new_page = AboutUsPage(driver)
    new_page.click_news_and_updates_button()

    new_page.verify_current_url("News and Updates", "https://openweather.co.uk/blog/category/weather")

def test_tc_001_15_10_verify_redirection_to_app_store(driver, wait):
    page = MainPage(driver, MainPage.URL)
    page.open_page()
    wait.until_not(EC.presence_of_element_located(load_div))
    page.allow_all_cookies()
    page.go_to_about_us_page()

    new_page = AboutUsPage(driver)
    new_page.click_on_app_store_button()

    new_page.verify_element_on_current_url()


from tests.test_group_trust_me_i_am_engineer.pages.about_us_page import AboutUsPage

def test_tc_001_15_01_verify_correct_header_about_us_page(driver, wait):
    about_us_page = AboutUsPage(driver)
    about_us_page.open()

    about_us_page.verify_correct_header_about_us_page(wait)

def test_tc_001_15_02_verify_image_beside_header_is_displayed(driver, wait):
    about_us_page = AboutUsPage(driver)
    about_us_page.open()

    about_us_page.verify_image_beside_header_is_displayed(wait)

def test_tc_001_15_05_there_are_five_headers_on_the_page_about_us_footer(driver, wait):
    about_us_page = AboutUsPage(driver)
    about_us_page.open()

    about_us_page.verify_five_headers_on_the_page_about_us_footer(wait)

def test_tc_001_15_07_verify_redirection_to_weather_category_blog_page(driver, wait):
    about_us_page = AboutUsPage(driver)
    about_us_page.open()
    about_us_page.allow_all_cookies()
    about_us_page.click_news_and_updates_button()

    about_us_page.verify_current_url("News and Updates", "https://openweather.co.uk/blog/category/weather")

def test_tc_001_15_10_verify_redirection_to_app_store(driver, wait):
    about_us_page = AboutUsPage(driver)
    about_us_page.open()
    about_us_page.allow_all_cookies()
    about_us_page.click_on_app_store_button()

    about_us_page.verify_element_on_current_url()

def test_tc_001_15_11_verify_cursor_transformation_after_hovering_over_on_element(driver, wait):
    about_us_page = AboutUsPage(driver)
    about_us_page.open()
    element = about_us_page.element_is_visible(about_us_page.page_locators.BYU_BY_SUBSCRIPTIONS)

    about_us_page.check_cursor_style_transformation(element)



from pages.about_us_page import AboutUsPage
from pages.blog_weather_category_page import BlogWeatherCategoryPage
from pages.main_page import MainPage


class TestAboutUsPage:

    def test_tc_001_15_07_verify_redirection_to_weather_category_blog_page(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.go_to_about_us_page_from_main_page(driver)

        about_us_page = AboutUsPage(driver)
        about_us_page.click_news_and_updates_button()
        about_us_page.driver.switch_to.window(about_us_page.driver.window_handles[1])

        blog_category_weather_page = BlogWeatherCategoryPage(driver)
        blog_category_weather_page.verify_page_url("News and Updates", blog_category_weather_page.URL)



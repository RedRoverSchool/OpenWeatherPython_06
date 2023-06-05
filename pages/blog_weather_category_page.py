from pages.base_page import BasePage

class BlogWeatherCategoryPage(BasePage):

    URL = "https://openweather.co.uk/blog/category/weather"

    def verify_page_url(self, button, expected_link):
        page_url = self.driver.current_url
        assert page_url == expected_link, button + " button link is not correct"


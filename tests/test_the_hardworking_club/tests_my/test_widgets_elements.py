from tests.test_the_hardworking_club.pages.widgets_page import WidgetsPage


class TestWidgets:

    def test_TC_001_09_04_YourAPIKey_fields_visible(self, driver):

        widgets_page = WidgetsPage(driver, 'https://openweathermap.org/widgets-constructor')
        widgets_page.open()
        display, enable = widgets_page.check_api_key_field()
        assert display == True and enable == True

    def test_TC_001_09_04_01_YourCityName_fields_visible(self, driver):

        widgets_page = WidgetsPage(driver, 'https://openweathermap.org/widgets-constructor')
        widgets_page.open()
        display, enable = widgets_page.check_city_name()
        assert display == True and enable == True


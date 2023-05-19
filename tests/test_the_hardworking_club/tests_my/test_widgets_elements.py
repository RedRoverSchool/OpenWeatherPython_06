from tests.test_the_hardworking_club.pages.widgets_page import WidgetsPage


class TestWidgets:

    def test_TC_001_09_04_Input_fields_visible(self, driver):

        widgets_page = WidgetsPage(driver, 'https://openweathermap.org/widgets-constructor')
        widgets_page.open_page()





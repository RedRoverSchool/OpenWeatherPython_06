from oldTests.test_the_hardworking_club.pages.widgets_page import WidgetsPage


class TestWidgets:


    def test_TC_001_09_04_Input_fields_visible(self, driver):

        widgets_page = WidgetsPage(driver)
        widgets_page.check_input_fields()

    def test_TC_001_09_07_verify_display_of_bottom_widget_1_for_selected_type(self, driver):

        widgets_page = WidgetsPage(driver)
        widgets_page.verify_display_of_bottom_widget_1_for_selected_type()


    def test_TC_001_09_08_select_the_specific_city(self, driver, wait):

        widgets_page = WidgetsPage(driver)
        widgets_page.check_the_specific_city_is_present(wait)


    def test_TC_001_09_02_verify_that_3_widgets_are_displayed(self, driver):

        widgets_page = WidgetsPage(driver)
        widgets_page.verify_that_3_widgets_are_displayed()

    def test_TC_001_09_14_verify_the_subtitle_of_the_page(self, driver):

        widget_page = WidgetsPage(driver)
        widget_page.verify_the_subtitle_of_the_page()


    def test_TC_001_09_04_verify_visibility_of_fahrenheit(self, driver):
        widget_page = WidgetsPage(driver)
        widget_page.verify_visibility_of_fahrenheit()

    def test_TC_001_09_03_verify_visibility_of_celsius(self, driver):
        widget_page = WidgetsPage(driver)
        widget_page.verify_visibility_of_celsius()
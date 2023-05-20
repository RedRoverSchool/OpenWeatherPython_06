from tests.test_the_hardworking_club.pages.widgets_page import WidgetsPage


class TestWidgets:


    def test_TC_001_09_04_Input_fields_visible(self, driver):

        widgets_page = WidgetsPage(driver)
        widgets_page.check_input_fields()

    def test_TC_001_09_07_verify_display_of_bottom_widget_1_for_selected_type(self, driver):

        widgets_page = WidgetsPage(driver)
        widgets_page.verify_display_of_bottom_widget_1_for_selected_type()





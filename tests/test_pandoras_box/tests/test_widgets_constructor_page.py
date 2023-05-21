from tests.test_pandoras_box.pages.widgets_constructor_page import WidgetsConstructor
def test_TC_001_09_05_switched_on_Celsius(driver):
    page = WidgetsConstructor(driver, link=WidgetsConstructor.widget_constructor_URL)
    page.open_page()
    page.check_switched_temperature_units('celsius')
from tests.test_the_hardworking_club.pages.weather_dashboard_page_1 import DashboardPage


class TestWeatherDashboard:

    def test_TC_006_05_03_verify_the_button_Contact_Us_works(self, driver):

        dashboard_page = DashboardPage(driver)
        dashboard_page.verify_the_button_Contact_Us_works()

    def test_006_05_04_button_leads_to_the_correct_page(self, driver):

        button_click = DashboardPage(driver)
        button_click.button_leads_to_the_correct_page()

    def test_TC_006_01_12_verify_weather_dashboard_full_description(self, driver):

        dashboard_page = DashboardPage(driver)
        dashboard_page.verify_weather_dashboard_full_description()






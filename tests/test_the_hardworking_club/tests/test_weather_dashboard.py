from tests.test_the_hardworking_club.pages.weather_dashboard_page_1 import DashboardPage


class TestWeatherDashboard:

    def test_TC_006_05_03_verify_the_button_Contact_Us_works(self, driver):

        dashboard_page = DashboardPage(driver)
        dashboard_page.verify_the_button_Contact_Us_works()


from tests.test_pandoras_box.pages.weather_dashboard_page import WeatherDashboard

def test_TC_006_04_04_pricing_plans_are_visible(driver):
    page = WeatherDashboard(driver, link=WeatherDashboard.dashboard_URL)
    page.open_page()
    page.check_pricing_plans()

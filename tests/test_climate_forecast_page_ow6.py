from locators.locators import ClimateForecastLocators as CFL
from pages.climate_forecast_page import ClimaticForecast


class TestClimaticForecast30:
    def test_tc_005_06_1_visibility_climatic_forecast_30_days_page_title(self, driver):
        page = ClimaticForecast(driver, CFL.URL_FORCAST30)
        page.open_page()
        page.check_visibility_climatic_forecast_30_days_page_title()

    def test_tc_005_06_02_redirect_to_the_how_to_make_an_api_call_section_of_the_page(self, driver):
        page = ClimaticForecast(driver, CFL.URL_FORCAST30)
        page.open_page()
        page.check_redirect_to_the_how_to_make_of_the_page()
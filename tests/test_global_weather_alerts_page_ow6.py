import pytest

from pages.global_weather_alerts_page import GlobalWeatherAlertsPage
from test_data.urls import ApiPageUrls


class TestGlobalWeatherAlertsPage:

    def test_TC_005_13_01_verify_7_anchor_links_redirect_to_correct_part_of_the_page(self, driver):
        page = GlobalWeatherAlertsPage(driver, ApiPageUrls.GLOBAL_WEATHER_ALERTS_LINK)
        page.open_page()
        page.verify_redirection_of_7_anchor_links()

import pytest

from pages.global_weather_alerts_page import GlobalWeatherAlertsPage
from test_data.urls import ApiPageUrls


class TestGlobalWeatherAlertsPage:

    def test_TC_005_13_04_verify_7_anchor_links_redirect_to_correct_part_of_the_page(self, driver):
        page = GlobalWeatherAlertsPage(driver, ApiPageUrls.GLOBAL_WEATHER_ALERTS_LINK)
        page.open_page()
        page.verify_redirection_of_7_anchor_links()

    def test_TC_005_13_05_verify_visibility_and_headings_of_5_blocks_of_the_page(self, driver):
        page = GlobalWeatherAlertsPage(driver, ApiPageUrls.GLOBAL_WEATHER_ALERTS_LINK)
        page.open_page()
        page.verify_visibility_and_headings_correctness_of_5_blocks_()

    def test_TC_005_13_06_verify_16_body_links_have_the_same_color(self, driver):
        page = GlobalWeatherAlertsPage(driver, ApiPageUrls.GLOBAL_WEATHER_ALERTS_LINK)
        page.open_page()
        page.verify_16_body_links_have_the_same_color()

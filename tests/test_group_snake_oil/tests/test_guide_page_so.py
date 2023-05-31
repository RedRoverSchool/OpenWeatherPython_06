import pytest

from tests.test_group_snake_oil.links.all_links import GUIDE_PAGE_URL
from tests.test_group_snake_oil.pages.guide_page import GuidePage
from tests.test_group_snake_oil.locators.guide_page_locators import GuidePageLocators


class TestGuidePage:

    @pytest.mark.parametrize("link_title, locator", [
        ("Solar Irradiance & Energy Prediction API", GuidePageLocators.SOLAR_IRRADIANCE_ENERGY_PREDICTION_API_LINK),
        ("Global Weather Alerts", GuidePageLocators.GLOBAL_WEATHER_ALERTS_LINK),
        ("Road Risk API", GuidePageLocators.ROAD_RISK_API_LINK),
        ("Global Precipitation Maps - Forecast and historical data", GuidePageLocators.GLOBAL_PRECIPITATION_MAPS_LINK),
        ("Weather Maps 2.0 with 1-hour step", GuidePageLocators.WEATHER_MAPS_2_0_WITH_1_HOUR_STEP_LINK)
    ])
    def test_tc_004_03_02_verify_links_clickability_in_dedicated_weather_products(self, driver, link_title, locator):
        guide_page = GuidePage(driver, GUIDE_PAGE_URL)
        guide_page.open_page()
        link = guide_page.element_is_visible(locator)
        assert link.is_enabled(), f"Link {link_title} is not clickable"

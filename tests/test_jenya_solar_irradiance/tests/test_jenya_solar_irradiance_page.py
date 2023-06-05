import pytest
from pages.base_page import BasePage
from pages.solar_irradiance_page import SolarIrradiancePage


def test_TC_005_09_01_verify_solar_irradiance_description(driver):
    description = SolarIrradiancePage(driver)
    description.verify_description_visibility()

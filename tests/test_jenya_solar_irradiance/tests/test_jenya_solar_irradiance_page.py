from tests.test_jenya_solar_irradiance.pages.solar_irradiance_page import SolarIrradiancePage
from locators.locators import SolarIrradianceLocators
def test_TC_005_09_01_verify_solar_irradiance_description(driver):
    page = SolarIrradiancePage(driver, SolarIrradianceLocators.URL_SolarIrradiancePage)
    page.open_page()
    page.verify_description_visibility()

def test_TC_005_09_03_verify_the_most_common_indices_description(driver):
    page = SolarIrradiancePage(driver, SolarIrradianceLocators.URL_SolarIrradiancePage)
    page.open_page()
    page.verify_indices_visibility()

def test_TC_005_09_03_verify_reference_data_visibility(driver):
    page = SolarIrradiancePage(driver, SolarIrradianceLocators.URL_SolarIrradiancePage)
    page.open_page()
    page.verify_reference_data_visibility()

def test_TC_005_09_04_verify_Clear_Sky_model_algorithms_visibility(driver):
    page = SolarIrradiancePage(driver, SolarIrradianceLocators.URL_SolarIrradiancePage)
    page.open_page()
    page.verify_Clear_Sky_model_visibility()


def test_TC_005_09_05_verify_Cloudy_Sky_model_algorithms_visibility(driver):
    page = SolarIrradiancePage(driver, SolarIrradianceLocators.URL_SolarIrradiancePage)
    page.open_page()
    page.verify_Cloudy_Sky_model_visibility()


def test_TC_005_09_06_verify_image_visibility(driver):
    page = SolarIrradiancePage(driver, SolarIrradianceLocators.URL_SolarIrradiancePage)
    page.open_page()
    page.verify_image_visibility()
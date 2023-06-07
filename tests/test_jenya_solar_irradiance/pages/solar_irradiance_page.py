from pages.base_page import BasePage
from locators.locators import SolarIrradianceLocators




class SolarIrradiancePage(BasePage):
    locators = SolarIrradianceLocators()


    def verify_description_visibility(self):
        locator = self.locators.SOLAR_IRRADIANCE_DESC
        element = self.driver.find_element(*locator)
        assert element.is_displayed()
#check description visibility
    def verify_indices_visibility(self):
        locators = [self.locators.INDICES_DHI, self.locators.INDICES_DNI, self.locators.INDICES_GHI]

        for locator in locators:
            element = self.driver.find_element(*locator)
            assert element.is_displayed()


    def verify_reference_data_visibility(self):
        locator = self.locators.REFERENCE_DATA
        element = self.driver.find_element(*locator)
        assert element.is_displayed()

    def verify_Clear_Sky_model_visibility(self):
        locator = self.locators.CLEAR_SKY_MODEL
        element = self.driver.find_element(*locator)
        assert element.is_displayed()


    def verify_Cloudy_Sky_model_visibility(self):
        locator = self.locators.CLOUDY_SKY_MODEL
        element = self.driver.find_element(*locator)
        assert element.is_displayed()

    def verify_image_visibility(self):
        locator = self.locators.IMAGE_SOLAR_RADIATION
        element = self.driver.find_element(*locator)
        assert element.is_displayed()
# check link clickability

#check table visibility
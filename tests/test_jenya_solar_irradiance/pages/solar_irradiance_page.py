from pages.base_page import BasePage
from locators.locators import SolarIrradianceLocators




class SolarIrradiancePage(BasePage):
    locators = SolarIrradianceLocators()


    def verify_description_visibility(self):
        locator = self.locators.SOLAR_IRRADIANCE_DESC
        element = self.driver.find_element(*locator)
        assert element.is_displayed()
#check description visibility

# check link hover

# check link clickability

#check table visibility
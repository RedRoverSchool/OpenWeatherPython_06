from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SolarIrradiancePage(BasePage):
    URL_SolarIrradiancePage = "https://openweathermap.org/api/solar-radiation/behind-solar-radiation-api#introduction"

    SOLAR_IRRADIANCE_DESC = (By.CSS_SELECTOR, "section#introduction")
    INDICES_DNI = (By.CSS_SELECTOR, "#introduction ul li:nth-child(1)")
    INDICES_DHI  = (By.CSS_SELECTOR, "#introduction ul li:nth-child(2)")
    INDICES_GHI = (By.CSS_SELECTOR, "#introduction ul li:nth-child(3)")
    REFERENCE_DATA = (By.CSS_SELECTOR, "section#reference")
    CLEAR_SKY_MODEL = (By.CSS_SELECTOR, "section#clearsky")
    CLOUDY_SKY_MODEL = (By.CSS_SELECTOR, "section#cloudysky")
    IMAGE_SOLAR_RADIATION = (By.CSS_SELECTOR, "#cloudysky img")
    SOLAR_IRRADIANCE_AND_ENERGY_PREDICTION_LINK = (By.CSS_SELECTOR, "p a[href='/api/solar-energy-prediction']")
    SOLIS_LINK = (By.CSS_SELECTOR, "[href='https://github.com/pvlib/pvlib-python/blob/709daa6f8feddb50ae50b1da13f5f720d8ebb78f/pvlib/clearsky.py#L406']")
    DATASETS_AND_PRODUCTS_LINK_CLOUDY = (By.CSS_SELECTOR, "#cloudysky [href='/api']")
    DATASETS_AND_PRODUCTS_LINK_REFERENCE = (By.CSS_SELECTOR, '#reference [href="/api"]')
    DIRINT_LINK = (By.CSS_SELECTOR, "[href='https://github.com/pvlib/pvlib-python/blob/709daa6f8feddb50ae50b1da13f5f720d8ebb78f/pvlib/irradiance.py#L1277']")
    CAMS_LINK = (By.CSS_SELECTOR, "[href='https://atmosphere.copernicus.eu/solar-radiation']")
    TECHNICAL_SUPPORT_LINK = (By.CSS_SELECTOR, "a[ href='mailto:info@openweathermap.org']")
    TABLE_OF_CONTENTS = (By.CSS_SELECTOR, "div nav")




    def verify_description_visibility(self):
        locator = (self.SOLAR_IRRADIANCE_DESC)
        assert locator
#check description visibility

# check link hover

# check link clickability

#check table visibility
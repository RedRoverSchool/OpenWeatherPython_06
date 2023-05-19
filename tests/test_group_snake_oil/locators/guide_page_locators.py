from selenium.webdriver.common.by import By


class GuidePageLocators:
    SOLAR_IRRADIANCE_ENERGY_PREDICTION_API_LINK = (By.CSS_SELECTOR, "li>a[href*='solar-energy-prediction']")
    GLOBAL_WEATHER_ALERTS_LINK = (By.CSS_SELECTOR, "li>a[href*='push-weather-alerts']")
    ROAD_RISK_API_LINK = (By.CSS_SELECTOR, "li>a[href*='road-risk']")
    GLOBAL_PRECIPITATION_MAPS_LINK = (By.CSS_SELECTOR, "li>a[href*='global-precipitation-map-forecast']")
    WEATHER_MAPS_2_0_WITH_1_HOUR_STEP_LINK = (By.CSS_SELECTOR, "li>a[href*='weather-map-1h']")

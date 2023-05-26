from selenium.webdriver.common.by import By


class IndustriesPageLocators:
    UPPER_TALK_TO_US_BUTTON = (By.XPATH, "(//a[text()='Talk to us'])[1]")
    INSURANCE_TALK_TO_US_BUTTON = (By.XPATH, "(//a[text()='Talk to us'])[2]")
    RETAIL_TALK_TO_US_BUTTON = (By.XPATH, "(//a[text()='Talk to us'])[3]")
    AUTOMOTIVE_TALK_TO_US_BUTTON = (By.XPATH, "(//a[text()='Talk to us'])[4]")
    ADVERTISING_TALK_TO_US_BUTTON = (By.XPATH, "(//a[text()='Talk to us'])[5]")
    ENERGY_TALK_TO_US_BUTTON = (By.XPATH, "(//a[text()='Talk to us'])[6]")
    AGRICULTURE_TALK_TO_US_BUTTON = (By.XPATH, "(//a[text()='Talk to us'])[7]")
    SHALL_WE_SPEAK_TALK_TO_US_BUTTON = (By.XPATH, "(//a[text()='Talk to us'])[8]")

    talk_to_us_buttons_locators = [UPPER_TALK_TO_US_BUTTON, INSURANCE_TALK_TO_US_BUTTON, RETAIL_TALK_TO_US_BUTTON,
                                   AUTOMOTIVE_TALK_TO_US_BUTTON, ADVERTISING_TALK_TO_US_BUTTON,
                                   ENERGY_TALK_TO_US_BUTTON,
                                   AGRICULTURE_TALK_TO_US_BUTTON, SHALL_WE_SPEAK_TALK_TO_US_BUTTON]

    INSURANCE_REQUEST_A_TRIAL_BUTTON = (By.XPATH, "(//a[text()='Request a trial'])[1]")
    RETAIL_REQUEST_A_TRIAL_BUTTON = (By.XPATH, "(//a[text()='Request a trial'])[2]")
    AUTOMOTIVE_REQUEST_A_TRIAL_BUTTON = (By.XPATH, "(//a[text()='Request a trial'])[3]")
    ADVERTISING_REQUEST_A_TRIAL_BUTTON = (By.XPATH, "(//a[text()='Request a trial'])[4]")
    ENERGY_REQUEST_A_TRIAL_BUTTON = (By.XPATH, "(//a[text()='Request a trial'])[5]")

    request_a_trial_buttons_locators = [INSURANCE_REQUEST_A_TRIAL_BUTTON, RETAIL_REQUEST_A_TRIAL_BUTTON,
                                        AUTOMOTIVE_REQUEST_A_TRIAL_BUTTON, ADVERTISING_REQUEST_A_TRIAL_BUTTON,
                                        ENERGY_REQUEST_A_TRIAL_BUTTON]

    LEARN_MORE_BUTTON = (By.XPATH, "//a[text()='Learn more']")


    CURRENT_AND_FORECAST_IMAGE = (By.XPATH, "//div[@class='current-img white-text half-section-right main-section-desktop']")
    HISTORICAL_WEATHER_IMAGE = (By.XPATH, "//div[@class='history-img half-section-left main-section-desktop']")
    WEATHER_ALERTS_IMAGE = (By.XPATH, "//div[@class='alerts-img white-text half-section-right main-section-desktop']")
    WEATHER_MAPS_IMAGE = (By.XPATH, "//div[@class='weather-map-img half-section-left main-section-desktop']")
    SOLAR_IRRADIANCE_IMAGE = (By.XPATH, "//div[@class='energy-img white-text half-section-right main-section-desktop']")
    ROAD_RISK_API_IMAGE = (By.XPATH, "//div[@class='road-img half-section-left main-section-desktop']")
    FIRE_WEATHER_INDEX_IMAGE = (By.XPATH, "//div[@class='fire-img white-text half-section-right main-section-desktop']")

    products_page_images_locators = [CURRENT_AND_FORECAST_IMAGE, HISTORICAL_WEATHER_IMAGE, WEATHER_ALERTS_IMAGE,
                                     WEATHER_MAPS_IMAGE, SOLAR_IRRADIANCE_IMAGE, ROAD_RISK_API_IMAGE,
                                     FIRE_WEATHER_INDEX_IMAGE]

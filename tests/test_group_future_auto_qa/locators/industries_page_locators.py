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

    buttons_locators = [UPPER_TALK_TO_US_BUTTON, INSURANCE_TALK_TO_US_BUTTON, RETAIL_TALK_TO_US_BUTTON,
                        AUTOMOTIVE_TALK_TO_US_BUTTON, ADVERTISING_TALK_TO_US_BUTTON, ENERGY_TALK_TO_US_BUTTON,
                        AGRICULTURE_TALK_TO_US_BUTTON, SHALL_WE_SPEAK_TALK_TO_US_BUTTON]
from selenium.webdriver.common.by import By


class MembersPageLocators:
    MEMBERS_PAGE_LINK = 'https://home.openweathermap.org/subscriptions/unauth_subscribe/weather/startup'
    INDIVIDUAL_RADIOBUTTON = (By.CSS_SELECTOR, 'input[value="individual"]')
    ORGANISATION_RADIOBUTTON = (By.CSS_SELECTOR, 'input[value="organisation"]')
    LEFT_FIELDS_FOR_SUBSCRIPTION = (By.CSS_SELECTOR, 'div.col-xs-6:nth-child(1)')


from selenium.webdriver.common.by import By


class StudentInitiativeLocators:

    URL = 'https://openweathermap.org/'
    STUDENT_INITIATIVE_URL = 'https://openweathermap.org/our-initiatives/student-initiative'
    WEBSITE_LINK_LOCATOR = (By.CSS_SELECTOR, 'section#terms.anchor_el a[href="/"]')
    ASK_US_POPUP_LOCATOR = (By.CSS_SELECTOR, 'section#terms.anchor_el a[href="mailto:info@openweathermap.org"]')

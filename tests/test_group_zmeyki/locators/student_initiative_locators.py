from selenium.webdriver.common.by import By


class StudentInitiativeLocators:
    STUDENT_INITIATIVE_URL = 'https://openweathermap.org/our-initiatives/student-initiative'
    website_link_locator = (By.CSS_SELECTOR, 'section#terms.anchor_el a[href="/"]')
    ask_us_popup_locator = (By.CSS_SELECTOR, 'section#terms.anchor_el a[href="mailto:info@openweathermap.org"]')

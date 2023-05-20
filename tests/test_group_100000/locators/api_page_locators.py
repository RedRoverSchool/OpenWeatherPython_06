from selenium.webdriver.common.by import By


class RoadRiskApi:
    ROAD_RISK_API_LINK = 'https://openweathermap.org/api/road-risk'
    TITLE_HOW_TO_RR_API = (By.XPATH, "//*[@id='how']/h2")
    LINK_HOW_TO_REQUEST_RR_API = (By.CSS_SELECTOR, 'a[href="#how"]')
    SECTION_R_CONCEPTS = (By.XPATH, "//*[@id='concept']")
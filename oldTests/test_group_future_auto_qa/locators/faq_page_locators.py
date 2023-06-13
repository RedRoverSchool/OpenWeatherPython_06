from selenium.webdriver.common.by import By

class FAQPageLocators:
    FAQ_PAGE_URL = ("https://openweathermap.org/faq")
    FAQ_QUESTIONS_HEADINGS = (By.CSS_SELECTOR, ".question-heading")
    FAQ_QUESTIONS_AREA = (By.CSS_SELECTOR, ".question.visible")
    FAQ_ANSWER_SECTIONS = (By.XPATH, "./following-sibling::div[@class='question-content']")
    FAQ_ANSWER_TEXT = (By.CSS_SELECTOR, "p")

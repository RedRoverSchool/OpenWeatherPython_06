from selenium.webdriver.common.by import By


class OurInitiativesPageLocators:
    INITIATIVES = By.CSS_SELECTOR, "ul[id='first-level-nav'] li:nth-child(7) a:nth-child(1)"
    SECTION = By.XPATH, "//span[contains(text(), '{}')]"
    EDUCATION_LEARN_MORE = By.CSS_SELECTOR, ".ow-btn.round.btn-black"
    QUESTION_XPATH = "//*[@id='faq']/div[{i}]/p"


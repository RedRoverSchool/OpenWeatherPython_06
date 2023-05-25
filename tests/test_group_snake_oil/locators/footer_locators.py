from selenium.webdriver.common.by import By

class FootersLocators:

    FOOTER_TECHNOLOGIES = (By.XPATH, "//p[@class='section-heading' and text()='Technologies']")

    FOOTER_TECHNOLOGIES_ICONS = [
        (By.XPATH, "//p[@class='section-heading' and text()='Technologies']/following-sibling::div/ul/li[1]/a"),
        (By.XPATH, "//p[@class='section-heading' and text()='Technologies']/following-sibling::div/ul/li[2]/a"),
        (By.XPATH, "//p[@class='section-heading' and text()='Technologies']/following-sibling::div/ul/li[3]/a")]

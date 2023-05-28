from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PricingForBusinessLocators:

    TABLE = (By.CSS_SELECTOR, "table tbody:nth-child(2)")
    # TABLE = (By.XPATH, "/html/body/main/div[2]/section[2]/div/div/table")


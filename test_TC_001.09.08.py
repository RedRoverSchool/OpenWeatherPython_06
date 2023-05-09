import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://openweathermap.org/widgets-constructor"
search_field = driver.find_element(By.XPATH, "//input[@id='city-name']")


def test_search_field(driver):
    driver.get(URL)
    search_field.clear()
    search_field.click()
    search_field.send_keys("Foster city")
    time.sleep(3)
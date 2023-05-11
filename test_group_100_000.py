import time
from selenium.webdriver.common.by import By


URL = 'https://openweathermap.org/'
search_sky_in_words = (By.XPATH, "//div[@class='day-list-values']/span[contains(@class,'sub')]")


def test_TC_001_04_02_Verify_state_of_sky_in_words_for_each_day_is_displayed(driver, open_and_load_main_page, wait):
    elements = driver.find_elements(*search_sky_in_words)
    for i in elements:
        print(i.text)
        time.sleep(1)
        assert i.is_displayed()
    driver.quit()

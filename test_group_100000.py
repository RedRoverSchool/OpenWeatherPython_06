from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


weather_symbol = (By.CSS_SELECTOR, "ul  > li:nth-child(3) > span.symbol")

def test_TC_001_05_03_Verify_humidity_percentage_in_detailed_weather_data_for_current_location(driver, open_and_load_main_page, wait):
    humidity_symbol = driver.find_element(*weather_symbol)
    assert humidity_symbol.is_displayed()
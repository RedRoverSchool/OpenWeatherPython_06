from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_temperature_switched_on_metric_system(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    driver.find_element(By.CSS_SELECTOR, "button.stick-footer-panel__link").click()

    metric_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]"))
    )

    assert metric_button.is_displayed() and metric_button.is_enabled(), \
        "The temperature switch button in the metric system is not displayed or is not available for clickability"

    metric_button.click()

    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    current_temp = driver.find_element(By.CSS_SELECTOR, "div.current-temp span.heading")

    assert "°C" in current_temp.text, "The current temperature does not correspond to the metric"
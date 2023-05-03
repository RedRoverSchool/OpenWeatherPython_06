from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



def test_TC_002_03_08_open_pricing(driver):
    driver.get("https://openweathermap.org/")
    button_pricing = driver.find_element(By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_pricing)
    driver.execute_script("arguments[0].click();", button_pricing)
    expected_title = "Pricing"
    displayed_title = driver.find_element(By.CSS_SELECTOR, 'h1.breadcrumb-title').text
    assert displayed_title == expected_title
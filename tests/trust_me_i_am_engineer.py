from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_nav_bar_api_title(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    button_nav_bar_api = WebDriverWait(driver, 35).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#desktop-menu>ul>li:nth-child(2)>a")))
    button_nav_bar_api.click()
    nav_bar_api_title_text = driver.find_element(By.CSS_SELECTOR, "h1[class]").text
    assert nav_bar_api_title_text == "Weather API"


def test_on_api_page_recommend_version_of_api(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    button_nav_bar_api = WebDriverWait(driver, 35).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#desktop-menu>ul>li:nth-child(2)>a")))
    button_nav_bar_api.click()
    recommend_version_of_api = driver.find_element(By.XPATH, '//p/a[contains(text(), "One Call API 3.0")]').text
    assert recommend_version_of_api == "One Call API 3.0"



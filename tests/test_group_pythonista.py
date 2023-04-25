from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url

def test_check_page_title(driver):
    # function checks page title
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'



def test_guide_button(driver):
    #  testing Guide tab button
    driver.get('https://openweathermap.org')
    time.sleep(5)
    tab_name_guide = driver.find_element(By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "guide")]')
    tab_name_guide.click()
    assert driver.title == 'OpenWeatherMap API guide - OpenWeatherMap'


def test_home_button(driver):
    #  testing going back to home from Guide page
    driver.get('https://openweathermap.org')
    time.sleep(5)
    tab_name_guide = driver.find_element(By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "guide")]')
    tab_name_guide.click()
    time.sleep(5)
    tab_home_link = driver.find_element(By.XPATH, '//div[@class="col-sm-5"]/ol/li/a')
    tab_home_link.click()
    time.sleep(5)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


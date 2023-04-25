from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://openweathermap.org/"
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
home_btn = (By.CSS_SELECTOR, '.breadcrumb.pull-right.hidden-xs li :nth-child(1)')
selector_dashboard = (By.XPATH, "//h1[contains(text(),'Weather dashboard')]")

def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    # function checks page title
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_python():
    print('Hello girls!')


def test_checkout_menu_tab_guide(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    tab_dashboard_bt = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@id='desktop-menu']//a[@href='/weather-dashboard']")))
    tab_dashboard_bt.click()
    exp_alert = 'Weather dashboard'
    disp_alert = WebDriverWait(driver, 25).until(EC.presence_of_element_located(selector_dashboard))
    disp_alert_text = disp_alert.text
    assert exp_alert == disp_alert_text

from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://openweathermap.org/'
URL2 = 'https://openweathermap.org/guide/'
displayed_current_location = (By.CSS_SELECTOR, '.icon-current-location')
logo = (By.XPATH, "//ul[@id='first-level-nav']/li/a/img")


def test_should_open_url(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_home_page_header(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    header = driver.find_element(By.CSS_SELECTOR, "h1")
    assert header.text == "OpenWeather", "Wrong h1 Header"



# def test_should_refresh_link(driver):
#     current_title = driver.title
#     driver.get(URL)
#     driver.refresh()
#     WebDriverWait(driver, 60).until(EC.title_is('OpenWeatherMap'))
#     assert current_title != driver.title

def test_page_source(driver):
    driver.get(URL)
    page_source = driver.page_source
    driver.quit()



def test_get_name(driver):
    driver.get(URL)
    driver_name = driver.name
    return driver_name




def test_should_be_email_field_placeholder(driver):
    driver.get(URL)
    WebDriverWait(driver, 20).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    try:
        sign_in_top_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='desktop-menu']//li[@class='user-li']/a")))
        sign_in_top_menu.click()
    except TimeoutException as e:
        print(f"error occurred: {e}")
    try:
        expected_placeholder_text = "Enter email"
        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_email")))
        assert email_input.get_attribute("placeholder") == expected_placeholder_text, \
            "Email field placeholder text is incorrect"
    except TimeoutException as e:
        print(f"error occurred: {e}")


# @pytest.mark.skip()
def test_change_measurement_systems_to_imperial(driver):
    driver.get(URL)
    radio_button = driver.find_element(*(By.XPATH, "//div[text()='Imperial: °F, mph']"))
    action_chains = ActionChains(driver)
    action_chains.move_to_element(radio_button)
    driver.execute_script("arguments[0].click();", radio_button)
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="heading"]')))
    # displayed_temperature = (By.CSS_SELECTOR, 'span[class="heading"]')
    actual_temperature = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[class="heading"]'))).text
    # actual_temperature = driver.find_element(*displayed_temperature).text
    assert actual_temperature[-1] == 'F'

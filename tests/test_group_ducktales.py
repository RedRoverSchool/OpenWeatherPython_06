from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_fill_search_city_field(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('New York')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
    search_option.click()
    expected_city = 'New York City, US'
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city


def test_check_page_title(driver):
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_authorization_page(driver):
    pass


def test_rename_api_key(driver):
    driver.get('https://openweathermap.org/')
    # Click on the "Sign In"
    # sign_in = driver.find_element(By.CSS_SELECTOR, "#desktop-menu > ul > li.user-li > a")
    # driver.execute_script("arguments[0].scrollIntoView();", sign_in)
    # action = ActionChains(driver)
    # action.move_to_element(sign_in).click().perform()
    # Enter valid Username and Password
    driver.get('https://openweathermap.org/home/sign_in')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_email"))).send_keys('badlolpro@gmail.com')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_password"))).send_keys('36Pv@tdm2H7/x-d')
    # Click on the "Submit Button"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Submit']"))).click()
    # Click on the dropdown button
    dropdown_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='user-dropdown']")))
    dropdown_button.click()
    # Click on the My API keys button
    my_api_keys_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'My API keys')]")))
    my_api_keys_button.click()
    # select Actions -> Rename API Key -> Click Checkbox -> Rename API Key - > Save Changes
    click_checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[4]/a[2]/i[1]")))
    click_checkbox.click()
    rename_checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "edit_key_form_name")))
    time.sleep(5)
    rename_checkbox.clear()
    rename_checkbox.send_keys("Main")
    save_changes = driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
    save_changes.click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_email = 'chosenonex1@gmail.com'
test_password = 'gNrts5W?K_.qLFu'
URL = 'https://openweathermap.org/'

def test_sing_in_empty_fields(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div'))) # ожидание загрузки элементов
    driver.find_element(By.XPATH, '//a[contains(@href, "sign_in")]').click()
    driver.find_element(By.XPATH, '//*[@id="new_user"]/input[3]').click()
    alert = driver.find_element(By.XPATH, '//*[@class="panel-body"]')
    assert alert.text == 'Invalid Email or password.'

def test_sing_in_positive(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    driver.find_element(By.XPATH, '//a[contains(@href, "sign_in")]').click()
    email_form = driver.find_element(By.XPATH, '//*[@id = "user_email"]')
    email_form.click()
    email_form.send_keys(test_email)
    password_form = driver.find_element(By.XPATH, '//*[@id = "user_password"]')
    password_form.click()
    password_form.send_keys(test_password)
    remember_checkbox = driver.find_element(By.XPATH, '//*[@id = "user_remember_me"]')
    assert remember_checkbox.is_selected() == False
    driver.find_element(By.XPATH, '//*[@id="new_user"]/input[3]').click()
    driver.implicitly_wait(15)
    assert 'home.openweathermap' in driver.current_url
    alert = driver.find_element(By.XPATH, '//*[@class="panel-body"]')
    assert alert.text == 'Signed in successfully.'

def test_open_weather_map(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    driver.find_element(By.XPATH, '//a[contains(@href, "weathermap?zoom")]').click()
    window_weathermap_zoom = driver.window_handles[1] # возвращаем дескриптор новой страницы
    driver.switch_to.window(window_weathermap_zoom) # переключаем selenium на новую страницу
    assert driver.title == 'Interactive weather maps - OpenWeatherMap'
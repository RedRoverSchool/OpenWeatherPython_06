from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_name = 'taf88156@mail.com'
password = "Taf88156"
login = 'taffy'


def test_login_form(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    driver.find_element(By.CSS_SELECTOR, '#desktop-menu a[href="https://openweathermap.org/home/sign_in"]').click()
    sign_in_form = driver.find_element(By.CSS_SELECTOR, '.container h3').text
    print(f'sign_in_form = {sign_in_form}')
    expected_answer = 'Sign In To Your Account'
    assert sign_in_form == expected_answer

    driver.find_element(By.CSS_SELECTOR, '.input-group input[id="user_email"]').click()
    driver.find_element(By.CSS_SELECTOR, '.input-group input[id="user_email"]').send_keys(user_name)

    driver.find_element(By.CSS_SELECTOR, '.input-group input[id="user_password"]').click()
    driver.find_element(By.CSS_SELECTOR, '.input-group input[id="user_password"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]').click()
    user_login = driver.find_element(By.CSS_SELECTOR, '#desktop-menu .inner-user-container').text
    print(f'user_login = {user_login}')
    expected_login = login
    assert user_login == expected_login
    driver.find_element(By.CSS_SELECTOR, '#desktop-menu .inner-user-container').click()
    driver.find_element(By.CSS_SELECTOR, '#user-dropdown-menu a[class="logout"]').click()
    driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]').click()
    user_logout = driver.find_element(By.CSS_SELECTOR, '.panel-heading').text
    assert user_logout == 'Alert'


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


def test_fill_email_negative(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    sign_in_button = driver.find_element(By.CSS_SELECTOR, ".user-li a")
    sign_in_button.click()
    email = driver.find_element(By.CSS_SELECTOR, ".input-group .string")
    email.click()
    email.send_keys('test@email.com')
    create_user = driver.find_element(By.CSS_SELECTOR, ".new_user .btn")
    create_user.click()
    expected_alert = 'Invalid Email or password.'
    displayed_alert = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".panel-body")))
    displayed_alert_text = displayed_alert.text
    assert displayed_alert_text == expected_alert

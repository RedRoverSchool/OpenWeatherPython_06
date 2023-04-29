
import pytest as pytest
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

@pytest.mark.parametrize('city', ["Moscow", "London", "New York", "Baku", "Istanbul"])
def test_user_can_search_for_cities(driver, city):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    driver.find_element(By.CSS_SELECTOR, "button.stick-footer-panel__link").click()

    search_city = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city.send_keys(city)

    driver.find_element(By.CSS_SELECTOR, "div.search button").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu')))

    list_of_cities_found = driver.find_elements(By.CSS_SELECTOR, "div.search-container ul.search-dropdown-menu li")

    assert len(list_of_cities_found) > 0, "City not found"

    if len(list_of_cities_found) > 0:
        for city_found in list_of_cities_found:
            if city in city_found.text:
                city_found.click()
                break
        WebDriverWait(driver, 10).until(EC.url_changes('https://openweathermap.org/'))
        city_title = driver.find_element(By.CSS_SELECTOR, "div.current-container.mobile-padding div h2")

        assert city in city_title.text, "The city does not match the search"

def test_block_our_new_products(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    driver.find_element(By.CSS_SELECTOR, "button.stick-footer-panel__link").click()

    new_products_list = driver.find_elements(By.CSS_SELECTOR, "p.orange-text a")

    assert len(new_products_list) > 0, "Products in block 'Our new products' not found"
    if len(new_products_list) > 0:
        for product in new_products_list:
            product_name = " ".join(product.text.split()[:2]).strip()
            product.click()
            product_title = driver.find_element(By.CSS_SELECTOR, "h1.breadcrumb-title")
            assert product_name.lower() in product_title.text.lower(), "Product does not match the link"
            driver.back()

def test_switching_degrees_fahrenheit(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    driver.find_element(By.CSS_SELECTOR, "button.stick-footer-panel__link").click()

    driver.find_element(By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]").click()

    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    current_temp = driver.find_element(By.CSS_SELECTOR, "div.current-temp span.heading")

    assert "°C" in current_temp.text, "The current temperature does not correspond to the metric"

    driver.find_element(By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]").click()

    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    current_temp = driver.find_element(By.CSS_SELECTOR, "div.current-temp span.heading")

    assert "°F" in current_temp.text, "The current temperature does not correspond to the metric"

def test_redirect_to_apple_store(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    driver.find_element(By.CSS_SELECTOR, "button.stick-footer-panel__link").click()

    driver.find_element(By.XPATH, "//a[contains(@href, 'apps.apple.com')]").click()

    window_after = driver.window_handles[1]

    driver.switch_to.window(window_after)
    app_title = driver.find_element(By.CSS_SELECTOR, "h1.product-header__title.app-header__title")
    assert 'https://apps.apple.com/gb/app/openweather/id1535923697' in driver.current_url, \
        "The current url to Apple store does not match"
    assert 'OpenWeather' in app_title.text, \
        "The current app title in Apple store does not match 'OpenWeather'"

def test_redirect_to_google_play(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))

    driver.find_element(By.CSS_SELECTOR, "button.stick-footer-panel__link").click()

    driver.find_element(By.XPATH, "//div[@class='my-5']/div/a[contains(@href, 'play.google.com')]").click()

    window_after = driver.window_handles[1]

    driver.switch_to.window(window_after)
    app_title = driver.find_element(By.XPATH, "//h1[@itemprop='name']")
    assert 'https://play.google.com/store/apps/details?id=uk.co.openweather' in driver.current_url, \
        "The current url to Google Play does not match"
    assert 'OpenWeather' in app_title.text, \
        "The current app title in Google Play does not match 'OpenWeather'"


def test_pricing_page(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    driver.maximize_window()
    pricing_button = driver.find_element(By.CSS_SELECTOR, "#desktop-menu  li:nth-child(5) a")
    pricing_button.click()
    header2_text = '"One Call by Call" subscription plan'
    displayed_header2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#onecall div > h2")))
    displayed_header2_text = displayed_header2.text
    assert displayed_header2_text == header2_text
    subscribe_button = driver.find_element(By.CSS_SELECTOR, 'center > .round.btn-orange')
    subscribe_button.click()
    assert '/unauth_subscribe/onecall_30/base' in driver.current_url

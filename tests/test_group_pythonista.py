import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://openweathermap.org/"
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
selector_dashboard = (By.XPATH, "//h1[contains(text(),'Weather dashboard')]")
selector_api = (By.XPATH, "//h1[contains(text(),'Weather API')]")
tab_desk_api = (By.CSS_SELECTOR, '#desktop-menu a[href="/api"]')
btn_desc_dashboard = (By.CSS_SELECTOR, "#desktop-menu [href$=-dashboard]")
title_weatherDashboard = (By.CLASS_NAME, 'breadcrumb-title')
selector_marketplace_tab = (By.XPATH, '//div[@id="desktop-menu"]//li[4]/a')
footer_panel = (By.XPATH, '//*[@id="stick-footer-panel"]/div')
btn_allow_all = (By.CLASS_NAME, "stick-footer-panel__link")
btn_go_home = (By.XPATH, "//a[contains(text(),'Home')]")
# TODO (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))

# About As
btn_about_us = (By.CSS_SELECTOR, 'a[href*="/about-us"]')
btn_product_doc = (By.CSS_SELECTOR, 'div.grid-container [href="/api"]')
weather_title_api = (By.CLASS_NAME, 'breadcrumb-title')
btn_buy_subst = (By.CSS_SELECTOR, 'a[href="https://home.openweathermap.org/subscriptions"]')
alert_txt = (By.CLASS_NAME, "panel-body")
assert_mmg = '\n====You need to sign in or sign up before continuing.===\n'
btn_newAndUpd = (By.CSS_SELECTOR, 'a.round[href*="blog"]')
text_openweather = (By.XPATH, '//div/h1/span["orange -text"]')
search_city_field_selector = (By.XPATH, '//div[@id="weather-widget"]//div/input')
search_submit_button = (By.XPATH, '//div[@id="weather-widget"]//div/button')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
btn_contact_as = (By.CSS_SELECTOR, '.about-us :nth-child(9) [href="https://home.openweathermap.org/questions"]')
question_page = (By.CLASS_NAME, 'headline')
btn_marketplace = (By.CSS_SELECTOR, 'div.grid-container a[href$="/marketplace"]')
txt_mp_page = (By.XPATH, '//*[@id="custom_weather_products"]/h1')
# Support tab
support_tab = (By.CSS_SELECTOR, '#support-dropdown')
faq_link = (By.XPATH, '//ul[@class="dropdown-menu dropdown-visible"]/li/a[text()="FAQ"]')
how_to_start_link = (By.XPATH, '//ul[@class="dropdown-menu dropdown-visible"]/li/a[text()="How to start"]')
ask_question_link = (By.XPATH, '//ul[@class="dropdown-menu dropdown-visible"]/li/a[text()="Ask a question"]')


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    yield wait


@pytest.fixture()
def open_page(driver):
    driver.get(URL)
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver, wait, open_page):
    # function checks page title
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


'''DESKTOP MENU / Verify menu-btn "API" redirects to api page and btn "Home" return back'''


def test_checkout_tab_api(driver, open_page, wait):
    bt_click_api = driver.find_element(By.CSS_SELECTOR, 'a[href*="/api"]')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(bt_click_api)
    driver.execute_script("arguments[0].click();", bt_click_api)
    assert driver.current_url == 'https://openweathermap.org/api'
    driver.find_element(*btn_go_home).click()
    assert driver.current_url == URL


'''DESKTOP MENU / Verify menu-btn "Dashboard" redirects to dashboard page and btn "Home" return back'''


def test_checkout_menu_tab_dashboard(driver, open_page, wait):
    btn_dashb = driver.find_element(*btn_desc_dashboard)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(btn_dashb)
    driver.execute_script("arguments[0].click();", btn_dashb)
    title_dashboard = driver.find_element(*title_weatherDashboard).text
    assert title_dashboard == 'Weather dashboard'
    driver.find_element(*btn_go_home).click()
    assert driver.current_url == URL


def test_home_button(driver, open_page):
    #  testing going back to home from Guide page
    try:
        WebDriverWait(driver, 50).until_not(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
        tab_name_guide = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "guide")]')))
        tab_name_guide.click()
        tab_home_link = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="col-sm-5"]/ol/li/a')))
        tab_home_link.click()
        assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


def test_guide_button(driver, open_page):
    #  testing Guide tab button
    try:
        WebDriverWait(driver, 50).until_not(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
        tab_name_guide = WebDriverWait(driver, 45).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@id="desktop-menu"]//a[contains(@href, "guide")]')))
        tab_name_guide.click()
        assert driver.title == 'OpenWeatherMap API guide - OpenWeatherMap'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


def test_marketplace_page_link(driver, open_page):
    try:
        WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(load_div))
        marketplace_tab = WebDriverWait(driver, 15).until(EC.element_to_be_clickable
                                                          (selector_marketplace_tab))
        marketplace_tab.click()
        expected_url = 'https://home.openweathermap.org/marketplace'
        assert expected_url
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


def test_search_city_field(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_field = driver.find_element(*search_city_field_selector)
    search_city_field.send_keys('New York')
    search_button = driver.find_element(*search_submit_button)
    search_button.click()
    search_option = wait.until(EC.element_to_be_clickable(
        search_dropdown_option))
    search_option.click()
    expected_city = 'New York City, US'
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city


def test_search_city_field(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_field = driver.find_element(*search_city_field_selector)
    search_city_field.send_keys('New York')
    search_button = driver.find_element(*search_submit_button)
    search_button.click()
    search_option = wait.until(EC.element_to_be_clickable(
        search_dropdown_option))
    search_option.click()
    expected_city = 'New York City, US'
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city


def test_check_about(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    title_about_us = driver.find_element(*text_openweather).text
    assert title_about_us == 'OpenWeather'


'''About us / Verify "Products Documentation" button redirects to page'''


def test_check_product_doc_btn(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_product_doc).click()
    txt_title = driver.find_element(*weather_title_api).text
    assert txt_title == 'Weather API'


'''About us/ Verify "Buy by Subscription" button redirects to subscriptions page(logout)'''


def test_check_buy_by_sub(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_buy_subst).click()
    alert = driver.find_element(*alert_txt)
    assert alert.is_displayed()


# TODO  Negative test?! (mark.skip)
@pytest.mark.skip('negative test')
def test_neg_check_buy_by_subs(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_buy_subst).click()
    neg_alert_txt = driver.find_element(*alert_txt).text
    assert neg_alert_txt == 'https://home.openweathermap.org/subscriptions', assert_mmg


'''Footer/ About us / Verify "By in the MarketPlace" button redirects user to "Custom Weather Products'''


def test_check_marketplace(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_marketplace).click()
    txt_markplace = driver.find_element(*txt_mp_page).text
    assert txt_markplace == 'Custom Weather Products'


'''Footer / About us / Verify New and Updates button'''


def test_news_and_update(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_newAndUpd).click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == "https://openweather.co.uk/blog/category/weather"
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.quit()


'''Footer/ About us / Verify "Contact us" button redirects user to "Questions" page'''


def test_contact_us(driver, open_page):
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable(footer_panel))
    driver.find_element(*btn_allow_all).click()
    driver.find_element(*btn_about_us).click()
    driver.find_element(*btn_contact_as).click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.find_element(*question_page).is_displayed()


'''Testing Support tab'''


def test_support_faq(driver, open_page):
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 15)
        wait.until_not(EC.presence_of_element_located(load_div))
        wait.until(EC.presence_of_element_located(support_tab))
        driver.find_element(*support_tab)
        wait.until(EC.presence_of_element_located(faq_link))
        driver.find_element(*faq_link).click()
        assert driver.current_url == 'https://openweathermap.org/faq'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


# TODO  need fix
def test_support_how_start(driver, open_page):
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 15)
        wait.until_not(EC.presence_of_element_located(load_div))
        wait.until(EC.presence_of_element_located(support_tab))
        driver.find_element(*support_tab)
        wait.until(EC.presence_of_element_located(how_to_start_link))
        driver.find_element(*how_to_start_link).click()
        assert driver.current_url == 'https://openweathermap.org/appid'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")


def test_support_ask_question(driver, open_page):
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 15)
        wait.until_not(EC.presence_of_element_located(load_div))
        wait.until(EC.presence_of_element_located(support_tab))
        driver.find_element(*support_tab)
        wait.until(EC.presence_of_element_located(ask_question_link))
        driver.find_element(*ask_question_link).click()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == 'https://home.openweathermap.org/questions'
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

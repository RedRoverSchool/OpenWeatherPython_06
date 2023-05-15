import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'
cities = ['New York', 'Los Angeles', 'Paris']
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")
displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')


def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


@pytest.mark.parametrize('city', cities)
def test_fill_search_city_field(driver, city):
    driver.get('https://openweathermap.org/')
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_input = driver.find_element(*search_city_field)
    search_city_input.send_keys(city)
    driver.find_element(*search_button).click()
    wait.until(EC.element_to_be_clickable(search_dropdown_option)).click()
    expected_city = city
    wait.until(EC.text_to_be_present_in_element(displayed_city, city))
    actual_city = driver.find_element(*displayed_city).text
    assert expected_city in actual_city


def test_search_field_present(driver):
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    assert search_city_field.is_displayed(), 'Search field not found on the Home page'


def test_search_field_placeholder(driver):
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    expected_placeholder = 'Search city'
    actual_placeholder = search_city_field.get_attribute('placeholder')
    assert actual_placeholder == expected_placeholder, f'Search field placeholder is {actual_placeholder}, expected {expected_placeholder}'


def test_logo_is_presented(driver):
    driver.get('https://openweathermap.org/')
    logo = driver.find_element(By.XPATH, "//li[contains(@class, 'logo')]")
    assert logo.is_displayed(), "Logo not found on the Home page"


def test_check_facebook_link_in_footer(driver):
    driver.get('https://openweathermap.org/')
    footer_buttons = driver.find_elements(By.CSS_SELECTOR, '.social a')
    assert footer_buttons[0].get_attribute('href') == 'https://www.facebook.com/groups/270748973021342'


@pytest.mark.skip("need to refactor why this test sometimes doesn't work")
def test_captcha_sign_in_form(driver):
    driver.get(URL)
    search_sign_in = driver.find_element(By.CSS_SELECTOR, "#desktop-menu > ul > li.user-li > a")
    search_sign_in.click()
    search_create_account = driver.find_element(By.XPATH, "//a[text() = 'Create an Account.']")
    search_create_account.click()
    search_field_username = driver.find_element(By.CSS_SELECTOR, "#user_username")
    search_field_username.send_keys("Test123")
    search_field_email = driver.find_element(By.CSS_SELECTOR, "#user_email")
    search_field_email.send_keys("testbordiotatiana@gmail.com")
    search_field_password = driver.find_element(By.CSS_SELECTOR, "#user_password")
    search_field_password.send_keys("123test")
    search_field_repeatpas = driver.find_element(By.CSS_SELECTOR, "#user_password_confirmation")
    search_field_repeatpas.send_keys("123test")
    search_checkbox_age = driver.find_element(By.CSS_SELECTOR, "#agreement_is_age_confirmed")
    search_checkbox_age.click()
    search_checkbox_privacy = driver.find_element(By.CSS_SELECTOR, "#agreement_is_accepted")
    search_checkbox_privacy.click()
    search_btn_create_account = driver.find_element(By.CSS_SELECTOR, "#new_user > div:nth-child(21) > input")
    search_btn_create_account.click()
    search_failed_message = driver.find_element(By.CSS_SELECTOR, "#new_user > div:nth-child(20) > div.has-error > div")
    assert search_failed_message.is_displayed()
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Sign in page and credentials
SIGN_IN_URL = "https://home.openweathermap.org/users/sign_in?campaign_id=weather_dashboard_website"
user_name = 'ta3711336@gmail.com'
password = '#MQPG@Ke+8+6#a)'
EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='user_email']")
PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='user_password']")
SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[value='Submit']")
SIGNED_IN_SUCCESSFULLY = (By.XPATH, "//div[contains(text(), 'Signed in successfully.')]")

# Homepage
ALLOW_ALL_COOKIES = (By.XPATH, "//button[contains(text(), 'Allow all')]")
DASHBOARD_BUTTON = (By.CSS_SELECTOR, "a[href='/weather-dashboard']")

# 'How to Start' section links
SIGN_UP_LINK = (By.XPATH, ".//a[b='Sign up']")
USERNAME_AND_PASSWORD_LINK = (By.XPATH, "//a[text()='OpenWeather username and password']")
GO_TO_DASHBOARD_LINK = (By.XPATH, ".//a[b='Go to the Dashboard']")
EVENTS_SECTION_LINK = (By.XPATH, "//a[contains(text(), 'section')]")
NEW_TRIGGER_SECTION_LINK = (By.XPATH, ".//a[b='Go to the \"New trigger\" section']")
HERE_LINK = (By.XPATH, "//a[text()='here']")
DETAILED_USER_MANUAL_LINK = (By.XPATH, ".//a[b='detailed user manual']")
TRY_THE_DASHBOARD_BUTTON = (By.XPATH, "(//a[text()='Try the Dashboard'])[2]")
# 7 links + 1 button
all_link_locators = [SIGN_UP_LINK, USERNAME_AND_PASSWORD_LINK, GO_TO_DASHBOARD_LINK, EVENTS_SECTION_LINK,
                     NEW_TRIGGER_SECTION_LINK,
                     HERE_LINK, DETAILED_USER_MANUAL_LINK, TRY_THE_DASHBOARD_BUTTON]

# Footer
linkedIn_icon = (By.CSS_SELECTOR, "div[class='social'] a:nth-child(3)")
Support_dropdown = (By.XPATH, "//*[@id='support-dropdown']")
FAQ_element = (By.XPATH, "//*[@id='support-dropdown-menu']/li[1]/a")
FAQ_url = "https://openweathermap.org/faq"
FOOTER_TECHNOLOGIES = (By.XPATH, "//p[@class='section-heading' and text()='Technologies']")
FOOTER_SOCIAL_MEDIA_MODULE_ICONS = [(By.CSS_SELECTOR, 'div[class="social"] a:nth-child(1)'),
                                    (By.CSS_SELECTOR, 'div[class="social"] a:nth-child(2)'),
                                    (By.CSS_SELECTOR, 'div[class="social"] a:nth-child(3)'),
                                    (By.CSS_SELECTOR, 'div[class="social"] a:nth-child(4)'),
                                    (By.CSS_SELECTOR, 'div[class="social"] a:nth-child(5)'),
                                    (By.CSS_SELECTOR, 'div[class="social"] a:nth-child(6)')]

URLs = ['https://openweathermap.org/',
        'https://openweathermap.org/guide',
        'https://openweathermap.org/api',
        'https://openweathermap.org/weather-dashboard',
        'https://openweathermap.org/price',
        'https://openweathermap.org/our-initiatives',
        'https://openweathermap.org/examples',
        'https://home.openweathermap.org/users/sign_in',
        'https://openweathermap.org/faq',
        'https://openweathermap.org/appid',
        'https://home.openweathermap.org/questions']
# Student Initiative page
STUDENT_INITIATIVE_PAGE_URL = "https://openweathermap.org/our-initiatives/student-initiative"
LEARN_MORE_LINK_DEVELOPER_PLAN = (By.CSS_SELECTOR, "center>a[href='/price']")
PRICING_PAGE_URL_FOR_DEVELOPER_PLAN = "https://openweathermap.org/price"


def test_tc_003_10_06_verify_linkedIn_link_is_visible(driver, open_and_load_main_page, wait):
    element = wait.until(EC.visibility_of_element_located(linkedIn_icon))
    assert element.is_displayed(), "LinkedIn interactive icon is not visible on a page"


def test_tc_003_10_08_verify_clickability_of_linkedIn_link(driver, open_and_load_main_page, wait):
    element = wait.until(EC.element_to_be_clickable(linkedIn_icon))
    assert element.is_enabled(), "LinkedIn interactive icon is not clickable on a page"


@pytest.mark.parametrize('locator', all_link_locators)
def test_TC_006_02_04_verify_all_links_redirecting_to_the_respective_pages(driver, open_and_load_main_page, wait,
                                                                           locator):
    wait.until(EC.element_to_be_clickable(ALLOW_ALL_COOKIES)).click()
    wait.until(EC.element_to_be_clickable(DASHBOARD_BUTTON)).click()
    element = wait.until(EC.element_to_be_clickable(locator))
    href_link = element.get_attribute('href')
    new_tab = element.get_attribute('target') == '_blank'
    response = requests.head(href_link)
    status_code = response.status_code
    if status_code == 302:
        driver.execute_script('window.open("");')
        driver.switch_to.window(driver.window_handles[1])
        driver.get(response.headers['Location'])
        wait.until(EC.presence_of_element_located(EMAIL_INPUT)).send_keys(user_name)
        wait.until(EC.presence_of_element_located(PASSWORD_INPUT)).send_keys(password)
        wait.until(EC.presence_of_element_located(SUBMIT_BUTTON)).click()
        wait.until(EC.presence_of_element_located(SIGNED_IN_SUCCESSFULLY))
        driver.close()
    driver.switch_to.window(driver.window_handles[0])
    try:
        request = requests.get(href_link)
    except Exception:
        current_url = "NOT VALID",
        status_code = "no_status_code"
    else:
        wait.until(EC.element_to_be_clickable(locator)).click()
        if new_tab:
            driver.switch_to.window(driver.window_handles[1])
        current_url = driver.current_url
        status_code = request.status_code
    assert href_link == current_url and status_code == 200, \
        f"This URL '{href_link}' is redirecting to '{current_url}' URL. Status code = {status_code}"


def test_tc_015_01_01_verify_support_faq_is_visible(driver, open_and_load_main_page, wait):
    dropdown = wait.until(EC.visibility_of_element_located(Support_dropdown))
    dropdown.click()
    element = wait.until(EC.visibility_of_element_located(FAQ_element))
    assert element.is_displayed(), "FAQ element is not visible on the page"


def test_tc_015_01_02_verify_support_faq_is_clickable(driver, open_and_load_main_page, wait):
    dropdown = wait.until(EC.visibility_of_element_located(Support_dropdown))
    dropdown.click()
    element = wait.until(EC.element_to_be_clickable(FAQ_element))
    assert element.is_enabled(), "FAQ element is not clickable on the page"


def test_tc_015_01_03_verify_support_faq_page_redirection(driver, open_and_load_main_page, wait):
    dropdown = wait.until(EC.visibility_of_element_located(Support_dropdown))
    dropdown.click()
    element = wait.until(EC.visibility_of_element_located(FAQ_element))
    element.click()
    current_url = driver.current_url
    wait.until(EC.url_to_be(FAQ_url))
    assert current_url == FAQ_url, f"Page redirection failed. Expected: {FAQ_url}, Actual: {driver.current_url}"


@pytest.mark.parametrize('URL', URLs)
def test_tc_003_04_01_title_is_present(driver, wait, URL):
    driver.get(URL)
    expected_footer_text = "Technologies"
    footer = driver.find_element(*FOOTER_TECHNOLOGIES)
    assert footer.is_displayed() and expected_footer_text in footer.text, \
        "The footer is not displayed or does not contain the expected text"


def test_TC_010_02_03_verify_the_learn_more_link_redirection_for_the_developer_plan(driver, open_and_load_main_page,
                                                                                    wait):
    wait.until(EC.element_to_be_clickable(ALLOW_ALL_COOKIES)).click()
    driver.get(STUDENT_INITIATIVE_PAGE_URL)
    learn_more_link = driver.find_element(*LEARN_MORE_LINK_DEVELOPER_PLAN)
    learn_more_link.click()
    current_url = driver.current_url
    assert current_url == PRICING_PAGE_URL_FOR_DEVELOPER_PLAN, "Incorrect page redirection for the Developer Plan"


@pytest.mark.parametrize('icon', FOOTER_SOCIAL_MEDIA_MODULE_ICONS)
@pytest.mark.parametrize('url', URLs)
def test_tc_003_10_02_verify_the_visibility_and_clickability_of_all_icon_links_for_several_pages(driver, wait, url,
                                                                                                 icon):
    driver.get(url)
    element = driver.find_element(*icon)
    element_link = element.get_attribute('href')
    assert element.is_displayed() and element.is_enabled(), f"Link {element_link} interactive icon is not visible on" \
                                                            f" a page or not clickable"

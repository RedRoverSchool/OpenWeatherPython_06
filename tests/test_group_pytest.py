from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

Button_under_how_to_start = (By.XPATH, '(//a[@class="btn_like btn-orange owm-block-mainpage__btn"])[2]')
Dashboard_header_link = (By.XPATH, '//div[@id="desktop-menu"]//a[.="Dashboard"]')
Weather_dashboard_home_link = (By.XPATH, '//a[.="Home"]')
How_to_Start_Sign_up_link = (By.XPATH, '//b[.="Sign up"]')
How_to_Start_OpenWeather_username_and_password_link = (By.XPATH, '//a[.="OpenWeather username and password"]')
How_to_Start_Go_to_the_Dashboard_link = (By.XPATH, '//b[.="Go to the Dashboard"]')
How_to_Start_Events_section_link = (By.XPATH, '//a[contains(text(), "Events")]')
How_to_Start_Go_to_the_New_trigger_section_link = (By.XPATH, '//b[contains(text(), "New trigger")]')
How_to_Start_here_link = (By.XPATH, '//a[.="here"]')
How_to_Start_detailed_user_manual_link = (By.XPATH, '//b[.="detailed user manual"]')


def test_tc_006_02_02_verify_how_to_start_block_7_links_are_visible(driver, open_and_load_main_page, wait):
    driver.find_element(*Dashboard_header_link).click()
    wait.until(EC.element_to_be_clickable(Weather_dashboard_home_link))
    how_to_start_block = driver.find_element(*Button_under_how_to_start)
    actions = ActionChains(driver)
    actions.move_to_element(how_to_start_block).perform()
    How_to_Start_Sign_up = driver.find_element(*How_to_Start_Sign_up_link)
    How_to_Start_OpenWeather_username_and_password = driver.find_element(
        *How_to_Start_OpenWeather_username_and_password_link)
    How_to_Start_Go_to_the_Dashboard = driver.find_element(*How_to_Start_Go_to_the_Dashboard_link)
    How_to_Start_Events_section = driver.find_element(*How_to_Start_Events_section_link)
    How_to_Start_Go_to_the_New_trigger_section = driver.find_element(*How_to_Start_Go_to_the_New_trigger_section_link)
    How_to_Start_here = driver.find_element(*How_to_Start_here_link)
    How_to_Start_detailed_user_manual = driver.find_element(*How_to_Start_detailed_user_manual_link)
    assert How_to_Start_Sign_up.is_displayed() and How_to_Start_OpenWeather_username_and_password.is_displayed() and \
           How_to_Start_Go_to_the_Dashboard.is_displayed() and  How_to_Start_Events_section.is_displayed() and \
           How_to_Start_Go_to_the_New_trigger_section.is_displayed() and How_to_Start_here.is_displayed() and \
           How_to_Start_detailed_user_manual.is_displayed(), "One of the links are not visible"



from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
URL = 'https://openweathermap.org/'


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get(URL)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'
    print(f'The site title is: {driver.title}')



def test_click_guide(driver):
    driver.get(URL)
    search_link_guide = driver.find_element(By.XPATH, '//*[@id="desktop-menu"]/ul/li[1]/a')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(search_link_guide)
    driver.execute_script("arguments[0].click();", search_link_guide)
    assert driver.title == 'OpenWeatherMap API guide - OpenWeatherMap'
    print(f'Website page title is: {driver.title}')

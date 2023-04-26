import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://openweathermap.org/"


def test_open_blog_article(driver):
    driver.get(URL)

    blog_btn = WebDriverWait(driver, 150).until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Blog")))
    blog_btn.click()


    driver.switch_to.window(driver.window_handles[1])

    all_btn = driver.find_element(By.LINK_TEXT, "ALL")
    all_btn.click()
    assert "Blog" in driver.title, "Заголовок страницы не содержит слово 'Blog'"


    first_article = driver.find_element(By.CSS_SELECTOR, "[class=post__title]")
    first_article.click()

    cookie = driver.find_element(By.CSS_SELECTOR, "button[type='button']")
    cookie.click()

    return_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".return [href='/blog']")))
    return_btn.click()

    time.sleep(5)


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_button_search_exist(driver):
    driver.get(URL)
    btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    assert btn.text == "Search"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_blog_article(driver):
    driver.get("https://openweathermap.org/")

    blog_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Blog")))
    time.sleep(5)
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

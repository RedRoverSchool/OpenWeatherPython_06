from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    sign_in_link = (By.CSS_SELECTOR, '.user-li a')
    guide_link = (By.CSS_SELECTOR, '#desktop-menu a[href*="guide"]')

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link


    def open_page(self):
        self.driver.get(self.link)

    def click_header_link(self, link_name):
        match link_name:
            case 'sign':
                self.driver.find_element(*self.sign_in_link).click()
            case 'guide':
                self.driver.find_element(*self.guide_link)

    def check_header_link(self, link_name):
        self.check_header_link(link_name)
        assert link_name in self.driver.current_url

    def element_is_displayed(self, method, locator, wait):
        try:
            wait.until(EC.visibility_of_element_located((method, locator)))
        except TimeoutException:
            return False
        return True


from pages.base_page import BasePage
from tests.test_group_no_pain_no_gain.locators.main_page_locators import MainPageLocators as MPL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

class MainPage(BasePage):

    def element_visibility(self, locator):
        element = wait(self.driver, timeout=3).until(EC.visibility_of_element_located(locator))
        assert element.is_displayed(), 'element is not visible'

    def element_clickability(self, locator):
        element = wait(self.driver, timeout=3).until(EC.element_to_be_clickable(locator))
        assert element.is_enabled(), 'element is not clickable'

    def scroll_down_the_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def check_link(self, locator, link):
        self.driver.find_element(*locator).click()
        assert link in self.driver.current_url

    def check_link_in_new_window(self, locator, link):
        self.driver.find_element(*locator).click()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        assert link in self.driver.current_url

    def check_page_title(self, data):
        title = self.driver.title
        assert data in title, f'{data} is not in the page title'

    def get_text_content_of_the_element(self, locator, data):
        element = self.driver.find_element(*locator).text
        assert element == data, f'{data} is not in the text context of the element'

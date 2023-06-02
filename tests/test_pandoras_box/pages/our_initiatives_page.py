from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OurInitiativesPage(BasePage):

    DISPLAYED_TITLE = (By.XPATH, '//div[2]//h1')
    BUTTON_LEARN_MORE = (By.CSS_SELECTOR, 'a[class="ow-btn round btn-black"]')
       
    
    def verify_learn_more_link_redirects_to_valid_page(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.find_element(*self.BUTTON_LEARN_MORE).click()
        actual_title = self.driver.find_element(*self.DISPLAYED_TITLE).text
        expected_title = "Free Data for Students"
        assert expected_title == actual_title

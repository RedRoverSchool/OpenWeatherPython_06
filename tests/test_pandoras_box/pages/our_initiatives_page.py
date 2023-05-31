from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OurInitiativesPage(BasePage):

    DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')
    BUTTON_LEARN_MORE = (By.CSS_SELECTOR, 'a[class="ow-btn round btn-black"]')
    our_initiatives_link = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(7) a')
    OUR_INITIATIVES_URL = 'https://openweathermap.org/our-initiatives'
    
    
    def check_header_title(self, link_name):
        self.click_header_link(link_name)
        expected_title = "Our Initiatives"
        displayed_title = self.driver.find_element(*self.DISPLAYED_TITLE).text
        assert displayed_title == expected_title
        
        
    def verify_learn_more_link_redirects_to_valid_page(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.find_element(*self.BUTTON_LEARN_MORE).click()
        actual_title = self.driver.find_element(*self.DISPLAYED_TITLE).text
        expected_title = "Student initiative"
        assert expected_title == actual_title

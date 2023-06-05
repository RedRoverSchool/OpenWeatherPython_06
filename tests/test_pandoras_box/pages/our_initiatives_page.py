from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OurInitiativesPage(BasePage):

    DISPLAYED_TITLE = (By.XPATH, '//div[2]//h1')
    BUTTON_LEARN_MORE = (By.CSS_SELECTOR, 'a[class="ow-btn round btn-black"]')
    our_initiatives_url = 'https://openweathermap.org/our-initiatives'
    
    def verify_learn_more_link_redirects_to_valid_page(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.find_element(*self.BUTTON_LEARN_MORE).click()
        actual_title = self.driver.find_element(*self.DISPLAYED_TITLE).text
        expected_title = "Free Data for Students"
        assert expected_title == actual_title


    def check_text_on_button_learn_more(self):
        button_learn_more = self.driver.find_element(*self.BUTTON_LEARN_MORE)
        expected_text = "Learn more"
        assert expected_text == button_learn_more.text

        
    def verify_correct_url_out_initiative(self):
        actual_url = self.driver.current_url
        expected_url = self.our_initiatives_url
        assert actual_url == expected_url


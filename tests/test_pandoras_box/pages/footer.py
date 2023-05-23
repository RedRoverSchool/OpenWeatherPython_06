from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Footer(BasePage):
    GOOGLE_PLAY_LINK = (By.XPATH, '//*[@id="footer-website"]/div/div[3]/div/a[2]/img')

    def check_leads_link_Googl_Play(self):
        self.driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")
        google_play = self.driver.find_element(*self.GOOGLE_PLAY_LINK)
        self.driver.execute_script("arguments[0].click();", google_play)
        self.driver.switch_to.window(self.driver.window_handles[1])
        expected_title = 'OpenWeather'
        assert '/play.google' in self.driver.current_url and expected_title in self.driver.title


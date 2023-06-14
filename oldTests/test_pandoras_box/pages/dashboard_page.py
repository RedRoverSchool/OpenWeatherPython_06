from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class Dashboard(BasePage):

    image_locator = (By.XPATH, "//*[@class='responsive']")

    def check_image_is_visible(self):
        image = self.driver.find_element(*self.image_locator)
        assert image.is_displayed(), "Image is not visible"

from pages.base_page import BasePage
from tests.test_group_future_auto_qa.locators.partners_page_locators import PartnersLocators


class PartnersPage(BasePage):

    locators = PartnersLocators()
    git_button_python = 'https://github.com/csparpa/pyowm'

    def open(self):
        self.driver.get("https://openweathermap.org/examples#python")

    def scroll_to_git_button_python(self):
        self.driver.execute_script("window.scrollTo(0, 500)")

    def click_git_button_python(self):
        git_button_python = self.driver.find_element(*PartnersLocators.GIT_BUTTON_PYTHON)
        git_button_python.click()

    def git_button_python_is_clickable(self):
        git_button_python = self.driver.find_element(*PartnersLocators.GIT_BUTTON_PYTHON)
        return git_button_python.is_enabled()

    def verify_redirection_git_button_python_to_the_new_webpage(self):
        self.driver.get("https://openweathermap.org/examples#python")
        link = self.driver.find_element(*self.locators.GIT_BUTTON_PYTHON)
        self.driver.execute_script("arguments[0].click();", link)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.git_button_python, self.driver.current_url

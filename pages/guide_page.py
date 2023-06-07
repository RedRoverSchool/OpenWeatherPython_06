from pages.base_page import BasePage
from locators.locators import GuideLocators

class GuidePage(BasePage):

    link = 'https://openweathermap.org/guide'

    def industry_standard_apis_link_redirection(self):
        element = self.driver.find_element(*GuideLocators.INDUSTRY_APIS_LOCATOR)
        self.driver.execute_script("arguments[0].click();", element)
        assert '/api' in self.driver.current_url, "The industry standard apis link leads to an incorrect page"

    def one_call_api_by_call_link_redirection(self):
        element = self.driver.find_element(*GuideLocators.ONE_CALL_API_BY_CALL_LOCATOR)
        self.driver.execute_script("arguments[0].click();", element)
        assert '/one-call-3' in self.driver.current_url, "The one call api by call link leads to an incorrect page"

    def subscribe_to_onecall_by_call_button_is_visible(self):
        subscribe_to_onecall_by_call_button = self.element_is_visible(GuideLocators.SUBSCRIBE_TO_ONE_CALL_BY_CALL_BUTTON)
        assert subscribe_to_onecall_by_call_button.is_displayed(), "The button 'subscribe to onecall by call' is not visible"

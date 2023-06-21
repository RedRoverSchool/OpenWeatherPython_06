from pages.base_page import BasePage
from locators.locators import AskAQuestionPageLocators


class AskQuestionPage(BasePage):
    ask_a_question_locators = AskAQuestionPageLocators()

    def check_header_title(self, link_name):
        self.click_header_link(link_name)
        expected_title = "Ask a question"
        displayed_title = self.driver.find_element(*self.ask_a_question_locators.DISPLAYED_TITLE).text
        assert displayed_title == expected_title
from pages.base_page import BasePage
from locators.locators import FAQPageLocators as faq

class FAQPage(BasePage):

    def get_questions(self):
        parent_elements = self.driver.find_elements(*faq.FAQ_QUESTIONS_HEADINGS)
        return parent_elements

    def click_parent_element(self, parent_element):
        self.driver.execute_script("arguments[0].click();", parent_element)

    def get_question_content(self, element):
        question_content = element.find_element(*faq.FAQ_ANSWER_SECTIONS)
        return question_content

    def is_previous_content_hidden(self, previous_content):
        return previous_content.is_displayed()

    def get_answer_text(self, parent_element):
        answer_text = parent_element.find_elements(*faq.FAQ_ANSWER_SECTIONS)
        return answer_text

    def is_answer_text_displayed(self, question_content):
        return question_content.is_displayed()

    def check_hidden_text_is_displayed(self):
        parent_elements = self.get_questions()
        previous_content = None

        for element in parent_elements:
            self.click_parent_element(element)
            question_content = self.get_question_content(element)

            assert self.is_answer_text_displayed(question_content), "The answer text is not shown"

            if previous_content is not None:
                assert not self.is_previous_content_hidden(
                    previous_content), "The previous answer content is not hidden"

            previous_content = question_content

    def check_header_title(self, link_name):
        self.click_header_link(link_name)
        expected_title = "Frequently Asked Questions"
        displayed_title = self.driver.find_element(*faq.DISPLAYED_TITLE).text
        assert displayed_title == expected_title

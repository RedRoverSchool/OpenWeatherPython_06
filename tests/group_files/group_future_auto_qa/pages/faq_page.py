from tests.group_files.group_future_auto_qa.locators.faq_page_locators import FAQPageLocators
from pages.base_page import BasePage


class FAQPage(BasePage):
    locators = FAQPageLocators()

    def open_faq_page(self):
        self.driver.get(self.locators.FAQ_PAGE_URL)

    def get_questions(self):
        parent_elements = self.driver.find_elements(*self.locators.FAQ_QUESTIONS_HEADINGS)
        return parent_elements

    def click_parent_element(self, parent_element):
        self.driver.execute_script("arguments[0].click();", parent_element)

    def get_question_content(self, element):
        question_content = element.find_element(*self.locators.FAQ_ANSWER_SECTIONS)
        return question_content

    def is_previous_content_hidden(self, previous_content):
        return previous_content.is_displayed()

    def get_answer_text(self, parent_element):
        answer_text = parent_element.find_elements(*self.locators.FAQ_ANSWER_SECTIONS)
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

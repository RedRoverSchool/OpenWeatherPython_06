from pages.ask_a_question_page import AskQuestionPage


class TestAskQuestionPage:

    def test_tc_002_03_09_ask_a_question(self, driver, open_and_load_main_page):
        ask_a_question_page = AskQuestionPage(driver)
        ask_a_question_page.check_header_title("ask a question")
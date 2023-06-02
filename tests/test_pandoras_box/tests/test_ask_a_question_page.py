from tests.test_pandoras_box.pages.ask_a_question_page import AskAQuestiontPage


def test_tc_002_03_09_ask_a_question(driver, open_and_load_main_page):
    ask_a_question_page = AskAQuestiontPage(driver)
    ask_a_question_page.check_header_title("ask a question")
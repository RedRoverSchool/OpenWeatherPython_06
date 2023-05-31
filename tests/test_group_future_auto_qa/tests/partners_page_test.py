from tests.test_group_future_auto_qa.pages.partners_page import PartnersPage

def test_TC_011_13_02_Verify_correct_redirection_of_the_link_View_on_Github(driver):
        partners_page = PartnersPage(driver)
        partners_page.open()
        partners_page.verify_redirection_git_button_python_to_the_new_webpage()


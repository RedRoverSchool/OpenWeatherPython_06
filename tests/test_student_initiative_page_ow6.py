from pages.student_initiatives_page import StudentInitiativePage
from pages.base_page import BasePage
from test_data.urls import StudentInitiativeUrls

class TestStudentInitiativePage:

    def test_tc_010_02_06_verify_website_link_redirects_to_main_page(self, driver, wait):
        student_initiative_page = StudentInitiativePage(driver, link='https://openweathermap.org/our-initiatives/student-initiative')
        student_initiative_page.open_page()
        student_initiative_page.verify_website_link_redirects_to_main_page(wait=wait),\
            'Website link does not redirect to main page'

    def test_tc_010_02_07_verify_correct_redirection_to_popup_window(self, driver, wait):
        student_initiative_page = StudentInitiativePage(driver, link='https://openweathermap.org/our-initiatives/student-initiative')
        student_initiative_page.open_page()
        student_initiative_page.verify_correct_redirection_to_popup_window(wait=wait),\
            'Pop up window does not open'


    def test_TC_010_02_05_Get_access_open_authorization_window(self, driver):
        student_initiative = StudentInitiativePage(driver, StudentInitiativeUrls.STUDENT_INITIATIVE)
        student_initiative.open_page()
        student_initiative.check_open_autorization()

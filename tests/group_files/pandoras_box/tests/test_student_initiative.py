from tests.group_files.pandoras_box.pages.student_initiative import StudentInitiative

def test_TC_010_02_05_Get_access_open_authorization_window(driver):
    student_initiative = StudentInitiative(driver, StudentInitiative.STUDENT_INITIATIVE_URL)
    student_initiative.open_page()
    student_initiative.check_open_autorization()

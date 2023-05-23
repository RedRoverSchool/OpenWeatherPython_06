
from tests.test_pandoras_box.pages.footer import Footer

def test_TC_003_12_11_link_Google_Play_leads_to_correct_page_in_GP(driver, open_and_load_main_page, wait):
    google_link = Footer(driver)
    google_link.check_leads_link_Googl_Play()

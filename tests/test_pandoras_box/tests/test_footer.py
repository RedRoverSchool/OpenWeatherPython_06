import pytest
from tests.test_pandoras_box.test_data.header_data import URLs
from tests.test_pandoras_box.pages.footer import Footer

@pytest.mark.parametrize('URL', URLs)
def test_TC_003_03_01_Product_Collections_title_is_visible(driver, URL):
    page = Footer(driver, link=URL)
    page.open_page()
    page.check_product_collections_module_title_is_visible()

def test_TC_003_12_11_link_Google_Play_leads_to_correct_page_in_GP(driver, open_and_load_main_page, wait):
    google_link = Footer(driver)
    google_link.check_leads_link_Googl_Play()

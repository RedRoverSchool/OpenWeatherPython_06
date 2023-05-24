import pytest
from tests.test_pandoras_box.test_data.header_data import URLs
from tests.test_pandoras_box.pages.footer import Footer

@pytest.mark.parametrize('URL', URLs)
def test_TC_003_03_01_Product_Collections_title_is_visible(driver, URL):
    page = Footer(driver, link=URL)
    page.open_page()
    page.check_product_collections_module_title_is_visible()
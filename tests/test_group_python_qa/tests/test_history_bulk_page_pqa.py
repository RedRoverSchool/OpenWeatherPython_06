from tests.test_group_python_qa.pages.history_bulk_page_pqy import HistoryBulk
from tests.test_group_python_qa.links.links_all_pages import *


class TestHistoryBulk:

    def test_tc_005_18_verify_the_blocks_are_presented_on_the_page(self, driver, wait):
        history_bulk_page = HistoryBulk(driver, URL_HISTORY_BULK)
        history_bulk_page.open_page()
        history_bulk_page.visibility_of_the_blocks(wait)

from pages.base_page import BasePage
from tests.test_group_python_qa.locators.locators import HistoryBulkLocators


class HistoryBulk(BasePage):
    locator = HistoryBulkLocators()

    def visibility_of_the_blocks(self):
        self.elements_are_present(HistoryBulkLocators.BLOCK_LOCATORS)
        self.elements_are_present(HistoryBulkLocators.BLOCK_2_LOCATORS)

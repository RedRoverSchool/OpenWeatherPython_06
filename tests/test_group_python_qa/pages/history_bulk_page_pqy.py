from pages.base_page import BasePage
from tests.test_group_python_qa.locators.locators import HistoryBulkLocators


class HistoryBulk(BasePage):
    locator = HistoryBulkLocators()

    def visibility_of_the_blocks(self, wait):
        self.element_is_displayed(HistoryBulkLocators.FEATURES_OF_HISTORY_BULK_BLOCK, wait)
        self.element_is_displayed(HistoryBulkLocators.HOW_TO_GET_HISTORICAL_WEATHER_DATA_BLOCK, wait)
        self.element_is_displayed(HistoryBulkLocators.SAMPLE_DATA_BLOCK, wait)
        self.element_is_displayed(HistoryBulkLocators.WEATHER_FIELDS_IN_HISTORY_BULK_BLOCK, wait)
        self.element_is_displayed(HistoryBulkLocators.PARAMETERS_BLOCK, wait)
        self.element_is_displayed(HistoryBulkLocators.EXAMPLE_BLOCK, wait)
        self.element_is_displayed(HistoryBulkLocators.LIST_OF_WEATHER_CONDITIONS_CODES, wait)
    


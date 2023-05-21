from tests.test_group_snake_oil.locators.dashboard_locators import DashboardPageLocators
from tests.test_group_snake_oil.links.all_links import EXPEXTED_URLS_SIGNED_IN_LIST, EXPECTED_URLS_SIGNED_OUT_LIST

# List of tuples, containing locators of text-links and respective URLs,
# where user expected to be redirected to, when NOT signed-in user clicks the text-link
EXPECTED_LINKS_AND_LOCATORS_SIGNED_OUT = [(DashboardPageLocators.ALL_TEXT_LINK_LOCATORS[i],
                                           EXPECTED_URLS_SIGNED_OUT_LIST[i])
                                          for i in range(len(DashboardPageLocators.ALL_TEXT_LINK_LOCATORS))]

# List of tuples, containing locators of text-links in and respective URLs,
# where user expected to be redirected to, when signed-in user clicks the text-link
EXPECTED_LINKS_AND_LOCATORS_SIGNED_IN = [(DashboardPageLocators.ALL_TEXT_LINK_LOCATORS[i],
                                          EXPEXTED_URLS_SIGNED_IN_LIST[i])
                                         for i in range(len(DashboardPageLocators.ALL_TEXT_LINK_LOCATORS))]

from oldTests.test_group_lutz_squad.pages.partners_and_solutions_page import PartnersAndSolutionsPage
from oldTests.test_group_lutz_squad.locators.partners_and_solutions_page_locators import PartnersAndSolutionsPageLocators as PAS


def test_TC_011_02_01_verify_more_details_link_is_clickable(driver, wait):
    page = PartnersAndSolutionsPage(driver, link=PAS.PARTNERS_AND_SOLUTIONS_PAGE_LINK)
    page.open_page()
    page.more_details_link_is_clickable(wait)


def test_TC_011_02_02_Verify_that_user_is_redirected_to_a_new_window_page_after_click_on_the_link_More_detailes_with_source_code(driver, wait):
    page = PartnersAndSolutionsPage(driver, link=PAS.PARTNERS_AND_SOLUTIONS_PAGE_LINK)
    page.open_page()
    page.redirecting_to_more_details_with_source_code_page(wait)
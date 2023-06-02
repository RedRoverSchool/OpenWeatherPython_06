from tests.test_group_lutz_squad.pages.partners_and_solutions_page import PartnersAndSolutionsPage
from tests.test_group_lutz_squad.locators.partners_and_solutions_page_locators import PartnersAndSolutionsPageLocators as PAS


def test_TC_011_02_01_verify_more_details_link_is_clickable(driver, wait):
    page = PartnersAndSolutionsPage(driver, link=PAS.PARTNERS_AND_SOLUTIONS_PAGE_LINK)
    page.open_page()
    page.more_details_link_is_clickable(wait)

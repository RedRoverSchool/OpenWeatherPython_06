from tests.test_group_100000.pages.api_page import RoadRiskApi
from tests.test_group_100000.locators.api_page_locators import RoadRiskApi as R


def test_TC_005_08_04_redirection_to_the_how_to_request_road_risk_API_section_of_the_page(driver):
    page = RoadRiskApi(driver, link=R.ROAD_RISK_API_LINK)
    page.open_page()
    page.check_redirect_to_page_section()


def test_TC_005_08_03_road_risk_api_visibility_of_road_risk_api_concept_section(driver):
    page = RoadRiskApi(driver, link=R.ROAD_RISK_API_LINK)
    page.open_page()
    page.check_visibility_concept_section()


def test_TC_005_08_01_road_risk_api_verify_page_title_for_road_risk_api(driver):
    page = RoadRiskApi(driver, link=R.ROAD_RISK_API_LINK)
    page.open_page()
    page.check_module_title_road_risk_page()
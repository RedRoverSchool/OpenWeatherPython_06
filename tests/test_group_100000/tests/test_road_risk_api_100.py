from tests.test_group_100000.pages.api_page import RoadRiskApi


def test_TC_005_08_04_redirection_to_the_how_to_request_road_risk_API_section_of_the_page(driver):
    page = RoadRiskApi(driver)
    page.check_redirect_to_page_section()


def test_TC_005_08_03_road_risk_api_visibility_of_road_risk_api_concept_section(driver):
    page = RoadRiskApi(driver)
    page.check_visibility_concept_section()


def test_TC_005_08_01_road_risk_api_verify_page_title_for_road_risk_api(driver):
    page = RoadRiskApi(driver)
    page.check_module_title_road_risk_page()


def test_TC_005_08_05_redirection_to_the_list_of_sectional_sources_of_weather_warnings_section_of_the_page(driver):
    page = RoadRiskApi(driver)
    page.check_redirection_to_the_section_of_the_page()
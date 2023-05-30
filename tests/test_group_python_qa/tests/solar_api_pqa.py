from tests.test_group_python_qa.pages.solar_api_pqa import SolarApi


def test_tc_005_10_03_correct_redirection_for_how_to_get_access_link(driver, wait):
    solar_api = SolarApi(driver, SolarApi.URL_SOLAR_API)
    solar_api.check_for_correct_redirection_for_how_to_get_access_link(wait)

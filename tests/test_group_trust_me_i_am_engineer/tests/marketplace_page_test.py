from tests.test_group_trust_me_i_am_engineer.pages.marketplace_page import MarketplacePage
import pytest

def test_TC_007_02_01_verify_the_method_of_input_location(driver):
    page = MarketplacePage(driver)
    page.verify_the_method_of_input_location()

def test_TC_007_02_02_verify_search_by_location_name(driver):
    page = MarketplacePage(driver)
    page.verify_search_by_location_name()

def test_TC_007_02_03_verify_search_by_coordinates(driver):
    page = MarketplacePage(driver)
    page.verify_search_by_coordinates()

def test_TC_007_02_05_verify_visibility_clickability_map_btn(driver):
    page = MarketplacePage(driver)
    page.verify_visibility_clickability_map_btn()

def test_TC_007_02_04_verify_search_by_import_csv(driver):
    page = MarketplacePage(driver)
    page.verify_search_by_import_csv()

def test_TC_007_02_06_verify_visibility_clickability_satellite_btn(driver):
    page = MarketplacePage(driver)
    page.verify_visibility_clickability_satellite_btn()

def test_TC_007_02_07_verify_visibility_clickability_terrain_checkbox(driver):
    page = MarketplacePage(driver)
    page.verify_visibility_clickability_terrain_checkbox()

def test_TC_007_02_09_verify_visibility_clickability_zoom_in_button(driver, wait):
    page = MarketplacePage(driver)
    page.verify_visibility_clickability_zoom_in(wait)

def test_TC_007_02_10_verify_visibility_clickability_zoom_out_button(driver):
    page = MarketplacePage(driver)
    page.verify_visibility_clickability_zoom_out()
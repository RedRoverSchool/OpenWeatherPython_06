def test_should_open_given_link(driver):
    driver.get('https://openweathermap.org/')
    assert 'openweathermap' in driver.current_url
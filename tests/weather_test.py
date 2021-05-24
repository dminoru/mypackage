from mypackage.weather import weather_forecast, search_city

def test_search_city():
    assert search_city('london') != None

def test_weather_forecast():
    assert type(weather_forecast(44418)) == list

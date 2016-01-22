from mock import patch
from stupid.weather import WeatherForecast


@patch("stupid.weather.requests.get", spec=True)
def test_weather_smoke(requests_get):
    requests_get.return_value.json.return_value = {
        'currently': {
            'windSpeed': 666,
            'precipProbability': 0.9,
            'apparentTemperature': 36.6,
            'temperature': 41.6,
        }
    }
    result = WeatherForecast().report()
    assert result == "37 \u00B0F at 666.0 mph wind and I am 90% sure it is raining"


@patch("stupid.weather.requests.get", spec=True)
def test_weather_no_perception(requests_get):
    requests_get.return_value.json.return_value = {
        'currently': {
            'windSpeed': 666,
            'precipProbability': 0,
            'apparentTemperature': 36.6,
            'temperature': 41.6,
        }
    }
    result = WeatherForecast().report()
    assert result == "37 \u00B0F at 666.0 mph wind"


@patch("stupid.weather.requests.get", spec=True)
def test_weather_snowing(requests_get):
    requests_get.return_value.json.return_value = {
        'currently': {
            'windSpeed': 666,
            'precipProbability': 0.9,
            'apparentTemperature': 16.6,
            'temperature': 21.6,
        }
    }
    result = WeatherForecast().report()
    assert result == "17 \u00B0F at 666.0 mph wind and I am 90% sure it is snowing"

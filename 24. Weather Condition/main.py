import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "318c42d8ceaf544f64704d57dec00e2e" #tengo que poner la key

weather_params = {
    "lat": 51.759050,
    "lon": 19.458600,
    "appid": api_key,
    "exclude": "current, minutely, daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data["hourly"])
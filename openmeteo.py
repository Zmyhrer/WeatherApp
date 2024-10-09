import requests
import json



class OpenMeteoAPI:

    def __init__(self, params):
        self._root_url = "https://api.open-meteo.com/v1/forecast?"
        self._params = params


    def get_weather_data(self):
        r = requests.get(self._root_url, self._params)

        with open('weather_info.json', 'w') as file:
            json.dump(r.json(), file)

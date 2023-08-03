# API keys | 3 August 2023

import requests
from pprint import pprint # A way to show json files without it being super ugly

API_KEY = "" # put the API key here.

city = input("Enter a city: ")

base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city},uk&APPID={API_KEY}"

weather_data = requests.get(base_url).json() # Python kinda treats the json object like a DICTIONARY

pprint(weather_data)

pprint("FEELS LIKE:", weather_data['main']['feels_like'])

# For it to work, do "Ottawa, CA" or something.
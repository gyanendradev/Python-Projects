import requests
from pprint import pprint

API_Key = "a20c63d437332080ffa40a3291878000"
city = input("Enter city's name to get it's weather : ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + \
    API_Key+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)

import requests
import openweather
city = 'islamabad'
API_key = 'f6e6060d03d7288cd08db756c5ce6726'
lat = 90
lon = 90
#conn = f'https://api.openweathermap.org/data/3.0/onecall/overview?lat={lat}&lon={lon}&appid={API_key}'
response = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip=E14,GB&appid={API_key}')
data = response.json()
for key,value in data.items():
    print(f'{key} : {value}')
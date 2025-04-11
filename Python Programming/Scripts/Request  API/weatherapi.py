import requests
import openweather
city = 'islamabad'
API_key = 'f6e6060d03d7288cd08db756c5ce6726'
response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_key}')
data = response.json()
for dic in data:
    for key, value in dic.items():
        print(f'{key} : {value}')
import requests
city = 'islamabad'
API_key = 'b18b3c1107f328c1afa2de5470e7cfaa'
lat = 26.2447
lon = 68.3935
response = requests.get(f'https://api.agromonitoring.com/agro/1.0/weather?lat={lat}&lon={lon}&appid={API_key}')
data = response.json()
#print(data)
for key,value in data.items():
    if type(value) == type([]):
        for x in value:
            for key,value in x.items():
                print(f'{key} : {value}')
    elif type(value) == type({'x':100}):
        for index, val in value.items():
            print(f'{index} : {val}')
    else:
        print(f'{key} : {value}')
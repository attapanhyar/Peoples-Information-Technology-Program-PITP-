import requests
response = requests.get('https://api.github.com') 
data = response.json()
#print(data)

for key,value in data.items():
    print(f'{key} : {value}')

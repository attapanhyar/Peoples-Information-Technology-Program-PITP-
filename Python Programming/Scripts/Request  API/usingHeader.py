import requests
headers = {'User-Agent': 'MyApp'}
response = requests.get('https://api.github.com', headers=headers)
data = response.json()
print(data)

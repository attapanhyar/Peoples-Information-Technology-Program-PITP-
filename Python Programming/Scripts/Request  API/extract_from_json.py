import requests
response = requests.get('https://api.github.com') 
data = response.json()
current_user_url = data['current_user_url']
print(current_user_url)


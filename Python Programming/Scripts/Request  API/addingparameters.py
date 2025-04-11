import requests
response = requests.get('https://api.github.com/search/users', params={'q': 'octocat'})
data = response.json()
print(data)


    
import requests
response = requests.get('https://api.github.com') 
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")

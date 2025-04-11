import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }
    
    response = requests.get(base_url, params=params)
    

    if response.status_code == 200:
        data = response.json()  # Parse the response to JSON
        return data
    else:
        return None


def display_weather(data):
    if data:
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_description}")
        print(f"Humidity: {humidity}%")
    else:
        print("Error fetching weather data.")


if __name__ == "__main__":
    city = input("Enter the city name: ")
    api_key = "f6e6060d03d7288cd08db756c5ce6726" 
    

    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

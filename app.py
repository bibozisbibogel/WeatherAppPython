from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

# print(f"Your API key is {api_key}")

city = input("Enter a city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

weather_data = requests.get(url)

if weather_data.status_code == 200: # The city works
    weather_info = weather_data.json()['weather'][0]['main']
    temperature_info = weather_data.json()['main']['temp']
    print(f"The current weather is {weather_info}")
    print(f"The current temperature is {round(temperature_info)}°C")
else:
    print(f"The city {city} is invalid!")
import os
import requests
from dotenv import load_dotenv

# This physically loads the data from your hidden .env file into Python
load_dotenv()

API_KEY = os.environ.get('OPENWEATHER_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric" 
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("❌ Error: Invalid API key. Please check your credentials.")
        elif response.status_code == 404:
            print("❌ Error: City not found. Please check the spelling.")
        else:
            print(f"❌ HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Connection error occurred: {req_err}")
        return None

def display_weather(data):
    if not data:
        return

    city = data.get("name")
    country = data.get("sys", {}).get("country")
    weather_desc = data.get("weather", [{}])[0].get("description", "N/A").title()

    main_metrics = data.get("main", {})
    temp = main_metrics.get("temp")
    feels_like = main_metrics.get("feels_like")
    humidity = main_metrics.get("humidity")
    wind_speed = data.get("wind", {}).get("speed")

    print(f"\n🌍 Weather Report for {city}, {country}:")
    print("-" * 35)
    print(f"Condition:    {weather_desc}")
    print(f"Temperature:  {temp}°C")
    print(f"Feels Like:   {feels_like}°C")
    print(f"Humidity:     {humidity}%")
    print(f"Wind Speed:   {wind_speed} m/s")
    print("-" * 35 + "\n")

def main():
    print("🌤️  Welcome to the Command-Line Weather App 🌤️")
    while True:
        city = input("Enter a city name (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        if not city:
            print("Please enter a valid city name.")
            continue

        weather_data = fetch_weather(city)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
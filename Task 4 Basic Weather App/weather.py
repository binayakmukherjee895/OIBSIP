import os
import requests
from dotenv import load_dotenv 

load_dotenv()


api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    print("API key not found. Please check your .env file.")
    exit()

url="https://api.openweathermap.org/data/2.5/weather"

continue_search = "y"

while continue_search == "y":


    city_input = ""

    while not city_input:
        city_input = input("Enter city name: ").strip()

        if not city_input:
            print("Please enter a city name.")

    params = {
        "q": city_input,
        "appid": api_key,
        "units": "metric"
    }

    try:

        response = requests.get(url,params=params,timeout=10)

        if response.status_code == 200:

            data=response.json()

            city = data.get("name")
            temperature = data.get("main",{}).get("temp")
            humidity = data.get("main",{}).get("humidity")
            weather_list = data.get("weather",[])
            if weather_list:
                description = weather_list[0].get("description")
            else:
                description = None

            if city is None:
                city = "Unavailable"
            if temperature is None:
                temperature = "Unavailable"
            if humidity is None:
                humidity = "Unavailable"
            if description is None:
                description = "Unavailable"


            print(f"City: {city}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description}")

        else:
            if response.status_code == 404:
                print("City not found. Please check the spelling.")
            elif response.status_code == 401:
                print("Invalid API key. Please check your API configuration.")
            elif response.status_code == 429:
                print("Too many requests. Please try again later.") 
            else:
                print(f"Weather service error. Status code: {response.status_code}")

    except requests.exceptions.RequestException:
        print("Unable to connect to the weather service.")

    while True:
        continue_search = input("Search another city? (y/n): ").strip().lower()

        if continue_search in ("y","n"):
            break
        print("Please enter y or n.")
    

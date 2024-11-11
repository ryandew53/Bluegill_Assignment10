# Name: Ryan Dew, Kayla Wilson
# email: dewrm@mail.uc.edu, 
# Assignment Number: 10
# Due Date:  11/14/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: 

# Brief Description of what this module does:
# Citations: https://weatherstack.com/documentation --> API documentation for entering key. 
# Anything else that's relevant: Used inclass assignment and module 10 slides for reference. 

import json
import requests


url = "https://api.weatherstack.com/current?access_key=2248de933bfdb1b2b7f831ddce40c468"

# Enter the city you want to get the weather data for
querystring = {"query":"London"}

response = requests.get(url, params=querystring)

parsed_json = response.json()

# Create a dictionary to store the weather data
if "current" in parsed_json:
    weather_data = {
        "location": parsed_json.get("location", {}).get("name", "Unknown"),
        "temperature": parsed_json["current"].get("temperature"),
        "humidity": parsed_json["current"].get("humidity"),
        "weather_descriptions": parsed_json["current"].get("weather_descriptions", ["No description"]),
        "wind_speed": parsed_json["current"].get("wind_speed"),
        "feels_like": parsed_json["current"].get("feelslike"),
    }

print(weather_data)
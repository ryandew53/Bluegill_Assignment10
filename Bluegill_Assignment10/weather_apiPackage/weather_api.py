# weather_api.py

# Name: Ryan Dew, Kayla Wilson
# email: dewrm@mail.uc.edu, wilso5ky@mail.uc.edu
# Assignment Number: 10
# Due Date:  11/14/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: This assignment is to use an API from the web to fetch data, create a dictionary with that data, print it to the terminal, and then finally save that data in a csv file.

# Brief Description of what this module does: This module is used to fetch weather data from the weatherstack API, create a dictionary with that data, informs the main what to print in the terminal, and then save that data to a csv file.
# Citations: https://weatherstack.com/documentation --> API documentation for entering key, for formatting the output in the termimal and what keywords to use to use the data from the api. https://www.geeksforgeeks.org/writing-csv-files-in-python/ --> Converting output to csv format
# Anything else that's relevant: Used inclass assignment and module 10 slides for reference. 

# weather_api.py
import requests
import json
import csv

class WeatherClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weatherstack.com/current"
    # This function pulls weather data for a given location
    def fetch_weather_data(self, location):
        querystring = {"access_key": self.api_key, "query": location}
        response = requests.get(self.base_url, params=querystring)
        
        parsed_json = json.loads(response.text)
        # Check if we have "current" weather data and then structure it nicely
        if "current" in parsed_json:
            weather_data = {
                "LOCATION": parsed_json.get("location", {}).get("name", "Unknown"),
                "REGION": parsed_json.get("location", {}).get("region", "Unknown"),
                "TEMPERATURE": parsed_json["current"].get("temperature"),
                "HUMIDITY": parsed_json["current"].get("humidity"),
                "WEATHER_DESCRIPTION": parsed_json["current"].get("weather_descriptions"),
                "WIND_SPEED": parsed_json["current"].get("wind_speed"),
                "FEELS_LIKE": parsed_json["current"].get("feelslike"),
                "CLOUD_COVER": parsed_json["current"].get("cloudcover"),
            }
            return weather_data
            return None
        
# This function saves the weather data to a CSV file
    def save_to_csv(self, data, filename="weather_data.csv"):
        if data:
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data.keys())
                writer.writerow(data.values())
            print(f"Data saved to {filename}")
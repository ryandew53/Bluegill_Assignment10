# main.py

# Name: Ryan Dew, Kayla Wilson
# email: dewrm@mail.uc.edu, wilso5ky@mail.uc.edu
# Assignment Number: 10
# Due Date:  11/14/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: This assignment is to use an API from the web to fetch data, create a dictionary with that data, print it to the terminal, and then finally save that data in a csv file.

# Brief Description of what this module does: this module is the main module that will run the program from weather_api.py. It imports the weather_api.py module and runs the main function which will prompt the user to enter a location and then fetch the weather data for that location.
# Citations: https://weatherstack.com/documentation --> API documentation for entering key, for formatting the output in the termimal and what keywords to use to use the data from the api.
# Anything else that's relevant: Used inclass assignment and module 10 slides for reference. 

import json
import requests
from weather_apiPackage.weather_api import WeatherClient

def main():
    # Enter your API key below
    api_key ="2248de933bfdb1b2b7f831ddce40c468"

    # Allows the user to input a city
    location = input("Enter the location: ")

    weather_client = WeatherClient(api_key)

    weather_data = weather_client.fetch_weather_data(location)

    if weather_data:
        print("Weather Data: ")
        for key, value in weather_data.items():
            print(f"{key}: {value}")

    # Saves data to a csv file
    weather_client.save_to_csv(weather_data)


if __name__ == '__main__':
    main()
 

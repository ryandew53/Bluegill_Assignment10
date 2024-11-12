# weather_api.py

# Name: Ryan Dew, Kayla Wilson
# email: dewrm@mail.uc.edu, wilso5ky@mail.uc.edu
# Assignment Number: 10
# Due Date:  11/14/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: This assignment is to use an API from the web to fetch data, create a dictionary with that data, print it to the terminal, and then finally save that data in a csv file.

# Brief Description of what this module does:
# Citations: https://weatherstack.com/documentation --> API documentation for entering key. 
# Anything else that's relevant: Used inclass assignment and module 10 slides for reference. 

import requests
import json
import csv

class WeatherClient:
    

# Name: Ryan Dew, Kayla Wilson
# email: dewrm@mail.uc.edu, 
# Assignment Number: 10
# Due Date:  11/14/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: 

# Brief Description of what this module does:
# Citations: 
# Anything else that's relevant:

import json
import requests



url = "https://api.weatherstack.com/current?access_key=2248de933bfdb1b2b7f831ddce40c468"


querystring = {"query":"New Delhi"}

response = requests.get(url, params=querystring)

print(response.json())
import requests
from dotenv import load_dotenv
load_dotenv()
import os

# base_url = "https://openapi.data.uwaterloo.ca/v3/FoodServices/outlets"
# term = "1249"
# endpoint = "Courses/{term}"
# url = base_url+"endpoint"
# print(url)

# headers = {
#     "x-api-key": "798F55DD931F4C8FB604A067E451FC57"
# }

# try:
#     response = requests.get(base_url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         print(data)  
#     else:
#         print(f"Failed to retrieve data. Status code: {response.status_code}")
#         print(f"Error message: {response.text}")

# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")

base_url = "https://openapi.data.uwaterloo.ca/v3/Courses/1249"
def get_food_services():
    # url = f"{base_url}/Locations"
    headers = {
        "x-api-key": "798F55DD931F4C8FB604A067E451FC57"
    }
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return []
    else:
        print(f"Failed to retrieve food services. Status code: {response.status_code}")
        return []
    
get_food_services()
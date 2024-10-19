import requests
from dotenv import load_dotenv
load_dotenv()

base_url = "https://openapi.data.uwaterloo.ca/v3/FoodServices/outlets"
term = "1249"
endpoint = "Courses/{term}"
url = base_url+"endpoint"
print(url)

headers = {
    "x-api-key": "798F55DD931F4C8FB604A067E451FC57"
}

try:
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)  
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print(f"Error message: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

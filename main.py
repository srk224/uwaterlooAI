from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
waterloo_api_key = os.environ.get("WATERLOO_API_KEY")
groq_api_key = os.environ.get("GROQ_API_KEY")

app = Flask(__name__)
CORS(app)
client = Groq(api_key=groq_api_key)

# Define base URL for the Waterloo API
base_url = "https://openapi.data.uwaterloo.ca/v3"

# Function to get food service outlets
def get_food_services():
    url = f"{base_url}/FoodServices/outlets"
    headers = {"x-api-key": "798F55DD931F4C8FB604A067E451FC57"}
    response = requests.get(url, headers=headers)
    # print(response.json())
    return response.json().get("data", []) if response.status_code == 200 else []

def get_news():
    url = f"{base_url}/Wcms/latestnews/3"
    headers = {"x-api-key": "798F55DD931F4C8FB604A067E451FC57"}
    response = requests.get(url, headers=headers)
    # print(response.json())
    return response.json()

# Function to get holiday dates
def get_holiday_dates():
    url = f"{base_url}/HolidayDates/paidholidays/2024"
    headers = {"x-api-key": "798F55DD931F4C8FB604A067E451FC57"}
    response = requests.get(url, headers=headers)
    # print(response.json())
    return response.json()

# Function to get campus locations (e.g., gyms, counseling centers)
def get_campus_services():
    url = f"{base_url}/Locations"
    headers = {"x-api-key": "798F55DD931F4C8FB604A067E451FC57"}
    response = requests.get(url, headers=headers)
    # print(response.json())
    return response.json().get("data", []) if response.status_code == 200 else []
    
def get_course():
    term_code = "1249"
    url = f"{base_url}/Courses/{term_code}"
    headers = {"x-api-key": "798F55DD931F4C8FB604A067E451FC57"}
    response = requests.get(url, headers=headers)
    # print(response.json())
    return response.json().get("data", []) if response.status_code == 200 else []
    

# Function to query Groq LLM for decision-making
def query_groq_llm(query):
    prompt = (
        f"You are a smart assistant for University of Waterloo students. "
        f"Based on the user's query, determine which API to call. Respond with only one of the following: "
        f"'FoodServices', 'HolidayDates', 'News', 'Course' or 'CampusServices'. User query: '{query}'"
    )
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content.strip()

# Function to handle user query dynamically
def handle_user_query(query):
    # Step 1: Use LLM to determine the action
    action = query_groq_llm(query)
    print(action)
    if action == "Course":
        response_content=""
        course = get_course()
        for c in course:
            name = c[('title')]
            description = new[('itemUri')]
            response_content += f"Title {title} with Url {description}"

        prompt = (
        f"Format the above answer {response_content} for the {query} in points.'"
        )
        chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
        )
        # print(chat_completion.choices[0].message.content.strip())
        return chat_completion.choices[0].message.content.strip()
    
    if action == "News":
        response_content=""
        news = get_news()
        for new in news:
            title = new[('title')]
            url = new[('itemUri')]
            response_content += f"Title {title} with Url {url}"

        prompt = (
        f"Format the above answer {response_content} for the {query} in points.'"
        )
        chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
        )
        # print(chat_completion.choices[0].message.content.strip())
        return chat_completion.choices[0].message.content.strip()

    if action == "FoodServices":
        # Step 2: Get food services and integrate holiday dates
        food_services = get_food_services()

        response_content = "Here are the available food outlets on campus:\n"
        for outlet in food_services:
            name = outlet.get('name', 'Unknown')
            location = outlet.get('location','Unknown')
            hours = outlet.get('hours', {}).get('mon', 'N/A')

            response_content += f"Name: {name}\nLocation: {location}\nHours: {hours}\n\n"
        
        prompt = (
        f"Format the above answer {response_content} for the {query} in points .'"
        )
        chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
        )
        # print(chat_completion.choices[0].message.content.strip())
        return chat_completion.choices[0].message.content.strip()
        # print(response_content)
    
    elif action == "CampusServices":
        # Step 2: Get campus services
        campus_services = get_campus_services()

        # Step 3: Construct the response
        response_content = "Here are some campus services:\n"
        for service in campus_services:
            name = service.get('name', 'Unknown')
            building = service.get('building_code', 'Unknown')
            description = service.get('description', 'No description available')
            response_content += f"{name} in {building}: {description}\n\n"
        
        # print(response_content)
        return response_content
    
    elif action == "HolidayDates":
        # Step 2: Get holiday dates
        holidays = get_holiday_dates()
        # print(holidays)
        # Step 3: Construct the response
        holiday_name = ""
        holiday_date = ""
        for holiday in holidays:
            holiday_name += (holiday['name'])
            holiday_date+= (holiday['holidayDate'][0:10])
            response_content = f"{holiday_name} on date : {holiday_date}"

        prompt = (
        f"Format the above answer {response_content} for the {query} in points and endline at the end.'"
        )
        chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
        )
        # print(chat_completion.choices[0].message.content.strip())
        return chat_completion.choices[0].message.content.strip()


# if __name__ == "__main__":
#     result = handle_user_query("Give me buildings about Waterloo")
#     print(result)
#     # app.run(port=5000, debug=True)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get("query", "")
    result = handle_user_query(user_query)
    print(result)
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
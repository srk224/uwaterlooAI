from dotenv import load_dotenv
import os
from groq import Groq
import requests

load_dotenv()

waterloo_api_key = os.environ.get("WATERLOO_API_KEY")
groq_api_key = os.environ.get("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)
base_url = "https://openapi.data.uwaterloo.ca/v3"

def get_food_services():
    url = f"{base_url}/FoodServices/outlets"
    headers = {
        "x-api-key": "798F55DD931F4C8FB604A067E451FC57"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Failed to retrieve food services. Status code: {response.status_code}")
        return []

def determine_action_with_llm(query):
    prompt = (
        f"You are an assistant for managing campus services at the University of Waterloo. "
        f"Based on the user's query, determine which API should be called and how to process it. "
        f"User query: '{query}'. Respond with just 'FoodServices' if the query is about food services."
    )
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
    )
    action = chat_completion.choices[0].message.content.strip()
    return action

def handle_user_query(query):
    # Step 1: Use the LLM to determine the appropriate action
    action = determine_action_with_llm(query)
    print(action)
    
    if action == "FoodServices":
        food_services = get_food_services()
        
        response_content = "Here are the available food outlets on campus:\n"
        for outlet in food_services:
            response_content += (
                f"Name: {outlet.get('name')}\n"
                f"Location: {outlet.get('location')}\n"
                f"Hours: {outlet.get('hours', {}).get('mon', 'N/A')} (Monday)\n\n"
            )
        
        print(response_content)
    else:
        print("I'm not sure how to handle this request. Please try rephrasing your question.")

if __name__ == "__main__":
    user_query = "Where can I get food on campus right now?"
    
    handle_user_query(user_query)

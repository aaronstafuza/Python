import requests
from datetime import datetime

#Define global variables for the user's information and API credentials. 
GENDER = "Male"
WEIGHT_KG = 84
HEIGHT_CM = 181
AGE = 25
APP_ID = "1489267a"
API_KEY = "a97aa9a5d3e52a51c3475218fbda7fd1"

#Prompt the user to input ther exercise text
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

#Define headers for the Nutricionix API request
#https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

#Define parameters for the Nutricionix API request, including excercise text and user info
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

#Send a POST request to the Nutritionix API with the headers and parameters
response = requests.post(exercise_endpoint, json=parameters, headers=headers)

#Convert the response to a JSON object
result = response.json()

#Get the current date and time as strings using the datetime module 
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

#Define the Sheety API endpoint for adding rows to the user's Google Sheet
sheet_endpoint = "https://api.sheety.co/3bde76707063f96bbc6e8145024fac66/myWorkouts/workouts"

#Iterate through the list of excersice in the result dictionary
for exercise in result["exercises"]:
    #Define the inputs for the Sheety API request, including exercise information and user info
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
#Send a POST request to the Sheety API with the inputs dictionary as the payload
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

#Print the response from the Sheety API request to the console
print(sheet_response.text)

import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  # could eliminate this line and combine above/below, but good practice for errors
results = response.json()["results"]
question_data = results

# use freeformatter.com to unescape html entities





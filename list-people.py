# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json

access_token = 'your_token_here'
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'user@example.com'
}
resp = requests.get(url, headers=headers, params=params)
print(json.dumps(resp.json(), indent=4))

person_id = 'previous_id'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
resp = requests.get(url, headers=headers)
print(json.dumps(resp.json(), indent=4))


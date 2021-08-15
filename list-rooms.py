# Fill in this file with the rooms/spaces listing code from the Webex Teams exercise
import requests

access_token = 'your_token_here'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())

# Fill in this file with the authentication code from the Webex Teams exercise
import requests
import json
access_token = 'MWNhMjU3NWUtZmZiYy00YjExLTk3NTktN2FmMWFlMzcwYTE1YjEzNGEyZmQtMzg3_P0A1_c1cccb6a-5e2d-4f80-86f9-f0dcefbd12f8'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
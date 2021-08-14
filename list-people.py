# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json

access_token = 'MWNhMjU3NWUtZmZiYy00YjExLTk3NTktN2FmMWFlMzcwYTE1YjEzNGEyZmQtMzg3_P0A1_c1cccb6a-5e2d-4f80-86f9-f0dcefbd12f8'
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'putu.hariyadi@universitasbumigora.ac.id'
}
resp = requests.get(url, headers=headers, params=params)
print(json.dumps(resp.json(), indent=4))

person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mZDQ3ODJmMi0yZjgzLTQ4NGYtYmQxOS1kNzhlNmM2NTZhOWI'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
resp = requests.get(url, headers=headers)
print(json.dumps(resp.json(), indent=4))


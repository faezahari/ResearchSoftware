import requests
import json

#get secret code from colab
from google.colab import userdata
token = userdata.get('DSIAPI')

#initialize request parameters
url = 'https://api.github.com/user'
headers = {'Authorization': 'Bearer ' + token}

#send request to Github
r = requests.get(url, headers=headers)

#print initial responses 
print(r.status_code)
print(r.text)

r_json = json.loads(r.text)
print(r_json)
import requests
from requests.auth import HTTPBasicAuth
import json

#getting the data 
response = requests.get('https://www.udemy.com/api-2.0/courses/',auth = HTTPBasicAuth('DmcabxNiiVj5slAK8ycd4F7Te7jySRezaZYfr4RS', 'pDdWt1Yw0bno9vMslAIAjelMIC95QuTHG3LBjB7rDUpMlpV2fkNpnQnD3MBR8QMoeAos0lzI06HSqz4lHDXflQQrYQbQdyiWJNVxqK0hjH8BQPwxYMl9BjixJTSaoTOa'))
packages_json = response.json()

# print(packages_json)

# #make it more readable
# readable_json = json.dumps(packages_json, sort_keys=True, indent=4)

# data = json.loads(response.text)
# data = json.dumps(data)

# Iterating through the json
# list

# print(data)
for i in packages_json['results']:
    print(i['id'])

 


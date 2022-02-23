import requests
from requests.auth import HTTPBasicAuth
import json


response = requests.get('https://www.udemy.com/api-2.0/courses/?search=javascript',auth = HTTPBasicAuth('DmcabxNiiVj5slAK8ycd4F7Te7jySRezaZYfr4RS', 'pDdWt1Yw0bno9vMslAIAjelMIC95QuTHG3LBjB7rDUpMlpV2fkNpnQnD3MBR8QMoeAos0lzI06HSqz4lHDXflQQrYQbQdyiWJNVxqK0hjH8BQPwxYMl9BjixJTSaoTOa'))


data = response.json()
for i in data['results']:
    title = (i['title'])
    url = ("https://www.udemy.com" + i['url'])
    image = (i['image_480x270'])
    price = (i['price'])
    id = str((i['id']))
    # creator_name = (i['instructor_name'])
    
    json_data = {
    'course name': title,
    'course link': url,
    'course piture' : image,
    'course price' : price,
    'course id' : id
    }
    with open('data_file.json', 'w') as fp:
        # fp.write('result nb: ' + str(a) + '\n')
        json.dump(json_data, fp, sort_keys=True, indent=4)



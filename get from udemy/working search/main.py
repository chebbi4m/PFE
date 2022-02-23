from textwrap import indent
from numpy import append
import requests
from requests.auth import HTTPBasicAuth
import json


link = "https://www.udemy.com/api-2.0/courses/"
print("Search")
search = input()
print("number of pages")
pages = input()
print("number of elements per page")
page_size = input()
price = 0
while price !="free" and price != "paid":
    print("free or paid")   
    price = input()
print("number of stars")
rating = input()     
new_link = link+"?page="+pages+"&page_size="+page_size+"&search="+search+"&price=price-"+price+"&language=en"+"&ratings="+rating
print(new_link)
response = requests.get(new_link,auth = HTTPBasicAuth('DmcabxNiiVj5slAK8ycd4F7Te7jySRezaZYfr4RS', 'pDdWt1Yw0bno9vMslAIAjelMIC95QuTHG3LBjB7rDUpMlpV2fkNpnQnD3MBR8QMoeAos0lzI06HSqz4lHDXflQQrYQbQdyiWJNVxqK0hjH8BQPwxYMl9BjixJTSaoTOa'))


data = response.json()
final_data=[]
creator=[]
for i in data['results']:
    title = (i['title'])
    url = ("https://www.udemy.com" + i['url'])
    image = (i['image_480x270'])
    price = (i['price'])
    id = str((i['id']))
    for j in i['visible_instructors']:
        creator.append(j['display_name'])

    json_data = {"course"
    'course name': title,
    'course link': url,
    'course piture' : image,
    'course price' : price,
    'course id' : id,
    'visible instructors' : creator,
    }
    final_data.append(json_data)

with open('data_file.json', 'w') as fp:
    json.dump(final_data, fp, sort_keys=True, indent=4)
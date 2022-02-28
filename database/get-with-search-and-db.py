from textwrap import indent
from numpy import append, insert
import requests
from requests.auth import HTTPBasicAuth
import json
from bs4 import BeautifulSoup
from http import client
import pymongo
client = pymongo.MongoClient()

mydb = client["training_nexus"]
mycollection = mydb["courses 3.0"]



link = "https://www.udemy.com/api-2.0/courses/"
print("Search")
search = input()
print("number of elements")
page_size = input()
price = 0
while price !="free" and price != "paid":
    print("free or paid")   
    price = input() 
new_link = link+"?page_size="+page_size+"&search="+search+"&price=price-"+price+"&language=en"
response = requests.get(new_link,auth = HTTPBasicAuth('DmcabxNiiVj5slAK8ycd4F7Te7jySRezaZYfr4RS', 'pDdWt1Yw0bno9vMslAIAjelMIC95QuTHG3LBjB7rDUpMlpV2fkNpnQnD3MBR8QMoeAos0lzI06HSqz4lHDXflQQrYQbQdyiWJNVxqK0hjH8BQPwxYMl9BjixJTSaoTOa'))

data = response.json()
final_data=[]
json_data = []
for i in data['results']:
    title = (i['title'])
    url = ("https://www.udemy.com" + i['url'])
    image = (i['image_480x270'])
    price = (i['price'])
    id = str((i['id']))
    for j in i['visible_instructors']:
        creator=(j['display_name'])

    comidocsite = url.replace("https://www.udemy.com/course", "https://comidoc.net/udemy")
    result = requests.get(comidocsite)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    td_working = soup.find_all('td',string = "working")
    coupons = []
    coupon_status = []
    for i in td_working:
        coupons = i.parent
        row_text = [x.text for x in coupons.find_all('td')]
        coupons = row_text[2]
        coupon_status = row_text[5]


    if coupons == [" "]:
        coupons = "no coupon here"


    json_data = {
    'course name': title,
    'course link': url,
    'course picture' : image,
    'course price' : price,
    'course id' : id,
    'visible instructors' : creator,
    'coupon' : coupons,
    'coupons status' : coupon_status
    }
    
    
    final_data.append(json_data)
    

with open('data_file.json', 'w') as fp:
    json.dump(final_data, fp, sort_keys=True, indent=4)
mycollection.insert_many(final_data)





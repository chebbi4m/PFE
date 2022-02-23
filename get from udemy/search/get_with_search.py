import requests
from requests.auth import HTTPBasicAuth
import json

link = "https://www.udemy.com/api-2.0/courses/?page=1&page_size=12"
print("Search")
x = input()
new_link = link +"&search="+x
print(new_link)
response = requests.get(new_link,auth = HTTPBasicAuth('DmcabxNiiVj5slAK8ycd4F7Te7jySRezaZYfr4RS', 'pDdWt1Yw0bno9vMslAIAjelMIC95QuTHG3LBjB7rDUpMlpV2fkNpnQnD3MBR8QMoeAos0lzI06HSqz4lHDXflQQrYQbQdyiWJNVxqK0hjH8BQPwxYMl9BjixJTSaoTOa'))


data = response.json()

for i in data['results']:
    print(i['id'])
    print(i['title'])

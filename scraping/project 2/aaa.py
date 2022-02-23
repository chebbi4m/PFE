from textwrap import indent
from numpy import append
import requests
from requests.auth import HTTPBasicAuth
import json
from bs4 import BeautifulSoup

result = requests.get("https://comidoc.net/udemy/how-to-read-music-step-by-step-guitar-lessons/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

coupons = []

for td in soup.find_all("td"):
        coupons.append(td.string)
print(coupons)
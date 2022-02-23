from bs4 import BeautifulSoup
import requests
import pprint

result = requests.get("https://comidoc.net/udemy/cross-cultural-management-made-easy")
src = result.content
soup = BeautifulSoup(src, 'lxml')
print(soup)


coupons = []
m=0
for td in soup.find_all("td"):
    m=m+1
    coupons.append(td.string)
    if m % 6==0:
        coupons.append("*****")
    
print(coupons)

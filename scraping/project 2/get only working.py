from bs4 import BeautifulSoup
import requests

result = requests.get("https://comidoc.net/udemy/cross-cultural-management-made-easy")
src = result.content
soup = BeautifulSoup(src, 'lxml')

td_working = soup.find_all('td',string = "working")
coupons = []

for parents in td_working:
    coupons = parents.parent

    print(coupons.get_text())



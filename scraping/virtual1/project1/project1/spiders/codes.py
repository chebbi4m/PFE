from fileinput import filename
import scrapy


name='codes'

start_urls = [
    'https://comidoc.net/udemy/digital-marketing-b2b'
]

def parse(self, response):
    # response.xpath("///html/body/div/div/div/main/article/section[9]")
    filename = 'response.html'
    result = response.xpath("//tbody").extract()
    with open(filename,'wb') as f:
        f.write(result)
    print(result)
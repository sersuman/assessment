import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.gyapu.com/category/mobile-phones').text


soup = BeautifulSoup(source, 'lxml')
        
proudct = []
data = {}
for item in soup.findAll("div", {"class": "fscont"}):
   
    # imageInfo = item.find("div",{"class":"product-tuple-image "})
    image = item.div.a.div.img['src']
    # priceDiv = item.find("div",{"class":"product-tuple-image "})
    # price = priceDiv.span.text
    # name = imageInfo.a.picture.source['title']
    # image = item.img['data-src']
    data = {
        "name": "name",
        "price": "price",
        "image": image
    }
    proudct.append(data)
print(data)
    
import requests
from aggregator.models import Item
from bs4 import BeautifulSoup

def getDrone():
    source = requests.get('https://www.okdam.com/category/drones-and-accessories').text
    source2 = requests.get('https://www.olx.in/items/q-drone?isSearchCall=true').text
  

    soup = BeautifulSoup(source, 'lxml')
    soup2 = BeautifulSoup(source2, 'lxml')

    for item in soup.findAll("div", {"class": "product-box"}):
        name = item.div.div.text
        price = item.div.p.span.text
        image = item.img['data-src']
        try:
            item = Item(
                name = name,
                price = price,
                image = image,
                topic = 'Drone'
            )
            item.save()
        except Item.DoesNotExist:
            return None
        

    for item in soup2.findAll("li", {"class": "EIR5N"}):
        image = item.a.figure.img['src']
        priceDiv = item.find("div",{"class":"IKo3_"})
        price = priceDiv.span.text
        name = item.a.figure.img['alt']
        
        try:
            item = Item(
                name = name,
                price = price,
                image = image,
                topic = 'Drone'
            )
            item.save()
        except Item.DoesNotExist:
            return None

def getTv():
    source = requests.get('https://www.okdam.com/category/led-tv').text

    soup = BeautifulSoup(source, 'lxml')

    for item in soup.findAll("div", {"class": "product-box"}):
        name = item.div.div.text
        price = item.div.p.span.text
        image = item.img['data-src']
        try:
            item = Item(
                name = name,
                price = price,
                image = image,
                topic = 'TV'
            )
            item.save()
        except Item.DoesNotExist:
            return None

        

def getMobile():
    source = requests.get('https://www.okdam.com/category/mobiles').text
    source2 = requests.get('https://www.olx.in/mobile-phones_c1453').text


    soup = BeautifulSoup(source, 'lxml')
    soup2 = BeautifulSoup(source2, 'lxml')

    for item in soup.findAll("div", {"class": "product-box"}):
        name = item.div.div.text
        price = item.div.p.span.text
        image = item.img['data-src']
        try:
            item = Item(
                name = name,
                price = price,
                image = image,
                topic = 'Mobile'
            )
            item.save()
        except Item.DoesNotExist:
            return None

        

    for item in soup2.findAll("li", {"class": "EIR5N"}):
        image = item.a.figure.img['src']
        priceDiv = item.find("div",{"class":"IKo3_"})
        price = priceDiv.span.text
        name = item.a.figure.img['alt']
        
        try:
            item = Item(
                name = name,
                price = price,
                image = image,
                topic = 'Mobile'
            )
            item.save()
        except Item.DoesNotExist:
            return None

      
def update_content():
    try:
        Item.objects.all().delete()
        getMobile()
        getTv()
        getDrone()
    except Item.DoesNotExist:
        return None


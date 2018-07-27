import json
import requests
from bs4 import BeautifulSoup
from random import randint

def joke():
    url = "http://latestsms.in"
    data = requests.get(url)
    page = data.text

    soup = BeautifulSoup((page), "lxml")
    block = soup.findAll("p", { "class" : "maincontent" })
    total = len(block)
    return block[randint(0,total)].text

def jokea():
    try:
        data = requests.get("http://api.icndb.com/jokes/random/")
        data = data.text.lower()
        joke = json.loads(data)
        return str(joke['value']['joke'].replace('chuck','Hero').replace('norris','Alom').replace('&quot;','"'))
    except:
        return ("Alom killed the server")

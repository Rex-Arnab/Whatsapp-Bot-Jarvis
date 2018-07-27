import requests
from bs4 import BeautifulSoup

def getLink(url):
    data = requests.get(url)
    data = data.text
    soup = BeautifulSoup((data), "lxml")
    q = ""
    page = soup.findAll("a")
    q += "Total Links : "+str(len(page))+"\n"
    for i in page:
        q += str(url)+str(i["href"])+"\n"
    return q

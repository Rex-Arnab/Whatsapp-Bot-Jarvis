import requests
from bs4 import BeautifulSoup

def phone(name):
    url = "https://www.gsmarena.com/"+name+".php"
    response = requests.get(url)
    page = response.text

    soup = BeautifulSoup(page, "lxml")
    page = soup.find("div",{"class":"main-review"})
    #phone pic
    pic = page.find("img")["src"]
    #spec table
    table = page.findAll("table")
    #phone Name
    title = page.find("h1",{"class":"specs-phone-name-title"})

    q = ""
    q += title.text

    for i in page.findAll("span",{"class":"specs-brief-accent"}):
        q += "\n"+i.text
    for i in range(len(table)):
        q += "\n"+table[i].text

    return q.replace("\n\n",""),pic

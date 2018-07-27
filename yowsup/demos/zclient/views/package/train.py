import requests
from bs4 import BeautifulSoup

def find(train="0"):
    if train == "0":
        return "Invalid Train Number"
    url = "https://runningstatus.in/status/"+str(train)+"-today"
    data = requests.get(url)
    data = data.text.encode("utf-8")
    soup = BeautifulSoup((data), "lxml")
    #print(soup)
    content = soup.find("div", {"class": "runningstatus-widget-content"})
    name = content.find("p")
    table = soup.find("table")
    q = ""
    q += "[SEARCH : *"+train+"*]\n"
    q += name.text
    #q += table.text
    return q.replace("\n\n\n\n\n","\n").replace("\n\n\n\n","\n").replace("\n\n\n","\n")

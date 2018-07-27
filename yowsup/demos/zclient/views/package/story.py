import requests
from bs4 import BeautifulSoup

def story():
    q = ""
    url = "https://www.indiansexstories.net/desi/howi-fucked-unsatisfied-colleague/"
    data = requests.get(url)
    page = data.text
    soup = BeautifulSoup((page), "lxml")
    heading = soup.find("div", { "class" : "single col-md-9" })
    story = soup.find("section", { "class" : "story-content" })
    q += heading.text +"\n"
    q += story.text
    return q

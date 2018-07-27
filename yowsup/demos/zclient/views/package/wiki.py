import requests
from bs4 import BeautifulSoup

def wiki(term):
    url = "https://en.wikipedia.org/wiki/"+term
    data = requests.get(url)
    data = data.text
    soup = BeautifulSoup((data), "lxml")
    q = ""
    try:
        if "not have an article" in soup.text:
            q += "sorry Not Found in wikipedia"
        elif "may refer to:" in soup.text:
            page = soup.find("div",{"class":"toc"})
            q += "The Word "+term+" Not Matched Try These:"
            q += page.text.replace("\n\n","").replace("See also","[Subscribe my youtube channel]")
        else:
            page = soup.findAll("p")
            for i in range(2):
                q += page[i].text+"\n"
    except:
        page = soup.find("div",{"class":"mw-content-ltr"})
        q += page.text
    return q

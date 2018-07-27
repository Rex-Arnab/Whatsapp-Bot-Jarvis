import requests
from bs4 import BeautifulSoup

def getLike(url):
    data = requests.get(url)
    page = data.text.encode()
    soup = BeautifulSoup((page), "lxml")
    span = soup.findAll('span')
    like = span[89].text
    dislike = span[94].text
    return like,dislike

def arnab(num="0"):
    url = "https://www.youtube.com/channel/UCo-j0bGZocOkrOVh32_jIhw/videos"
    data = requests.get(url)
    page = data.text.encode()
    soup = BeautifulSoup((page), "lxml")
    if num == "0":
        logo = soup.find("img")["src"]
    q = "[Programmer Arnab]"
    soup = BeautifulSoup((page), "lxml")
    video = soup.findAll("div", { "class" : "yt-lockup-content" })
    if num == "0":
        for i in video:
            like = i.find('div', {"class" : "yt-lockup-meta"})
            number = like.text.split(" views")
            link = i.find("h3", { "class" : "yt-lockup-title" })
            a = link.find('a')['href']
            l,d = getLike("https://www.youtube.com"+a)
            q += "\n\n*Title : "+link.text+"*\n"
            q += "https://www.youtube.com"+a+"\n"
            q += number[0]+" Views "+number[1]+"\n"
            q += "Like "+l.replace("\n","")+" Dislike "+d.replace("\n","")
        return q.replace("Like this video?","").replace("Like Add translations ","").replace("Don't like this video?","").replace("Sign in to make your opinion count.","").replace("Sign in",""),logo
    else:
        i = video[int(num)-1]
        like = i.find('div', {"class" : "yt-lockup-meta"})
        number = like.text.split(" views")
        link = i.find("h3", { "class" : "yt-lockup-title" })
        a = link.find('a')['href']
        l,d = getLike("https://www.youtube.com"+a)
        q += "\n\n*Title : "+link.text+"*\n"
        q += "https://www.youtube.com"+a+"\n"
        q += number[0]+" Views "+number[1]+"\n"
        q += "Like "+l.replace("\n","")+" Dislike "+d.replace("\n","")
        return q.replace("Like this video?","").replace("Like Add translations ","").replace("Don't like this video?","").replace("Sign in to make your opinion count.","").replace("Sign in","")

import requests
from bs4 import BeautifulSoup
from yowsup.demos.zclient.utils.media_downloader import ImageSender

def send_img(me,query,pic_sender):
    url = "https://www.pexels.com/search/"
    response = requests.get(url + query)
    page = response.text

    soup = BeautifulSoup(page, "lxml")
    tags=soup.findAll('img')
    try:
        img = tags[1]["src"]
        img,trash = img.split("?")
        print(img)
        pic_sender.send_by_url(jid=me, file_url=img)
    except:
        return "Invalid Image Name"

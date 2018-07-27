from .utils.config import *
import random
from .utils.session1 import SessionDB
from yowsup.demos.zclient.utils.media_downloader import ImageSender
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import requests
from bs4 import BeautifulSoup
import json
from yowsup.demos.zclient.views.package.hentai_comic import myhentaicomic
from yowsup.demos.zclient.views.package.phone import phone
from yowsup.demos.zclient.views.package.findlink import getLink
from yowsup.demos.zclient.views.package.google_img import Gimg

class StoreViews:
    def __init__(self, interface_layer):
        self.image_sender = ImageSender(interface_layer)
        self.interface_layer = interface_layer
        self.session_db = SessionDB("/tmp/session2.db", "example")

        # One route to start a new quiz, one to answer.
        self.routes = [
            ("/img\s(?P<term>[^$]+)$", self.image_search),
            ("/google\s(?P<term>[^$]+)$", self.G_image_search),
            ("/phone\s(?P<term>[^$]+)$", self.phone),
            ("/png\s(?P<term>[^$]+)$", self.png_search),
            ("linksearch (?P<url>[^$]+)$", self.linksearch),
            ("^test10\s?$", self.test),
            ("^book 2\s? $", self.test2),
            ("^book 1\s? (?P<number>[^$]+)$", self.inj),
            ("^book (?P<number1>[^$]+) (?P<number>[^$]+)$", self.test4),
            ("^book.ds\s? (?P<number>[^$]+)$", self.data_structure),
            ("^!test0\s?$", self.test),
            ("set_menu (?P<inputw>[^$]+)$", self.set),
            ("set_link (?P<inputw>[^$]+)$", self.setlink),
            ("select_menu (?P<inputw>[^$]+)$", self.setpath),
        ]

    def linksearch(self, message, match):
        url = match.group("url")
        links = getLink("https://"+url)
        if len(links) > 20:
            return TextMessageProtocolEntity(result, to=message.getFrom())
        else:
            return TextMessageProtocolEntity("No Links Found On "+url, to=message.getFrom())
        
    def G_image_search(self, message, match):
        pic = match.group("term")

        if " " in pic:
            pic = pic.split(" ")
            num = pic[-1]
            pic = "".join(pic[0:-1])
        else:
            num = 1
        img = Gimg(str(pic),num)
        try:
            self.image_sender.send_by_url(jid=message.getFrom(), file_url=str(img))
        except:
            result = "Invalid Image Name"
            return TextMessageProtocolEntity(result, to=message.getFrom())
        
    def image_search(self, message, match):
        pic = match.group("term")

        if " " in pic:
            pic = pic.split(" ")
            num = pic[-1]
            pic = "".join(pic[0:-1])
        else:
            num = 1
        
        url = "https://www.pexels.com/search/"
        response = requests.get(url + pic)
        page = response.text

        soup = BeautifulSoup(page, "lxml")
        tags=soup.findAll('img')
        try:
            print(num)
            img = tags[int(num)]["src"]
            img,trash = img.split("?")
            print(img)
            self.image_sender.send_by_url(jid=message.getFrom(), file_url=img)
        except:
            result = "Invalid Image Name"
            return TextMessageProtocolEntity(result, to=message.getFrom())

    def png_search(self, message, match):
        pic = match.group("term")

        if " " in pic:
            pic = pic.split(" ")
            num = int(pic[-1])
            pic = " ".join(pic[0:-1]).replace(" ","+")
        else:
            num = 1

        tags = ""
        if num <= 16:
            url = "http://www.freepngimg.com/search/?pg=1&query="
            response = requests.get(url + pic)
            page = response.text
        elif num <= 32:
            num = num - 16
            url = "http://www.freepngimg.com/search/?pg=2&query="
            response = requests.get(url + pic)
            page = response.text
        elif num <= 48:
            num = num - 32
            url = "http://www.freepngimg.com/search/?pg=3&query="
            response = requests.get(url + pic)
            page = response.text
        elif num <= 64:
            num = num - 48
            url = "http://www.freepngimg.com/search/?pg=4&query="
            response = requests.get(url + pic)
            page = response.text
        elif num <= 80:
            num = num - 64
            url = "http://www.freepngimg.com/search/?pg=5&query="
            response = requests.get(url + pic)
            page = response.text
        elif num <= 88:
            num = num - 80
            url = "http://www.freepngimg.com/search/?pg=6&query="
            response = requests.get(url + pic)
            page = response.text
        soup = BeautifulSoup(page, "lxml")
        tags = soup.findAll('img')
        try:
            img = "http://www.freepngimg.com"+tags[int(num)]["src"]
            if "images/folder.png" in img:
                err = "Image Not Found"
            else:
                self.image_sender.send_by_url(jid=message.getFrom(), file_url=img)
        except:
            err = "Invalid Image Name"
        return TextMessageProtocolEntity(err, to=message.getFrom())
        
    def phone(self, message, match):
        name = match.group("term")
        result,pic = phone(name)
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=pic)
        return TextMessageProtocolEntity(result, to=message.getFrom())


    def test2(self, message, match):
        num = match.group("number")
        try:
            ep,fmt = num.split(" ")
        except:
            ep = num
            fmt = "jpg"
            
        if int(ep) < 10:
            ep = "000"+ep
        elif int(ep) < 100:
            ep = "00"+ep
        elif int(ep) < 1000:
            ep = "0"+ep
        url = "http://www.dragonball-multiverse.com/en/pages/final/"+ep+"."+fmt
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=url)

    def inj(self, message, match):
        num = match.group("number")
        try:
            ep,fmt = num.split(" ")
            #if "-" in ep:
            #    start,last = ep.split("-")
        except:
            ep = num
            fmt = "jpg"
            
        if int(ep) < 10:
            ep = "00"+ep
        elif int(ep) < 100:
            ep = "0"+ep
        url = "http://readcomicbooksonline.net/reader/mangas/Injustice%20Gods%20Among%20Us%20Year%2001/Chapter%2001/Injustice%20-%20Gods%20Among%20Us%20001%20(2013)%20(Digital)%20(K6%20of%20Ultron-Empire)%2"+ep+"."+fmt
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=url)

    def data_structure(self, message, match):
        num = match.group("number")
        try:
            ep,fmt = num.split(" ")
            #if "-" in ep:
            #    start,last = ep.split("-")
        except:
            ep = num
            fmt = "jpg"

        url = "http://exchange.eu5.org/bot/book/data_structure/"+ep+"."+fmt
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=url)
        
    def test4(self, message, match):
        num = match.group("number")
        num1 = match.group("number1")
        url = myhentaicomic(num,num1)
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=url)
        
        
    def test(self, message, match):
        # Gets a random quiz and store in the sender' session
        number = random.randint(0,100)
        self.session_db.set(message.getFrom(), number)
        return TextMessageProtocolEntity("You Have Stored the Number "+str(number), to=message.getFrom())

    def setpath(self, message, match):
        file_name = match.group("inputw")
        file = open("/app/storage/menu.txt","w")
        file.write(file_name)
        file.close()
        return TextMessageProtocolEntity("done", to=message.getFrom())
        
    def set(self, message, match):
        content = match.group("inputw")
        file = open("/app/storage/menu.txt","r")
        menu = file.read()
        file.close()
        url = "http://jarbot.top/bot/bot/sett.php?p="+menu+"&con="+content
        data = requests.get(url)
        data = data.text
        cur = json.loads(data)
        return TextMessageProtocolEntity(cur, to=message.getFrom())

    def setlink(self, message, match):
        content = match.group("inputw")
        file = open("/app/storage/link.txt","r")
        menu = file.read()
        file.close()
        return TextMessageProtocolEntity(cur, to=message.getFrom())
                                                                 
    def test1(self, message, match):
        number = self.session_db.get(message.getFrom())
        return TextMessageProtocolEntity("Stored Number is "+str(number), to=message.getFrom())

